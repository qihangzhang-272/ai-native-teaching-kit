# 安装、调用与检查教学 Skill

[返回首页](../README.md) · [English](skill-setup.en.md)

本指南说明如何把仓库里的 `build-visual-teaching` 放进本地项目。它是指令与参考文件包，不包含模型、图像生成服务或 PPT 导出引擎。开始前先读 [SKILL.md](../skills/build-visual-teaching/SKILL.md)，了解它会要求读取哪些材料、制作什么、检查什么。

## 选择范围

建议第一次只放进一个课程项目，便于观察其行为。整个 `build-visual-teaching/` 目录必须一起复制，不能只复制 SKILL.md。若已有同名目录，先比较并备份你的修改；以下操作不是更新或清理旧 Skill 的命令。

先获取仓库：

```bash
git clone https://github.com/qihangzhang-272/ai-native-teaching-kit.git
cd ai-native-teaching-kit
```

## macOS / Linux / WSL

按宿主选一种，在仓库根目录运行。

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

也可以用文件管理器复制到相同目录，不要求使用终端。要在另一个课程项目使用，复制到那个项目的 `.agents/skills/` 或 `.claude/skills/`，并在那里启动对应宿主。

## 先做加载检查

以 Codex 为例，最终目录应包含：

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

在 Codex CLI / IDE 中用 `$build-visual-teaching` 或 `/skills` 选择；Claude Code 用 `/build-visual-teaching`。先提交一个只读检查任务：

```text
请使用 build-visual-teaching，但先不要修改或生成文件。
说明你实际读取的 SKILL.md 路径，以及 references 中与教学结构、素材和验收有关的文件。
然后列出制作一个教学小节前，需要我提供哪些资料。
```

检查实际读取路径是否指向你放置的版本。能列出名字不等于已完成一次产物测试；后续仍需用小节验证文字深度、图文关系与导出结果。

## 第一个小节要准备什么

| 输入 | 建议内容 |
| --- | --- |
| 原始资料 | 文档、原文链接、已有课件；说明哪些可以引用或公开 |
| 受众 | 已有知识、希望学会什么、使用场景 |
| 范围 | 一个概念或一个小节，先不要求整门课 |
| 输出 | PPTX / PDF / 讲稿 / Markdown 等实际需要的格式 |
| 视觉参考 | 可使用的版式、配图、角色素材；没有就明确从新基准开始 |
| 检查要求 | 来源、内容、版面、备注、链接与最终导出文件 |

在[首页调用示例](../README.md#skill)中替换自己的材料与受众。不要把课程角色图当作默认开放的通用肖像素材；是否可再用，应按项目许可范围判断。

<a id="troubleshooting"></a>
## 加载与排错

| 现象 | 先检查 | 下一步 |
| --- | --- | --- |
| 列表里没有 Skill | 当前项目、目录层级、SKILL.md 文件名 | 检查是否意外套了两层同名目录；必要时重新打开宿主会话 |
| 读取了别的同名 Skill | Agent 报告的实际路径 | 对比版本与宿主的作用域规则，不直接覆盖或删除旧目录 |
| 只读了主文件，没读参考文档 | references/ 是否完整；相对链接是否保留 | 指明当前任务需要的参考文件，并确认读取成功 |
| 给出了计划但没交文件 | 是否有写文件、导出或生图能力 | 要求说明缺失能力；可以先交可编辑正文，不将其称为最终课件 |
| 输出图文不符 | 原始材料、受众、视觉参考是否充分 | 具体指出有问题的页面、文字或图层，先修一个小节 |
| 导出后乱码、截断或错位 | 实际导出文件、字体与阅读软件 | 打开最终产物检查，修复后重新导出；不要只验源文件 |

## 更新与权限

复制到项目里的 Skill 不会随仓库更新自动同步。需要更新时，先比较上游变更与自己的修改，再决定合并范围。安装 Skill 不会代替对文件、外部账号、网络与发布权限的授权；使用宿主现有的权限控制。

## 官方依据与验证边界

安装目录和调用入口于 2026-10-04 对照 [OpenAI 的 Skills 文档](https://learn.chatgpt.com/docs/build-skills)与 [Claude Code 的 Skills 文档](https://code.claude.com/docs/en/skills)整理。命令只复制本仓库已有文件；本项目尚未提供跨宿主、跨版本的完整兼容性测试结果。遇到差异，请在反馈中注明宿主、版本、系统与实际路径，且不要提交密钥或私人材料。
