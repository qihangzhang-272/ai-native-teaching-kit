# Set up, invoke, and check the teaching Skill

[Back to the README](../README.en.md) · [简体中文](skill-setup.md)

This guide puts `build-visual-teaching` into a local project. The package contains instructions and references, not a model, image-generation service, or presentation-export engine. Read [SKILL.md](../skills/build-visual-teaching/SKILL.md) first to understand its inputs, method, and checks.

## Choose the scope

Start with one course project. Copy the whole `build-visual-teaching/` directory, not just SKILL.md. If a same-named directory exists, compare it and back up your changes first. These are setup instructions, not commands to update or remove an existing Skill.

Start by cloning the repository:

```bash
git clone https://github.com/qihangzhang-272/ai-native-teaching-kit.git
cd ai-native-teaching-kit
```

## macOS / Linux / WSL

Choose one host and run its commands from the repository root.

**Codex CLI / IDE**

```bash
mkdir -p .agents/skills
cp -R skills/build-visual-teaching .agents/skills/
```

**Claude Code**

```bash
mkdir -p .claude/skills
cp -R skills/build-visual-teaching .claude/skills/
```

## Windows PowerShell

**Codex CLI / IDE**

```powershell
New-Item -ItemType Directory -Force .agents/skills | Out-Null
Copy-Item -Recurse skills/build-visual-teaching .agents/skills/
```

**Claude Code**

```powershell
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse skills/build-visual-teaching .claude/skills/
```

A file manager works too. To use the Skill in another course project, copy it to that project's `.agents/skills/` or `.claude/skills/` directory and start the relevant host there.

## Check loading before production

For Codex, the resulting structure should be:

```text
.agents/skills/build-visual-teaching/
├── SKILL.md
├── LICENSE
└── references/
    ├── teaching-depth.md
    ├── visual-benchmarks.md
    ├── material-integration.md
    ├── lecture-persona.md
    └── delivery-qa.md
```

In Codex CLI / IDE, use `$build-visual-teaching` or select it through `/skills`. In Claude Code, use `/build-visual-teaching`. Begin with a read-only check:

```text
Use build-visual-teaching, but do not modify or generate files yet.
Report the SKILL.md path you actually read and identify the references
covering teaching structure, source materials, and delivery checks.
Then list the inputs you need to prepare one lesson section.
```

Check that the reported path is the version you intended. A discovered Skill name is not evidence of a successful production run. Test one section before relying on the setup for a full course.

## Prepare the first section

| Input | What to supply |
| --- | --- |
| Sources | Documents, original links, or existing slides; state what may be quoted or published |
| Audience | Prior knowledge, learning goal, and setting |
| Scope | One concept or section to start with |
| Outputs | The formats you actually need: PPTX, PDF, script, Markdown, etc. |
| Visual references | Permitted layouts, illustrations, or characters; say if a new baseline is needed |
| Checks | Sources, content, layout, notes, links, and final exported files |

Adapt the [README example](../README.en.md#skill) with your own sources and audience. Do not assume that the course character artwork is an unrestricted general-purpose asset; consult the project's license scope.

<a id="troubleshooting"></a>
## Troubleshooting

| Symptom | Check first | Next step |
| --- | --- | --- |
| Skill is missing | Project location, directory nesting, and SKILL.md filename | Look for an accidentally doubled folder; reopen the host session if needed |
| A different same-named Skill loads | The path reported by the agent | Compare versions and the host's scope rules; do not immediately overwrite or delete the old copy |
| References are not read | references/ exists and relative links are intact | Point to the relevant reference and confirm it was read |
| A plan appears but no files are produced | File-writing, export, and image tools | Ask which capability is missing; editable text may be a partial output, not a finished deck |
| The text and visuals do not match | Sources, audience brief, and visual references | Identify the specific page or element and repair one section first |
| Exports have missing text or broken layout | Actual exports, fonts, and reader app | Inspect and re-export the final artifact rather than checking only its source |

## Updates and permissions

A copied Skill does not update automatically when the repository changes. Compare upstream revisions with local edits before merging. Installing a Skill does not grant access to files, accounts, external services, or publishing destinations; use the host's existing permission controls.

## Sources and testing boundary

The locations and invocation methods were checked on 2026-10-04 against the [OpenAI Skills documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code Skills documentation](https://code.claude.com/docs/en/skills). The commands copy existing repository files. This project has not published a complete host/version compatibility test matrix. Report differences with the host, version, operating system, and actual path, without secrets or private materials.
