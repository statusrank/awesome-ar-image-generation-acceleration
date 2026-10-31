# Conditional Computation

[Home](../README.md) · [Collections](../papers/README.md)

Feature reuse and selective execution, including attention-state storage.

**32 papers.**

## Contents

- [Feature Reuse and Refresh](#feature-reuse-and-refresh)
- [KV-cache Management and Sparse Attention](#kv-cache-management-and-sparse-attention)
- [Spatial and Depth-wise Computation Reduction](#spatial-and-depth-wise-computation-reduction)
- [Conditional Guidance Simplification](#conditional-guidance-simplification)
- [Iterative Conditional Sampling](#iterative-conditional-sampling)
- [Numerical Precision and Quantization](#numerical-precision-and-quantization)
- [Hardware and Collaborative Execution](#hardware-and-collaborative-execution)

## Feature Reuse and Refresh

<a id="paper-marche"></a>

- [**MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**](https://arxiv.org/pdf/2506.12035) (ECCV, 2026).
  - **Focus:** MAR attention and feed-forward recomputation.
  - **Mechanism:** Cache-aware attention and selective KV refresh.
  - **Source location:** PDF p. 1.

<a id="paper-lazymar"></a>

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025).
  - **Focus:** MAR repeated feature computation and guidance.
  - **Mechanism:** Caches stable token features and branch differences.
  - **Source location:** PDF p. 5.

<a id="paper-recap"></a>

- [**Plug-and-Play Context Feature Reuse for Efficient Masked Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) (NeurIPS, 2025).
  - **Focus:** MAR context-feature recomputation.
  - **Mechanism:** Alternates full evaluations with low-cost cached-context steps.
  - **Source location:** PDF p. 1.

## KV-cache Management and Sparse Attention

<a id="paper-amskv"></a>

- [**AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers**](https://arxiv.org/pdf/2511.16047) (AAAI, 2026).
  - **Focus:** Next-scale VAR KV memory and attention.
  - **Mechanism:** Retains condensed and local scales with adaptive cache allocation.
  - **Source location:** PDF p. 7.

<a id="paper-sparsear"></a>

- [**Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) (ICML, 2026).
  - **Focus:** AR image KV attention.
  - **Mechanism:** Entropy-aware cache sparsification.
  - **Source location:** PDF p. 1.

<a id="paper-hack"></a>

- [**Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2504.09261) (AAAI, 2026).
  - **Focus:** VAR historical KV storage.
  - **Mechanism:** Head-dependent cache compression.
  - **Source location:** PDF p. 1.

<a id="paper-linear"></a>

- [**LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**](https://arxiv.org/pdf/2512.04857v1) (ECCV, 2026).
  - **Focus:** Causal visual AR KV storage.
  - **Mechanism:** Progressively evicts historical lines outside retained dependency regions.
  - **Source location:** PDF p. 1.

<a id="paper-packforcingvideo"></a>

- [**PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference**](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) (ECCV, 2026).
  - **Focus:** Stored historical KV entries and historical attention in a Wan2.1-based AR video generator.
  - **Mechanism:** Separate sink, compressed middle and recent history. Compress middle blocks and route selected historical blocks into attention, with incremental temporal RoPE adjustment.
  - **Source location:** PDF pp. 1 and 5–10, Sections 3.1–3.5 and inference settings; pp. 12–14, quality comparisons and ablations.

<a id="paper-radar"></a>

- [**RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** VAR sparse attention plus decoded images.
  - **Mechanism:** Cost-constrained sparse prediction and decoder adaptation.
  - **Source location:** PDF p. 1.

<a id="paper-sparvar"></a>

- [**SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** Next-scale VAR attention.
  - **Mechanism:** Predicts sparse attention patterns from earlier scales.
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

<a id="paper-scalekv"></a>

- [**Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) (NeurIPS, 2025).
  - **Focus:** Next-scale VAR KV cache.
  - **Mechanism:** Layer-dependent retention of scales and cache entries.
  - **Source location:** PDF p. 6.

## Spatial and Depth-wise Computation Reduction

<a id="paper-nova"></a>

- [**Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) (ICML, 2026).
  - **Focus:** Next-scale visual AR token processing.
  - **Mechanism:** Entropy-guided adaptive token reduction and cached residual reuse.
  - **Source location:** PDF p. 1.

<a id="paper-arvar"></a>

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026).
  - **Focus:** HART and Infinity next-scale inference.
  - **Mechanism:** Uses earlier attention for token selection and removes a late guidance branch.
  - **Source location:** PDF p. 14.

<a id="paper-fastervar"></a>

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://arxiv.org/pdf/2512.16483) (ICML, 2026).
  - **Focus:** Late-scale VAR execution.
  - **Mechanism:** Adaptive stage selection and reduced computation at costly scales.
  - **Source location:** PDF p. 18.

<a id="paper-lazyvar"></a>

- [**LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** VAR token processing and scale schedule.
  - **Mechanism:** Scale-dependent token pruning plus grouped scale decoding.
  - **Source location:** PDF p. 8.

<a id="paper-stepvar"></a>

- [**StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models**](https://arxiv.org/pdf/2603.01757) (ACM ICMR, 2026).
  - **Focus:** High-resolution VAR token evaluation.
  - **Mechanism:** Structural and texture criteria select retained tokens.
  - **Source location:** PDF p. 10.

<a id="paper-toprovar"></a>

- [**ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization**](https://arxiv.org/pdf/2602.22948) (ICLR, 2026).
  - **Focus:** VAR tokens, layers and scale computation.
  - **Mechanism:** Entropy-guided sparse execution.
  - **Source location:** PDF p. 7.

<a id="paper-fastvar"></a>

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://arxiv.org/pdf/2503.23367) (ICCV, 2025).
  - **Focus:** High-resolution next-scale token processing.
  - **Mechanism:** Cached token pruning forwards selected tokens and recovers omitted states.
  - **Source location:** PDF p. 1.

<a id="paper-sparsevar"></a>

- [**Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis**](https://arxiv.org/pdf/2507.20454) (ICCV, 2025).
  - **Focus:** Late-scale VAR spatial computation.
  - **Mechanism:** Frequency-guided token omission and recovery.
  - **Source location:** PDF p. 5.

## Conditional Guidance Simplification

<a id="paper-arvar"></a>

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026).
  - **Focus:** HART and Infinity next-scale inference.
  - **Mechanism:** Uses earlier attention for token selection and removes a late guidance branch.
  - **Source location:** PDF p. 14.

<a id="paper-fastervar"></a>

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://arxiv.org/pdf/2512.16483) (ICML, 2026).
  - **Focus:** Late-scale VAR execution.
  - **Mechanism:** Adaptive stage selection and reduced computation at costly scales.
  - **Source location:** PDF p. 18.

<a id="paper-core2reviewcandidate"></a>

- [**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**](https://arxiv.org/pdf/2503.09662v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026).
  - **Focus:** LlamaGen guidance computation.
  - **Mechanism:** Weak-model training supports guidance and later replacement of expensive computation.
  - **Source location:** PDF p. 16.

<a id="paper-lazymar"></a>

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025).
  - **Focus:** MAR repeated feature computation and guidance.
  - **Mechanism:** Caches stable token features and branch differences.
  - **Source location:** PDF p. 5.

## Iterative Conditional Sampling

<a id="paper-barmbm"></a>

- [**Autoregressive Image Generation with Masked Bit Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) (ICML, 2026).
  - **Focus:** Bitwise AR image generation.
  - **Mechanism:** Masked bit modeling supports efficient prediction of large-vocabulary image representations.
  - **Source location:** PDF p. 7.

<a id="paper-fasthybrid"></a>

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** Hybrid AR image generator with diffusion decoder.
  - **Mechanism:** Lookahead and guided decoding reduce hybrid generation computation.
  - **Source location:** PDF p. 6.

<a id="paper-gtr"></a>

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** MAR stages and inner sampling budget.
  - **Mechanism:** Separates structure generation and detail reconstruction with frequency-weighted selection.
  - **Source location:** PDF p. 1.

<a id="paper-surpriseforcingvideo"></a>

- [**Surprise Forcing: What to Remember, When to Skip in Long Video Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) (ECCV, 2026).
  - **Focus:** Conditional denoising updates per AR video chunk and retained historical frames.
  - **Mechanism:** Adapt the denoising budget to chunk difficulty and retain selected evicted frames in a bounded memory bank.
  - **Source location:** PDF pp. 12–15, Sections 4.1–4.3 and Tables 1 and 4.

<a id="paper-emigm"></a>

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025).
  - **Focus:** Continuous masked image generation including MAR.
  - **Mechanism:** Revises masking, sampling schedule and conditional token modeling.
  - **Source location:** PDF p. 29.

## Numerical Precision and Quantization

<a id="paper-varcompressor"></a>

- [**Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs**](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) (ICPR, 2026).
  - **Focus:** 8B bitwise AR image generation on edge GPUs.
  - **Mechanism:** Compresses inference memory for deployment.
  - **Source location:** PDF p. 11.

<a id="paper-ptq4arvg"></a>

- [**PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** AR visual predictor arithmetic.
  - **Mechanism:** Post-training weight/activation quantization and calibration.
  - **Source location:** PDF p. 9.

<a id="paper-shiftsum"></a>

- [**Shift-and-Sum Quantization for Visual Autoregressive Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** VAR quantized matrix computation.
  - **Mechanism:** Shift-and-sum value quantization with calibration resampling.
  - **Source location:** PDF p. 17.

## Hardware and Collaborative Execution

<a id="paper-ciar"></a>

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026).
  - **Focus:** Cloud-device AR image decoding.
  - **Mechanism:** On-device interval verification reduces cloud verification calls.
  - **Source location:** PDF p. 7.

<a id="paper-liveavatarvideo"></a>

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026).
  - **Focus:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Mechanism:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.
  - **Source location:** PDF pp. 2–3, streaming definition; PDF pp. 9–11, execution and setup; PDF p. 13, Table 3.

<a id="paper-varturbo"></a>

- [**VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy**](https://xplorestaging.ieee.org/ielx8/11408404/11408433/11408607.pdf?arnumber=11408607) (HPCA, 2026).
  - **Focus:** VAR execution and dedicated accelerator.
  - **Mechanism:** Parallel decoding, token aggregation and bypass with hardware support.
  - **Source location:** Official HPCA 2026 main-conference abstract, software/hardware co-design and result paragraphs.
