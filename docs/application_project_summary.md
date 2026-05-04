# 相互作用 Haldane 模型 NQS/VMC 项目经历

这是我目前最完整、最满意的科研项目。项目研究半填充蜂窝格子上的相互作用 Haldane 模型：非相互作用 Haldane hopping 产生 Chern-insulator 结构，最近邻排斥相互作用推动 charge-density-wave 有序。在近临界区域，拓扑分支和电荷有序分支竞争，能量、拓扑诊断和电荷有序涨落可能不同步闭合，因此非常适合作为 NQS/VMC 的 benchmark。

我的工作包括模型定义、观测量口径整理、ED benchmark、NQS ansatz 设计、VMC 训练、strict replay、checkpoint audit、拓扑与电荷有序诊断，以及科研工程文档整理。项目中我特别强调多观测量评估，而不是只看训练最低能量。对于蜂窝格子的 A/B 子晶格粒子数不平衡，令 `Q=(N_A-N_B)/(N/2)`，使用 `CDW=<|Q|>` 和 `Q2=<Q^2>` 作为 symmetry-even amplitude diagnostics。它们不是 signed order parameter，因此有限尺寸中非零 CDW/Q2 需要结合 finite-size baseline、能量和 topology diagnostic 共同解释。

这个项目让我理解到，NQS 作为新兴量子多体算法，有机会处理传统方法难以覆盖的二维强关联和拓扑体系，但必须配合严格 benchmark、复算协议和物理观测量审计，才能形成可信的科学结论。

