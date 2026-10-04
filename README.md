<p align="center">
  <img src="assets/readme/hero.jpg" alt="AI Native Teaching Kit：把 AI 放进科研与教学的真实任务。手绘讲解者和黑色小鸟展示课程材料。" width="100%">
</p>

# AI Native Teaching Kit

<p align="center">简体中文 · <a href="README.en.md">English</a></p>

**一套面向研究生和教师的中文课程，以及可以带走复用的视觉教学 Skill。**

从 Prompt、Context、Agent 到工作台与 Skills，讲清它们各自解决什么问题、怎样一起完成任务。课件、逐页讲稿、学生手册和可编辑源文件配套提供，方便自学、授课，也方便改成自己的课。

<p align="center">
  <a href="https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/latest"><strong>下载公开课件</strong></a> ·
  <a href="course/overview.md">课程导览</a> ·
  <a href="skills/build-visual-teaching/SKILL.md">使用教学 Skill</a> ·
  <a href="sources/README.md">查看来源</a>
</p>

<p align="center">
  109 页课件 · 48 页讲课稿 · 71 页学生手册 · 66 份原创 SVG 教学示意
</p>

## 先看两页

讲概念时，把定义、任务和反馈放在同一页；讲方法时，说明它是什么、为什么有用、怎样开始。

<a href="assets/readme/preview-agent.jpg"><img src="assets/readme/preview-agent.jpg" alt="公开版第12页：Agent 围绕目标选择行动并利用反馈，配本课原创目标—行动—反馈示意。" width="100%"></a>

<details>
<summary><strong>再看一页：怎样把设计写成执行计划</strong></summary>

<p>公开版第 86 页，解释 Writing Plans 的用途与计划组成。点击图片可看大图。</p>

<a href="assets/readme/preview-writing-plans.jpg"><img src="assets/readme/preview-writing-plans.jpg" alt="公开版第86页：Writing Plans 的定义、用途、起步方法，以及目标、方案、技术、文件、步骤和验证。" width="100%"></a>

</details>

## 按你的用途开始

| 你想做什么 | 建议入口 | 接下来做什么 |
| --- | --- | --- |
| 学懂概念，开始自己的实践 | [课程导览](course/overview.md) + 学生参考手册 | 选一个手头任务，对照课程辨认材料、工具、执行与检查的位置 |
| 给学生或同事讲这门课 | 视觉教学版 PPT + 讲课稿 | 按模块取舍内容；两版 PPT 都带逐页讲者备注 |
| 改成自己的课程 | 文字可编辑版 PPT + 内容与原创素材包 | 修改正文、示例和讲述顺序，再同步讲稿与手册 |
| 复用制作方法 | [build-visual-teaching](skills/build-visual-teaching/SKILL.md) | 提供自己的材料和视觉参考，从一个小节开始 |

课件文件从 [Releases](https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/latest) 取得，格式与配对方式见[课件版本与分发](releases/README.md)。阅读课程不需要安装 Skill。

## 课程讲什么

课程全名：**构建 AI 原生科研与教学工作环境**。

| 模块 | 页码 | 要回答的问题 |
| --- | --- | --- |
| 01 · 关键概念与真实任务 | 1–28 | Prompt、Context、工具、Agent、MCP、Skill、Harness 各负责什么？行动的结果怎样进入下一次判断？ |
| 02 · 我怎么选工作台 | 29–56 | 材料放在哪里，任务在哪里执行，结果到哪里检查？怎样按工作需要选择入口？ |
| 03 · 让个人 Agent 接续工作 | 57–69 | 怎样保留任务状态、接住反馈、继续推进？记住、继续做和定时做分别需要什么条件？ |
| 04 · 把开源 Skill 打开 | 70–100 | 设计、计划、实现、验证和资料读取的方法，怎样写进可复用的 Skill？ |
| 05 · 我怎样继续学习和更新 | 101–109 | 怎样从一条推荐追到官方文档、作者原文和适用版本，再判断能否用于自己的任务？ |

