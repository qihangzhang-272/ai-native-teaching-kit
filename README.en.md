<p align="center">
  <img src="assets/readme/hero.jpg" alt="AI Native Teaching Kit: bringing AI into real research and teaching tasks. A hand-drawn lecturer and a small black bird present course materials." width="100%">
</p>

# AI Native Teaching Kit

<p align="center"><a href="README.md">简体中文</a> · English</p>

**A Chinese-language course for graduate students and educators, with a reusable visual-teaching Skill.**

Understand how prompts, context, agents, workspaces, and Skills fit together in real work. The kit pairs slides with speaker notes, a teaching script, a student handbook, and editable source materials, so you can study the course, teach it, or adapt it for your own audience.

<p align="center">
  <a href="https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/latest"><strong>Download course materials</strong></a> ·
  <a href="course/overview.md">Course guide</a> ·
  <a href="skills/build-visual-teaching/SKILL.md">Use the teaching Skill</a> ·
  <a href="sources/README.md">Sources</a>
</p>

<p align="center">
  109 slides · 48-page teaching script · 71-page student handbook · 66 original SVG teaching diagrams
</p>

This README is available in English and Chinese. The course, supporting documents, and teaching Skill are currently in Chinese.

## A look inside

Concept pages connect a definition to a task and its feedback. Method pages explain what a method does, why it helps, and how to begin.

<a href="assets/readme/preview-agent.jpg"><img src="assets/readme/preview-agent.jpg" alt="Public edition, slide 12: how an agent selects actions toward a goal and uses feedback, with an original goal–action–feedback teaching diagram." width="100%"></a>

<details>
<summary><strong>Another example: turning a design into an implementation plan</strong></summary>

<p>Slide 86 explains Writing Plans and the elements of a useful plan. Click the image for a larger view.</p>

<a href="assets/readme/preview-writing-plans.jpg"><img src="assets/readme/preview-writing-plans.jpg" alt="Public edition, slide 86: Writing Plans, covering its purpose and a plan's goal, architecture, technology, files, tasks, and verification." width="100%"></a>

</details>

## Choose your starting point

| Your goal | Start with | Next step |
| --- | --- | --- |
| Learn the concepts and try them | [Course guide](course/overview.md) + student handbook | Pick a real task and identify its materials, tools, execution environment, and checks |
| Teach a class or workshop | Visual slides + teaching script | Select the modules you need; both slide editions include speaker notes |
| Adapt the course | Text-editable slides + source archive | Revise the text, examples, and sequence, then update the script and handbook to match |
| Reuse the production method | [build-visual-teaching](skills/build-visual-teaching/SKILL.md) | Bring your own sources and visual references, and start with one section |

Get the files from [Releases](https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/latest). See the [file and version guide](releases/README.md) for formats and matching editions. You do not need to install a Skill to read the course.

## What the course covers

The course title is **Building an AI-Native Research and Teaching Environment**.

| Module | Slides | Questions it addresses |
| --- | --- | --- |
| 01 · Concepts through real tasks | 1–28 | What do prompts, context, tools, agents, MCP, Skills, and harnesses each do? How do action results inform the next decision? |
| 02 · Choosing a workspace | 29–56 | Where are the materials, where does execution happen, and where do you inspect the result? Which environment fits the task? |
| 03 · Working with a personal agent over time | 57–69 | How can task state and feedback carry forward? What is needed for memory, continued work, and scheduled work? |
| 04 · Reading open-source Skills | 70–100 | How are methods for design, planning, implementation, verification, and research packaged for reuse? |
| 05 · Keeping your knowledge current | 101–109 | How do you follow a recommendation back to official documentation, original authors, and the relevant version? |

Use the [slide index](course/slides.tsv) to find a topic and the [source list](sources/README.md) to reach the original material. Product interfaces, prices, installation steps, and capabilities can change; check the linked official documentation before acting on them.

## What's included

| File | Contents | Best for |
| --- | --- | --- |
| Visual edition · PPTX / PDF | 109 illustrated slides | Presenting and reading; the PPTX includes speaker notes |
| Text-editable edition · PPTX / PDF | 109 slides built primarily from editable text and native shapes | Replacing examples, revising explanations, and adapting lessons |
| Teaching script · DOCX | 48 pages of accompanying narration | Preparation, examples, and transitions |
| Student handbook · DOCX | 71 pages of course text and examples | Review and reference |
| Content and original assets · ZIP | Course text, narration, and source indexes in Markdown / JSON; 66 SVG diagrams with PNG versions | Editing content, reusing diagrams, and tracing sources |

Some backgrounds in the visual edition are full-slide images. Their text cannot all be edited character by character. For substantial changes, use the text-editable edition and the source archive.

## Use the Skill for your own teaching materials

[build-visual-teaching](skills/build-visual-teaching/SKILL.md) captures a production method: establish the sources and teaching structure, develop the text and visuals, then inspect the exported files. You can use it independently of this course.

1. Copy the entire [skills/build-visual-teaching](skills/build-visual-teaching/) directory, keeping SKILL.md and references/ in their relative locations
2. Load or install it according to your agent host's documentation, or simply read the method
3. Provide your source materials, audience, purpose, visual references, and required output formats
4. Finish one section first; check the depth, layout, and exported result before expanding to the full course

A starting request might look like this:

> Use build-visual-teaching to turn the materials I provide into a lesson for graduate students. First propose the questions to answer, sources to use, and slide structure. Then create the slides and teaching script. Explain each concept's meaning, purpose, and limits; preserve source references; inspect the exported text, images, links, and speaker notes.

The Skill does not include private conversations or master artwork for the personal character. If you want an illustrated presenter, supply artwork you own or have permission to use.

## Adapting and contributing

- **Keep what already works.** When changing an example, check its related text, captions, narration, and sources. You do not need to rebuild the whole course
- **Keep sources traceable.** The index supports fact-checking and helps the next person update the material
- **Distinguish diagrams from evidence.** Replacement product illustrations and examples in the public edition are labeled as teaching diagrams. They are not actual interfaces, execution records, or performance tests
- **Check the exported files.** Editing source text does not automatically update text baked into slide images

Found an error? [Open an issue](https://github.com/qihangzhang-272/ai-native-teaching-kit/issues) with the file version, slide or page number, a description, and a supporting source when relevant. Text corrections and improved examples are welcome as pull requests. Please do not upload private conversations, account information, or third-party assets without permission.

## Author and licensing

Author: **张启航 / BLAZE**.

- Original project Skills and code: [MIT](LICENSE)
- Original teaching text with confirmed ownership: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit the author, link to the source and license, and indicate changes
- Third-party methods, quotations, trademarks, fonts, and external projects retain their own rights and licenses. The project license does not automatically cover them, and their inclusion does not imply endorsement

The public course retains the authorized lecturer character and small black teaching bird. Third-party screenshots, book pages, artwork, and portraits of named authors from the earlier edition have been replaced with original teaching diagrams. See the [license scope](LICENSE-SCOPE.md) and the usage notes in each package for details; do not treat all mixed-content files as having a single blanket license.

Thanks to the authors and open-source projects referenced in the course. Their original work remains an essential part of using and adapting these materials.
