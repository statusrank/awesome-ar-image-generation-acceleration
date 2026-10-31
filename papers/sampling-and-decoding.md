# Sampling and Decoding

[Home](../README.md) · [Collections](../papers/README.md)

Parallel evaluation, speculative decoding and generation scheduling.

**31 papers.**

## Contents

- [Parallel and Speculative Candidate Generation](#parallel-and-speculative-candidate-generation)
- [Verification and Commitment](#verification-and-commitment)
- [Generation Scheduling and Context Organization](#generation-scheduling-and-context-organization)
- [Other parallel sampling](#other-parallel-sampling)

## Parallel and Speculative Candidate Generation

<a id="paper-tmlrxyatz9hpe7"></a>

- [**Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding**](https://arxiv.org/pdf/2505.24791) (TMLR, 2026).
  - **Focus:** Image generation by autoregressive normalizing flows.
  - **Mechanism:** Selective Jacobi iterations parallelize sequential flow inversions.
  - **Source location:** PDF p. 9.

<a id="paper-ciar"></a>

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026).
  - **Focus:** Cloud-device AR image decoding.
  - **Mechanism:** On-device interval verification reduces cloud verification calls.
  - **Source location:** PDF p. 7.

<a id="paper-fasthybrid"></a>

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** Hybrid AR image generator with diffusion decoder.
  - **Mechanism:** Lookahead and guided decoding reduce hybrid generation computation.
  - **Source location:** PDF p. 6.

<a id="paper-lisa"></a>

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026).
  - **Focus:** Visual AR speculative verification.
  - **Mechanism:** Locality-informed verifier modifies acceptance behavior.
  - **Source location:** PDF p. 13.

<a id="paper-mulosd"></a>

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** High-resolution AR image speculative generation.
  - **Mechanism:** Low-resolution proposals with upsampling and spatially local verification.
  - **Source location:** PDF p. 1.

<a id="paper-sjdplus"></a>

- [**SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation**](https://arxiv.org/pdf/2512.07503v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026).
  - **Focus:** AR text-to-image Jacobi candidate reuse.
  - **Mechanism:** Retains high-confidence unaccepted draft states.
  - **Source location:** PDF p. 1.

<a id="paper-sjdpac"></a>

- [**SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** AR image Jacobi candidate generation.
  - **Mechanism:** Proactive drafting and adaptive continuation.
  - **Source location:** PDF p. 6.

<a id="paper-scd"></a>

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026).
  - **Focus:** AR image stochastic speculative execution.
  - **Mechanism:** Couples proposal/verification randomness.
  - **Source location:** PDF p. 1.

<a id="paper-supervoxelgpt"></a>

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026).
  - **Focus:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Mechanism:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.
  - **Source location:** PDF pp. 10–11, AR training and Jacobi decoding; PDF p. 12, Tables 1–2; PDF pp. 13–14, setup and generation efficiency.

<a id="paper-sjd"></a>

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025).
  - **Focus:** AR text-to-image next-token execution.
  - **Mechanism:** Jacobi candidate reuse with stochastic verification.
  - **Source location:** PDF p. 8.

<a id="paper-hawk"></a>

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025).
  - **Focus:** AR text-to-image speculative proposals.
  - **Mechanism:** Spatial-context drafting improves candidate prediction.
  - **Source location:** PDF p. 1.

## Verification and Commitment

<a id="paper-coolsd"></a>

- [**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**](https://arxiv.org/pdf/2601.09212) (AAAI, 2026).
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Anneals relaxed acceptance with a specified resampling distribution.
  - **Source location:** PDF p. 7.

<a id="paper-cspd"></a>

- [**Continuous Speculative Decoding for Autoregressive Image Generation**](https://arxiv.org/pdf/2411.11925) (ECCV, 2026).
  - **Focus:** MAR continuous conditional sampling.
  - **Mechanism:** Uses continuous speculative proposals and approximate trajectory alignment.
  - **Source location:** PDF p. 2.

<a id="paper-csd"></a>

- [**CSD: Content-aware Speculative Decoding for Efficient Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) (ICML, 2026).
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Uses content-dependent acceptance relaxation and resampling.
  - **Source location:** PDF p. 9.

<a id="paper-lisa"></a>

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026).
  - **Focus:** Visual AR speculative verification.
  - **Mechanism:** Locality-informed verifier modifies acceptance behavior.
  - **Source location:** PDF p. 13.

<a id="paper-mulosd"></a>

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** High-resolution AR image speculative generation.
  - **Mechanism:** Low-resolution proposals with upsampling and spatially local verification.
  - **Source location:** PDF p. 1.

<a id="paper-sjdsv"></a>

- [**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) (ICML, 2026).
  - **Focus:** AR image speculative verification.
  - **Mechanism:** Semantic subsequence verification changes the tested/committed positions.
  - **Source location:** PDF p. 7.

<a id="paper-vvs"></a>

- [**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** AR visual speculative verification.
  - **Mechanism:** Skips verification for selected provisional positions.
  - **Source location:** PDF p. 1.

<a id="paper-sjd"></a>

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025).
  - **Focus:** AR text-to-image next-token execution.
  - **Mechanism:** Jacobi candidate reuse with stochastic verification.
  - **Source location:** PDF p. 8.

<a id="paper-gsd"></a>

- [**Grouped Speculative Decoding for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  - **Focus:** AR image speculative decoding.
  - **Mechanism:** Groups spatially related token candidates for verification.
  - **Source location:** PDF p. 8.

<a id="paper-hawk"></a>

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025).
  - **Focus:** AR text-to-image speculative proposals.
  - **Mechanism:** Spatial-context drafting improves candidate prediction.
  - **Source location:** PDF p. 1.

<a id="paper-lantern"></a>

- [**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) (ICLR, 2025).
  - **Focus:** Visual AR speculative acceptance.
  - **Mechanism:** Latent-neighborhood relaxed acceptance.
  - **Source location:** PDF p. 22.

<a id="paper-entropydecoding"></a>

- [**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) (NeurIPS, 2025).
  - **Focus:** Visual AR sampling and speculation.
  - **Mechanism:** Entropy controls temperature and relaxed acceptance.
  - **Source location:** PDF p. 9.

## Generation Scheduling and Context Organization

<a id="paper-gtr"></a>

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026).
  - **Focus:** MAR stages and inner sampling budget.
  - **Mechanism:** Separates structure generation and detail reconstruction with frequency-weighted selection.
  - **Source location:** PDF p. 1.

<a id="paper-hiarvideo"></a>

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026).
  - **Focus:** Hierarchical denoising and pipelined execution of AR video blocks.
  - **Mechanism:** Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.
  - **Source location:** PDF p. 9, Table 1 and Section 4.1; PDF pp. 10–11, Section 4.2.