用[逐页索引](course/slides.tsv)定位标题，用[来源清单](sources/README.md)回到原文。课程中的产品入口、价格、安装方式和能力描述有版本背景，实际操作前请核对对应官方文档。

## 成品里有什么

| 文件 | 内容 | 适合怎么用 |
| --- | --- | --- |
| 视觉教学版 · PPTX / PDF | 109 页，保留讲解插画与手绘风格 | 课堂展示、阅读；PPTX 带讲者备注 |
| 文字可编辑版 · PPTX / PDF | 109 页，以原生文字和图形为主 | 换例子、改正文、调整教学安排 |
| 讲课稿 · DOCX | 48 页，配套完整口播 | 备课，补充解释与转场 |
| 学生参考手册 · DOCX | 71 页，配套正文与示例 | 课后阅读和查阅 |
| 内容与原创素材 · ZIP | 正文、口播和来源索引的 Markdown / JSON；66 份 SVG 及配套 PNG | 编辑内容、复用教学示意、保留可追溯来源 |

视觉教学版的部分页面背景是整页图像，不能把所有文字逐字拆开修改。需要大幅改课时，优先使用文字可编辑版与源文件包。

## 用这个 Skill 做你自己的课

[build-visual-teaching](skills/build-visual-teaching/SKILL.md) 保存的是制作方法：先弄清材料与讲述逻辑，再组织正文和视觉，最后检查实际导出的文件。它可以独立于这门课使用。

1. 复制完整的 [skills/build-visual-teaching](skills/build-visual-teaching/) 目录，保留 SKILL.md 与 references/ 的相对位置
2. 按你使用的 Agent 宿主文档加载或安装这个目录；也可以直接阅读其中的方法
3. 提供原始材料、受众、用途、视觉参考和需要交付的格式
4. 先完成一个小节，检查内容深度、图文关系和导出结果，再继续全课

例如，可以从这样一个任务开始：

> 请使用 build-visual-teaching，把我提供的材料做成一个面向研究生的教学小节。先列出要讲清的问题、采用的来源和页面安排，再制作课件与配套讲稿。概念需要有定义、用途和边界；引用保留出处；成品导出后检查文字、图像、链接和备注。

Skill 不附带私人对话或个人角色母版。需要讲解角色时，请提供自己拥有权利或获准使用的素材。

## 复用与修改

- **先沿用能用的部分。** 改一个例子，就同步检查相关正文、图注、讲稿和来源；不必重做整套课
- **保留内容的来处。** 来源索引帮助查证，也方便下一位使用者继续更新
- **区分教学示意与真实证据。** 公开版中替换的产品画面、关系图和示例标明为教学示意，不能当作实际界面、运行记录或性能测试
- **检查最终文件。** 源文字改好了，不代表 PPT 中的图像文字已经更新；导出后仍需打开检查

发现概念、来源或页面问题，可以[提交 Issue](https://github.com/qihangzhang-272/ai-native-teaching-kit/issues)，写明文件版本、页码、问题和建议依据。文字修订或示例改进也欢迎提交 Pull Request；请勿上传私人聊天、账号信息或未获授权的第三方素材。

## 作者与许可

作者：**张启航 / BLAZE**。

- 本项目原创 Skill 与代码：[MIT](LICENSE)
- 已确认权属的原创教学文字：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)，复用时署名、提供来源及许可链接，并说明修改
- 第三方方法、引用、商标、字体和外部项目仍遵守各自权利与许可；项目许可不自动覆盖这些内容，也不表示相关作者或厂商为本课程背书

公开课件保留经授权的讲者形象与黑色教学小鸟，原版中的第三方截图、书页、作品图和具名作者肖像已换成原创教学示意。具体范围以[许可说明](LICENSE-SCOPE.md)和附件中的使用说明为准，不能把整包混合内容一概视为同一许可。

感谢课程所引用的作者与开源项目。阅读他们的原文，是继续使用和修改这套材料的一部分。
