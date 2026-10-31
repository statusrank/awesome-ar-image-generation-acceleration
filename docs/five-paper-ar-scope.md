# 五篇论文的AR依赖与Flow角色复核

[首页](../README.zh-CN.md) · [逐项字段与原文位置](../data/five_paper_ar_scope_recheck.csv)

当前书目255条，152核心、74背景、29待核。ActionPlan从核心转为待核。五篇均已核实为ECCV 2026正式主会论文。它们研究的是视频或3D动作，没有一篇属于本Survey当前的静态图像生成任务。下表的相关性结论对应较宽的AR视觉生成仓库范围。

|论文|生成内容的AR依赖|Flow或扩散的角色|当前结论|
|---|---|---|---|
|[ActionPlan](https://link.springer.com/chapter/10.1007/978-3-032-37225-3_30)|主文第3.4节按时间激活latent并交叠去噪，第3.1节使用因果TAE。尚未核实完整预测器的注意力访问限制|第3.3节式2采用Rectified Flow速度预测|待核。已确认流式动作生成效率，不能单凭因果TAE或顺序激活确认完整AR预测依赖|
|[GeoFlow](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_22)|第3.5节明确短期frame autoregression，每块含1参考帧和5新帧|块内使用条件Flow Matching，几何变换的历史latent构造起始分布|核心，AR驾驶视频生成加速。原文4.2倍对应特定chunk及采样预算变化|
|[Doe-2](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_29)|第3.4节式7–8由历史场景latent和动作预测下一场景|三层条件DiT采用Rectified Flow，见式11|核心中的高效混合生成器设计。表5支持压缩对推理成本的作用，不能称添加Flow头比纯AR更快|
|[ShotStream](https://link.springer.com/chapter/10.1007/978-3-032-37261-1_12)|第4.2节图4按历史镜头生成下一镜头，镜头内按chunk递推，历史由双缓存保留|多步双向教师蒸馏为四步因果条件生成器|核心中的高效AR视频生成器设计。大吞吐差距主要相对双向基线，不是已有快速AR模型的普遍提速|
|[ScaleMoGen](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_24)|第3.2节下一骨骼时间尺度依赖已生成的粗尺度token maps|已核的逐尺度bitwise预测机制中没有Flow Matching头|核心中的高效AR动作生成器设计。表6给出0.071秒，MoMask++为0.051秒，阶段更少不等于最快|

AR依赖描述的是生成内容如何条件于此前内容。Flow Matching描述条件样本如何从初始随机变量取得，两者可以出现在同一模型的不同环节。普通Flow模型求解ODE时的顺序时间步，不能单独构成AR视觉生成的准入依据。

本次重读原PDF的对应方法与实验段落，并重新打开五篇官方发表页面。没有新增独立实验或全证明检查。ActionPlan待核表示缺少完整依赖确认，不判断原算法错误。其余四篇也必须保留任务类型及新生成器设计的区别，不直接纳入当前静态图像Survey。

Survey未改动。仓库发布不表示待核项目已解决。
