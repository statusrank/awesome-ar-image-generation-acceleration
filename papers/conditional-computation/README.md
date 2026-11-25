# Reducing Conditional Computation

[Home](../../README.md) · [Categories](../README.md)

Methods reduce the work and resource demands within conditional prediction.

**26 papers.**

## 4.1 Feature Reuse and KV-Cache Management

- [**AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers**](https://arxiv.org/pdf/2511.16047) (AAAI, 2026).
  Retains condensed and local scales with adaptive cache allocation.

- [**Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2504.09261) (AAAI, 2026).
  Head-dependent cache compression.

- [**HeatKV: Head-tuned KV-cache Compression for Visual Autoregressive Modeling**](https://arxiv.org/pdf/2605.14877) (NeurIPS, 2026, to appear).
  Uses offline attention calibration to allocate a fixed KV-cache memory budget to individual head-scale pairs.

- [**LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**](https://arxiv.org/pdf/2512.04857v1) (ECCV, 2026).
  Progressively evicts historical lines outside retained dependency regions.

- [**MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**](https://arxiv.org/pdf/2506.12035) (ECCV, 2026).
  Cache-aware attention and selective KV refresh.

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025).
  Caches stable token features and branch differences.

- [**Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) (NeurIPS, 2025).
  Layer-dependent retention of scales and cache entries.

- [**Plug-and-Play Context Feature Reuse for Efficient Masked Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) (NeurIPS, 2025).
  Alternates full evaluations with low-cost cached-context steps.

## 4.2 Selective Attention and Network Computation

- [**Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) (ICML, 2026).
  Entropy-guided adaptive token reduction and cached residual reuse.

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026).
  Uses earlier attention for token selection and removes a late guidance branch.

- [**Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) (ICML, 2026).
  Entropy-aware cache sparsification.

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26go/li26go.pdf) (ICML, 2026).
  Projects approximately low-rank late-scale features so the Transformer processes representative positions.

- [**LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) (CVPR, 2026).
  Scale-dependent token pruning plus grouped scale decoding.

- [**RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) (CVPR, 2026).
  Cost-constrained sparse prediction and decoder adaptation.

- [**SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) (CVPR, 2026).
  Predicts sparse attention patterns from earlier scales.

- [**StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models**](https://arxiv.org/pdf/2603.01757) (ACM ICMR, 2026).
  Structural and texture criteria select retained tokens.

- [**ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization**](https://arxiv.org/pdf/2602.22948) (ICLR, 2026).
  Entropy-guided sparse execution.

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) (ICCV, 2025).
  Selects pivotal token positions using frequency-based scores and restores omitted outputs from preceding-scale cached activations.

- [**Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis**](https://arxiv.org/pdf/2507.20454) (ICCV, 2025).
  Frequency-guided token omission and recovery.

## 4.3 Guidance and Conditional-Sampling Reduction

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026).
  Uses parallel lookahead candidates and conditioning-feature consistency to guide a shorter diffusion sampling trajectory.

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025).
  Combines an exponential masked-position schedule with reduced solver updates and classifier-free guidance restricted to selected intervals.

## 4.4 Numerical Precision and Quantization

- [**Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs**](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) (ICPR 2026, proceedings 2027).
  Compresses inference memory for deployment.

- [**Post-training Quantization for Hybrid Iterative Generative Models**](https://arxiv.org/pdf/2608.13932) (IEEE TCSVT, 2026).
  Applies hierarchical cluster decoupling and scaling recalibration to low-bit hybrid AR-diffusion models.

- [**PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) (ICLR, 2026).
  Post-training weight/activation quantization and calibration.

- [**Shift-and-Sum Quantization for Visual Autoregressive Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) (ICLR, 2026).
  Shift-and-sum value quantization with calibration resampling.

- [**VAR-Q: Tuning-free KV Cache Quantization for Visual Autoregressive Image and Video Generation**](https://arxiv.org/pdf/2611.05380) (NeurIPS, 2026, to appear).
  Quantizes KV caches by feature channel and generation block, using bit-packing kernels to reduce actual inference memory.


## License

[CC BY 4.0](../../LICENSE.md). Linked papers retain their original licenses.
