# 双语校订版 / Reviewed bilingual edition

当前成品是根目录的四册：两本教材各有中文与英文版本，每册均提供PDF、LaTeX、Markdown。中文是可阅读的排印稿，保留原笔记的中英术语、数学符号和个人直觉；不是扫描图像嵌入版。

## 文件

| 版本 | PDF | 自包含LaTeX | Markdown | 彩色预览 |
|---|---|---|---|---|
| STATS 361 中文 | [PDF](../STATS361-Chinese.pdf) | [TeX](../STATS361-Chinese.tex) | [MD](../STATS361-Chinese.md) | [HTML](reviewed/STATS361-Chinese.html) |
| STATS 361 English | [PDF](../STATS361-English.pdf) | [TeX](../STATS361-English.tex) | [MD](../STATS361-English.md) | [HTML](reviewed/STATS361-English.html) |
| Brave and True 中文 | [PDF](../Brave-and-True-Chinese.pdf) | [TeX](../Brave-and-True-Chinese.tex) | [MD](../Brave-and-True-Chinese.md) | [HTML](reviewed/Brave-and-True-Chinese.html) |
| Brave and True English | [PDF](../Brave-and-True-English.pdf) | [TeX](../Brave-and-True-English.tex) | [MD](../Brave-and-True-English.md) | [HTML](reviewed/Brave-and-True-English.html) |

根目录TeX包含完整正文与样式，无需外部输入文件。日常修订应编辑`reviewed/src/`中的对应片段，再重建。Markdown公式可编辑，图形来自同一份TikZ源代码。GitHub会删除正文CSS颜色；PDF显示完整颜色。HTML预览保留颜色，但公式排版需要联网加载MathJax。PDF与LaTeX不需要该网络服务。

`src/`、`build.py`及`output/pdf/`中的早期四分册仅为历史材料，已被根目录双语版取代，其中旧译注不代表当前校核结论。原扫描PDF已按要求从当前工作树移除，来源可通过`source-manifest.json`中的原Git提交、文件名、页数和哈希追溯。

## 编辑规则

- 黑、红、蓝保留原笔色类别，不模拟扫描RGB或手写字形。
- 紫色：原手写笔记本身有错；保留原述并邻近校正。
- 橙色：缺少条件、字迹不清、简写有歧义或仍待确认；不自动意味着原命题为假。
- 识别、翻译错误直接改正，只记入审计，不添加彩色纠错框。

个人批注以其确实出现在手写稿为依据，不声称该内容一定没有出现在教材中。左右页按内容与箭头接续，不套用统一奇偶页规则。中英文共享公式、校注type/ID、原色与箭头结构；必要的文字标签作语言替换。

## 审计与复核

| 来源笔记 | 覆盖与原色/箭头 | 审计JSON | 独立复核 |
|---|---|---|---|
| STATS 361，第1–10讲，58页 | [覆盖](reviewed/stats1-coverage.md) | [记录](reviewed/stats1-findings.json) | [重点数学复核](reviewed/stats1-independent-review.md) |
| STATS 361，第11–14讲，31页 | [覆盖](reviewed/stats2-coverage.md) | [记录](reviewed/stats2-findings.json) | [复核](reviewed/stats2-independent-review.md) |
| Brave and True，第1–23章，40页 | [覆盖](reviewed/brave1-coverage.md) | [记录](reviewed/brave1-findings.json) | [复核](reviewed/brave1-independent-review.md) |
| Brave and True，第24–25章及附录，14页 | [覆盖](reviewed/brave2-coverage.md) | [记录](reviewed/brave2-findings.json) | [复核](reviewed/brave2-independent-review.md) |

记录包括页码、问题类别、判断、修正或限定、置信度和原始资料链接。校注旁的ID用于回查记录；同一问题在原稿中重复出现时，可重复引用同一ID。直接修译只记录在JSON。独立复核范围以各报告为准；这些检查不保证穷尽所有错误。

[来源清单](reviewed/source-manifest.json)保留删除扫描前核对的页数与SHA-256。[验证报告](reviewed/verification.json)检查四册的校注ID、实际PDF颜色、图像引用、页边界、目录链接和中英文陈列公式结构。

## 重建

需要Python 3及Pillow、pypdf、pdfplumber；XeLaTeX/TeX Live（含ctex、Fandol字体和所列宏包）；Poppler的`pdftoppm`；Pandoc。西文字体为TeX Gyre Pagella、TeX Gyre Heros、Latin Modern Mono，中文采用Fandol。

在仓库根目录运行：

```sh
python english/build_bilingual.py --pandoc /path/to/pandoc
python english/verify_reviewed.py
```

Pandoc在PATH时可省略参数。构建单册可指定`stats`、`brave`、`stats-zh`或`brave-zh`。每册运行XeLaTeX三次以稳定目录和链接，并单独渲染TikZ图供Markdown使用。`build_reviewed.py`提供共享的构建与转换函数。临时编译和渲染文件在被Git忽略的`tmp/`中。

不需要原扫描即可重建排印版。源扫描移除后，验证程序使用保留的来源清单核对覆盖范围，并检查当前树中不再含这些扫描文件。

Documents工作区与Git克隆区仅在完整任务完成后统一同步；最终成品、源码及审计记录在两边保持一致。
