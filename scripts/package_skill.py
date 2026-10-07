#!/usr/bin/env python3
"""Check portable references and package the complete reviewed Skill directory."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
import zipfile


def validate(root):
    manifest = json.loads((root / 'assets/manifest.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        data = (root / item['path']).read_bytes()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError('Asset differs from manifest: ' + item['path'])
    for doc in root.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            path = (doc.parent / unquote(target.split('#')[0])).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                raise ValueError(f'Non-portable link in {doc.name}: {target}')
    with zipfile.ZipFile(root / 'examples/approved-slides.pptx') as deck:
        if deck.testzip() is not None:
            raise ValueError('Corrupt example PPTX')
    print('PASS: asset hashes and all Skill Markdown file links')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true')
    parser.add_argument('--output', type=Path, default=Path('dist/build-visual-teaching.zip'))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1] / 'skills/build-visual-teaching'
    validate(root)
    if args.check_only:
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob('*')):
            if path.is_file():
                name = 'build-visual-teaching/' + path.relative_to(root).as_posix()
                info = zipfile.ZipInfo(name, date_time=(2026, 10, 7, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    args.output.with_suffix('.zip.sha256').write_text(
        digest + '  ' + args.output.name + '\n', encoding='utf-8')
    print(f'{args.output}: {args.output.stat().st_size} bytes; SHA-256 {digest}')


if __name__ == '__main__':
    main()
