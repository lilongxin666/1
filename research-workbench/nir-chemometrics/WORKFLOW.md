# NIR / 化学计量学科研工作流

## 目标

把一次近红外研究组织成可重复、可审查、可直接写入论文的方法链，而不是零散地“跑几个算法比较准确率”。

---

## Stage 0：研究问题定义

开始写代码前先回答四个问题：

1. **研究对象是什么？** 分类、定量预测、批次迁移、仪器迁移，还是抗干扰？
2. **真正的问题是什么？** 特征冗余、模型不稳定、批次漂移、样品状态变化、仪器差异、局部最优，还是泛化能力不足？
3. **主比较对象是什么？** 全光谱、传统特征选择、智能优化特征选择、迁移/校正方法。
4. **论文最终需要证明什么？** 不只“准确率更高”，还可能是特征更少、方差更低、跨批次更稳定、计算更快或解释性更强。

输出：`research_question.md` 或论文方法设计草案。

---

## Stage 1：数据冻结与质量检查

### 1.1 原始数据只读

- 原始光谱保存于 `data_raw/`。
- 不在原始 CSV/XLSX 上直接覆盖处理结果。
- 保存样本 ID、类别/参考值、批次、仪器、采集时间和可能的干扰因素。

### 1.2 基础检查

至少检查：

- 光谱维度和波数/波长顺序
- 缺失值、无穷值、重复样本
- 标签分布
- 异常光谱
- 不同类别/批次的样本数量
- 光谱平均值、标准差和整体形状

### 1.3 数据划分先于建模

固定：

- hold-out test set，或
- 外层交叉验证折。

**从这一刻开始，外层测试标签不能参与任何预处理参数学习、特征选择或调参。**

---

## Stage 2：预处理策略

预处理作为候选方案比较，而不是默认叠加越多越好。

常见候选：

- Raw
- Savitzky–Golay smoothing
- SNV
- MSC
- 1st derivative
- 2nd derivative
- detrending
- SG + SNV / SG + derivative 等有科学依据的组合

原则：

- 任何需要从数据估计参数的预处理，只在训练折拟合。
- 不根据最终测试结果反向挑预处理。
- 论文中说明每一步预处理解决的物理/统计问题。

输出：预处理比较表 + 代表性光谱图。

---

## Stage 3：嵌套交叉验证框架

推荐：

```text
Outer CV
├─ Outer train
│  └─ Inner CV
│     ├─ preprocessing choice
│     ├─ feature selection
│     └─ model hyperparameter tuning
└─ Outer test
   └─ final unbiased evaluation only
```

### 分类任务推荐指标

- Accuracy
- Balanced Accuracy
- Macro-F1
- class-wise Precision / Recall / F1
- confusion matrix
- MCC（类别不均衡时尤其有价值）

### 回归任务推荐指标

- R²
- RMSE
- MAE
- bias
- RPD / RPIQ（视领域习惯使用）

最终报告：outer folds 的均值 ± 标准差，而不是只给一个最优数字。

---

## Stage 4：特征选择

### 4.1 基线组

必须保留全光谱模型作为 baseline。

### 4.2 传统/统计特征选择

可按问题选择：

- UVE / MC-UVE
- CARS
- SPA
- VIP
- interval methods
- 稳定性选择

### 4.3 智能优化方法

可包括：

- BPSO
- APSO
- DBO
- 改进 DBO / PSO
- 区间 + 点级联合搜索

### 4.4 对智能优化算法的论文要求

不能只说“采用某优化算法搜索最优特征”。需要回答：

- 搜索空间是什么？
- 个体编码是什么？
- fitness 同时考虑哪些目标？
- 如何限制特征数量？
- 如何避免局部最优？
- 如何处理连续谱变量的高度共线性？
- 是否在重复运行中稳定选择相同谱区？

建议 fitness：

```text
classification loss
+ λ1 × feature ratio
+ λ2 × instability penalty
```

如果研究强调稳定性，可把跨内层折/重复运行的选择一致性直接放入优化目标。

---

## Stage 5：模型训练

### 分类

优先基线：

- SVM
- PLS-DA
- Random Forest
- XGBoost / LightGBM（如适用）

### 回归

优先基线：

- PLSR
- SVR
- RF regression
- boosting regression

不要用大量模型“撒网”代替科学问题。主模型一般 1–3 个即可，其余作为补充验证。

---

## Stage 6：稳定性与统计验证

这是 NIR 特征选择论文中经常比“单次最高准确率”更重要的部分。

至少建议包含：

### 6.1 重复运行

对随机算法运行 20–50 次，记录：

- 性能分布
- 特征数分布
- 每个波数的选择频率
- 运行时间

### 6.2 外层折稳定性

记录各 outer fold：

- 选中特征数量
- 性能
- 核心谱区重合度

### 6.3 特征稳定性指标

可使用：

- Jaccard similarity
- Kuncheva index
- selection frequency
- top-k recurrent bands

### 6.4 模型比较

根据设计选择：

- paired t-test
- Wilcoxon signed-rank test
- Friedman + post-hoc
- bootstrap CI

不要把交叉验证中的大量相关预测值当作完全独立样本直接进行普通显著性检验。

---

## Stage 7：光谱解释

最终特征不能只画“红线”。需要尽可能讨论：

- 选中特征所在波数/波长
- O–H、C–H、N–H 等组合频/倍频区
- 与水分、乙醇、有机物、蛋白/淀粉等研究对象相关的可能吸收带
- 不同方法是否反复选择相似谱区

光谱归属必须由真实文献支持，避免凭经验硬解释。

推荐调用：`nature-academic-search` + `nature-ref-verifier`。

---

## Stage 8：结果图设计

建议一套研究至少包含：

1. 原始/预处理后光谱
2. 数据划分或研究流程图
3. 特征选择结果
4. 重复运行选择频率
5. 模型性能比较
6. confusion matrix 或 predicted-vs-reference
7. 稳定性/特征数分布
8. 关键谱带解释图

详见 [`FIGURE_STANDARD.md`](FIGURE_STANDARD.md)。

---

## Stage 9：论文写作顺序

推荐顺序不是从 Introduction 开始：

```text
Figures + Tables
→ Methods
→ Results
→ Discussion
→ Introduction
→ Conclusion
→ Abstract
→ Title
```

### Results 重点

回答“观察到了什么”。

### Discussion 重点

回答：

- 为什么会这样？
- 与已有方法相比真正改进在哪里？
- 为什么在不同 outer folds / 批次下仍然稳定？
- 选中特征是否有光谱学意义？
- 局限是什么？

---

## Stage 10：投稿前检查

- 测试集是否泄漏？
- 所有模型是否使用相同数据划分？
- 是否报告重复运行而非挑最好的一次？
- 图中误差条含义是否明确？
- 每个结论是否有图/表/统计依据？
- 特征谱带解释是否有真实参考文献？
- Methods 是否足够让他人复现？
- 代码随机种子和软件版本是否记录？

最后依次调用：

`nature-reviewer` → 修改 → `nature-polishing` → `nature-ref-verifier`。
