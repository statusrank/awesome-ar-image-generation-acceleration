# Accelerating Sampling and Decoding

[Home](../../README.md) · [Categories](../README.md)

Parallel and speculative decoding, followed by generation scheduling.

**34 papers.**

## 3.1 Parallel and Speculative Decoding

- [**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**](https://arxiv.org/pdf/2601.09212) (AAAI, 2026).
  Anneals relaxed acceptance with a specified resampling distribution.

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026).
  Coordinates device-side proposals and interval-based cloud verification to reduce autoregressive image-generation cost and cloud calls.

- [**Continuous Speculative Decoding for Autoregressive Image Generation**](https://arxiv.org/pdf/2411.11925) (ECCV, 2026).
  Uses continuous speculative proposals and approximate trajectory alignment.

- [**CSD: Content-aware Speculative Decoding for Efficient Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) (ICML, 2026).
  Uses content-dependent acceptance relaxation and resampling.

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026).
  Locality-informed verifier modifies acceptance behavior.

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  Low-resolution proposals with upsampling and spatially local verification.

- [**PathRelax: Parallel-Path Relaxed Speculative Jacobi Decoding for Accelerating Auto-Regressive Text-to-Image Generation**](https://arxiv.org/pdf/2606.10492) (arXiv preprint, 2026).
  Searches multiple draft paths with PathExplore and relaxes verification using cross-path semantic similarity in PathRelax.

- [**SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation**](https://arxiv.org/pdf/2512.07503v1) (IEEE TPAMI, 2026).
  Retains high-confidence unaccepted draft states.

- [**SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) (CVPR, 2026).
  Proactive drafting and adaptive continuation.

- [**SJD-PV: Speculative Jacobi Decoding with Phrase Verification for Autoregressive Image Generation**](https://arxiv.org/pdf/2603.06666) (ACM MM, 2026).
  Groups visual-token phrases using corpus co-occurrence and verifies aggregated proposal ratios to reduce repeated Jacobi rounds.

- [**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) (ICML, 2026).
  Semantic subsequence verification changes the tested/committed positions.

- [**SJD-VP: Speculative Jacobi Decoding with Verification Prediction for Autoregressive Image Generation**](https://arxiv.org/pdf/2603.27115v1) (arXiv preprint, 2026).
  Uses historical probability trajectories to guide candidate construction and verification in Speculative Jacobi Decoding.

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026).
  Couples stochastic draws across Jacobi iterations to stabilize draft candidates.

- [**SSD: Spatially Speculative Decoding Accelerates Autoregressive Image Generation**](https://arxiv.org/pdf/2606.20543) (arXiv preprint, 2026).
  Proposes horizontal and vertical continuations, then verifies and corrects two-dimensional speculative drafts in parallel.

- [**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) (CVPR, 2026).
  Skips verification for selected provisional positions.

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025).
  Jacobi candidate reuse with stochastic verification.

- [**Fast Inference of Visual Autoregressive Model with Adjacency-Adaptive Dynamical Draft Trees**](https://arxiv.org/pdf/2512.21857) (arXiv preprint, 2025).
  Adapts draft-tree depth and branching to spatial adjacency during speculative image decoding.

- [**Grouped Speculative Decoding for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Groups spatially related token candidates for verification.

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025).
  Spatial-context drafting improves candidate prediction.

- [**LANTERN++: Enhancing Relaxed Speculative Decoding with Static Tree Drafting for Visual Auto-regressive Models**](https://arxiv.org/pdf/2502.06352) (ICLR SCOPE Workshop, 2025).
  Combines static draft trees with relaxed speculative acceptance for visual autoregressive decoding.

- [**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) (ICLR, 2025).
  Latent-neighborhood relaxed acceptance.

- [**Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf) (NeurIPS, 2025).
  Fine-tunes noisy embeddings for next-clean-token prediction.

- [**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) (NeurIPS, 2025).
  Entropy controls temperature and relaxed acceptance.

- [**Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving**](https://proceedings.mlr.press/v139/song21a/song21a.pdf) (ICML, 2021).
  Parallel nonlinear fixed-point solving.

- [**Predictive Sampling with Forecasting Autoregressive Models**](https://proceedings.mlr.press/v119/wiggers20a/wiggers20a.pdf) (ICML, 2020).
  Uses fixed-point updates and learned forecasts to sample future image variables with fewer sequential AR evaluations.

## 3.2 Generation Scheduling

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026).
  Establishes spatial context with hierarchical checkerboard groups and allocates diffusion-head updates across generation stages and detail regions.

- [**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) (AAAI, 2026).
  Mixes scale work and dispatches late refinement selectively.

- [**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  Spatial parallel drafts with adaptive attention masks.

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026).
  Combines cross-scale conditioning with progressive checkerboard groups to reduce sequential sampling rounds.

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) (ICCV, 2025).
  Selects pivotal token positions using frequency-based scores and restores omitted outputs from preceding-scale cached activations.

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025).
  Organizes multiscale autoregressive generation from low to high frequencies. reported runtime comparisons also vary model capacity.

- [**SkipVAR: Accelerating Visual Autoregressive Modeling via Adaptive Frequency-Aware Skipping**](https://arxiv.org/pdf/2506.08908v3) (arXiv preprint, 2025).
  Uses sample-dependent frequency statistics to skip later scales or omit selected unconditional guidance evaluations.

- [**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) (ICML, 2025).
  Spatially parallel decoding with local context windows.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017).
  Uses a learned multiscale pixel-group factorization for parallel image sampling, changing the original PixelCNN dependencies.


## License

[CC BY 4.0](../../LICENSE.md). Linked papers retain their original licenses.
