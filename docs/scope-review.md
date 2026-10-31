> Historical 69-entry tranche. Its admission decisions are superseded by the [complete inventory review](full-review.md) and [current decisions](../data/scope_decisions.csv). Counts below describe the earlier reading state, not current core admission.

# Scope Review of the 69 Additions

[Home](../README.md) · [Paper-by-paper CSV](../data/scope_review_69.csv) · [Related-survey comparison](../data/related_survey_comparison.csv)

Checked 30 October 2026. The 69 additions are a historical screening cohort, not 69 independently confirmed AR-image accelerators. TMLR is explicitly allowed by the author. Workshop-only records are excluded.

| Scope decision | Records |
|---|---|
| 直接改变已有AR图像生成的推理执行 | 4 |
| 设计更高效的AR图像生成器或表示 | 19 |
| AR生成或表示背景，尚不能据此声称推理加速 | 29 |
| 相关非AR掩码生成，不计入AR核心 | 6 |
| 测试时搜索预算分配，单独讨论 | 2 |
| 当前AR图像生成加速范围之外 | 3 |
| 已核发表，具体加速相关性仍待原文确认 | 6 |

23 records have confirmed mechanism relevance at the stated reading extent. This includes efficient generator design. It does not assert 23 independently checked end-to-end speedups. Six published records await a mechanism check. The master catalog retains excluded records for transparency.

The CCF grades in the CSV come from a mirrored 2026 directory document. The official host could not be retrieved. TMLR is not relabeled CCF. Findings is not a Workshop and is not relabeled as the corresponding main conference.

## Paper-by-paper decisions

