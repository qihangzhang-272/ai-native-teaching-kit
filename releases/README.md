# 公开版交付与分发

文本与技能已经公开。七件独立公开版文件已制作、通过检验并完成 Release 上传。附件下载以[正式发布的 Release](https://github.com/qihangzhang-272/ai-native-teaching-kit/releases)为准；本页只列公开版交付内容，不提供未发布草稿的下载地址。

## 七件交付文件

| 文件名 | 内容 | 大小（字节） |
| --- | --- | ---: |
| `ai-native-teaching-kit-v1.0.0-visual-slides.pptx` | 视觉教学版，109 页 | 14,369,185 |
| `ai-native-teaching-kit-v1.0.0-visual-slides.pdf` | 视觉教学版，109 页 | 16,834,677 |
| `ai-native-teaching-kit-v1.0.0-editable-slides.pptx` | 文字可编辑版，109 页 | 633,721 |
| `ai-native-teaching-kit-v1.0.0-editable-slides.pdf` | 文字可编辑版，109 页 | 3,321,783 |
| `ai-native-teaching-kit-v1.0.0-lecture-notes.docx` | 讲课稿 | 97,895 |
| `ai-native-teaching-kit-v1.0.0-student-handbook.docx` | 学生参考手册 | 3,034,065 |
| `ai-native-teaching-kit-v1.0.0-original-content-and-assets.zip` | 课程内容与原创素材 | 3,530,337 |

视觉版用于投影和整页阅读，文字可编辑版用于修改正文、备注及来源链接。讲课稿补充口述展开与转场，学生参考手册用于课后阅读，内容包用于复用课程内容和纳入公开范围的原创素材。

这些文件是独立整理的公开版。原 v6 课件、原始素材包和其他未纳入公开范围的文件完整保留，不作为 Release 附件。

公开版保留原创正文、布局及已允许的作者视觉，排除第三方图片和头像，以独立设计的原创教学示意替换必要图层，并保留来源链接。生成的示意不标为真实界面、作者原图或实测结果。具体范围见 [许可说明](../LICENSE-SCOPE.md) 与附件中的素材说明。

## 下载校验

以下 SHA-256 来自已上传附件的元数据，可用于核对下载文件。

```text
5b08b4845e49991576c8dbabd072678d72604d3dbec9926dd64d933f0a35b87e  ai-native-teaching-kit-v1.0.0-visual-slides.pptx
90c6dc71e1105594761733b1b9cc3e0cf93bd2db65f9fd6266394a53617bb0ca  ai-native-teaching-kit-v1.0.0-visual-slides.pdf
e23abd64dc606b667ed224dbdf0509d1c9343168f655986a9f0282f938b38eeb  ai-native-teaching-kit-v1.0.0-editable-slides.pptx
3664f0d056a2dd4c82c7e52256c7b04c3c1dca3c233424896cb449ada958bba6  ai-native-teaching-kit-v1.0.0-editable-slides.pdf
c291968793b006c00def6337779a23095e82009163ef84d08e324ad8158e8d03  ai-native-teaching-kit-v1.0.0-lecture-notes.docx
2cb11b8e3d623e544fca79abe1ee9bfb3e778a2de071829ae3158370e7e85de4  ai-native-teaching-kit-v1.0.0-student-handbook.docx
70b31661224ab9627fddcf7952479caa3b5b240747812decd6ec63cc97fc8731  ai-native-teaching-kit-v1.0.0-original-content-and-assets.zip
```

## 按版本配套使用

同一 Release 的 PPTX、PDF、讲稿、手册与内容包配套使用，避免混入原版或其他版本。发布后核对七件附件能正常下载和打开，见 [发布检查清单](../RELEASE-CHECKLIST.md)。

仓库跟踪文本、来源、技能和经过审核的预览，课程二进制放在版本化 Release 中，方便读者按需下载并减少 Git 历史负担。当前采用这一分发方式，无需引入 LFS。[GitHub 大文件说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)、[Release 说明](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)。
