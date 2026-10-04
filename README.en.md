<a id="top"></a>
<p align="center">
  <img src="assets/readme/hero.jpg" alt="AI Native Teaching Kit: bringing AI into real research and teaching tasks" width="100%">
</p>
<h1 align="center">AI Native Teaching Kit</h1>
<p align="center"><strong>Build an AI-native research and teaching environment</strong><br>A Chinese-language course, editable teaching materials, and a reusable visual-teaching Skill</p>
<p align="center"><a href="README.md">简体中文</a> · English</p>
<p align="center">
  <a href="https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/latest"><img src="https://img.shields.io/github/v/release/qihangzhang-272/ai-native-teaching-kit?style=flat-square&color=2457e6" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Skill%20%26%20Code-MIT-2457e6?style=flat-square" alt="Original Skill and code: MIT"></a>
  <a href="LICENSE-SCOPE.md"><img src="https://img.shields.io/badge/Original%20Text-CC%20BY%204.0-15856b?style=flat-square" alt="Original teaching text: CC BY 4.0"></a>
</p>
<p align="center">
  <a href="#quick-start"><strong>Quick start</strong></a> ·
  <a href="#downloads"><strong>Download materials</strong></a> ·
  <a href="#skill"><strong>Set up the Skill</strong></a>
</p>

Using AI for real work raises connected questions: Where do the materials go? What can the model actually see? How do tools execute actions? How does a task continue, and how do you check the result? This course uses those questions to explain prompts, context, agents, MCP, harnesses, and Skills, then moves into workspace choices and practical methods.

Use it for self-study, teach selected sections, or adapt the slides, script, and examples. The repository also shares the production method so you can start a new course from your own sources.

<table>
<tr><td align="center"><strong>109 slides</strong><br>Two editions with speaker notes</td><td align="center"><strong>48 pages</strong><br>Teaching script</td><td align="center"><strong>71 pages</strong><br>Student handbook</td><td align="center"><strong>66 SVGs</strong><br>Original diagrams with PNGs</td></tr>
</table>

