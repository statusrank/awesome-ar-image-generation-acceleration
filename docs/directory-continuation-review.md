> 本页为此前245条阶段的记录。当前结果见[213项候选核查](candidate213-review.md)。

# 本轮本地复核说明

[首页](../README.zh-CN.md) · [核心清单](../papers/core/README.md) · [逐篇来源](../papers/paper-notes.md) · [目录进度](../data/complete_directory_progress_20261031.csv)

本轮新增13条记录，当前共245条，分为148篇核心、72篇背景和25篇待核。改动仅保存在本地，等待作者复核。Survey未修改，GitHub未推送。

## 新增核心

| 论文 | 具体加速对象 | 已核原文依据及限定 |
|---|---|---|
| [OmniMamba](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_6) | 使用Mamba-2预测图像token | PDF第12–13页、表4。单张RTX 4090、FP16、batch 16、256分辨率的图像生成实验。摘要中的119.2倍属于文本输出，不用于图像提速结论 |
| [OmniForcing](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_31) | 将双向音视频教师蒸馏为少步流式AR生成器 | 第12、14页，计时协议及表1–2。完整片段runtime包括VAE和vocoder，首chunk延迟另列。属于高效AR生成器设计，教师为双向模型 |
| [PackForcing](https://link.springer.com/chapter/10.1007/978-3-032-37464-6_31) | 压缩AR视频历史KV，并选择参与注意力的历史块 | 第5–10页，历史缓存定义及压缩机制。约32倍针对中段历史token。原文另报单H200的14–16 FPS，没有据此填写完整方法加速比 |
| [Surprise Forcing](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_16) | 依据chunk难度减少条件去噪更新 | 第12–15页、表1和表4。15.8%在正文中解释为去噪计算减少。完整配置的FPS低于LongLive，不能写成端到端加速15.8% |
| [NaLA](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) | 以紧凑AR姿态编码及连续回归生成3D布局 | 第7–8、10、12–13页，图7d为资产数量与运行时间的比较。未从曲线估算数字，未假设各agent使用相同硬件 |
| [InteractiveAvatar](https://link.springer.com/chapter/10.1007/978-3-032-37032-7_37) | 蒸馏少步AR头像生成，并并行执行DiT与VAE | 第11、13–14页，表2含无DMD配置的1.27 FPS和完整模型的26.68 FPS。DiT和VAE部署在不同设备，不能写成单卡提速。对话TTFF另含音频响应 |
| [MPAD](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) | 将完整3D去噪改为平面AR生成，并减少后续平面的采样更新 | 第2页图1、第9页采样设置。针对跨对比度MRI体数据合成。约三倍FLOPs减少不等于三倍延迟减少 |

MPAD的完整题名为 *Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis*。图像、视频及布局任务的结果不合并排名。各论文的详细配置与尚未说明的计时内容见逐篇来源。

## 背景与待核

新增背景为Recurrent Autoregressive Diffusion及三篇Computational Visual Media论文。RAD表5的时间是训练单步时间。Multiway Transformer原文明确采用非自回归推理。CCNet的约65 FPS是绝对速度。服装动画论文的速度比较针对CPU物理模拟器ARCSim，不能解释成AR生成模型加速。

TinyHistory和InterCMDM新增为待核。前者已核到历史context token预算，尚未建立包含新增encoder的实际推理成本变化。后者报告了流式生成时间，尚未建立相对于明确AR基线的计算减少。已有STAT补充了正式PDF来源和表4，仍保持待核。其229对576的生成token数量不能转写为实测速度比。

## 逐条目录进度

- 本轮按原始目录顺序阅读3,324条题名，其中3,247条此前没有逐条阅读记录。
- ECCV 2026全部2,835个题名已读。Computational Visual Media的347条保留目录记录、ACM TACO的572条记录均已逐条看过题名。封面、目录和编辑寄语不算研究论文。
- 题名筛选表在[本轮逐条记录](../data/continuation_title_screening_20261031.csv)。逐篇原文结论在[来源决定表](../data/directory_candidate_decisions_20261031.csv)。本轮新增83项来源决定，当前共134项。本轮保留候选中仍有213项原文判断未完成，见[后续清单](../data/continuation_source_queue_20261031.csv)。

上述完成范围是题名阅读。候选论文的原文判断仍有缺口，其余会议和期刊目录也未全部逐条读完。已取回网页或PDF的记录不会自动标成已读。没有将Workshop条目纳入核心。

## 核对内容

新增记录逐篇保留正式发表页面和PDF来源。原论文复杂表格通过实际渲染页面对照，区分了文本输出与图像输出，也区分了训练时间与生成推理时间。本轮没有复现实验或独立检查全部证明。

发布前作者可先复核新增核心的任务范围。MRI合成及3D布局均有独立任务标记，不能据此自动改动静态图像Survey。