| Paper | Scope | Reason |
|---|---|---|
| [CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration](https://iclr.cc/virtual/2026/poster/10008851) | 直接改变已有AR图像生成的推理执行 | 云端与设备协同解码，摘要明确报告图像生成加速。不能据此赋予标准推测采样的精确保证。 |
| [HART: Efficient Visual Generation with Hybrid Autoregressive Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) | 设计更高效的AR图像生成器或表示 | 混合离散表示和连续残差扩散构成新的图像生成器，摘要报告推理吞吐与MACs。不是保持原生成器不变的执行优化。 |
| [Adaptive Length Image Tokenization via Recurrent Allocation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/534ec8dfc0312d96e1c1b357304fadc2-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | 变长图像表示，摘要验证重建与token数量，没有给出AR生成推理加速实验。 |
| [Bridging Continuous and Discrete Tokens for Autoregressive Visual Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Bridging_Continuous_and_Discrete_Tokens_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) | AR生成或表示背景，尚不能据此声称推理加速 | TokenBridge改变连续到离散表示及预测方式，摘要主要支持重建和生成质量，尚不能确认推理节省。 |
| [CAT: Content-Adaptive Image Tokenization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/014898b821e3ce966ae1db68cb8d9966-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | 摘要明确报告的是生成模型训练吞吐，不能转写成推理吞吐。 |
| [A Spark of Vision-Language Intelligence: 2-Dimensional Autoregressive Transformer for Efficient Finegrained Image Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/674ad201bc8fa74b3c9979230aa0c63b-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | 模型深度方向的代码预测提升同尺寸模型的质量，摘要没有建立更短推理时间。 |
| [Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) | 设计更高效的AR图像生成器或表示 | 可变长度量化与位置/内容预测直接处理生成表示冗余，摘要支持生成效率改善。 |
| [Denoising Token Prediction in Masked Autoregressive Models](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html) | 设计更高效的AR图像生成器或表示 | MAR中的去噪预测设计，摘要报告图像推理速度比较。比较对象包含DiT，不能称作同一AR采样器的保持分布加速。 |
| [GPSToken: Gaussian Parameterized Spatially-adaptive Tokenization for Image Representation and Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/10831838f1cdd8fcba90188e88e7a121-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | 空间自适应表示与两阶段生成有关，已读摘要主要给出token数量和质量，尚未核实推理计时。 |
| [ImageFolder: Autoregressive Image Generation with Folded Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/hash/82519a9d318f39096ea507615c61c340-Abstract-Conference.html) | 设计更高效的AR图像生成器或表示 | token折叠直接缩短AR建模长度。已核机制相关，尚未独立核对其完整图像推理计时表。 |
| [MAGE: MAsked Generative Encoder To Unify Representation Learning and Image Synthesis](https://openaccess.thecvf.com/content/CVPR2023/html/Li_MAGE_MAsked_Generative_Encoder_To_Unify_Representation_Learning_and_Image_CVPR_2023_paper.html) | 相关非AR掩码生成，不计入AR核心 | 统一表示学习和掩码图像合成的背景，不能仅因有迭代生成就计为AR推理加速。 |
| [MAGVLT: Masked Generative Vision-and-Language Transformer](https://openaccess.thecvf.com/content/CVPR2023/html/Kim_MAGVLT_Masked_Generative_Vision-and-Language_Transformer_CVPR_2023_paper.html) | 相关非AR掩码生成，不计入AR核心 | 原摘要明确使用non-autoregressive mask prediction。即使比ARGVLT快，也须标为非AR替代。 |
| [Democratizing Text-to-Image Masked Generative Models with Compact Text-Aware One-Dimensional Tokens](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_Democratizing_Text-to-Image_Masked_Generative_Models_with_Compact_Text-Aware_One-Dimensional_Tokens_ICCV_2025_paper.html) | 相关非AR掩码生成，不计入AR核心 | TA-TiTok与MaskGen属于相关掩码生成及表示背景，不自动作为AR加速实验。 |
| [Meissonic: Revitalizing Masked Generative Transformers for Efficient High-Resolution Text-to-Image Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b7fd4aa7246ccfe46e61b52884bf1d11-Abstract-Conference.html) | 相关非AR掩码生成，不计入AR核心 | 原摘要明确是non-autoregressive text-to-image MIM。 |
| [Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) | 设计更高效的AR图像生成器或表示 | 生成前去除冗余位置，Stackformer预测代码及其位置，摘要直接讨论慢生成问题与效率。 |
| [NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) | 设计更高效的AR图像生成器或表示 | 频率顺序下的多阶段AR生成，摘要报告相对VAR的推理加速。 |
| [From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html) | 设计更高效的AR图像生成器或表示 | TensorAR的重叠窗口预测改变生成器，摘要给出质量与延迟的比较。 |
| [End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer](https://proceedings.mlr.press/v306/chu26b.html) | AR生成或表示背景，尚不能据此声称推理加速 | 摘要支持端到端tokenizer与生成器联合训练和质量，没有据此建立推理加速。 |
| [SpectralAR: Spectral Autoregressive Visual Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) | 设计更高效的AR图像生成器或表示 | 频谱序列与更少token属于高效生成器设计，不能把token数量改善等同于已核端到端延迟。 |
| [Text-Conditioned Sampling Framework for Text-to-Image Generation with Masked Generative Models](https://openaccess.thecvf.com/content/ICCV2023/html/Lee_Text-Conditioned_Sampling_Framework_for_Text-to-Image_Generation_with_Masked_Generative_Models_ICCV_2023_paper.html) | 相关非AR掩码生成，不计入AR核心 | 对掩码生成模型的token选择确有推理时间比较，属于相关非AR采样背景。 |
| [UniCompress: Token Compression for Unified Vision-Language Understanding and Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) | 设计更高效的AR图像生成器或表示 | 统一模型同时评估理解和图像生成，摘要报告推理延迟改善。只纳入图像生成部分，不能转用理解任务指标。 |
| [VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) | 设计更高效的AR图像生成器或表示 | 动态长度tokenizer与AR生成器，摘要报告推理FLOPs。FLOPs不是端到端计时。 |
| [Soft Tail-Dropping for Adaptive Visual Tokenization](https://link.springer.com/chapter/10.1007/978-3-032-37553-7_24) | 设计更高效的AR图像生成器或表示 | 变长表示连接到AR自适应长度采样，相关性成立。摘要未给出可独立复核的完整计时配置。 |
| [Vision Foundation Models as Effective Visual Tokenizers for Autoregressive Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a829e299ebc1c1615ddb09e98fb6ce8-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | 主要是表示、生成质量及训练收敛改善，三倍收敛不能算三倍推理加速。 |
| [Spectral Image Tokenizer](https://openaccess.thecvf.com/content/ICCV2025/html/Esteves_Spectral_Image_Tokenizer_ICCV_2025_paper.html) | AR生成或表示背景，尚不能据此声称推理加速 | 频谱tokenizer支持分辨率变化与部分解码，当前已读摘要不足以建立AR推理速度收益。 |
| [Autoregressive Image Generation Using Residual Quantization](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html) | 设计更高效的AR图像生成器或表示 | 残差量化缩短空间序列，摘要明确报告更快采样。 |
| [Language Model Beats Diffusion: Tokenizer is Key to Visual Generation](https://openreview.net/forum?id=gzqrANCF4g) | AR生成或表示背景，尚不能据此声称推理加速 | 视觉tokenizer和生成模型背景，本轮未读取到新的原始摘要，不提升为独立验证的加速结果。 |
| [Pixel Recurrent Neural Networks](https://proceedings.mlr.press/v48/oord16.html) | AR生成或表示背景，尚不能据此声称推理加速 | 基础像素AR生成，不是本轮发现的直接加速方法。 |
| [Generative Pretraining From Pixels](https://proceedings.mlr.press/v119/chen20s.html) | AR生成或表示背景，尚不能据此声称推理加速 | 主要研究图像自监督表示预训练，不能作为推理加速工作。 |
| [Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) | 设计更高效的AR图像生成器或表示 | 局部/全局注意力结构减少生成计算，摘要明确说明生成速度改善。 |
| [Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) | 直接改变已有AR图像生成的推理执行 | CoRe²有LlamaGen实验，学习弱模型替代部分guidance计算。仅涉及其AR图像实验，不能挪用扩散实验数字。 |
| [SoftVQ-VAE: Efficient 1-Dimensional Continuous Tokenizer](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SoftVQ-VAE_Efficient_1-Dimensional_Continuous_Tokenizer_CVPR_2025_paper.html) | 当前AR图像生成加速范围之外 | SoftVQ-VAE已读摘要的推理提速针对SiT等denoising生成器，没有确认AR加速实验。 |
| [Progress by Pieces: Test-Time Scaling for Autoregressive Image Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Park_Progress_by_Pieces_Test-Time_Scaling_for_Autoregressive_Image_Generation_CVPR_2026_paper.html) | 测试时搜索预算分配，单独讨论 | GridAR在多候选搜索中分配预算，参照Best-of-N。不是同一单轨迹AR采样规则的加速。 |
| [StructMAR: Structure-Aware Masked Autoregression for Explicit Layout Alignment in Text-to-Image Generation](https://proceedings.mlr.press/v306/cao26ab.html) | 设计更高效的AR图像生成器或表示 | StructMAR是布局条件MAR生成器，摘要报告推理速度，属于任务限定的高效生成器设计。 |
| [ScalingAR: Scaling Confidence for Autoregressive Image Generation](https://proceedings.mlr.press/v306/chen26fc.html) | 测试时搜索预算分配，单独讨论 | ScalingAR进行轨迹裁剪与guidance预算配置。token消耗与质量比较应保留其测试时搜索设置。 |
| [JetFormer: An autoregressive generative model of raw images and text](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d5a8e37f38a08c68162452dcba89ae9c-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | JetFormer是连续AR多模态基础生成器，摘要主要支持联合建模与质量。 |
| [Denoising Autoregressive Transformers for Scalable Text-to-Image Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ebd8a977883fd8d5bccf9575e873ce75-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | DART是AR与扩散混合的生成结构背景，摘要没有可据以独立确认的AR推理节省配置。 |
| [Fluid: Scaling Autoregressive Text-to-image Generative Models with Continuous Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f8e7248f3e659cfe70c6debcdae1b023-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | Fluid主要分析表示、顺序和模型扩展带来的质量变化，不能仅凭scaling解释为推理加速。 |
| [WeTok: Powerful Discrete Tokenization for High-Fidelity Visual Reconstruction](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0b2a58f2b5943b9c356f10db32073275-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | WeTok的高压缩与重建结果不能自动当作AR生成器的端到端加速。 |
| [Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html) | 设计更高效的AR图像生成器或表示 | AliTok的tokenizer/AR生成器设计，摘要明确报告更快采样，参照模型与参数规模须按原文保留。 |
| [Neural Autoregressive Distribution Estimation](https://jmlr.org/papers/v17/16-272.html) | AR生成或表示背景，尚不能据此声称推理加速 | 2016年的基础密度估计论文，不是近五年新增AR图像加速方法。 |
| [Normalizing Flows for Probabilistic Modeling and Inference](https://jmlr.org/papers/v22/19-1028.html) | AR生成或表示背景，尚不能据此声称推理加速 | 2021年的一般normalizing-flow综述，不是专门的AR图像加速综述。 |
| [Efficient High-Resolution Image Synthesis via Autoregressive Modeling in a Diffusion-Learned Continuous Latent Space](https://openreview.net/forum?id=wkNwPZ0g3G) | 已核发表，具体加速相关性仍待原文确认 | 正式TMLR目录与BibTeX已核，当前未能独立读取原始全文，不凭标题补全其具体加速机制。 |
| [Autoregressive Image Generation with Frequency Progression](https://openreview.net/forum?id=cEfd15ouQ1) | 设计更高效的AR图像生成器或表示 | FAR的频率递进与连续token生成相关。正式目录题名已核，不能用旧投稿页替代最终发表状态。 |
| [Progressive Checkerboards for Autoregressive Multiscale Image Generation](https://openreview.net/forum?id=wkCTCXo1a9) | 设计更高效的AR图像生成器或表示 | 渐进棋盘顺序提供组内并行与组间条件关系，原作者摘要讨论较少串行采样步。 |
| [Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding](https://openreview.net/forum?id=xYATz9HpE7) | 直接改变已有AR图像生成的推理执行 | 选择性Jacobi加速自回归normalizing flows，有CIFAR/AFHQ图像实验。flow不等于逐token Transformer，其结论须保留模型范围。 |
| [InfoScale: Unleashing Training-free Variable-scaled Image Generation via Effective Utilization of Information](https://openreview.net/forum?id=iB8PzxdpMf) | 当前AR图像生成加速范围之外 | InfoScale原文明确针对SDXL等扩散模型的变分辨率生成。此前误放入AR sampling目录，必须移出。 |
| [ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer](https://openreview.net/forum?id=OuFNXESoCO) | AR生成或表示背景，尚不能据此声称推理加速 | ACDiT有图像与视频实验，属于块条件扩散/AR混合结构。不是所有视觉任务都属于静态图像推理加速。 |
| [MaskBit: Embedding-free Image Generation via Bit Tokens](https://openreview.net/forum?id=NYe2JuN3v3) | 相关非AR掩码生成，不计入AR核心 | MaskBit是相关掩码生成背景，不按标准AR加速方法计数。 |
| [Scaling Autoregressive Models for Content-Rich Text-to-Image Generation](https://openreview.net/forum?id=AFDcYJKhND) | AR生成或表示背景，尚不能据此声称推理加速 | Parti是AR图像生成基础模型，现稿Introduction已引用，并非Survey新遗漏。 |
| [When Worse is Better: Navigating the Compression Generation Trade-off In Visual Tokenization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b6425ecad28e4960cb4a622beb338ffe-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | CRT研究压缩、生成建模与compute scaling。摘要中训练/计算效率与token减少不能直接转成已核端到端推理加速。 |
| [Single-pass Adaptive Image Tokenization for Minimum Program Search](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dc35c593e61f6df62db541b976d09dcf-Abstract-Conference.html) | AR生成或表示背景，尚不能据此声称推理加速 | KARL减少自适应tokenizer自身的搜索，没有确认完整AR生成推理加速。 |
| [SSDD: Single-Step Diffusion Decoder for Efficient Image Tokenization](https://link.springer.com/chapter/10.1007/978-3-032-37556-8_19) | 当前AR图像生成加速范围之外 | SSDD的已读摘要报告DiT生成提速，未确认AR生成实验。解码器蒸馏是相关背景，不计入AR核心。 |
| [Spanning Tree Autoregressive Visual Generation](https://link.springer.com/chapter/10.1007/978-3-032-36839-3_15) | AR生成或表示背景，尚不能据此声称推理加速 | STAR改变生成顺序以支持结构化前缀与补全。顺序灵活及编辑能力不等于推理加速。 |
| [DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) | 设计更高效的AR图像生成器或表示 | 多粒度token路径路由，原摘要报告生成吞吐。在线2026与书目印记2027应分别记录。 |
| [Local Autoregression with Finite-Support Random Variables for Image Generation](https://link.springer.com/chapter/10.1007/978-3-032-31654-7_12) | AR生成或表示背景，尚不能据此声称推理加速 | 有限支撑局部随机变量模型有图像生成，和现代token/scale/MAR加速的参照过程不同，不作为直接加速方法。 |
| [Breaking Codebook Redundancy for Faster Autoregressive Image Generation with Retrieval-Augmented Speculative Decoding](https://doi.org/10.1109/icassp55912.2026.11461425) | 已核发表，具体加速相关性仍待原文确认 | 正式ICASSP论文身份与题名已核。标题显示推测解码方向，完整机制和实验未独立读到，暂不计入已确认核心。 |
| [Enhancing Quantization for Visual Autoregressive Generation Via Uncertainty Identification](https://doi.org/10.1109/icassp55912.2026.11462147) | 已核发表，具体加速相关性仍待原文确认 | 正式ICASSP论文与作者页已核，不能从quantization一词判断是token量化还是数值精度压缩，也不猜测计时收益。 |
| [VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy](https://doi.org/10.1109/hpca68181.2026.11408607) | 直接改变已有AR图像生成的推理执行 | HPCA官方Main Conference页面明确给出VAR软硬件协同和减少计算的机制。硬件比较不能混同同GPU软件提速。 |
| [TMXVAR: Twin Microscaling Floating-Point Quantization for Efficient Visual Autoregressive Model Inference on FPGA](https://doi.org/10.1109/tcad.2026.3734745) | 已核发表，具体加速相关性仍待原文确认 | 正式TCAD元数据支持FPGA推理量化题名，当前具体实验和计时范围未读取，暂保留候选。 |
| [A 28nm 47.3TFLOPs/W 894mJ/Inference Visual Autoregressive Accelerator with Differential-Amplifier Speculation and Chain-Reaction-Like Parallel Generation](https://doi.org/10.1109/isscc49663.2026.11409075) | 已核发表，具体加速相关性仍待原文确认 | 正式ISSCC出版元数据已核，当前没有完整读到原文。并且ISSCC未出现在本次所得CCF目录副本。 |
| [31.4 VARSA: A Visual Autoregressive Generation Accelerator Using Performance-Scalable Multi-Precision PE-LUT and Grid-Similarity Attention Compression](https://doi.org/10.1109/isscc49663.2026.11409066) | 已核发表，具体加速相关性仍待原文确认 | 正式ISSCC出版元数据已核，当前没有完整读到原文。不能因使用VAR缩写就自动计为已验证的核心方法。 |
| [Lumina-mGPT: Flexible Photorealistic Autoregressive Text-to-Image Generation](https://doi.org/10.1007/s11263-026-02795-2) | AR生成或表示背景，尚不能据此声称推理加速 | Lumina-mGPT是AR图像生成基础模型和其他加速方法的baseline，不能自动算作独立加速方法。现稿已有名称提及。 |
| [SCALAR++: Efficient Controllable Generation via Scale-wise Visual Autoregressive Learning](https://doi.org/10.1007/s11263-026-02984-z) | AR生成或表示背景，尚不能据此声称推理加速 | SCALAR++的摘要支持参数与内存开销减少，其主任务是可控生成，当前尚未确认推理计时收益。 |
| [Nativetok: Native Visual Tokenization for Improved Image Generation](https://doi.org/10.1109/icassp55912.2026.11462037) | AR生成或表示背景，尚不能据此声称推理加速 | 已补读作者arXiv摘要，重点为因果tokenizer、重建与分层训练效率，没有从该摘要确认AR生成推理加速。正式ICASSP身份另核。 |
| [Parallel Multiscale Autoregressive Density Estimation](https://proceedings.mlr.press/v70/reed17a.html) | 设计更高效的AR图像生成器或表示 | 2017年直接针对像素AR串行采样的并行多尺度设计，具有历史机制相关性，但不属于近五年的新论文。 |
| [Image Transformer](https://proceedings.mlr.press/v80/parmar18a.html) | AR生成或表示背景，尚不能据此声称推理加速 | 2018年局部注意力AR基础模型，作为历史背景保留，不能自动当作本轮新增的直接加速实验。 |
| [Neural Discrete Representation Learning](https://proceedings.neurips.cc/paper/2017/hash/7a98af17e63a0ac09ce2e96d03992fbc-Abstract.html) | AR生成或表示背景，尚不能据此声称推理加速 | 2017年离散表示基础方法，不是独立的AR推理加速论文。 |
| [Generating Diverse High-Fidelity Images with VQ-VAE-2](https://proceedings.neurips.cc/paper/2019/hash/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Abstract.html) | AR生成或表示背景，尚不能据此声称推理加速 | 2019年分层离散表示与高保真生成背景，不计入近五年直接加速方法。 |

## Related surveys

The TMLR review *Autoregressive Models in Vision: A Survey* already discusses computational cost and efficient generation. No dedicated, formally published AR-image-acceleration survey meeting the present venue rule was established by this search. This does not establish a first-survey claim. The [comparison CSV](../data/related_survey_comparison.csv) separates published, withdrawn and preprint records.
