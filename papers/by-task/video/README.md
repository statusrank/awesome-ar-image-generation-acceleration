# Video Generation Acceleration

[Home](../../../README.md) · [By output](../README.md) · [By mechanism](../../README.md) · [Background](../../background/README.md) · [Pending](../../pending/README.md)

**43 core papers.** A study with verified image and video applications appears in both task lists. Counts must not be added to obtain unique papers.

## image; video

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026). [Paper](https://openreview.net/forum?id=OuFNXESoCO) · [PDF](https://arxiv.org/pdf/2412.07720) · [Details](../../paper-notes.md#tmlroufnxesoco)
  - **Accelerates:** Image and video block-AR conditional diffusion.
  - **Approach:** Block-causal denoising with reusable past context.
  - **Original-source evidence:** Source Fig. 5 compares sampling time for different AR lengths.
  - **Source location:** PDF p. 10; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2412.07720#page=10).
  - **Measured scope:** Image/video sampling-time boundaries remain distinct. Reading extent: selected primary PDF passages.

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/so26a.html) · [PDF](https://arxiv.org/pdf/2510.24211v2) · [Details](../../paper-notes.md#scd)
  - **Accelerates:** AR image stochastic speculative execution.
  - **Approach:** Couples proposal/verification randomness.
  - **Original-source evidence:** Source reports image and video inference gains; the two task results remain separate.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2510.24211v2#page=1).
  - **Measured scope:** No new independent exactness certification. Reading extent: selected primary PDF passages.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.10696) · [Details](../../paper-notes.md#nar)
  - **Accelerates:** Image and video AR position decoding.
  - **Approach:** Neighbor expansion with dimension-oriented parallel prediction heads.
  - **Original-source evidence:** Source reports image and UCF101 generation throughput.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://arxiv.org/pdf/2503.10696#page=8).
  - **Measured scope:** Image and video results remain separate. Reading extent: selected primary PDF passages.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) · [Details](../../paper-notes.md#par)
  - **Accelerates:** Image and video AR sequential decoding.
  - **Approach:** Generates spatially distant groups concurrently.
  - **Original-source evidence:** Source evaluates ImageNet and UCF101 speed and quality.
  - **Source location:** PDF p. 1; abstract/selected method and performance passages · [Original source](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf#page=1).
  - **Measured scope:** Image/video throughput, separately. Reading extent: selected primary PDF passages.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017). [Paper](https://proceedings.mlr.press/v70/reed17a.html) · [PDF](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) · [Details](../../paper-notes.md#parallelmultiscale2017)
  - **Accelerates:** Pixel AR sampling dependency depth.
  - **Approach:** Parallel multiscale density factorization.
  - **Original-source evidence:** Original source explicitly analyzes faster parallel image sampling.
  - **Source location:** PDF p. 8; abstract/selected method and performance passages · [Original source](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf#page=8).
  - **Measured scope:** Table 4 separates ImageNet image sampling and robot-video frame sampling with different batch settings. Reading extent: selected primary PDF passages.

## video

- [**AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26iw.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) · [Details](../../paper-notes.md#aad1video)
  - **Accelerates:** AR video denoising evaluation budget.
  - **Approach:** Asymmetric adversarial distillation trains a one-NFE causal student.
  - **Original-source evidence:** Original experiment description compares one-NFE generation with four-NFE AR baselines.
  - **Source location:** PDF p. 6 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf#page=6).
  - **Measured scope:** Denoiser-evaluation count, not measured end-to-end latency. Reading extent: selected primary PDF passages.

- [**Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#arcachevideo)
  - **Accelerates:** AR video diffusion recomputation.
  - **Approach:** History-guided cache timing with enhanced residual correction.
  - **Original-source evidence:** Original source evaluates caching on sequentially generated video segments.
  - **Source location:** PDF p. 1 · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf#page=1).
  - **Measured scope:** AR video diffusion inference, not generic image diffusion. Reading extent: selected primary PDF passages.

- [**Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhu26bf.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) · [Details](../../paper-notes.md#causalforcingvideo)
  - **Accelerates:** Few-step causal video diffusion generator.
  - **Approach:** AR-teacher ODE initialization followed by distribution-matching distillation.
  - **Original-source evidence:** Original Table 1 reports FPS and latency for the distilled AR generator.
  - **Source location:** PDF p. 8 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf#page=8).
  - **Measured scope:** Efficient generator design, reported reference models differ. Reading extent: selected primary PDF passages.

- [**Context Forcing: Consistent Autoregressive Video Generation with Long Context**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26eu.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) · [Details](../../paper-notes.md#contextforcingvideo)
  - **Accelerates:** AR video context-memory growth.
  - **Approach:** Bounded slow/fast memory retains selected historical frames.
  - **Original-source evidence:** Original method specifies bounded historical token storage; experiments report FPS for long contexts.
  - **Source location:** PDF p. 6 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf#page=6).
  - **Measured scope:** Context-memory budget, not a claimed standalone wall-clock speedup. Reading extent: selected primary PDF passages.

- [**Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/yi26c.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) · [Details](../../paper-notes.md#deepforcingvideo)
  - **Accelerates:** AR video historical KV storage.
  - **Approach:** Persistent sink context with importance-aware KV pruning.
  - **Original-source evidence:** Original source specifies compressed historical storage and reports long-video throughput.
  - **Source location:** PDF p. 1 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf#page=1).
  - **Measured scope:** KV-retention budget, not proof of faster wall-clock generation. Reading extent: selected primary PDF passages.

- [**FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/samuel26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) · [Details](../../paper-notes.md#fastarvideo)
  - **Accelerates:** AR video self/cross-attention and KV cache.
  - **Approach:** Temporal cache compression and approximate-neighbor sparse attention.
  - **Original-source evidence:** Original source reports end-to-end runtime, sustained throughput and peak-memory behavior.
  - **Source location:** PDF p. 7 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf#page=7).
  - **Measured scope:** Source-defined end-to-end generation, attention sub-results remain separate. Reading extent: selected primary PDF passages.

- [**Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge**](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8488454077cb0fd9d31772274c78115d-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) · [Details](../../paper-notes.md#fastcarvideo)
  - **Accelerates:** AR video decoder MLP computation.
  - **Approach:** Replays cached MLP outputs with temporal attention-based selection and FPGA scheduling.
  - **Original-source evidence:** Original experiments report decoder acceleration and energy behavior.
  - **Source location:** PDF p. 8 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf#page=8).
  - **Measured scope:** Edge hardware/software co-design. Reading extent: selected primary PDF passages.

- [**FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis**](https://arxiv.org/pdf/2603.07192) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37098-3_12) · [PDF](https://arxiv.org/pdf/2603.07192) · [Details](../../paper-notes.md#faststarvideo)
  - **Accelerates:** InfinityStar spatiotemporal token refinement.
  - **Approach:** Prunes converged spatial/temporal tokens with partial residual updates.
  - **Original-source evidence:** Original source reports latency and paired/output quality for InfinityStar.
  - **Source location:** PDF p. 1 · [Original source](https://arxiv.org/pdf/2603.07192#page=1).
  - **Measured scope:** Video generation latency, separate from static-image VAR. Reading extent: selected primary PDF passages.

- [**Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/ma26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) · [Details](../../paper-notes.md#flexforcingvideo)
  - **Accelerates:** AR video generation execution schedule.
  - **Approach:** Flexible chunks with bidirectional planning and autoregressive within-chunk inference.
  - **Original-source evidence:** Original table compares FPS and neural-function evaluations for generation variants.
  - **Source location:** PDF p. 6 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf#page=6).
  - **Measured scope:** Model-design runtime comparison, not unchanged reference sampling. Reading extent: selected primary PDF passages.

- [**Flow Caching for Autoregressive Video Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/85dc8f85ff978b9c606d3b2f5b0da69a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) · [Details](../../paper-notes.md#flowcachevideo)
  - **Accelerates:** AR video denoising and KV storage.
  - **Approach:** Independent chunk cache policies with bounded KV compression.
  - **Original-source evidence:** Original experiments compare caching speed and video metrics on MAGI-1 and SkyReels-V2.
  - **Source location:** PDF p. 9 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf#page=9).
  - **Measured scope:** Generation speed and cache memory, no independent output-law guarantee. Reading extent: selected primary PDF passages.

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) · [Details](../../paper-notes.md#hiarvideo)
  - **Accelerates:** Hierarchical denoising and pipelined execution of AR video blocks.
  - **Approach:** Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.
  - **Original-source evidence:** Section 3 defines hierarchical causal denoising. Table 1 and Section 4.2 report 30 FPS and 0.30 s per-chunk latency, compared with 17 FPS and 0.69 s for other four-step distilled AR generators sharing Wan2.1-1.3B.
  - **Source location:** PDF p. 9, Table 1 and Section 4.1; PDF pp. 10–11, Section 4.2 · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf).
  - **Measured scope:** Streaming throughput and per-chunk latency, not complete-video latency. The approximately 1.8x headline matches the throughput ratio, not the listed latency ratio. Reading extent: selected primary PDF passages.

- [**InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars**](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37032-7_37) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) · [Details](../../paper-notes.md#interactiveavatarvideo)
  - **Accelerates:** Sampling steps in a causal Wan2.2-5B talking-avatar generator.
  - **Approach:** Apply causal ODE initialization and Self-Forcing DMD to form a few-step AR generator. Use KV caching and separate DiT/VAE devices for streaming execution.
  - **Original-source evidence:** Section 3.4 identifies the distillation stages. Table 2 reports 1.27 FPS without DMD and 26.68 FPS for the complete model. Section 4.1 states 576p output and places DiT and VAE on different GPU devices. It separately reports approximately 2.6 s TTFF including an LLM audio-response stage.
  - **Source location:** Official ECCV PDF p. 11, Sections 3.4 and 4.1; pp. 13–14, Tables 1–2. Table 2 visually checked · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf).
  - **Measured scope:** Source-reported streaming FPS with parallel execution. The 2.6 s conversational TTFF includes additional components. Neither value is a single-GPU complete-video latency. Reading extent: selected primary PDF passages.

- [**Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/lv26i.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) · [Details](../../paper-notes.md#lightforcingvideo)
  - **Accelerates:** AR video attention.
  - **Approach:** Chunk-aware sparsity allocation with hierarchical sparse attention.
  - **Original-source evidence:** Original source reports standalone and combined end-to-end speedups.
  - **Source location:** PDF p. 7 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf#page=7).
  - **Measured scope:** Standalone and combined results must remain distinct. Reading extent: selected primary PDF passages.

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) · [Details](../../paper-notes.md#liveavatarvideo)
  - **Accelerates:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Approach:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.
  - **Original-source evidence:** The method uses causal noisy-history KV caches. Table 3 separates DMD, sequence parallelism, timestep-forcing parallelism, VAE parallelism and kernel optimization. It reports 45.2 FPS and 1.21 s time to first frame for the full five-H100 configuration.
  - **Source location:** PDF pp. 2–3, streaming definition; PDF pp. 9–11, execution and setup; PDF p. 13, Table 3 · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf).
  - **Measured scope:** Streaming FPS and time to first frame at 720x400. GPU count changes across ablations. These values are not complete conversational latency or a same-hardware speed ratio. Reading extent: selected primary PDF passages.

- [**Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective**](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/59ad89d72559dd4ce557d56f36313724-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) · [Details](../../paper-notes.md#lumos1video)
  - **Accelerates:** LLM-based AR video generation.
  - **Approach:** Frame-causal masked parallel decoding with KV cache.
  - **Original-source evidence:** Table 6 compares next-token prediction and masked prediction with/without cache on H20.
  - **Source location:** PDF p. 9 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf#page=9).
  - **Measured scope:** Video inference time, RoPE overhead is separately reported. Reading extent: selected primary PDF passages.

- [**Motion-Aware Caching for Efficient Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/xu26an.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) · [Details](../../paper-notes.md#motioncachevideo)
  - **Accelerates:** AR video diffusion denoising computation.
  - **Approach:** Motion-weighted token updates after a full-computation warmup.
  - **Original-source evidence:** Original source reports inference latency and FLOPs on AR video backbones.
  - **Source location:** PDF p. 7 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf#page=7).
  - **Measured scope:** Warmup and token-update overhead remain part of the method. Reading extent: selected primary PDF passages.

- [**OmniForcing: Unleashing Real-Time Joint Audio-Visual Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) · [Details](../../paper-notes.md#omniforcingvideo)
  - **Accelerates:** Causal audio-video block generation and conditional denoising updates.
  - **Approach:** Distill a bidirectional LTX-2 teacher into a streaming AR student with block-causal modality alignment and rolling KV caches.
  - **Original-source evidence:** Section 4.2 and Table 1 report 5.7 s for a five-second 480p audio-video clip versus 197 s for the offline teacher. Section 4.1 specifies a single H200, bf16, three warmups and 100 iterations, and includes VAE decoding and vocoder processing. The measured median TTFC and throughput are separately 0.71 s and 24.8 FPS.
  - **Source location:** Official ECCV PDF pp. 5–11, method; pp. 12 and 14, timing protocol and Tables 1–2. Tables visually checked · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf).
  - **Measured scope:** Efficient learned AR generator compared with a bidirectional teacher. Full-clip runtime, time to first chunk and steady streaming FPS are distinct measurements. Reading extent: selected primary PDF passages.

- [**PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference**](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37464-6_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) · [Details](../../paper-notes.md#packforcingvideo)
  - **Accelerates:** Stored historical KV entries and historical attention in a Wan2.1-based AR video generator.
  - **Approach:** Separate sink, compressed middle and recent history. Compress middle blocks and route selected historical blocks into attention, with incremental temporal RoPE adjustment.
  - **Original-source evidence:** Section 3.1 identifies linear cache growth. Sections 3.2–3.5 define bounded history partitions, dual-branch compression and top-k context selection. The abstract reports approximately 32x compression of middle-history tokens and 14–16 FPS for 832x480 video on one H200. These are not whole-system speedup measurements.
  - **Source location:** Official ECCV PDF pp. 1 and 5–10, Sections 3.1–3.5 and inference settings; pp. 12–14, quality comparisons and ablations · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf).
  - **Measured scope:** Historical KV/context storage reduction and source-reported streaming throughput. The compression factor applies to the middle-history representation, not total GPU memory or complete-video runtime. Reading extent: selected primary PDF passages.

- [**Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/xi26f.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) · [Details](../../paper-notes.md#quantvideogen)
  - **Accelerates:** AR video KV storage.
  - **Approach:** Semantic smoothing and progressive residual cache quantization.
  - **Original-source evidence:** Original source reports reduced KV memory with a small latency overhead.
  - **Source location:** PDF p. 1 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf#page=1).
  - **Measured scope:** Memory efficiency, not a measured latency reduction. Reading extent: selected primary PDF passages.

- [**Real-Time Motion-Controllable Autoregressive Video Diffusion**](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/71c1d6ec1f0003d8ea10bbea4291002d-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) · [Details](../../paper-notes.md#ardragvideo)
  - **Accelerates:** Motion-controlled AR video diffusion.
  - **Approach:** Few-step causal distillation with motion conditioning.
  - **Original-source evidence:** Original source reports latency and real-time generation comparisons.
  - **Source location:** PDF p. 7 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf#page=7).
  - **Measured scope:** Controlled video generation, not motion-estimation acceleration. Reading extent: selected primary PDF passages.

- [**Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#rewardforcing)
  - **Accelerates:** Streaming AR video attention and conditional denoising.
  - **Approach:** Few-step causal distillation with a smaller attention window and fixed-size EMA sink state.
  - **Original-source evidence:** Table 1 reports video generation FPS; Figure 6 relates attention-window size to inference FPS.
  - **Source location:** PDF p. 6, Table 1; PDF p. 8, Figure 6 and Section 4.3 · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf#page=6).
  - **Measured scope:** Complete-generator comparison between different trained models, not an unchanged-checkpoint acceleration result. Reading extent: selected primary PDF passages.

- [**Rolling Forcing: Autoregressive Long Video Diffusion in Real Time**](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) · [Details](../../paper-notes.md#rollingforcingvideo)
  - **Accelerates:** Streaming AR video denoising.
  - **Approach:** Rolling-frame generation and few-step distillation with extended windows.
  - **Original-source evidence:** Experiments measure throughput and latency after stable execution speed is reached.
  - **Source location:** PDF p. 8 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf#page=8).
  - **Measured scope:** Steady-state latency, not first-frame latency. Reading extent: selected primary PDF passages.

- [**SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer**](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b93c59da0d0f835907fd661d419db2-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) · [Details](../../paper-notes.md#sanavideo)
  - **Accelerates:** Long-video AR attention and cache growth.
  - **Approach:** Linear attention with constant-memory block-causal state.
  - **Original-source evidence:** Original tables compare video latency and describe fixed-size historical state.
  - **Source location:** PDF p. 7 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf#page=7).
  - **Measured scope:** New-generator latency and memory, quantized deployment is a separate setting. Reading extent: selected primary PDF passages.

- [**Streaming Autoregressive Video Generation via Diagonal Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d899eabc6c8fefd0d4064762aba407e2-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) · [Details](../../paper-notes.md#diagonaldistillvideo)
  - **Accelerates:** Streaming AR video diffusion.
  - **Approach:** Diagonal distillation restructures few-step frame synthesis.
  - **Original-source evidence:** Experiments separately measure H100 FPS and first-frame latency.
  - **Source location:** PDF p. 7 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf#page=7).
  - **Measured scope:** First-frame delay and sustained FPS are different measures. Reading extent: selected primary PDF passages.

- [**Surprise Forcing: What to Remember, When to Skip in Long Video Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) · [Details](../../paper-notes.md#surpriseforcingvideo)
  - **Accelerates:** Conditional denoising updates per AR video chunk and retained historical frames.
  - **Approach:** Adapt the denoising budget to chunk difficulty and retain selected evicted frames in a bounded memory bank.
  - **Original-source evidence:** The method builds on LongLive/Wan2.1-T2V-1.3B. Table 4 varies the skip ratio and reports an Acc. Ratio of 15.8% at the default 0.4 setting. The accompanying text describes denoising-compute reduction. Table 1 separately reports 16.45/17.18 FPS on short/long videos versus LongLive's 18.01/18.01 FPS.
  - **Source location:** Official ECCV PDF pp. 12–15, Sections 4.1–4.3 and Tables 1 and 4. Table 4 visually checked · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf).
  - **Measured scope:** Component-level update/compute reduction. The complete configuration is slower than LongLive in the reported FPS table. Do not describe the 15.8% component figure as a measured end-to-end speedup. Reading extent: selected primary PDF passages.

- [**Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_25) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) · [Details](../../paper-notes.md#ispavideo)
  - **Accelerates:** KV-cache storage and attention computation in streaming AR video generators.
  - **Approach:** Replace selected full-attention layers with local attention after instance-specific closed-form weight modulation absorbs historical context.
  - **Original-source evidence:** Sections 3–4 describe the absorption of historical attention into projection weights. Figure 2 reports memory reduction. Figure 7 reports a 1.35x overall gain for ISPA and 1.86x when combined with W8A8, separately from the 1.89x attention-operator gain.
  - **Source location:** PDF pp. 2–3 and Section 3; PDF p. 11, Figure 2; PDF pp. 14–15, Figure 7 · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf).
  - **Measured scope:** Peak GPU memory and the source-reported latency breakdown. Attention-only and quantized combined results remain separate. Reading extent: selected primary PDF passages.

- [**Towards One-step Causal Video Generation via Adversarial Self-Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3ae86071c169649bff21188c536163dc-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) · [Details](../../paper-notes.md#asdcausalvideo)
  - **Accelerates:** AR video conditional denoising evaluations.
  - **Approach:** Adversarial self-distillation with extra first-frame updates.
  - **Original-source evidence:** Table 1 compares one/two-step student settings and video quality.
  - **Source location:** PDF p. 8 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf#page=8).
  - **Measured scope:** Conditional update budget only, first-frame enhancement adds steps, no measured latency claimed. Reading extent: selected primary PDF passages.

- [**Autoregressive Video Generation without Vector Quantization**](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6e5112eaa45f8c30b242c5f576213a92-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) · [Details](../../paper-notes.md#novavideo)
  - **Accelerates:** Temporal/spatial AR video generation.
  - **Approach:** Frame-wise temporal causality and set-wise spatial generation with continuous tokens.
  - **Original-source evidence:** Original source reports video inference latency against prior video generators.
  - **Source location:** PDF p. 7 · [Original source](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf#page=7).
  - **Measured scope:** New video generator, distinct from image accelerator NOVA. Reading extent: selected primary PDF passages.

- [**Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/gao25m.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) · [Details](../../paper-notes.md#ca2vdmvideo)
  - **Accelerates:** AR video conditional-frame recomputation.
  - **Approach:** Causal feature computation and cache sharing across denoising steps.
  - **Original-source evidence:** Original experiments measure video generation speed and GPU cache memory.
  - **Source location:** PDF p. 8 · [Original source](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf#page=8).
  - **Measured scope:** Generation speed and cache memory. Reading extent: selected primary PDF passages.

- [**From Slow Bidirectional to Fast Autoregressive Video Diffusion Models**](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) · [Details](../../paper-notes.md#causvidvideo)
  - **Accelerates:** Causal video diffusion inference.
  - **Approach:** Distills a bidirectional many-step teacher into a KV-cached causal few-step generator.
  - **Original-source evidence:** Table 3 reports latency and FPS including the text encoder, diffusion model and VAE decoder.
  - **Source location:** PDF p. 7 · [Original source](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf#page=7).
  - **Measured scope:** New AR generator, teacher originally bidirectional. Reading extent: selected primary PDF passages.

- [**MarDini: Masked Auto-regressive Diffusion for Video Generation at Scale**](https://arxiv.org/pdf/2410.20280) (TMLR, 2025). [Paper](https://openreview.net/forum?id=fuOHI59rUW) · [PDF](https://arxiv.org/pdf/2410.20280) · [Details](../../paper-notes.md#mardinivideo)
  - **Accelerates:** Masked-AR video planning and spatial diffusion.
  - **Approach:** Low-resolution planning with a lightweight high-resolution diffusion model.
  - **Original-source evidence:** Original Table 3 compares asymmetric design latency and memory on A100.
  - **Source location:** PDF p. 8 · [Original source](https://arxiv.org/pdf/2410.20280#page=8).
  - **Measured scope:** Video latency and GPU memory. Reading extent: selected primary PDF passages.

- [**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f4823f831af67a3ef15e41a85434422a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) · [Details](../../paper-notes.md#selfforcingvideo)
  - **Accelerates:** Few-step streaming AR video generator.
  - **Approach:** Self-generated training rollouts with rolling KV-cache inference.
  - **Original-source evidence:** Original experiments report first-frame latency and throughput on H100.
  - **Source location:** PDF p. 7 · [Original source](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf#page=7).
  - **Measured scope:** New/distilled generator, not an unchanged-model execution optimization. Reading extent: selected primary PDF passages.

- [**Efficiency-optimized Video Diffusion Models**](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) (ACM MM, 2023). [Paper](https://dl.acm.org/doi/10.1145/3581783.3612406) · [PDF](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) · [Details](../../paper-notes.md#evdmacmmm2023)
  - **Accelerates:** Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation.
  - **Approach:** Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm.
  - **Original-source evidence:** The original [MCVD paper, Section 2.1 and Figure 2](https://proceedings.neurips.cc/paper_files/paper/2022/file/944618542d80a63bbec16dfbd2bd689a-Paper-Conference.pdf#page=3) defines blockwise AR video generation. EVDM evaluates this denoiser family in multi-block prediction. Tables 2–3 report inference FLOPs reductions and Table 9 separately reports A40 latency measurements.
  - **Source location:** EVDM PDF pp. 5–6, Tables 2–3 and experimental setup; PDF p. 8, Table 9. MCVD original Section 2.1 and Figure 2 · [Original source](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf).
  - **Measured scope:** Denoiser FLOPs and reported model latency. The approximately 10x headline concerns arithmetic reduction. Table 9 lists 16.5 to 6.1 ms and 26.4 to 7.5 ms for two unlabeled configurations, not a 10x end-to-end video gain. Reading extent: selected primary PDF passages.

## video / scene forecasts

- [**Doe-2: 3D Representation World Model for Unified Driving Scene Forecasting**](https://link.springer.com/content/pdf/10.1007/978-3-032-37235-2_29.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_29) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37235-2_29.pdf) · [Details](../../paper-notes.md#doe2world)
  - **Accelerates:** Compact 3D latent prediction with an AR predictor and conditional DiT head.
  - **Approach:** Section 3.4 conditions next-scene prediction on historical latents Z_{<=t} and ego-actions a_{<=t}; Eqs. (7)–(8) specify historical cross-attention and coarse future-latent prediction. A three-layer conditional DiT head uses Rectified Flow, Eq. (11), to sample the next-scene latent; the temporal AR predictor supplies its conditioning features.
  - **Original-source evidence:** Retain only as efficient hybrid AR visual world-model design, supported by representation-compression ablations. It is not an execution-only accelerator for an unchanged AR generator. Table 5 reports about 2.3 to 4.0 FPS as latent dimension changes from 768 to 64. Table 7 pure AR is about 6.0 FPS, hybrid 4.0 and pure DiT 1.9. Adding the conditional head is not faster than the pure-AR ablation.
  - **Source location:** Original PDF pp. 7–9, Sections 3.3–3.5, Eqs. (7)–(11); p. 16 Tables 5 and 7 · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37235-2_29.pdf).
  - **Measured scope:** Table 5 reports about 2.3 to 4.0 FPS as latent dimension changes from 768 to 64. Table 7 pure AR is about 6.0 FPS, hybrid 4.0 and pure DiT 1.9. Adding the conditional head is not faster than the pure-AR ablation. Reading extent: selected primary PDF passages.

- [**GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors**](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_22.pdf) · [Details](../../paper-notes.md#geoflowdriving)
  - **Accelerates:** Geometry-aligned initialization and fewer denoising steps for autoregressive driving-video chunks.
  - **Approach:** Section 3.5 explicitly specifies short-horizon frame autoregression: each six-frame chunk contains one reference frame and five newly generated frames. Conditional latent Flow Matching inside each video chunk; geometry-warped historical content initializes its source distribution.
  - **Original-source evidence:** Retain as AR driving-video generation acceleration through fewer within-chunk sampling updates. It does not concern static-image AR decoding. Reported 4.2 times compares 16-frame generation with eight steps over four passes against 40 steps over one pass. Chunk sizes and solver budgets change. The five-step six-frame Table 3 timing is separate.
  - **Source location:** Original PDF pp. 6–10, Sections 3.1–3.5; p. 13 inference efficiency and Table 3 · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_22.pdf).
  - **Measured scope:** Reported 4.2 times compares 16-frame generation with eight steps over four passes against 40 steps over one pass. Chunk sizes and solver budgets change. The five-step six-frame Table 3 timing is separate. Reading extent: selected primary PDF passages.

- [**ShotStream: Streaming Multi-shot Video Generation for Interactive Storytelling**](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_12.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37261-1_12) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_12.pdf) · [Details](../../paper-notes.md#shotstreamvideo)
  - **Accelerates:** Four-step causal multi-shot video generation replacing a multi-step bidirectional teacher.
  - **Approach:** Section 4.2 and Figure 4 generate shots from previous shots and each shot chunk-by-chunk. Global and local caches store historical context and recently generated frames. A few-step conditional video denoiser operates within the causal chunk-generation procedure; distribution matching distillation replaces the slow teacher.
  - **Original-source evidence:** Retain as efficient AR video-generator design through distillation. The principal slow comparators and teacher are bidirectional models. Single H200 Table 1: ShotStream 15.95 FPS, Self Forcing 16.36 and LongLive 16.55. Do not report the bidirectional-to-causal throughput gain as a gain over these fast AR baselines.
  - **Source location:** Original PDF pp. 6–8, Section 4 and Figure 4; pp. 10 and 12, Table 1 and efficiency protocol · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_12.pdf).
  - **Measured scope:** Single H200 Table 1: ShotStream 15.95 FPS, Self Forcing 16.36 and LongLive 16.55. Do not report the bidirectional-to-causal throughput gain as a gain over these fast AR baselines. Reading extent: selected primary PDF passages.

## video avatar

- [**Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#avatarforcing)
  - **Accelerates:** Causal avatar-motion generation latency.
  - **Approach:** Blockwise causal diffusion forcing with KV reuse replaces a bidirectional motion generator.
  - **Original-source evidence:** Equation 4 specifies autoregressive motion generation; Table 1 compares latency against a reproduced INFP baseline.
  - **Source location:** PDF p. 3, Eq. 4; PDF p. 4, Figure 4; PDF p. 6, Table 1 and Sections 5.2–5.3 · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf#page=6).
  - **Measured scope:** Motion-generation time assumes pre-extracted audio features and 10 neural-function evaluations. This is not complete audiovisual-system latency. Reading extent: selected primary PDF passages.

## video view expansion

- [**CubeComposer: Spatio-Temporal Autoregressive 4K 360deg Video Generation from Perspective Video**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#cubecomposervideo)
  - **Accelerates:** Autoregressive cubemap video synthesis.
  - **Approach:** Sparse context across cube faces and temporal windows.
  - **Original-source evidence:** Source context ablation reports reduced TFLOPs and discusses lower peak memory.
  - **Source location:** PDF p. 8 · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf#page=8).
  - **Measured scope:** Computational work for panorama generation, not measured latency reduction. Reading extent: selected primary PDF passages.
