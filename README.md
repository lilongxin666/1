# 科研工作台：NIR · 化学计量学 · Nature 风格论文

![skills](https://img.shields.io/badge/skills-19-0ea5e9)
![focus](https://img.shields.io/badge/focus-NIR%20%7C%20Chemometrics%20%7C%20Scientific%20Writing-111827)
![license](https://img.shields.io/badge/license-Apache--2.0-2ea44f)

这是基于 [`Yuan1z0825/nature-skills`](https://github.com/Yuan1z0825/nature-skills) 整理的个人科研版本。原始 Nature Skills 能力全部保留，但日常使用入口重新组织为：**近红外光谱数据处理 → 特征选择 → 分类/回归建模 → 稳定性与统计验证 → Nature 风格科研绘图 → 论文写作与润色 → 文献与引用核验 → 投稿与审稿回复**。

> 原仓库的完整英文说明仍保留在 [README_EN.md](README_EN.md)。本页作为个人科研工作台首页使用。

## 1. 我最常用的科研流程

| 阶段 | 目标 | 优先使用的 Skill |
|---|---|---|
| 文献检索 | 找近红外、化学计量学、特征选择、模型迁移等真实文献 | [`nature-academic-search`](skills/nature-academic-search/README.md) |
| 论文精读 | 提取方法、样本、仪器、算法、图表、创新点和不足 | [`nature-reader`](skills/nature-reader/README.md) |
| 引用管理 | DOI、参考文献格式、引用真实性核验 | [`nature-citation`](skills/nature-citation/README.md) + [`nature-ref-verifier`](skills/nature-ref-verifier/README.md) |
| 数据与实验 | 整理实验数据、可重复性、实验记录与数据声明 | [`nature-data`](skills/nature-data/README.md) + [`nature-experiment-log`](skills/nature-experiment-log/README.md) |
| 统计分析 | 显著性、交叉验证、置信区间、稳定性、模型比较 | [`nature-statistics`](skills/nature-statistics/README.md) |
| 科研绘图 | 光谱图、特征频率图、模型性能图、多面板 Nature 风格图 | [`nature-figure`](skills/nature-figure/README.md) |
| 论文写作 | 摘要、引言、方法、结果、讨论、结论 | [`nature-writing`](skills/nature-writing/README.md) |
| 英文润色 | Nature / Nature Communications 风格英文 | [`nature-polishing`](skills/nature-polishing/README.md) |
| 审稿模拟 | 投稿前从审稿人视角找问题 | [`nature-reviewer`](skills/nature-reviewer/README.md) |
| 返修回复 | response letter、逐点回复、修改说明 | [`nature-response`](skills/nature-response/README.md) |

**直接进入我的 NIR 工作流：** [research-workbench/nir-chemometrics/WORKFLOW.md](research-workbench/nir-chemometrics/WORKFLOW.md)

**常用科研提示词：** [research-workbench/nir-chemometrics/PROMPTS.md](research-workbench/nir-chemometrics/PROMPTS.md)

**论文作图规范：** [research-workbench/nir-chemometrics/FIGURE_STANDARD.md](research-workbench/nir-chemometrics/FIGURE_STANDARD.md)

## 2. NIR / 化学计量学推荐研究链

```text
原始光谱 / 样本标签
        ↓
数据质量检查与异常样本识别
        ↓
预处理候选：SG / SNV / MSC / 导数 / 去趋势
        ↓
严格的数据划分与嵌套交叉验证
        ↓
特征选择：UVE / MC-UVE / CARS / SPA / BPSO / DBO 等
        ↓
分类或回归模型：SVM / PLS-DA / RF / XGBoost / PLSR 等
        ↓
稳定性分析：重复运行、特征频率、外层折波动、统计检验
        ↓
可解释性：特征波数、谱带归属、模型贡献
        ↓
Nature 风格多面板图 + 表格
        ↓
结果与讨论 → 引言回扣 → 摘要 → 投稿材料
```

### 必须坚持的建模原则

1. **特征选择只能在校准/训练数据内部进行。** 测试集标签不能参与 UVE、IAMB、PSO/DBO、参数调优或特征筛选。
2. **优先使用嵌套交叉验证。** 外层用于无偏性能估计，内层用于特征选择和超参数寻优。
3. **不要只汇报一次最优结果。** 同时报告均值、标准差、重复运行稳定性、外层折波动和特征选择频率。
4. **图与统计必须服务于科学问题。** 不为了“图好看”而增加无法解释的可视化。
5. **算法改进必须对应具体问题。** 例如稳定性不足、局部最优、特征冗余、批次漂移、仪器差异或样本干扰，而不是单纯叠加优化算法。

## 3. 核心 Skills：日常优先

日常优先使用：`nature-academic-search`、`nature-reader`、`nature-citation`、`nature-ref-verifier`、`nature-data`、`nature-experiment-log`、`nature-statistics`、`nature-figure`、`nature-writing`、`nature-polishing`、`nature-reviewer`、`nature-response`。

其余 Skills 保留为扩展能力，需要时再调用；不移动、不删除，以避免破坏上游依赖和更新机制。

## 4. 完整技能索引

> 下表保持上游仓库 CI 所需的标准索引格式，同时也是完整能力入口。

| Skill | 用途 |
|---|---|
| [`nature-academic-search`](skills/nature-academic-search/README.md) | 多源学术检索与证据链 |
| [`nature-citation`](skills/nature-citation/README.md) | 引用与参考文献管理 |
| [`nature-data`](skills/nature-data/README.md) | 数据治理与数据声明 |
| [`nature-downloader`](skills/nature-downloader/README.md) | 文献下载辅助 |
| [`nature-experiment-log`](skills/nature-experiment-log/README.md) | 实验记录与追踪 |
| [`nature-figure`](skills/nature-figure/README.md) | 投稿级科研绘图 |
| [`nature-image2ppt`](skills/nature-image2ppt/README.md) | 图片重建 PPT |
| [`nature-literature-pipeline`](skills/nature-literature-pipeline/README.md) | 文献流水线 |
| [`nature-paper-card`](skills/nature-paper-card/README.md) | 论文卡片与证据整理 |
| [`nature-paper-to-patent`](skills/nature-paper-to-patent/README.md) | 论文转专利材料 |
| [`nature-paper2ppt`](skills/nature-paper2ppt/README.md) | 论文转汇报 PPT |
| [`nature-polishing`](skills/nature-polishing/README.md) | 学术英文润色 |
| [`nature-proposal-writer`](skills/nature-proposal-writer/README.md) | 项目/基金文本 |
| [`nature-reader`](skills/nature-reader/README.md) | 论文精读与结构化拆解 |
| [`nature-ref-verifier`](skills/nature-ref-verifier/README.md) | 参考文献真实性核验 |
| [`nature-response`](skills/nature-response/README.md) | 审稿回复与返修材料 |
| [`nature-reviewer`](skills/nature-reviewer/README.md) | 投稿前审稿模拟 |
| [`nature-statistics`](skills/nature-statistics/README.md) | 统计分析与报告 |
| [`nature-writing`](skills/nature-writing/README.md) | 学术论文写作 |

共享支持包：`nature-shared`（供其他 Skill 内部读取，不作为独立触发 Skill 计入上表）。

## 5. 我的科研工作台目录

```text
research-workbench/
├─ README.md
└─ nir-chemometrics/
   ├─ WORKFLOW.md           # 从数据到论文的完整流程
   ├─ PROMPTS.md            # 可以直接复制使用的提示词
   ├─ FIGURE_STANDARD.md    # NIR / Nature 风格图规范
   └─ research-profile.yaml # 默认研究配置与原则
```

建议新项目按下面结构组织：

```text
project-name/
├─ data_raw/               # 原始数据，永不覆盖
├─ data_processed/         # 预处理结果
├─ splits/                 # 固定的数据划分
├─ models/                 # 模型与参数
├─ results/                # CSV / JSON 结果
├─ figures/                # 最终图
├─ tables/                 # 最终表
├─ scripts/                # 可重复运行代码
├─ literature/             # 关键文献与证据表
└─ manuscript/             # 论文正文与补充材料
```

## 6. 一句话启动方式

在 Codex / Agent 环境里，不必先想“应该调用哪个 Skill”，直接描述科研任务即可，例如：

```text
请按本仓库 research-workbench/nir-chemometrics/WORKFLOW.md 的规范，
分析我的近红外三分类数据。严格避免数据泄漏，使用嵌套交叉验证，
比较全光谱、稳定性特征选择和智能优化特征选择，最终输出统计结果、
Nature 风格多面板图，以及可以直接写进论文 Results and Discussion 的结论。
```

## 7. 上游项目与许可证

本仓库由开源项目 [`Yuan1z0825/nature-skills`](https://github.com/Yuan1z0825/nature-skills) 整理而来。原项目代码、资源和作者信息均保留在仓库历史与对应文件中；使用和再分发请遵循根目录 [LICENSE](LICENSE)。

---

**当前定位：不是“把所有 Skill 都用一遍”，而是把最相关的 Skill 串成一条可重复、可验证、能直接产出论文结果的科研流水线。**
