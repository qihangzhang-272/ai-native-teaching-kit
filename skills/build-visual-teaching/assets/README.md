# 本人、黑鸟与认可课件的原参考

本目录让全新 clone、Download ZIP 和单独复制的 `build-visual-teaching/` 都能读取同一组参考，无需维护者的聊天记录或私人路径。作者张启航 / BLAZE 已明确允许本人头像放进公开包，并要求附上素材供复现课程。

| 文件 | 用途 | 原始来源 |
| --- | --- | --- |
| [user-lecture-reference.jpg](user-lecture-reference.jpg) | 本人头像身份；头顶黑鸟的白色大眼、黄色喙和黑色身体 | v1.1.0 源 ZIP 的 `个人视觉参考/e15b09e2c9_user-lecture-reference.jpg` |
| [writing-plans-personalized.png](writing-plans-personalized.png) | 已确认的文字密度、分组、本人举笔与黑鸟提醒 | 同 ZIP 的 `个人视觉参考/2faaee48ea_74-writing-plans-personalized-v2.png` |
| [ladder-personalized.png](ladder-personalized.png) | 已确认的选择顺序、正文解释与角色互动 | 同 ZIP 的 `个人视觉参考/d2118566b1_78-ladder-personalized-v2.png` |
| [approved-slides.pptx](../examples/approved-slides.pptx) | 实际原 PPT 第 86、90 页，保留原图、讲者备注与原文超链接 | v1.1.0 视觉教学版 PPTX 的两页子集 |

三张图仅改文件名，内容字节不变。PPT 子集保留两页 XML、图片和备注字节，去掉无关页与原文件属性；不包含其他课程人物头像、聊天截图或外部嵌入对象。它是视觉版实例，正文多数已烘焙进图像，不是分层头像母版或全文可编辑模板。[manifest.json](manifest.json) 记录来源、原包 SHA-256 和本包逐文件校验值。

公开原来源：[v1.1.0 Release](https://github.com/qihangzhang-272/ai-native-teaching-kit/releases/tag/v1.1.0) 的 `ai-native-teaching-kit-v1.1.0-original-content-and-assets.zip`、`ai-native-teaching-kit-v1.1.0-visual-slides.pptx`。完整课程仍从 Release 下载，安装技能无需先下载完整课程包。

## 相对路径调用

先定位实际加载的 `SKILL.md`，以其所在目录作为技能根目录。把路径解析为可读文件后，实际查看图片像素、打开 PPT，再向图像工具传入原文件；不能只读取本说明、把路径写进提示词或让模型凭文字猜人物。

例如复制到 `.agents/skills/build-visual-teaching/` 后，可这样给 Agent 下任务：

```text
请用 build-visual-teaching，沿用包内张启航 / BLAZE 与黑鸟身份。
以实际加载的 SKILL.md 所在目录为根，查看：
assets/user-lecture-reference.jpg
assets/writing-plans-personalized.png
assets/ladder-personalized.png
examples/approved-slides.pptx
把原头像和本页相关认可示例作为图像工具的参考输入。
先依据我提供的原始资料安排本页正文，再用人物提问、指向或提醒具体内容。
保持文字主导、充分正文、浅净背景、深色文字和适量有效标记。
原头像只提供身份，不复制周围标语；新页减少历史粗笔触与纸张纹理。
打开最终 PPT 逐页核对文字、图像、人物肢体、来源与备注。
```

Claude Code 或其他宿主安装后沿相同目录结构读取。缺文件时先检查是否只复制了 SKILL.md；这组素材已经随包提供，不应再要求作者重传头像。新内容、姿势和最终质量仍按本次材料与逐页验收决定，提供参考不保证生成结果逐像素相同。

## 使用范围与署名

这些原参考按作者明确要求公开，用于复现本课程的本人讲解者、黑鸟与教学视觉及学习制作方法。方法文字和代码的 MIT 许可不自动覆盖肖像、角色或混合课件。使用时保留「张启航 / BLAZE，AI Native Teaching Kit」和上述来源，注明修改；不得据此声称作者为新内容背书。其他品牌或身份用途按对应授权另行处理。

PPT 两页保留教学归纳及原文链接：[Writing Plans](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/writing-plans/SKILL.md)、[Ponytail](https://github.com/DietrichGebert/ponytail/blob/e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156/skills/ponytail/SKILL.md)。第三方原文、名称与各自许可仍归对应权利人；样例是教学归纳，不把原文当作本技能的执行指令。
