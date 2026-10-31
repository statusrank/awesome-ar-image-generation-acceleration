# Conditional Computation

[Home](../README.md) · [All categories](../papers/README.md) · [By year](../papers/by-year.md)

Feature reuse and selective execution, including attention-state storage.

**32 papers.** Titles link to recorded PDFs or the official paper page.

## Contents

- [Feature Reuse and Refresh](#feature-reuse-and-refresh)
- [KV-cache Management and Sparse Attention](#kv-cache-management-and-sparse-attention)
- [Spatial and Depth-wise Computation Reduction](#spatial-and-depth-wise-computation-reduction)
- [Conditional Guidance Simplification](#conditional-guidance-simplification)
- [Iterative Conditional Sampling](#iterative-conditional-sampling)
- [Numerical Precision and Quantization](#numerical-precision-and-quantization)
- [Hardware and Collaborative Execution](#hardware-and-collaborative-execution)

## Feature Reuse and Refresh

- [**MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**](https://arxiv.org/pdf/2506.12035) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_34) · [PDF](https://arxiv.org/pdf/2506.12035) · [Details](paper-notes.md#marche)
  - **Accelerates:** MAR attention and feed-forward recomputation.
  - **Approach:** Cache-aware attention and selective KV refresh.

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [Code](https://github.com/feihongyan1/LazyMAR) · [Details](paper-notes.md#lazymar)
  - **Accelerates:** MAR repeated feature computation and guidance.
  - **Approach:** Caches stable token features and branch differences.

- [**Plug-and-Play Context Feature Reuse for Efficient Masked Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e628a90ac4accdbcc67e8c960c1817f-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) · [Details](paper-notes.md#recap)
  - **Accelerates:** MAR context-feature recomputation.
  - **Approach:** Alternates full evaluations with low-cost cached-context steps.

## KV-cache Management and Sparse Attention

- [**AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers**](https://arxiv.org/pdf/2511.16047) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39936) · [PDF](https://arxiv.org/pdf/2511.16047) · [Details](paper-notes.md#amskv)
  - **Accelerates:** Next-scale VAR KV memory and attention.
  - **Approach:** Retains condensed and local scales with adaptive cache allocation.

- [**Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/tong26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) · [Details](paper-notes.md#sparsear)
  - **Accelerates:** AR image KV attention.
  - **Approach:** Entropy-aware cache sparsification.

- [**Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2504.09261) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39686) · [PDF](https://arxiv.org/pdf/2504.09261) · [Details](paper-notes.md#hack)
  - **Accelerates:** VAR historical KV storage.
  - **Approach:** Head-dependent cache compression.

- [**LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**](https://arxiv.org/pdf/2512.04857v1) (ECCV, 2026). [Paper](https://doi.org/10.1007/978-3-032-37035-8_33) · [PDF](https://arxiv.org/pdf/2512.04857v1) · [Details](paper-notes.md#linear)
  - **Accelerates:** Causal visual AR KV storage.
  - **Approach:** Progressively evicts historical lines outside retained dependency regions.

- [**PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference**](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37464-6_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) · [Details](paper-notes.md#packforcingvideo)
  - **Accelerates:** Stored historical KV entries and historical attention in a Wan2.1-based AR video generator.
  - **Approach:** Separate sink, compressed middle and recent history. Compress middle blocks and route selected historical blocks into attention, with incremental temporal RoPE adjustment.

- [**RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) · [Details](paper-notes.md#radar)
  - **Accelerates:** VAR sparse attention plus decoded images.
  - **Approach:** Cost-constrained sparse prediction and decoder adaptation.

- [**SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) · [Details](paper-notes.md#sparvar)
  - **Accelerates:** Next-scale VAR attention.
  - **Approach:** Predicts sparse attention patterns from earlier scales.

- [**Surprise Forcing: What to Remember, When to Skip in Long Video Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) · [Details](paper-notes.md#surpriseforcingvideo)
  - **Accelerates:** Conditional denoising updates per AR video chunk and retained historical frames.
  - **Approach:** Adapt the denoising budget to chunk difficulty and retain selected evicted frames in a bounded memory bank.

- [**Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_25) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) · [Details](paper-notes.md#ispavideo)
  - **Accelerates:** KV-cache storage and attention computation in streaming AR video generators.
  - **Approach:** Replace selected full-attention layers with local attention after instance-specific closed-form weight modulation absorbs historical context.

- [**Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/14550b451b65682b09f9080026d00a7e-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) · [Details](paper-notes.md#scalekv)
  - **Accelerates:** Next-scale VAR KV cache.
  - **Approach:** Layer-dependent retention of scales and cache entries.

## Spatial and Depth-wise Computation Reduction

- [**Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26dq.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) · [Details](paper-notes.md#nova)
  - **Accelerates:** Next-scale visual AR token processing.
  - **Approach:** Entropy-guided adaptive token reduction and cached residual reuse.

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37429-5_9) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) · [Details](paper-notes.md#arvar)
  - **Accelerates:** HART and Infinity next-scale inference.
  - **Approach:** Uses earlier attention for token selection and removes a late guidance branch.

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://arxiv.org/pdf/2512.16483) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26go.html) · [PDF](https://arxiv.org/pdf/2512.16483) · [Details](paper-notes.md#fastervar)
  - **Accelerates:** Late-scale VAR execution.
  - **Approach:** Adaptive stage selection and reduced computation at costly scales.

- [**LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) · [Details](paper-notes.md#lazyvar)
  - **Accelerates:** VAR token processing and scale schedule.
  - **Approach:** Scale-dependent token pruning plus grouped scale decoding.

- [**StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models**](https://arxiv.org/pdf/2603.01757) (ACM ICMR, 2026). [Paper](https://doi.org/10.1145/3805622.3810814) · [PDF](https://arxiv.org/pdf/2603.01757) · [Details](paper-notes.md#stepvar)
  - **Accelerates:** High-resolution VAR token evaluation.
  - **Approach:** Structural and texture criteria select retained tokens.

- [**ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization**](https://arxiv.org/pdf/2602.22948) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8edb116d5b288b6a9bba4c16ab647702-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2602.22948) · [Details](paper-notes.md#toprovar)
  - **Accelerates:** VAR tokens, layers and scale computation.
  - **Approach:** Entropy-guided sparse execution.

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://arxiv.org/pdf/2503.23367) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.23367) · [Details](paper-notes.md#fastvar)
  - **Accelerates:** High-resolution next-scale token processing.
  - **Approach:** Cached token pruning forwards selected tokens and recovers omitted states.

- [**Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis**](https://arxiv.org/pdf/2507.20454) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Frequency-Aware_Autoregressive_Modeling_for_Efficient_High-Resolution_Image_Synthesis_ICCV_2025_paper.html) · [PDF](https://arxiv.org/pdf/2507.20454) · [Details](paper-notes.md#sparsevar)
  - **Accelerates:** Late-scale VAR spatial computation.
  - **Approach:** Frequency-guided token omission and recovery.

## Conditional Guidance Simplification

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37429-5_9) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) · [Details](paper-notes.md#arvar)
  - **Accelerates:** HART and Infinity next-scale inference.
  - **Approach:** Uses earlier attention for token selection and removes a late guidance branch.

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://arxiv.org/pdf/2512.16483) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26go.html) · [PDF](https://arxiv.org/pdf/2512.16483) · [Details](paper-notes.md#fastervar)
  - **Accelerates:** Late-scale VAR execution.
  - **Approach:** Adaptive stage selection and reduced computation at costly scales.

- [**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**](https://arxiv.org/pdf/2503.09662v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) · [PDF](https://arxiv.org/pdf/2503.09662v1) · [Details](paper-notes.md#core2reviewcandidate)
  - **Accelerates:** LlamaGen guidance computation.
  - **Approach:** Weak-model training supports guidance and later replacement of expensive computation.

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [Code](https://github.com/feihongyan1/LazyMAR) · [Details](paper-notes.md#lazymar)
  - **Accelerates:** MAR repeated feature computation and guidance.
  - **Approach:** Caches stable token features and branch differences.

## Iterative Conditional Sampling

- [**Autoregressive Image Generation with Masked Bit Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/yu26z.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) · [Details](paper-notes.md#barmbm)
  - **Accelerates:** Bitwise AR image generation.
  - **Approach:** Masked bit modeling supports efficient prediction of large-vocabulary image representations.

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) · [Details](paper-notes.md#fasthybrid)
  - **Accelerates:** Hybrid AR image generator with diffusion decoder.
  - **Approach:** Lookahead and guided decoding reduce hybrid generation computation.

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) · [Details](paper-notes.md#gtr)
  - **Accelerates:** MAR stages and inner sampling budget.
  - **Approach:** Separates structure generation and detail reconstruction with frequency-weighted selection.

- [**Surprise Forcing: What to Remember, When to Skip in Long Video Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) · [Details](paper-notes.md#surpriseforcingvideo)
  - **Accelerates:** Conditional denoising updates per AR video chunk and retained historical frames.
  - **Approach:** Adapt the denoising budget to chunk difficulty and retain selected evicted frames in a bounded memory bank.

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/you25d.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) · [Details](paper-notes.md#emigm)
  - **Accelerates:** Continuous masked image generation including MAR.
  - **Approach:** Revises masking, sampling schedule and conditional token modeling.

## Numerical Precision and Quantization

- [**Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs**](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) (ICPR, 2026). [Paper](https://doi.org/10.1007/978-3-032-31920-3_1) · [PDF](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) · [Details](paper-notes.md#varcompressor)
  - **Accelerates:** 8B bitwise AR image generation on edge GPUs.
  - **Approach:** Compresses inference memory for deployment.

- [**PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/81a28be483155f802ddef448d6fc4b57-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) · [Details](paper-notes.md#ptq4arvg)
  - **Accelerates:** AR visual predictor arithmetic.
  - **Approach:** Post-training weight/activation quantization and calibration.

- [**Shift-and-Sum Quantization for Visual Autoregressive Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/89379d5fc6eb34ff98488202fb52b9d0-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) · [Details](paper-notes.md#shiftsum)
  - **Accelerates:** VAR quantized matrix computation.
  - **Approach:** Shift-and-sum value quantization with calibration resampling.

## Hardware and Collaborative Execution

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026). [Paper](https://iclr.cc/virtual/2026/poster/10008851) · [PDF](https://arxiv.org/pdf/2603.25463v1) · [Details](paper-notes.md#ciar)
  - **Accelerates:** Cloud-device AR image decoding.
  - **Approach:** On-device interval verification reduces cloud verification calls.

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) · [Details](paper-notes.md#liveavatarvideo)
  - **Accelerates:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Approach:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.

- [**VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy**](https://doi.org/10.1109/hpca68181.2026.11408607) (HPCA, 2026). [Paper](https://doi.org/10.1109/hpca68181.2026.11408607) · [Details](paper-notes.md#varturbo)
  - **Accelerates:** VAR execution and dedicated accelerator.
  - **Approach:** Parallel decoding, token aggregation and bypass with hardware support.
