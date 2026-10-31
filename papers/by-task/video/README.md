# Video Generation Acceleration

[Home](../../../README.md) · [By output](../README.md) · [Mechanisms](../../README.md)

**43 acceleration papers.**

## image; video

<a id="paper-tmlroufnxesoco"></a>

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026).
  - **Focus:** Image and video block-AR conditional diffusion.
  - **Mechanism:** Block-causal denoising with reusable past context.
  - **Source location:** PDF p. 10.

<a id="paper-scd"></a>

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026).
  - **Focus:** AR image stochastic speculative execution.
  - **Mechanism:** Couples proposal/verification randomness.
  - **Source location:** PDF p. 1.

<a id="paper-nar"></a>

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025).
  - **Focus:** Image and video AR position decoding.
  - **Mechanism:** Neighbor expansion with dimension-oriented parallel prediction heads.
  - **Source location:** PDF p. 8.

<a id="paper-par"></a>

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025).
  - **Focus:** Image and video AR sequential decoding.
  - **Mechanism:** Generates spatially distant groups concurrently.
  - **Source location:** PDF p. 1.

<a id="paper-parallelmultiscale2017"></a>

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017).
  - **Focus:** Pixel AR sampling dependency depth.
  - **Mechanism:** Parallel multiscale density factorization.
  - **Source location:** PDF p. 8.

## video

<a id="paper-aad1video"></a>

- [**AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) (ICML, 2026).
  - **Focus:** AR video denoising evaluation budget.
  - **Mechanism:** Asymmetric adversarial distillation trains a one-NFE causal student.
  - **Source location:** PDF p. 6.

<a id="paper-arcachevideo"></a>

