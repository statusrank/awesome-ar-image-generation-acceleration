# AR video-generation acceleration

[Home](../../README.md) · [All categories](../../papers/README.md) · [By year](../../papers/by-year.md)

Acceleration of autoregressive video generation and streaming synthesis.

**36 papers.** Titles link to recorded PDFs or the official paper page.

## Papers

- [**AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26iw.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) · [Details](../paper-notes.md#aad1video)
  - **Accelerates:** AR video denoising evaluation budget.
  - **Approach:** Asymmetric adversarial distillation trains a one-NFE causal student.

- [**Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#arcachevideo)
  - **Accelerates:** AR video diffusion recomputation.
  - **Approach:** History-guided cache timing with enhanced residual correction.

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026). [Paper](https://openreview.net/forum?id=OuFNXESoCO) · [PDF](https://arxiv.org/pdf/2412.07720) · [Details](../paper-notes.md#tmlroufnxesoco)
  - **Accelerates:** Image and video block-AR conditional diffusion.
  - **Approach:** Block-causal denoising with reusable past context.

- [**Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#avatarforcing)
  - **Accelerates:** Causal avatar-motion generation latency.
  - **Approach:** Blockwise causal diffusion forcing with KV reuse replaces a bidirectional motion generator.

- [**Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhu26bf.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) · [Details](../paper-notes.md#causalforcingvideo)
  - **Accelerates:** Few-step causal video diffusion generator.
  - **Approach:** AR-teacher ODE initialization followed by distribution-matching distillation.

- [**Context Forcing: Consistent Autoregressive Video Generation with Long Context**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26eu.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) · [Details](../paper-notes.md#contextforcingvideo)
  - **Accelerates:** AR video context-memory growth.
  - **Approach:** Bounded slow/fast memory retains selected historical frames.

- [**CubeComposer: Spatio-Temporal Autoregressive 4K 360deg Video Generation from Perspective Video**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#cubecomposervideo)
  - **Accelerates:** Autoregressive cubemap video synthesis.
  - **Approach:** Sparse context across cube faces and temporal windows.

- [**Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/yi26c.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) · [Details](../paper-notes.md#deepforcingvideo)
  - **Accelerates:** AR video historical KV storage.
  - **Approach:** Persistent sink context with importance-aware KV pruning.

- [**FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/samuel26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) · [Details](../paper-notes.md#fastarvideo)
  - **Accelerates:** AR video self/cross-attention and KV cache.
  - **Approach:** Temporal cache compression and approximate-neighbor sparse attention.

- [**Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge**](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8488454077cb0fd9d31772274c78115d-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) · [Details](../paper-notes.md#fastcarvideo)
  - **Accelerates:** AR video decoder MLP computation.
  - **Approach:** Replays cached MLP outputs with temporal attention-based selection and FPGA scheduling.

- [**FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis**](https://arxiv.org/pdf/2603.07192) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37098-3_12) · [PDF](https://arxiv.org/pdf/2603.07192) · [Details](../paper-notes.md#faststarvideo)
  - **Accelerates:** InfinityStar spatiotemporal token refinement.
  - **Approach:** Prunes converged spatial/temporal tokens with partial residual updates.

- [**Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/ma26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) · [Details](../paper-notes.md#flexforcingvideo)
  - **Accelerates:** AR video generation execution schedule.
  - **Approach:** Flexible chunks with bidirectional planning and autoregressive within-chunk inference.

- [**Flow Caching for Autoregressive Video Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/85dc8f85ff978b9c606d3b2f5b0da69a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) · [Details](../paper-notes.md#flowcachevideo)
  - **Accelerates:** AR video denoising and KV storage.
  - **Approach:** Independent chunk cache policies with bounded KV compression.

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) · [Details](../paper-notes.md#hiarvideo)
  - **Accelerates:** Hierarchical denoising and pipelined execution of AR video blocks.
  - **Approach:** Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.

- [**Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/lv26i.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) · [Details](../paper-notes.md#lightforcingvideo)
  - **Accelerates:** AR video attention.
  - **Approach:** Chunk-aware sparsity allocation with hierarchical sparse attention.

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) · [Details](../paper-notes.md#liveavatarvideo)
  - **Accelerates:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Approach:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.

- [**Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective**](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/59ad89d72559dd4ce557d56f36313724-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) · [Details](../paper-notes.md#lumos1video)
  - **Accelerates:** LLM-based AR video generation.
  - **Approach:** Frame-causal masked parallel decoding with KV cache.

- [**Motion-Aware Caching for Efficient Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/xu26an.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) · [Details](../paper-notes.md#motioncachevideo)
  - **Accelerates:** AR video diffusion denoising computation.
  - **Approach:** Motion-weighted token updates after a full-computation warmup.

- [**Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/xi26f.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) · [Details](../paper-notes.md#quantvideogen)
  - **Accelerates:** AR video KV storage.
  - **Approach:** Semantic smoothing and progressive residual cache quantization.

- [**Real-Time Motion-Controllable Autoregressive Video Diffusion**](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/71c1d6ec1f0003d8ea10bbea4291002d-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) · [Details](../paper-notes.md#ardragvideo)
  - **Accelerates:** Motion-controlled AR video diffusion.
  - **Approach:** Few-step causal distillation with motion conditioning.

- [**Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#rewardforcing)
  - **Accelerates:** Streaming AR video attention and conditional denoising.
  - **Approach:** Few-step causal distillation with a smaller attention window and fixed-size EMA sink state.

- [**Rolling Forcing: Autoregressive Long Video Diffusion in Real Time**](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) · [Details](../paper-notes.md#rollingforcingvideo)
  - **Accelerates:** Streaming AR video denoising.
  - **Approach:** Rolling-frame generation and few-step distillation with extended windows.

- [**SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer**](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b93c59da0d0f835907fd661d419db2-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) · [Details](../paper-notes.md#sanavideo)
  - **Accelerates:** Long-video AR attention and cache growth.
  - **Approach:** Linear attention with constant-memory block-causal state.

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/so26a.html) · [PDF](https://arxiv.org/pdf/2510.24211v2) · [Details](../paper-notes.md#scd)
  - **Accelerates:** AR image stochastic speculative execution.
  - **Approach:** Couples proposal/verification randomness.

- [**Streaming Autoregressive Video Generation via Diagonal Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d899eabc6c8fefd0d4064762aba407e2-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) · [Details](../paper-notes.md#diagonaldistillvideo)
  - **Accelerates:** Streaming AR video diffusion.
  - **Approach:** Diagonal distillation restructures few-step frame synthesis.

- [**Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_25) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) · [Details](../paper-notes.md#ispavideo)
  - **Accelerates:** KV-cache storage and attention computation in streaming AR video generators.
  - **Approach:** Replace selected full-attention layers with local attention after instance-specific closed-form weight modulation absorbs historical context.

- [**Towards One-step Causal Video Generation via Adversarial Self-Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3ae86071c169649bff21188c536163dc-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) · [Details](../paper-notes.md#asdcausalvideo)
  - **Accelerates:** AR video conditional denoising evaluations.
  - **Approach:** Adversarial self-distillation with extra first-frame updates.

- [**Autoregressive Video Generation without Vector Quantization**](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6e5112eaa45f8c30b242c5f576213a92-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) · [Details](../paper-notes.md#novavideo)
  - **Accelerates:** Temporal/spatial AR video generation.
  - **Approach:** Frame-wise temporal causality and set-wise spatial generation with continuous tokens.

- [**Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/gao25m.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) · [Details](../paper-notes.md#ca2vdmvideo)
  - **Accelerates:** AR video conditional-frame recomputation.
  - **Approach:** Causal feature computation and cache sharing across denoising steps.

- [**From Slow Bidirectional to Fast Autoregressive Video Diffusion Models**](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) · [Details](../paper-notes.md#causvidvideo)
  - **Accelerates:** Causal video diffusion inference.
  - **Approach:** Distills a bidirectional many-step teacher into a KV-cached causal few-step generator.

- [**MarDini: Masked Auto-regressive Diffusion for Video Generation at Scale**](https://arxiv.org/pdf/2410.20280) (TMLR, 2025). [Paper](https://openreview.net/forum?id=fuOHI59rUW) · [PDF](https://arxiv.org/pdf/2410.20280) · [Details](../paper-notes.md#mardinivideo)
  - **Accelerates:** Masked-AR video planning and spatial diffusion.
  - **Approach:** Low-resolution planning with a lightweight high-resolution diffusion model.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.10696) · [Details](../paper-notes.md#nar)
  - **Accelerates:** Image and video AR position decoding.
  - **Approach:** Neighbor expansion with dimension-oriented parallel prediction heads.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) · [Details](../paper-notes.md#par)
  - **Accelerates:** Image and video AR sequential decoding.
  - **Approach:** Generates spatially distant groups concurrently.

- [**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f4823f831af67a3ef15e41a85434422a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) · [Details](../paper-notes.md#selfforcingvideo)
  - **Accelerates:** Few-step streaming AR video generator.
  - **Approach:** Self-generated training rollouts with rolling KV-cache inference.

- [**Efficiency-optimized Video Diffusion Models**](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) (ACM MM, 2023). [Paper](https://dl.acm.org/doi/10.1145/3581783.3612406) · [PDF](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) · [Details](../paper-notes.md#evdmacmmm2023)
  - **Accelerates:** Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation.
  - **Approach:** Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017). [Paper](https://proceedings.mlr.press/v70/reed17a.html) · [PDF](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) · [Details](../paper-notes.md#parallelmultiscale2017)
  - **Accelerates:** Pixel AR sampling dependency depth.
  - **Approach:** Parallel multiscale density factorization.