<a id="paper-moss"></a>

- [**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) (AAAI, 2026).
  - **Focus:** High-resolution next-scale transformer execution.
  - **Mechanism:** Mixes scale work and dispatches late refinement selectively.
  - **Source location:** PDF p. 7.

<a id="paper-pjd"></a>

- [**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  - **Focus:** AR image Jacobi candidate refinement.
  - **Mechanism:** Spatial parallel drafts with adaptive attention masks.
  - **Source location:** PDF p. 1.

<a id="paper-tmlrwkctcxo1a9"></a>

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026).
  - **Focus:** Multiscale AR serial sampling schedule.
  - **Mechanism:** Progressive checkerboards permit parallel positions within scales.
  - **Source location:** PDF p. 6.

<a id="paper-mpadmri"></a>

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026).
  - **Focus:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Mechanism:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.
  - **Source location:** PDF p. 2, Figure 1; p. 9, Section 4.2; pp. 14–15, reduced-refinement discussion. Figure 1.

<a id="paper-emigm"></a>

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025).
  - **Focus:** Continuous masked image generation including MAR.
  - **Mechanism:** Revises masking, sampling schedule and conditional token modeling.
  - **Source location:** PDF p. 29.

<a id="paper-fastvar"></a>

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://arxiv.org/pdf/2503.23367) (ICCV, 2025).
  - **Focus:** High-resolution next-scale token processing.
  - **Mechanism:** Cached token pruning forwards selected tokens and recovers omitted states.
  - **Source location:** PDF p. 1.

<a id="paper-nfig"></a>

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025).
  - **Focus:** Next-scale AR frequency stages.
  - **Mechanism:** Generates low-frequency structure before higher-frequency detail.
  - **Source location:** PDF p. 7.

<a id="paper-zipar"></a>

- [**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) (ICML, 2025).
  - **Focus:** Causal visual AR decoding.
  - **Mechanism:** Spatially parallel decoding with local context windows.
  - **Source location:** PDF p. 7.

<a id="paper-parallelmultiscale2017"></a>

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017).
  - **Focus:** Pixel AR sampling dependency depth.
  - **Mechanism:** Parallel multiscale density factorization.
  - **Source location:** PDF p. 8.

## Other parallel sampling

<a id="paper-ardm2022"></a>

- [**Autoregressive Diffusion Models**](https://arxiv.org/pdf/2110.02037) (ICLR, 2022).
  - **Focus:** Order-agnostic AR image model evaluations.
  - **Mechanism:** Parallel generation under a selected network-evaluation budget.
  - **Source location:** PDF p. 7.
