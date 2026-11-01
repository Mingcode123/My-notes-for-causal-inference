# Notes on Causal Inference

[English](#notes-on-causal-inference) · [中文](#因果推断学习笔记)

These links contain my personal notes on studying causal inference, and I’m delighted to share them with you. The original notes are written in a mix of Chinese and English.

[Read and download](#read-and-download) · [Contents](#contents) · [Topic index](#topic-index) · [References](#references)

## Read and download

[Read online](https://mingcode123.github.io/My-notes-for-causal-inference/website/) · [Offline website files](website/index.html).

| Textbook | English PDF | English Markdown | Chinese PDF | Chinese Markdown |
|---|---|---|---|---|
| STATS 361 | [PDF](STATS361-English.pdf) | [Markdown](STATS361-English.md) | [PDF](STATS361-Chinese.pdf) | [Markdown](STATS361-Chinese.md) |
| Brave and True | [PDF](Brave-and-True-English.pdf) | [Markdown](Brave-and-True-English.md) | [PDF](Brave-and-True-Chinese.pdf) | [Markdown](Brave-and-True-Chinese.md) |

## Contents

Expand a textbook to browse its chapters. Each link opens the corresponding section in the English notes.

<details>
<summary>STATS 361 — 14 lectures</summary>

| Lecture | Topic |
|---|---|
| 1 | [Randomized Controlled Trials](STATS361-English.md#lecture-1-randomized-controlled-trials) |
| 2 | [Unconfoundedness and the Propensity Score](STATS361-English.md#lecture-2-unconfoundedness-and-the-propensity-score) |
| 3 | [Efficient Treatment Effect Estimation via Augmented IPW](STATS361-English.md#lecture-3-efficient-treatment-effect-estimation-via-augmented-ipw) |
| 4 | [Estimating Treatment Heterogeneity](STATS361-English.md#lecture-4-estimating-treatment-heterogeneity) |
| 5 | [Regression Discontinuity Designs](STATS361-English.md#lecture-5-regression-discontinuity-designs) |
| 6 | [Finite-Sample Inference in RDDs](STATS361-English.md#lecture-6-finite-sample-inference-in-rdds) |
| 7 | [Balancing Estimators](STATS361-English.md#lecture-7-balancing-estimators) |
| 8 | [Methods for Panel Data](STATS361-English.md#lecture-8-methods-for-panel-data) |
| 9 | [Instrumental variables regression](STATS361-English.md#lecture-9-instrumental-variables-regression) |
| 10 | [Local average treatment effects](STATS361-English.md#lecture-10-local-average-treatment-effects) |
| 11 | [Policy learning](STATS361-English.md#lecture-11-policy-learning) |
| 12 | [Evaluating dynamic policies](STATS361-English.md#lecture-12-evaluating-dynamic-policies) |
| 13 | [Structural equation modeling](STATS361-English.md#lecture-13-structural-equation-modeling) |
| 14 | [Adaptive experiments](STATS361-English.md#lecture-14-adaptive-experiments) |

</details>

<details>
<summary>Brave and True — 25 chapters and appendix</summary>

| Chapter | Topic |
|---|---|
| 1 | [Introduction to causality](Brave-and-True-English.md#chapter-1-introduction-to-causality) |
| 2 | [Randomized experiments](Brave-and-True-English.md#chapter-2-randomized-experiments) |
| 3 | [A review of statistics](Brave-and-True-English.md#chapter-3-a-review-of-statistics) |
| 4 | [Graphical causal models](Brave-and-True-English.md#chapter-4-graphical-causal-models) |
| 5 | [The usefulness of linear regression](Brave-and-True-English.md#chapter-5-the-usefulness-of-linear-regression) |
| 6 | [Grouping and dummy regression](Brave-and-True-English.md#chapter-6-grouping-and-dummy-regression) |
| 7 | [Beyond controlling for confounders](Brave-and-True-English.md#chapter-7-beyond-controlling-for-confounders) |
| 8 | [Instrumental variables](Brave-and-True-English.md#chapter-8-instrumental-variables) |
| 9 | [Noncompliance and local average treatment effects](Brave-and-True-English.md#chapter-9-noncompliance-and-local-average-treatment-effects) |
| 10 | [Matching](Brave-and-True-English.md#chapter-10-matching) |
| 11 | [Propensity scores](Brave-and-True-English.md#chapter-11-propensity-scores) |
| 12 | [Doubly robust estimation](Brave-and-True-English.md#chapter-12-doubly-robust-estimation) |
| 13 | [Difference-in-differences](Brave-and-True-English.md#chapter-13-difference-in-differences) |
| 14 | [Panel data and fixed effects](Brave-and-True-English.md#chapter-14-panel-data-and-fixed-effects) |
| 15 | [Synthetic control](Brave-and-True-English.md#chapter-15-synthetic-control) |
| 16 | [Regression discontinuity design](Brave-and-True-English.md#chapter-16-regression-discontinuity-design) |
| 17 | [Predictive Models 101](Brave-and-True-English.md#chapter-17-predictive-models-101) |
| 18 | [Heterogeneous treatment effects and personalization](Brave-and-True-English.md#chapter-18-heterogeneous-treatment-effects-and-personalization) |
| 19 | [Evaluating causal models](Brave-and-True-English.md#chapter-19-evaluating-causal-models) |
| 20 | [Plug-and-play estimators](Brave-and-True-English.md#chapter-20-plug-and-play-estimators) |
| 21 | [Meta-learners](Brave-and-True-English.md#chapter-21-meta-learners) |
| 22 | [Debiased / orthogonal machine learning](Brave-and-True-English.md#chapter-22-debiased--orthogonal-machine-learning) |
| 23 | [Effect heterogeneity and nonlinearity](Brave-and-True-English.md#chapter-23-effect-heterogeneity-and-nonlinearity) |
| 24 | [The Difference-in-Differences Saga](Brave-and-True-English.md#chapter-24-the-difference-in-differences-saga) |
| 25 | [Synthetic Difference-in-Differences](Brave-and-True-English.md#chapter-25-synthetic-difference-in-differences) |
| Appendix | [Debiasing and Prediction](Brave-and-True-English.md#appendix-debiasing-and-prediction) |

</details>

## Topic index

| Topic | STATS 361 | Brave and True |
|---|---|---|
| Randomized experiments and regression adjustment | [L1](STATS361-English.md#lecture-1-randomized-controlled-trials) | [Ch. 2](Brave-and-True-English.md#chapter-2-randomized-experiments) · [Ch. 5](Brave-and-True-English.md#chapter-5-the-usefulness-of-linear-regression) · [Ch. 6](Brave-and-True-English.md#chapter-6-grouping-and-dummy-regression) |
| Propensity scores, matching, and balance | [L2](STATS361-English.md#lecture-2-unconfoundedness-and-the-propensity-score) · [L7](STATS361-English.md#lecture-7-balancing-estimators) | [Ch. 10](Brave-and-True-English.md#chapter-10-matching) · [Ch. 11](Brave-and-True-English.md#chapter-11-propensity-scores) |
| Doubly robust estimation and AIPW | [L3](STATS361-English.md#lecture-3-efficient-treatment-effect-estimation-via-augmented-ipw) | [Ch. 12](Brave-and-True-English.md#chapter-12-doubly-robust-estimation) |
| Treatment heterogeneity and causal machine learning | [L4](STATS361-English.md#lecture-4-estimating-treatment-heterogeneity) | [Ch. 18](Brave-and-True-English.md#chapter-18-heterogeneous-treatment-effects-and-personalization) · [Ch. 20](Brave-and-True-English.md#chapter-20-plug-and-play-estimators) · [Ch. 21](Brave-and-True-English.md#chapter-21-meta-learners) · [Ch. 22](Brave-and-True-English.md#chapter-22-debiased--orthogonal-machine-learning) · [Ch. 23](Brave-and-True-English.md#chapter-23-effect-heterogeneity-and-nonlinearity) |
| Regression discontinuity | [L5](STATS361-English.md#lecture-5-regression-discontinuity-designs) · [L6](STATS361-English.md#lecture-6-finite-sample-inference-in-rdds) | [Ch. 16](Brave-and-True-English.md#chapter-16-regression-discontinuity-design) |
| Panel data and difference-in-differences | [L8](STATS361-English.md#lecture-8-methods-for-panel-data) | [Ch. 13](Brave-and-True-English.md#chapter-13-difference-in-differences) · [Ch. 14](Brave-and-True-English.md#chapter-14-panel-data-and-fixed-effects) · [Ch. 24](Brave-and-True-English.md#chapter-24-the-difference-in-differences-saga) |
| Synthetic control and synthetic DiD | [L8: interactive models](STATS361-English.md#interactive-panel-models) | [Ch. 15](Brave-and-True-English.md#chapter-15-synthetic-control) · [Ch. 25](Brave-and-True-English.md#chapter-25-synthetic-difference-in-differences) |
| Instrumental variables and LATE | [L9](STATS361-English.md#lecture-9-instrumental-variables-regression) · [L10](STATS361-English.md#lecture-10-local-average-treatment-effects) | [Ch. 8](Brave-and-True-English.md#chapter-8-instrumental-variables) · [Ch. 9](Brave-and-True-English.md#chapter-9-noncompliance-and-local-average-treatment-effects) |
| Causal graphs and structural equations | [L13](STATS361-English.md#lecture-13-structural-equation-modeling) | [Ch. 4](Brave-and-True-English.md#chapter-4-graphical-causal-models) |
| Policy learning and dynamic policies | [L11](STATS361-English.md#lecture-11-policy-learning) · [L12](STATS361-English.md#lecture-12-evaluating-dynamic-policies) | — |
| Adaptive experiments | [L14](STATS361-English.md#lecture-14-adaptive-experiments) | — |
| Prediction and causal-model evaluation | — | [Ch. 17](Brave-and-True-English.md#chapter-17-predictive-models-101) · [Ch. 19](Brave-and-True-English.md#chapter-19-evaluating-causal-models) · [Appendix](Brave-and-True-English.md#appendix-debiasing-and-prediction) |

## References

- Matheus Facure Alves, [Causal Inference for The Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html).
- Stefan Wager, [STATS 361: Causal Inference](https://web.stanford.edu/~swager/stats361.pdf).

---

# 因果推断学习笔记

[English](#notes-on-causal-inference) · [中文](#因果推断学习笔记)

这里是我学习因果推断时的个人笔记，很高兴与你分享。原笔记以中英文混合书写。

[阅读与下载](#阅读与下载) · [内容目录](#内容目录) · [主题索引](#主题索引) · [参考教材](#参考教材)

## 阅读与下载

[在线阅读](https://mingcode123.github.io/My-notes-for-causal-inference/website/) · [离线网站文件](website/index.html)。

| 教材 | 英文 PDF | 英文 Markdown | 中文 PDF | 中文 Markdown |
|---|---|---|---|---|
| STATS 361 | [PDF](STATS361-English.pdf) | [Markdown](STATS361-English.md) | [PDF](STATS361-Chinese.pdf) | [Markdown](STATS361-Chinese.md) |
| Brave and True | [PDF](Brave-and-True-English.pdf) | [Markdown](Brave-and-True-English.md) | [PDF](Brave-and-True-Chinese.pdf) | [Markdown](Brave-and-True-Chinese.md) |

## 内容目录

展开教材查看各章目录，点击标题可跳转到中文版笔记的对应位置。

<details>
<summary>STATS 361：14讲</summary>

| 讲次 | 内容 |
|---|---|
| 1 | [随机对照试验](STATS361-Chinese.md#第-1-讲随机对照试验) |
| 2 | [无混杂性与倾向得分](STATS361-Chinese.md#第-2-讲无混杂性与倾向得分) |
| 3 | [通过增广 IPW 高效估计处理效应](STATS361-Chinese.md#第-3-讲通过增广-ipw-高效估计处理效应) |
| 4 | [估计处理效应的异质性](STATS361-Chinese.md#第-4-讲估计处理效应的异质性) |
| 5 | [断点回归设计](STATS361-Chinese.md#第-5-讲断点回归设计) |
| 6 | [断点回归的有限样本推断](STATS361-Chinese.md#第-6-讲断点回归的有限样本推断) |
| 7 | [平衡估计量](STATS361-Chinese.md#第-7-讲平衡估计量) |
| 8 | [面板数据方法](STATS361-Chinese.md#第-8-讲面板数据方法) |
| 9 | [工具变量回归](STATS361-Chinese.md#第-9-讲工具变量回归) |
| 10 | [局部平均处理效应](STATS361-Chinese.md#第-10-讲局部平均处理效应) |
| 11 | [策略学习](STATS361-Chinese.md#第-11-讲策略学习) |
| 12 | [动态策略评估](STATS361-Chinese.md#第-12-讲动态策略评估) |
| 13 | [结构方程建模](STATS361-Chinese.md#第-13-讲结构方程建模) |
| 14 | [自适应实验](STATS361-Chinese.md#第-14-讲自适应实验) |

</details>

<details>
<summary>Brave and True：25章与附录</summary>

| 章节 | 内容 |
|---|---|
| 1 | [因果推断入门](Brave-and-True-Chinese.md#第1章因果推断入门) |
| 2 | [随机实验](Brave-and-True-Chinese.md#第2章随机实验) |
| 3 | [统计学回顾](Brave-and-True-Chinese.md#第3章统计学回顾) |
| 4 | [图模型](Brave-and-True-Chinese.md#第4章图模型) |
| 5 | [线性回归的作用](Brave-and-True-Chinese.md#第5章线性回归的作用) |
| 6 | [分组与虚拟变量回归](Brave-and-True-Chinese.md#第6章分组与虚拟变量回归) |
| 7 | [控制混杂因素之外](Brave-and-True-Chinese.md#第7章控制混杂因素之外) |
| 8 | [工具变量](Brave-and-True-Chinese.md#第8章工具变量) |
| 9 | [不依从与局部平均处理效应](Brave-and-True-Chinese.md#第9章不依从与局部平均处理效应) |
| 10 | [匹配](Brave-and-True-Chinese.md#第10章匹配) |
| 11 | [倾向得分](Brave-and-True-Chinese.md#第11章倾向得分) |
| 12 | [双重稳健估计](Brave-and-True-Chinese.md#第12章双重稳健估计) |
| 13 | [双重差分](Brave-and-True-Chinese.md#第13章双重差分) |
| 14 | [面板数据与固定效应](Brave-and-True-Chinese.md#第14章面板数据与固定效应) |
| 15 | [合成控制](Brave-and-True-Chinese.md#第15章合成控制) |
| 16 | [断点回归设计](Brave-and-True-Chinese.md#第16章断点回归设计) |
| 17 | [预测模型基础](Brave-and-True-Chinese.md#第17章预测模型基础) |
| 18 | [异质处理效应与个性化](Brave-and-True-Chinese.md#第18章异质处理效应与个性化) |
| 19 | [评价因果模型](Brave-and-True-Chinese.md#第19章评价因果模型) |
| 20 | [即插即用估计量](Brave-and-True-Chinese.md#第20章即插即用估计量) |
| 21 | [元学习器](Brave-and-True-Chinese.md#第21章元学习器) |
| 22 | [去偏／正交机器学习](Brave-and-True-Chinese.md#第22章去偏正交机器学习) |
| 23 | [效应异质性与非线性](Brave-and-True-Chinese.md#第23章效应异质性与非线性) |
| 24 | [双重差分的发展与问题](Brave-and-True-Chinese.md#第24章双重差分的发展与问题) |
| 25 | [合成双重差分](Brave-and-True-Chinese.md#第25章合成双重差分) |
| 附录 | [去偏与预测](Brave-and-True-Chinese.md#附录去偏与预测) |

</details>

## 主题索引

| 主题 | STATS 361 | Brave and True |
|---|---|---|
| 随机实验与回归调整 | [第1讲](STATS361-Chinese.md#第-1-讲随机对照试验) | [第2章](Brave-and-True-Chinese.md#第2章随机实验) · [第5章](Brave-and-True-Chinese.md#第5章线性回归的作用) · [第6章](Brave-and-True-Chinese.md#第6章分组与虚拟变量回归) |
| 倾向得分、匹配与平衡 | [第2讲](STATS361-Chinese.md#第-2-讲无混杂性与倾向得分) · [第7讲](STATS361-Chinese.md#第-7-讲平衡估计量) | [第10章](Brave-and-True-Chinese.md#第10章匹配) · [第11章](Brave-and-True-Chinese.md#第11章倾向得分) |
| 双重稳健估计与 AIPW | [第3讲](STATS361-Chinese.md#第-3-讲通过增广-ipw-高效估计处理效应) | [第12章](Brave-and-True-Chinese.md#第12章双重稳健估计) |
| 处理效应异质性与因果机器学习 | [第4讲](STATS361-Chinese.md#第-4-讲估计处理效应的异质性) | [第18章](Brave-and-True-Chinese.md#第18章异质处理效应与个性化) · [第20章](Brave-and-True-Chinese.md#第20章即插即用估计量) · [第21章](Brave-and-True-Chinese.md#第21章元学习器) · [第22章](Brave-and-True-Chinese.md#第22章去偏正交机器学习) · [第23章](Brave-and-True-Chinese.md#第23章效应异质性与非线性) |
| 断点回归 | [第5讲](STATS361-Chinese.md#第-5-讲断点回归设计) · [第6讲](STATS361-Chinese.md#第-6-讲断点回归的有限样本推断) | [第16章](Brave-and-True-Chinese.md#第16章断点回归设计) |
| 面板数据与双重差分 | [第8讲](STATS361-Chinese.md#第-8-讲面板数据方法) | [第13章](Brave-and-True-Chinese.md#第13章双重差分) · [第14章](Brave-and-True-Chinese.md#第14章面板数据与固定效应) · [第24章](Brave-and-True-Chinese.md#第24章双重差分的发展与问题) |
| 合成控制与合成双重差分 | [第8讲：交互效应](STATS361-Chinese.md#交互效应面板模型) | [第15章](Brave-and-True-Chinese.md#第15章合成控制) · [第25章](Brave-and-True-Chinese.md#第25章合成双重差分) |
| 工具变量与局部平均处理效应 | [第9讲](STATS361-Chinese.md#第-9-讲工具变量回归) · [第10讲](STATS361-Chinese.md#第-10-讲局部平均处理效应) | [第8章](Brave-and-True-Chinese.md#第8章工具变量) · [第9章](Brave-and-True-Chinese.md#第9章不依从与局部平均处理效应) |
| 因果图与结构方程 | [第13讲](STATS361-Chinese.md#第-13-讲结构方程建模) | [第4章](Brave-and-True-Chinese.md#第4章图模型) |
| 策略学习与动态策略 | [第11讲](STATS361-Chinese.md#第-11-讲策略学习) · [第12讲](STATS361-Chinese.md#第-12-讲动态策略评估) | — |
| 自适应实验 | [第14讲](STATS361-Chinese.md#第-14-讲自适应实验) | — |
| 预测与因果模型评价 | — | [第17章](Brave-and-True-Chinese.md#第17章预测模型基础) · [第19章](Brave-and-True-Chinese.md#第19章评价因果模型) · [附录](Brave-and-True-Chinese.md#附录去偏与预测) |

## 参考教材

- Matheus Facure Alves, [Causal Inference for The Brave and True](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)。
- Stefan Wager, [STATS 361: Causal Inference](https://web.stanford.edu/~swager/stats361.pdf)。