- [**Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** AR video diffusion recomputation.
  - **Mechanism:** History-guided cache timing with enhanced residual correction.
  - **Source location:** PDF p. 1.

<a id="paper-causalforcingvideo"></a>

- [**Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) (ICML, 2026).
  - **Focus:** Few-step causal video diffusion generator.
  - **Mechanism:** AR-teacher ODE initialization followed by distribution-matching distillation.
  - **Source location:** PDF p. 8.

<a id="paper-contextforcingvideo"></a>

- [**Context Forcing: Consistent Autoregressive Video Generation with Long Context**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) (ICML, 2026).
  - **Focus:** AR video context-memory growth.
  - **Mechanism:** Bounded slow/fast memory retains selected historical frames.
  - **Source location:** PDF p. 6.

<a id="paper-deepforcingvideo"></a>

- [**Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) (ICML, 2026).
  - **Focus:** AR video historical KV storage.
  - **Mechanism:** Persistent sink context with importance-aware KV pruning.
  - **Source location:** PDF p. 1.

<a id="paper-fastarvideo"></a>

- [**FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) (ICML, 2026).
  - **Focus:** AR video self/cross-attention and KV cache.
  - **Mechanism:** Temporal cache compression and approximate-neighbor sparse attention.
  - **Source location:** PDF p. 7.

<a id="paper-fastcarvideo"></a>

- [**Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge**](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** AR video decoder MLP computation.
  - **Mechanism:** Replays cached MLP outputs with temporal attention-based selection and FPGA scheduling.
  - **Source location:** PDF p. 8.

<a id="paper-faststarvideo"></a>

- [**FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis**](https://arxiv.org/pdf/2603.07192) (ECCV, 2026).
  - **Focus:** InfinityStar spatiotemporal token refinement.
  - **Mechanism:** Prunes converged spatial/temporal tokens with partial residual updates.
  - **Source location:** PDF p. 1.

<a id="paper-flexforcingvideo"></a>

- [**Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) (ICML, 2026).
  - **Focus:** AR video generation execution schedule.
  - **Mechanism:** Flexible chunks with bidirectional planning and autoregressive within-chunk inference.
  - **Source location:** PDF p. 6.

<a id="paper-flowcachevideo"></a>

- [**Flow Caching for Autoregressive Video Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** AR video denoising and KV storage.
  - **Mechanism:** Independent chunk cache policies with bounded KV compression.
  - **Source location:** PDF p. 9.

<a id="paper-hiarvideo"></a>

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026).
  - **Focus:** Hierarchical denoising and pipelined execution of AR video blocks.
  - **Mechanism:** Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.
  - **Source location:** PDF p. 9, Table 1 and Section 4.1; PDF pp. 10–11, Section 4.2.

<a id="paper-interactiveavatarvideo"></a>

- [**InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars**](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) (ECCV, 2026).
  - **Focus:** Sampling steps in a causal Wan2.2-5B talking-avatar generator.
  - **Mechanism:** Apply causal ODE initialization and Self-Forcing DMD to form a few-step AR generator. Use KV caching and separate DiT/VAE devices for streaming execution.
  - **Source location:** PDF p. 11, Sections 3.4 and 4.1; pp. 13–14, Tables 1–2.

<a id="paper-lightforcingvideo"></a>

- [**Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) (ICML, 2026).
  - **Focus:** AR video attention.
  - **Mechanism:** Chunk-aware sparsity allocation with hierarchical sparse attention.
  - **Source location:** PDF p. 7.

<a id="paper-liveavatarvideo"></a>

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026).
  - **Focus:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Mechanism:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.
  - **Source location:** PDF pp. 2–3, streaming definition; PDF pp. 9–11, execution and setup; PDF p. 13, Table 3.

<a id="paper-lumos1video"></a>

- [**Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective**](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** LLM-based AR video generation.
  - **Mechanism:** Frame-causal masked parallel decoding with KV cache.
  - **Source location:** PDF p. 9.

<a id="paper-motioncachevideo"></a>

- [**Motion-Aware Caching for Efficient Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) (ICML, 2026).
  - **Focus:** AR video diffusion denoising computation.
  - **Mechanism:** Motion-weighted token updates after a full-computation warmup.
  - **Source location:** PDF p. 7.

<a id="paper-omniforcingvideo"></a>

- [**OmniForcing: Unleashing Real-Time Joint Audio-Visual Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) (ECCV, 2026).
  - **Focus:** Causal audio-video block generation and conditional denoising updates.
  - **Mechanism:** Distill a bidirectional LTX-2 teacher into a streaming AR student with block-causal modality alignment and rolling KV caches.
  - **Source location:** PDF pp. 5–11, method; pp. 12 and 14, timing protocol and Tables 1–2. Tables.

<a id="paper-packforcingvideo"></a>

- [**PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference**](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) (ECCV, 2026).
  - **Focus:** Stored historical KV entries and historical attention in a Wan2.1-based AR video generator.
  - **Mechanism:** Separate sink, compressed middle and recent history. Compress middle blocks and route selected historical blocks into attention, with incremental temporal RoPE adjustment.
  - **Source location:** PDF pp. 1 and 5–10, Sections 3.1–3.5 and inference settings; pp. 12–14, quality comparisons and ablations.

<a id="paper-quantvideogen"></a>

- [**Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) (ICML, 2026).
  - **Focus:** AR video KV storage.
  - **Mechanism:** Semantic smoothing and progressive residual cache quantization.
  - **Source location:** PDF p. 1.

<a id="paper-ardragvideo"></a>

- [**Real-Time Motion-Controllable Autoregressive Video Diffusion**](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** Motion-controlled AR video diffusion.
  - **Mechanism:** Few-step causal distillation with motion conditioning.
  - **Source location:** PDF p. 7.

<a id="paper-rewardforcing"></a>

- [**Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** Streaming AR video attention and conditional denoising.
  - **Mechanism:** Few-step causal distillation with a smaller attention window and fixed-size EMA sink state.
  - **Source location:** PDF p. 6, Table 1; PDF p. 8, Figure 6 and Section 4.3.

<a id="paper-rollingforcingvideo"></a>

- [**Rolling Forcing: Autoregressive Long Video Diffusion in Real Time**](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** Streaming AR video denoising.
  - **Mechanism:** Rolling-frame generation and few-step distillation with extended windows.
  - **Source location:** PDF p. 8.

<a id="paper-sanavideo"></a>

- [**SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer**](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** Long-video AR attention and cache growth.
  - **Mechanism:** Linear attention with constant-memory block-causal state.
  - **Source location:** PDF p. 7.

<a id="paper-diagonaldistillvideo"></a>

- [**Streaming Autoregressive Video Generation via Diagonal Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** Streaming AR video diffusion.
  - **Mechanism:** Diagonal distillation restructures few-step frame synthesis.
  - **Source location:** PDF p. 7.

<a id="paper-surpriseforcingvideo"></a>

- [**Surprise Forcing: What to Remember, When to Skip in Long Video Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) (ECCV, 2026).
  - **Focus:** Conditional denoising updates per AR video chunk and retained historical frames.
  - **Mechanism:** Adapt the denoising budget to chunk difficulty and retain selected evicted frames in a bounded memory bank.
  - **Source location:** PDF pp. 12–15, Sections 4.1–4.3 and Tables 1 and 4.

<a id="paper-ispavideo"></a>

- [**Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) (ECCV, 2026).
  - **Focus:** KV-cache storage and attention computation in streaming AR video generators.
  - **Mechanism:** Replace selected full-attention layers with local attention after instance-specific closed-form weight modulation absorbs historical context.
  - **Source location:** PDF pp. 2–3 and Section 3; PDF p. 11, Figure 2; PDF pp. 14–15, Figure 7.

<a id="paper-asdcausalvideo"></a>

- [**Towards One-step Causal Video Generation via Adversarial Self-Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** AR video conditional denoising evaluations.
  - **Mechanism:** Adversarial self-distillation with extra first-frame updates.
  - **Source location:** PDF p. 8.

<a id="paper-novavideo"></a>

- [**Autoregressive Video Generation without Vector Quantization**](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) (ICLR, 2025).
  - **Focus:** Temporal/spatial AR video generation.
  - **Mechanism:** Frame-wise temporal causality and set-wise spatial generation with continuous tokens.
  - **Source location:** PDF p. 7.

<a id="paper-ca2vdmvideo"></a>

- [**Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) (ICML, 2025).
  - **Focus:** AR video conditional-frame recomputation.
  - **Mechanism:** Causal feature computation and cache sharing across denoising steps.
  - **Source location:** PDF p. 8.

<a id="paper-causvidvideo"></a>

- [**From Slow Bidirectional to Fast Autoregressive Video Diffusion Models**](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) (CVPR, 2025).
  - **Focus:** Causal video diffusion inference.
  - **Mechanism:** Distills a bidirectional many-step teacher into a KV-cached causal few-step generator.
  - **Source location:** PDF p. 7.

<a id="paper-mardinivideo"></a>

- [**MarDini: Masked Auto-regressive Diffusion for Video Generation at Scale**](https://arxiv.org/pdf/2410.20280) (TMLR, 2025).
  - **Focus:** Masked-AR video planning and spatial diffusion.
  - **Mechanism:** Low-resolution planning with a lightweight high-resolution diffusion model.
  - **Source location:** PDF p. 8.

<a id="paper-selfforcingvideo"></a>

- [**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) (NeurIPS, 2025).
  - **Focus:** Few-step streaming AR video generator.
  - **Mechanism:** Self-generated training rollouts with rolling KV-cache inference.
  - **Source location:** PDF p. 7.

<a id="paper-evdmacmmm2023"></a>

- [**Efficiency-optimized Video Diffusion Models**](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) (ACM MM, 2023).
  - **Focus:** Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation.
  - **Mechanism:** Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm.
  - **Source location:** EVDM PDF pp. 5–6, Tables 2–3 and experimental setup; PDF p. 8, Table 9. MCVD original Section 2.1 and Figure 2.

## video / scene forecasts

<a id="paper-doe2world"></a>

- [**Doe-2: 3D Representation World Model for Unified Driving Scene Forecasting**](https://link.springer.com/content/pdf/10.1007/978-3-032-37235-2_29.pdf) (ECCV, 2026).
  - **Focus:** Compact 3D latent prediction with an AR predictor and conditional DiT head.
  - **Mechanism:** Section 3.4 conditions next-scene prediction on historical latents Z_{<=t} and ego-actions a_{<=t}; Eqs. (7)–(8) specify historical cross-attention and coarse future-latent prediction. A three-layer conditional DiT head uses Rectified Flow, Eq. (11), to sample the next-scene latent; the temporal AR predictor supplies its conditioning features.
  - **Source location:** PDF pp. 7–9, Sections 3.3–3.5, Eqs. (7)–(11); p. 16 Tables 5 and 7.

<a id="paper-geoflowdriving"></a>

- [**GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors**](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_22.pdf) (ECCV, 2026).
  - **Focus:** Geometry-aligned initialization and fewer denoising steps for autoregressive driving-video chunks.
  - **Mechanism:** Section 3.5 explicitly specifies short-horizon frame autoregression: each six-frame chunk contains one reference frame and five newly generated frames. Conditional latent Flow Matching inside each video chunk; geometry-warped historical content initializes its source distribution.
  - **Source location:** PDF pp. 6–10, Sections 3.1–3.5; p. 13 inference efficiency and Table 3.

<a id="paper-shotstreamvideo"></a>

- [**ShotStream: Streaming Multi-shot Video Generation for Interactive Storytelling**](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_12.pdf) (ECCV, 2026).
  - **Focus:** Four-step causal multi-shot video generation replacing a multi-step bidirectional teacher.
  - **Mechanism:** Section 4.2 and Figure 4 generate shots from previous shots and each shot chunk-by-chunk. Global and local caches store historical context and recently generated frames. A few-step conditional video denoiser operates within the causal chunk-generation procedure; distribution matching distillation replaces the slow teacher.
  - **Source location:** PDF pp. 6–8, Section 4 and Figure 4; pp. 10 and 12, Table 1 and efficiency protocol.

## video avatar

<a id="paper-avatarforcing"></a>

- [**Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** Causal avatar-motion generation latency.
  - **Mechanism:** Blockwise causal diffusion forcing with KV reuse replaces a bidirectional motion generator.
  - **Source location:** PDF p. 3, Eq. 4; PDF p. 4, Figure 4; PDF p. 6, Table 1 and Sections 5.2–5.3.

## video view expansion

<a id="paper-cubecomposervideo"></a>

- [**CubeComposer: Spatio-Temporal Autoregressive 4K 360deg Video Generation from Perspective Video**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** Autoregressive cubemap video synthesis.
  - **Mechanism:** Sparse context across cube faces and temporal windows.
  - **Source location:** PDF p. 8.