**On this page**　[Quick start](#quick-start) · [Gallery](#gallery) · [Curriculum](#curriculum) · [Downloads](#downloads) · [Teaching Skill](#skill) · [Repository map](#structure) · [FAQ](#faq) · [Status](#status) · [Contributing](#contributing) · [License & credits](#license)

<a id="quick-start"></a>
## Quick start

**Just browsing?** Download the [visual PDF][visual-pdf] and start with the concepts on slides 1–28. No Git, API key, or agent account is needed.

| Your goal | What you need | First steps | What to check |
| --- | --- | --- | --- |
| **Learn** | A PDF reader; optionally a DOCX reader | Read the [course guide](course/overview.md), choose a module, and apply it to one of your own tasks | Can you locate the materials, tools, actions, and feedback? |
| **Teach** | PowerPoint or a compatible presentation app | Get the [visual PPTX][visual-pptx] and [teaching script][lecture]; rehearse one section | Fonts, images, speaker notes, and fit for the audience |
| **Adapt** | An editor for PPTX / DOCX | Get the [text-editable slides][editable-pptx] and [source archive][source-zip]; work on a copy and replace one example | Keep text, captions, narration, sources, and exports in sync |
| **Create a new lesson** | An agent that can read local files, plus your own sources | [Load the Skill](#skill), then provide a small source set and an audience brief | Establish the content and sources before visual production |

Reading and adapting the course do not require a particular AI product. Models, image generation, file export capabilities, and any associated costs depend on your chosen host and tools.

<a id="gallery"></a>
## Gallery

These images come from the public edition and its original asset archive. Click any image for full resolution. The first row compares the same content in the two slide editions.

<table>
<tr>
<td width="50%"><a href="assets/readme/preview-agent.jpg"><img src="assets/readme/preview-agent.jpg" alt="Visual edition, slide 12: an agent's goals, actions, and feedback"></a><br><strong>Visual edition · Slide 12</strong><br>Explanation, task diagram, and illustrated presenter</td>
<td width="50%"><a href="assets/readme/preview-editable.jpg"><img src="assets/readme/preview-editable.jpg" alt="Text-editable edition, slide 12: the same content using editable text and native shapes"></a><br><strong>Text-editable edition · Slide 12</strong><br>The same lesson organized for revision</td>
</tr>
<tr>
<td width="50%"><a href="assets/readme/preview-writing-plans.jpg"><img src="assets/readme/preview-writing-plans.jpg" alt="Visual edition, slide 86: the purpose and use of Writing Plans"></a><br><strong>Explaining a method · Slide 86</strong><br>What it is, why it helps, and how to begin</td>
<td width="50%"><a href="assets/readme/preview-diagram.png"><img src="assets/readme/preview-diagram.png" alt="Original MCP teaching diagram used on slide 17"></a><br><strong>Original asset · Slide 17</strong><br>Editable SVG source; a teaching diagram, not a product screenshot</td>
</tr>
</table>

<a id="curriculum"></a>
## Curriculum

Follow the five modules in order or use the [slide index](course/slides.tsv) to select a section. Each module includes a suggested activity to connect the material to your own work.

| Module / slides | Topics | A suggested activity |
| --- | --- | --- |
| **01 · Concepts through real tasks**<br>1–28 | Tasks, prompts, context, models and tools, agents / loops, function calling, MCP, Skills, harnesses, workflows, CLI / IDE | Explain the roles within a real task and define what would count as complete |
| **02 · Choosing a workspace**<br>29–56 | Development and office workflows; materials, workspaces, execution locations, permissions, progress, and outputs | Make an environment checklist and explain why the chosen workspace fits |
| **03 · Working with a personal agent over time**<br>57–69 | Ongoing collaboration, task state, human feedback, memory, continued execution, and schedules | Write a task-state record that someone could use to resume the work |
| **04 · Reading open-source Skills**<br>70–100 | Design judgment, brainstorming, writing plans, TDD, verification, simpler implementation, review, and research | Read an original SKILL.md and identify its inputs, method, outputs, and limits |
| **05 · Keeping your knowledge current**<br>101–109 | Following recommendations back to authors, official documentation, original work, and applicable versions | Find the original source and version for a claim you intend to use |

**Explore:** [Course guide](course/overview.md) · [109-slide index](course/slides.tsv) · [Source notes](sources/README.md) · [Reference list](sources/references.tsv)

The workspaces and projects discussed are examples, not dependencies of this repository. Check their official documentation before relying on product interfaces, pricing, capabilities, or installation instructions.

<a id="downloads"></a>
## Downloads and versions

**Public release: v1.0.0.** Use the seven matching attachments together. PPTX / DOCX files are for editing, PDFs for reading, and the source archive for course text, narration, references, and original diagrams.

| Material | Direct download | Size / length | Notes |
| --- | --- | --- | --- |
| Visual slides | [PPTX][visual-pptx] · [PDF][visual-pdf] | 109 slides; 13.70 / 16.05 MiB | Presentation edition; PPTX includes notes. Some backgrounds are full-slide images |
| Text-editable slides | [PPTX][editable-pptx] · [PDF][editable-pdf] | 109 slides; 0.60 / 3.17 MiB | Best for substantial edits; primarily native text and shapes |
| Teaching script | [DOCX][lecture] | 48 pages; 0.09 MiB | Narration, explanations, and transitions |
| Student handbook | [DOCX][handbook] | 71 pages; 2.89 MiB | Review and reference |
| Content and original assets | [ZIP][source-zip] | 3.37 MiB | Markdown / JSON text, narration, and sources; 66 SVGs with PNGs |

[Release notes][release] · [All versions](https://github.com/qihangzhang-272/ai-native-teaching-kit/releases) · [Distribution guide](releases/README.md)

> **Two different ZIPs:** GitHub's automatically generated **Source code (zip)** is a repository snapshot. It does not contain the seven course attachments. For editable course text and diagrams, choose **Content and original assets** above. DOCX page counts can vary with the reader, fonts, and layout environment.

Cloning the repository downloads the indexes, Skill, and documentation; it does not automatically download the PPTX, PDF, or DOCX attachments.

<a id="skill"></a>
## Use the visual-teaching Skill

`build-visual-teaching` is a directory of instructions and supporting references. It guides content decisions, source use, visual references, and delivery checks. Your host still needs the tools to generate images or export files.

### 1. Get the repository

```bash
git clone https://github.com/qihangzhang-272/ai-native-teaching-kit.git
cd ai-native-teaching-kit
```

Without Git, use **Code → Download ZIP** and extract it. Read [SKILL.md](skills/build-visual-teaching/SKILL.md) first, and keep the complete directory, including `references/`.

### 2. Choose a loading method

| Environment | Location / method | Explicit invocation |
| --- | --- | --- |
| **Codex CLI / IDE, project scope** | Copy to `.agents/skills/build-visual-teaching/` in the project | `$build-visual-teaching`, or select it through `/skills` |
| **Claude Code, project scope** | Copy to `.claude/skills/build-visual-teaching/` in the project | `/build-visual-teaching` |
| **Other agents with local file access** | Provide the full path to SKILL.md and ask the agent to read its linked references | Name the method in your request; this is not native Skill installation |

The loading methods follow the [OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code documentation](https://code.claude.com/docs/en/skills). This repository distributes the Skill as a standalone directory.

<details>
<summary><strong>Copy commands for macOS / Linux / WSL</strong></summary>

Run one option from the cloned repository root. If a Skill with the same name already exists at the destination, compare and back it up first rather than overwriting your changes.

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

See the [setup guide](docs/skill-setup.en.md) for PowerShell, use in another project, loading checks, and troubleshooting.

</details>

### 3. Give it a complete, small task

Provide your own source files first. In a native Skill host, begin with that host's explicit invocation, followed by a request like this:

```text
Use build-visual-teaching.

Sources: Read the materials I provide; preserve their origins and necessary quotations.
Audience: Graduate students encountering this topic for the first time.
Task: Create one lesson section that explains a key concept and its practical use.

First propose: questions to answer, sources to use, slide structure, and missing information.
After confirmation: produce slides, a teaching script, and editable course text.
Visuals: let the text carry the explanation; use images to support understanding.
Follow the visual references I supply.
Check: open the final exports and inspect text, images, sources, links, and notes.
```

**What should a useful first run produce?** Before visual work, an audience-specific content plan grounded in supplied sources. After production, actual files you can open, with checks tied to those files. Missing tools should be disclosed; a plan or preview should not be presented as the finished course.

**Method references:** [Teaching structure](skills/build-visual-teaching/references/teaching-depth.md) · [Visual benchmarks](skills/build-visual-teaching/references/visual-benchmarks.md) · [Material integration](skills/build-visual-teaching/references/material-integration.md) · [Delivery checks](skills/build-visual-teaching/references/delivery-qa.md)

<a id="structure"></a>
## Repository map

```text
ai-native-teaching-kit/
├── README.md / README.en.md       # Chinese and English entry points
├── course/
│   ├── overview.md               # Course guide
│   └── slides.tsv                # 109-slide title index
├── skills/build-visual-teaching/
│   ├── SKILL.md                  # Reusable teaching-production method
│   ├── references/               # Structure, sources, visuals, and checks
│   └── LICENSE                   # MIT license for the Skill
├── docs/                         # Bilingual setup and troubleshooting
├── sources/                      # Source notes and reference list
├── assets/readme/                # Cover and public-edition previews
├── releases/README.md            # File and version guide
├── CONTRIBUTING.md               # Reporting and revision checklist
├── LICENSE                       # Original Skill / code license
└── LICENSE-SCOPE.md              # Scope of text and asset permissions
```

The content archive separately contains Chinese-named files for course text, narration, and source indexes in Markdown / JSON, plus an original-diagram directory. Changing those sources does not automatically update text baked into images; check the slides and exports as well.

<a id="faq"></a>
## Frequently asked questions

<details>
<summary><strong>Do I need programming skills or a paid AI account?</strong></summary>

No programming or AI subscription is required to read the PDFs or edit the Office files. Using the teaching Skill requires an agent with file access. Image generation, exports, external services, and their costs depend on the host you choose.

</details>

<details>
<summary><strong>Do the two slide editions cover the same material? Why can't I select some text?</strong></summary>

Both follow the same 109-slide course and include matching speaker notes. Some visual-edition backgrounds are full-slide images. The text-editable edition uses mainly native text and shapes and is the better starting point for revisions. Either PDF works for reading.

</details>

<details>
<summary><strong>Why are the course files missing after cloning or downloading the repository?</strong></summary>

The large files are [Release attachments][release], outside Git history. Download the named PPTX, PDF, DOCX, and content archive. GitHub's generated Source code archive contains only the repository files.

</details>

<details>
<summary><strong>The Skill is missing or behaving unexpectedly. What should I check?</strong></summary>

Check the expected directory and make sure it contains SKILL.md and references/. Confirm the session is using that project, try explicit invocation, and ask which Skill path was actually read. See the [troubleshooting guide](docs/skill-setup.en.md#troubleshooting) before repeatedly reinstalling, overwriting, or deleting existing Skills.

</details>

<details>
<summary><strong>May I teach, adapt, or commercially reuse the materials?</strong></summary>

MIT and CC BY 4.0 permit use and adaptation, including commercial use, for the content they cover and subject to their conditions. This is a mixed-content course: third-party quotations, trademarks, fonts, and character master artwork do not automatically fall under those licenses. Read the [license scope](LICENSE-SCOPE.md) and package notes first.

</details>

<details>
<summary><strong>Are the product images actual screenshots?</strong></summary>

Third-party screenshots, book pages, artwork, and portraits of named authors from the earlier edition have been replaced with original teaching diagrams. Source links remain. Illustrations labeled as teaching diagrams explain relationships; they are not evidence of a real interface, execution result, or performance benchmark.

</details>

<details>
<summary><strong>Is there an English course or a one-command course generator?</strong></summary>

The README and setup guide are bilingual. The course, script, handbook, and Skill are primarily in Chinese. The repository does not include a one-command rebuild script or the personal character's master artwork. The Skill supplies a method; results depend on sources, tools, and review.

</details>

<a id="status"></a>
## Project status

| Area | Current state |
| --- | --- |
| Course | v1.0.0 public edition: five modules, 109 slides, two slide formats |
| Supporting materials | Teaching script, student handbook, course text, and original asset archive |
| Production method | Standalone Skill with reference documents; no marketplace package |
| Languages | Bilingual README and setup guide; mostly Chinese course content |
| Product currency | Reflects the course's version context; verify current product details at their sources |

Useful contributions include source-backed corrections, updated product entry points, examples from other disciplines, real host-setup reports, and translations. Start by discussing the scope in [Issues](https://github.com/qihangzhang-272/ai-native-teaching-kit/issues).

<a id="contributing"></a>
## Contributing

1. **Report a problem:** include the release, filename, slide/page or path, the problem, and supporting evidence
2. **Improve the content:** keep each change focused, preserve sources and qualifications, and keep bilingual documentation aligned
3. **Check before submitting:** review links, layout, illustrations, and notes; exclude private conversations, account information, and unauthorized assets

See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and a copyable issue template.

<a id="license"></a>
## License and credits

**Author: 张启航 / BLAZE**

| Content | License / permission scope |
| --- | --- |
| Original project Skill and code | [MIT](LICENSE) |
| Original teaching text with confirmed ownership | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): credit the author, link the source and license, indicate changes |
| Personal characters, mixed-content slides, and original diagrams | See [LICENSE-SCOPE.md](LICENSE-SCOPE.md) and the notes included in each package |
| Third-party methods, quotations, trademarks, fonts, and external works | Their respective rights and licenses remain; a source link does not grant redistribution rights |

Suggested credit: **张启航 / BLAZE, AI Native Teaching Kit**, with a link to this repository and a description of any changes.

Thanks to the authors and projects cited in the course, including [Anthropic Skills](https://github.com/anthropics/skills), [Superpowers](https://github.com/obra/superpowers), and the original materials in the [source list](sources/README.md). Teaching interpretations and personal usage accounts do not represent those authors' or vendors' official positions.

<p align="right"><a href="#top">Back to top ↑</a></p>

[release]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/tag/v1.0.0
[visual-pptx]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/download/v1.0.0/ai-native-teaching-kit-v1.0.0-visual-slides.pptx
[visual-pdf]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/download/v1.0.0/ai-native-teaching-kit-v1.0.0-visual-slides.pdf
[editable-pptx]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/download/v1.0.0/ai-native-teaching-kit-v1.0.0-editable-slides.pptx
[editable-pdf]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/download/v1.0.0/ai-native-teaching-kit-v1.0.0-editable-slides.pdf
[lecture]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/download/v1.0.0/ai-native-teaching-kit-v1.0.0-lecture-notes.docx
[handbook]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/download/v1.0.0/ai-native-teaching-kit-v1.0.0-student-handbook.docx
[source-zip]: https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/download/v1.0.0/ai-native-teaching-kit-v1.0.0-original-content-and-assets.zip
