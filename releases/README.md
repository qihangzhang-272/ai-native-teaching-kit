# 原版课程交付与分发

v1.1.0 按原版 v6 文件分发，保留课程原有版式、插画、第三方引用图片和来源。七件文件配套使用，下载入口为 [v1.1.0 Release](https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/tag/v1.1.0)。

## 七件交付文件

| 文件名 | 内容 | 大小（字节） |
| --- | --- | ---: |
| `ai-native-teaching-kit-v1.1.0-visual-slides.pptx` | 视觉教学版，109 页 | 18,867,906 |
| `ai-native-teaching-kit-v1.1.0-visual-slides.pdf` | 视觉教学版，109 页 | 19,400,922 |
| `ai-native-teaching-kit-v1.1.0-editable-slides.pptx` | 文字可编辑版，109 页 | 6,903,410 |
| `ai-native-teaching-kit-v1.1.0-editable-slides.pdf` | 文字可编辑版，109 页 | 7,636,302 |
| `ai-native-teaching-kit-v1.1.0-lecture-notes.docx` | 讲课稿，47 页 | 98,620 |
| `ai-native-teaching-kit-v1.1.0-student-handbook.docx` | 学生参考手册，74 页 | 6,566,716 |
| `ai-native-teaching-kit-v1.1.0-original-content-and-assets.zip` | 课程内容、来源与原版素材 | 14,047,495 |

视觉版用于投影和整页阅读；文字可编辑版用于修改正文、备注及来源链接。讲课稿补充口述展开与转场，学生参考手册用于课后阅读。DOCX 的分页可能随字体和阅读软件变化。

源 ZIP 包含 Markdown / JSON 正文、口播、来源索引、页面与素材对应记录，以及 77 件课程素材和 3 份个人视觉参考。素材涵盖原图、裁片、兼容图和插画，并非全部为本项目原创。

## 版本与许可

v1.1.0 是原版课程分发；v1.0.0 是此前采用替换图的重绘整理版。两者分别使用各自附件、预览、页数和校验值，不混用。v1.1.0 的七个附件仅更换分发文件名，保留选定原版文件内容。

原版中的第三方截图、图表、书页、作品图、肖像、引文和商标仍保留各自权利，不因随课公开而纳入本项目 MIT 或 CC BY 授权。具体边界见 [许可范围](../LICENSE-SCOPE.md)；源 ZIP 内原有引用说明与来源记录一并保留。

## 下载校验

以下 SHA-256 对应本版七件文件：

```text
410fa6099bc9b20bf73c4498b3d44c805b62976ffd2b46fddf40cbc8a8da71e5  ai-native-teaching-kit-v1.1.0-visual-slides.pptx
f0745863c3c3e1c9333b899ab9f7ff68431874d607d79113186157f1727d1217  ai-native-teaching-kit-v1.1.0-visual-slides.pdf
5c9f320a26543f9cc5b57cfb04b5d995011cc1473449867d0a4af63f140da1ff  ai-native-teaching-kit-v1.1.0-editable-slides.pptx
654a292479ecab6b91081538106476e6ed7187da21b7b92e57ad781856dc4772  ai-native-teaching-kit-v1.1.0-editable-slides.pdf
33889010a50c08930c6a15bcc1c058267d84b7d76b91ceddd330d3d6a7540d5e  ai-native-teaching-kit-v1.1.0-lecture-notes.docx
b51920a913548f5cc9887a7c776a144f5a81c13fd8d609f554f4eee77d541082  ai-native-teaching-kit-v1.1.0-student-handbook.docx
9a59007ec9dc3a8ac6828489a8b8b6f4b589d05a516a5178048815165124c2e7  ai-native-teaching-kit-v1.1.0-original-content-and-assets.zip
```

## 按版本使用

GitHub 自动生成的 Source code 压缩包是仓库快照，不含课程二进制附件。请从 Release 的 Assets 区选择上述七件文件，按需要下载。

仓库跟踪文本、来源、技能与预览，PPTX、PDF、DOCX 和课程源 ZIP 放在 Release 中。发布后应逐件核对下载、格式与哈希，见[检查清单](../RELEASE-CHECKLIST.md)。
