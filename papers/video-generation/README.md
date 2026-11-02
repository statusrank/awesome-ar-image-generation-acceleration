# Video Generation Acceleration

[Home](../../README.md) · [Categories](../README.md)

Acceleration of autoregressive video generation and streaming synthesis.

**43 papers.**

## Papers

- [**AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) (ICML, 2026).
  Asymmetric adversarial distillation trains a one-NFE causal student.

- [**Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) (CVPR, 2026).
  History-guided cache timing with enhanced residual correction.

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026).
  Caches completed blocks under block-causal attention and samples within each block by diffusion. image and video timings are reported separately.

- [**Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) (CVPR, 2026).
  Blockwise causal diffusion forcing with KV reuse replaces a bidirectional motion generator.

- [**Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) (ICML, 2026).
  AR-teacher ODE initialization followed by distribution-matching distillation.

- [**Context Forcing: Consistent Autoregressive Video Generation with Long Context**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) (ICML, 2026).
  Bounded slow/fast memory retains selected historical frames.

- [**CubeComposer: Spatio-Temporal Autoregressive 4K 360deg Video Generation from Perspective Video**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) (CVPR, 2026).
  Sparse context across cube faces and temporal windows.

- [**Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) (ICML, 2026).
  Persistent sink context with importance-aware KV pruning.

- [**Doe-2: 3D Representation World Model for Unified Driving Scene Forecasting**](https://link.springer.com/content/pdf/10.1007/978-3-032-37235-2_29.pdf) (ECCV, 2026).
  Section 3.4 conditions next-scene prediction on historical latents Z_{<=t} and ego-actions a_{<=t}; Eqs. (7)–(8) specify historical cross-attention and coarse future-latent prediction. A three-layer conditional DiT head uses Rectified Flow, Eq. (11), to sample the next-scene latent; the temporal AR predictor supplies its conditioning features.

- [**FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) (ICML, 2026).
  Temporal cache compression and approximate-neighbor sparse attention.

- [**Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge**](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) (ICLR, 2026).
  Replays cached MLP outputs with temporal attention-based selection and FPGA scheduling.

- [**FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis**](https://arxiv.org/pdf/2603.07192) (ECCV, 2026).
  Prunes converged spatial/temporal tokens with partial residual updates.

- [**Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) (ICML, 2026).
  Flexible chunks with bidirectional planning and autoregressive within-chunk inference.

- [**Flow Caching for Autoregressive Video Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) (ICLR, 2026).
  Independent chunk cache policies with bounded KV compression.

- [**GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors**](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_22.pdf) (ECCV, 2026).
  Section 3.5 explicitly specifies short-horizon frame autoregression: each six-frame chunk contains one reference frame and five newly generated frames. Conditional latent Flow Matching inside each video chunk; geometry-warped historical content initializes its source distribution.

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026).
  Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.

- [**InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars**](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) (ECCV, 2026).
  Apply causal ODE initialization and Self-Forcing DMD to form a few-step AR generator. Use KV caching and separate DiT/VAE devices for streaming execution.

- [**Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) (ICML, 2026).
  Chunk-aware sparsity allocation with hierarchical sparse attention.

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026).
  Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.

- [**Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective**](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) (ICLR, 2026).
  Frame-causal masked parallel decoding with KV cache.

- [**Motion-Aware Caching for Efficient Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) (ICML, 2026).
  Motion-weighted token updates after a full-computation warmup.

- [**OmniForcing: Unleashing Real-Time Joint Audio-Visual Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) (ECCV, 2026).
  Distill a bidirectional LTX-2 teacher into a streaming AR student with block-causal modality alignment and rolling KV caches.

- [**PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference**](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) (ECCV, 2026).
  Separate sink, compressed middle and recent history. Compress middle blocks and route selected historical blocks into attention, with incremental temporal RoPE adjustment.

- [**Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) (ICML, 2026).
  Semantic smoothing and progressive residual cache quantization.

- [**Real-Time Motion-Controllable Autoregressive Video Diffusion**](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) (ICLR, 2026).
  Few-step causal distillation with motion conditioning.

- [**Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) (CVPR, 2026).
  Few-step causal distillation with a smaller attention window and fixed-size EMA sink state.

- [**Rolling Forcing: Autoregressive Long Video Diffusion in Real Time**](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) (ICLR, 2026).
  Rolling-frame generation and few-step distillation with extended windows.

- [**SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer**](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) (ICLR, 2026).
  Linear attention with constant-memory block-causal state.

- [**ShotStream: Streaming Multi-shot Video Generation for Interactive Storytelling**](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_12.pdf) (ECCV, 2026).
  Section 4.2 and Figure 4 generate shots from previous shots and each shot chunk-by-chunk. Global and local caches store historical context and recently generated frames. A few-step conditional video denoiser operates within the causal chunk-generation procedure; distribution matching distillation replaces the slow teacher.

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026).
  Couples proposal/verification randomness.

- [**Streaming Autoregressive Video Generation via Diagonal Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) (ICLR, 2026).
  Diagonal distillation restructures few-step frame synthesis.

- [**Surprise Forcing: What to Remember, When to Skip in Long Video Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) (ECCV, 2026).
  Adapt the denoising budget to chunk difficulty and retain selected evicted frames in a bounded memory bank.

- [**Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) (ECCV, 2026).
  Replace selected full-attention layers with local attention after instance-specific closed-form weight modulation absorbs historical context.

- [**Towards One-step Causal Video Generation via Adversarial Self-Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) (ICLR, 2026).
  Adversarial self-distillation with extra first-frame updates.

- [**Autoregressive Video Generation without Vector Quantization**](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) (ICLR, 2025).
  Frame-wise temporal causality and set-wise spatial generation with continuous tokens.

- [**Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) (ICML, 2025).
  Causal feature computation and cache sharing across denoising steps.

- [**From Slow Bidirectional to Fast Autoregressive Video Diffusion Models**](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) (CVPR, 2025).
  Distills a bidirectional many-step teacher into a KV-cached causal few-step generator.

- [**MarDini: Masked Auto-regressive Diffusion for Video Generation at Scale**](https://arxiv.org/pdf/2410.20280) (TMLR, 2025).
  Low-resolution planning with a lightweight high-resolution diffusion model.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025).
  Neighbor expansion with dimension-oriented parallel prediction heads.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025).
  Generates spatially distant groups concurrently.

- [**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) (NeurIPS, 2025).
  Self-generated training rollouts with rolling KV-cache inference.

- [**Efficiency-optimized Video Diffusion Models**](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) (ACM MM, 2023).
  Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017).
  Uses a learned multiscale pixel-group factorization for parallel image sampling, changing the original PixelCNN dependencies.


## License

[CC BY 4.0](../../LICENSE.md). Linked papers retain their original licenses.
