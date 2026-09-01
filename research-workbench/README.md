# 个人科研工作台

这个目录用于把 Nature Skills 从“技能集合”变成“可以直接执行的科研流程”。

## 当前主工作流

### 1. NIR / 化学计量学

入口：[`nir-chemometrics/WORKFLOW.md`](nir-chemometrics/WORKFLOW.md)

适用于：

- 近红外光谱分类与回归
- 白酒、基酒、酒醅等光谱数据
- 特征波长/波数选择
- UVE、MC-UVE、CARS、SPA、BPSO、DBO 等特征选择或优化方法
- SVM、PLS-DA、RF、XGBoost、PLSR 等建模
- 嵌套交叉验证、重复运行与稳定性评估
- 仪器差异、批次漂移、样品状态扰动与模型鲁棒性
- Nature 风格科研绘图与论文写作

## 使用原则

1. **先定义科学问题，再选算法。**
2. **数据划分优先于特征选择和调参。**
3. **测试集保持完全隔离。**
4. **所有图都应能回答一个论文问题。**
5. **所有结论都应能追溯到表格、图、统计或真实文献。**
6. **优先可重复性，而不是单次最好成绩。**

## 推荐调用顺序

`nature-academic-search` → `nature-reader` → `nature-data` / `nature-experiment-log` → `nature-statistics` → `nature-figure` → `nature-writing` → `nature-polishing` → `nature-ref-verifier` → `nature-reviewer` / `nature-response`

后续如果增加新的研究方向，可以在本目录下继续新增独立工作流，而不用改动原始 `skills/` 目录。
