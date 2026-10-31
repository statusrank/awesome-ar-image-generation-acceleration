# Learning Efficient Generators

[Home](../README.md) · [Collections](../papers/README.md)

Efficient predictors and representations, including learned sampling procedures.

**63 papers.**

## Contents

- [Efficient Conditional Predictors](#efficient-conditional-predictors)
- [Learning Generation Orders and Conditioning Structures](#learning-generation-orders-and-conditioning-structures)
- [Hierarchy and Compact Representations](#hierarchy-and-compact-representations)
- [Distillation and Shorter Sampling Processes](#distillation-and-shorter-sampling-processes)
- [Other efficient generator designs](#other-efficient-generator-designs)

## Efficient Conditional Predictors

<a id="paper-dynamicvar"></a>

- [**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) (ICIC, 2027). [Paper](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16)
  - **Focus:** High-resolution AR token-path computation.
  - **Mechanism:** Routes samples among discrete/hybrid/continuous representation paths.
  - **Source:** [Paper](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16), Publisher abstract, inference-throughput statement.

<a id="paper-evar"></a>

- [**EVAR: Edge Visual Autoregressive Models via Principled Pruning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37086-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf)
  - **Focus:** Next-scale VAR parameter and execution cost.
  - **Mechanism:** Structured pruning with scale-aware compensation and distillation.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf#page=1), PDF p. 1.

<a id="paper-nalalayout"></a>

- [**NaLA: A 3D Native LLM Layout Agent for High-Quality 3D Scene Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf)
  - **Focus:** AR asset-pose output tokens and repeated optimization in 3D layout generation.
  - **Mechanism:** Encode room/asset point clouds, generate coarse discrete poses and refine them with a continuous regression head.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf), PDF pp. 7–8, token construction; pp. 10 and 12–13, baseline setup, Section 5.6 and Figure 7d. Figure.

<a id="paper-omnimamba"></a>

- [**OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_6) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf)
  - **Focus:** Autoregressive image-token prediction with a Mamba-2 state-space backbone.
  - **Mechanism:** Train a unified next-token image/text generator with Mamba-2 and modality-specific vocabularies and adapters.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf), PDF pp. 3, 12–13, Section 4.5 and Table 4.

<a id="paper-prismmoe"></a>

- [**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26gy.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf)
  - **Focus:** Dense visual AR predictor computation.
  - **Mechanism:** Dense-to-MoE conversion with sparse expert activation.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf#page=7), PDF p. 7.

<a id="paper-variant"></a>

- [**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.16546) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Progressive_Supernet_Training_for_Efficient_Visual_Autoregressive_Modeling_CVPR_2026_paper.html) · [PDF](https://arxiv.org/pdf/2511.16546)
  - **Focus:** VAR inference depth and memory.
  - **Mechanism:** Progressive supernet training permits scale-dependent subnet execution.
  - **Source:** [Paper](https://arxiv.org/pdf/2511.16546#page=5), PDF p. 5.

<a id="paper-mpadmri"></a>

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf)
  - **Focus:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Mechanism:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf), PDF p. 2, Figure 1; p. 9, Section 4.2; pp. 14–15, reduced-refinement discussion. Figure 1.

<a id="paper-viar"></a>

- [**Visual Implicit Autoregressive Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/jiang26ah.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf)
  - **Focus:** Next-scale visual AR stack.
  - **Mechanism:** Implicit equilibrium layer with variable inference iterations.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf#page=6), PDF p. 6.

<a id="paper-code"></a>

- [**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**](https://arxiv.org/pdf/2411.17787) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2411.17787)
  - **Focus:** Next-scale VAR computation and memory.
  - **Mechanism:** Large model predicts coarse scales and a smaller model refines later scales.
  - **Source:** [Paper](https://arxiv.org/pdf/2411.17787#page=2), PDF p. 2.

<a id="paper-ccfdtp"></a>

- [**Denoising Token Prediction in Masked Autoregressive Models**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf)
  - **Focus:** Continuous MAR token prediction.
  - **Mechanism:** Adds denoising refinement of unmasked predictions.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf#page=8), PDF p. 8.

<a id="paper-freqexit"></a>

- [**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/95cb60b65d9f2c0cd78b567ffebde9e6-Abstract-Conference.html) · [PDF](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf)
  - **Focus:** VAR transformer depth at inference.
  - **Mechanism:** Trains frequency-aware early-exit behavior.
  - **Source:** [Paper](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf#page=25), PDF p. 25.

<a id="paper-hart"></a>

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf)
  - **Focus:** High-resolution AR image generator.
  - **Mechanism:** Discrete AR structure with a small residual diffusion module.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-numericalpruning"></a>

- [**Numerical Pruning for Efficient Autoregressive Models**](https://arxiv.org/pdf/2412.12441) (AAAI, 2025). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/34249) · [PDF](https://arxiv.org/pdf/2412.12441)
  - **Focus:** Decoder-only AR transformer parameters.
  - **Mechanism:** Numerical-score structured pruning.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/download/34249/36404#page=7), PDF p. 7.

<a id="paper-evdmacmmm2023"></a>

- [**Efficiency-optimized Video Diffusion Models**](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) (ACM MM, 2023). [Paper](https://dl.acm.org/doi/10.1145/3581783.3612406) · [PDF](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf)
  - **Focus:** Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation.
  - **Mechanism:** Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm.
  - **Source:** [Paper](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf), EVDM PDF pp. 5–6, Tables 2–3 and experimental setup; PDF p. 8, Table 9. MCVD original Section 2.1 and Figure 2.

<a id="paper-efficientvqgan"></a>

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023). [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf)
  - **Focus:** High-resolution AR image attention and local code generation.
  - **Mechanism:** Local tokenization with blockwise parallel generation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html#page=6), PDF p. 6.

## Learning Generation Orders and Conditioning Structures

<a id="paper-sar"></a>

- [**Autoregression with Self-Token Prediction**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26du.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf)
  - **Focus:** Grouped AR image generation.
  - **Mechanism:** Self-token prediction generates flexible token groups per step.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf#page=5), PDF p. 5.

<a id="paper-arpg"></a>

- [**Autoregressive Image Generation with Randomized Parallel Decoding**](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/267852def1fd0db257622892c7e3be2a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf)
  - **Focus:** Random-order AR image decoding.
  - **Mechanism:** Decouples position guidance and content prediction for grouped decoding.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf#page=14), PDF p. 14.

<a id="paper-ccfpredictionrefinement"></a>

- [**From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf)
  - **Focus:** Causal AR image prediction unit.
  - **Mechanism:** Predicts overlapping tensors to refine previous discrete outputs.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf#page=6), PDF p. 6.

<a id="paper-ear"></a>

- [**Learning to Expand Images for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.15499v1) (ACM MM, 2026). [Paper](https://2026.acmmm.org/site/technical-programme.html) · [PDF](https://arxiv.org/pdf/2511.15499v1)
  - **Focus:** AR image generation order and parallel groups.
  - **Mechanism:** Spiral expansion with length-adaptive parallel decoding.
  - **Source:** [Paper](https://arxiv.org/pdf/2511.15499v1#page=11), PDF p. 11.

<a id="paper-lpd"></a>

- [**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**](https://arxiv.org/pdf/2507.01957v2) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2507.01957v2)
  - **Focus:** AR position grouping and inference schedule.
  - **Mechanism:** Position query tokens and locality-aware parallel generation order.
  - **Source:** [Paper](https://arxiv.org/pdf/2507.01957v2#page=24), PDF p. 24.

<a id="paper-madformer"></a>

- [**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7cdf000d22c6cda21f3cbd7467aaf26f-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf)
  - **Focus:** AR/diffusion hybrid block computation.
  - **Mechanism:** Allocates AR conditioning layers and iterative diffusion layers.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-markovvar"></a>

- [**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf)
  - **Focus:** VAR historical context and memory.
  - **Mechanism:** Compressed history state and limited scale context.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf#page=7), PDF p. 7.

<a id="paper-mvar"></a>

- [**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37c6d0bc4d2917dcbea693b18504bd87-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf)
  - **Focus:** VAR spatial and scale context.
  - **Mechanism:** Restricts conditioning to adjacent scales and local neighborhoods.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf#page=6), PDF p. 6.

<a id="paper-tmlrwkctcxo1a9"></a>

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkCTCXo1a9) · [PDF](https://arxiv.org/pdf/2602.03811)
  - **Focus:** Multiscale AR serial sampling schedule.
  - **Mechanism:** Progressive checkerboards permit parallel positions within scales.
  - **Source:** [Paper](https://arxiv.org/pdf/2602.03811#page=6), PDF p. 6.

<a id="paper-xar"></a>

- [**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR image prediction units and conditional sampling.
  - **Mechanism:** Next-X prediction over flexible entities.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=2), PDF p. 2.

<a id="paper-nar"></a>

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.10696)
  - **Focus:** Image and video AR position decoding.
  - **Mechanism:** Neighbor expansion with dimension-oriented parallel prediction heads.
  - **Source:** [Paper](https://arxiv.org/pdf/2503.10696#page=8), PDF p. 8.

<a id="paper-nfig"></a>

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf)
  - **Focus:** Next-scale AR frequency stages.
  - **Mechanism:** Generates low-frequency structure before higher-frequency detail.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-par"></a>

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf)
  - **Focus:** Image and video AR sequential decoding.
  - **Mechanism:** Generates spatially distant groups concurrently.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf#page=1), PDF p. 1.

<a id="paper-randar"></a>

- [**RandAR: Decoder-only Autoregressive Visual Generation in Random Orders**](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) · [Code](https://github.com/ziqipang/RandAR)
  - **Focus:** Random-order AR image inference.
  - **Mechanism:** Position instruction tokens enable parallel decoding.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf#page=7), PDF p. 7.

<a id="paper-rar"></a>

- [**Randomized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR image generator execution at a quality target.
  - **Mechanism:** Randomized-order training yields an AR generator evaluated with KV-cached serving.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=7), PDF p. 7.

<a id="paper-spectralar"></a>

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR spectral image-token generation.
  - **Mechanism:** Orders tokens by increasing spectral detail.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=6), PDF p. 6.

<a id="paper-sjd2"></a>

- [**Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/726ab29b61a749b36d2593648716ae3c-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf)
  - **Focus:** AR text-to-image Jacobi refinement.
  - **Mechanism:** Fine-tunes noisy embeddings for next-clean-token prediction.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf#page=8), PDF p. 8.

<a id="paper-mqvae"></a>

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf)
  - **Focus:** AR image sequence redundancy.
  - **Mechanism:** Masks less-important regions and predicts selected/content positions with Stackformer.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf#page=8), PDF p. 8.

<a id="paper-dqvae"></a>

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf)
  - **Focus:** AR image code length and decoding.
  - **Mechanism:** Dynamic quantization plus coarse-to-fine position/content prediction.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf#page=8), PDF p. 8.

## Hierarchy and Compact Representations

<a id="paper-lactokgen"></a>

- [**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf)
  - **Focus:** High-resolution AR prior plus image reconstruction.
  - **Mechanism:** Compact discrete tokens with latent-consistency decoding.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf#page=6), PDF p. 6.

<a id="paper-scan"></a>

- [**SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37400) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362)
  - **Focus:** AR coarse image prediction and selected refinement.
  - **Mechanism:** Coarse generation followed by calibrated local refinement.
  - **Source:** [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37400#page=6), PDF p. 6.

<a id="paper-supervoxelgpt"></a>

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf)
  - **Focus:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Mechanism:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf), PDF pp. 10–11, AR training and Jacobi decoding; PDF p. 12, Tables 1–2; PDF pp. 13–14, setup and generation efficiency.

<a id="paper-proceedings215"></a>

- [**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf)
  - **Focus:** AR generation with aligned compact visual tokens.
  - **Mechanism:** Causal decoder constrains tokenizer dependencies.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-ccfunicompress"></a>

- [**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf)
  - **Focus:** Unified-model AR image output sequences.
  - **Mechanism:** Token compression/decompression shortens visual generation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf#page=6), PDF p. 6.

<a id="paper-uniar"></a>

- [**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/peng26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf)
  - **Focus:** Unified AR image-generation token decoding.
  - **Mechanism:** Channel-bitwise prediction reduces serial autoregressive steps.
  - **Source:** [Paper](https://proceedings.mlr.press/v306/peng26k.html#page=15), PDF p. 15.

<a id="paper-ccfvibetoken"></a>

- [**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf)
  - **Focus:** Resolution-flexible AR image prior.
  - **Mechanism:** Resolution-agnostic 1D tokenization bounds AR sequence burden.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf#page=1), PDF p. 1.

<a id="paper-dcar"></a>

- [**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf)
  - **Focus:** Hybrid masked AR text-to-image generator.
  - **Mechanism:** Deep-compression hybrid tokenizer reduces spatial sequence burden.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf#page=1), PDF p. 1.

<a id="paper-flexvar"></a>

- [**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d0d75da30e2d81b928d793afe389ad4-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf)
  - **Focus:** Next-scale generator schedule.
  - **Mechanism:** Ground-truth scale prediction supports variable inference-stage budgets.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf#page=6), PDF p. 6.

<a id="paper-hart"></a>

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf)
  - **Focus:** High-resolution AR image generator.
  - **Mechanism:** Discrete AR structure with a small residual diffusion module.
  - **Source:** [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf#page=1), PDF p. 1.

<a id="paper-himar"></a>

- [**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**](https://arxiv.org/pdf/2505.20288v1) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/zheng25i.html) · [PDF](https://arxiv.org/pdf/2505.20288v1)
  - **Focus:** Hierarchical continuous masked AR image generation.
  - **Mechanism:** Low-resolution pivots condition later high-resolution groups.
  - **Source:** [Paper](https://arxiv.org/pdf/2505.20288v1#page=8), PDF p. 8.

<a id="paper-hmar"></a>

- [**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**](https://arxiv.org/pdf/2506.04421v1) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.html) · [PDF](https://arxiv.org/pdf/2506.04421v1)
  - **Focus:** Hierarchical next-scale masked AR execution.
  - **Mechanism:** Hierarchical ordering and IO-aware block-sparse attention kernels.
  - **Source:** [Paper](https://arxiv.org/pdf/2506.04421v1#page=1), PDF p. 1.

<a id="paper-spectralar"></a>

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf)
  - **Focus:** AR spectral image-token generation.
  - **Mechanism:** Orders tokens by increasing spectral detail.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf#page=6), PDF p. 6.

<a id="paper-efficientvqgan"></a>

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023). [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf)
  - **Focus:** High-resolution AR image attention and local code generation.
  - **Mechanism:** Local tokenization with blockwise parallel generation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html#page=6), PDF p. 6.

<a id="paper-mqvae"></a>

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf)
  - **Focus:** AR image sequence redundancy.
  - **Mechanism:** Masks less-important regions and predicts selected/content positions with Stackformer.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf#page=8), PDF p. 8.

<a id="paper-dqvae"></a>

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf)
  - **Focus:** AR image code length and decoding.
  - **Mechanism:** Dynamic quantization plus coarse-to-fine position/content prediction.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf#page=8), PDF p. 8.

<a id="paper-rqtransformer"></a>

- [**Autoregressive Image Generation Using Residual Quantization**](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) (CVPR, 2022). [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf)
  - **Focus:** AR image spatial sequence and depth code prediction.
  - **Mechanism:** Residual quantization compresses spatial maps and predicts code stacks.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html#page=7), PDF p. 7.

## Distillation and Shorter Sampling Processes

<a id="paper-driftar"></a>

- [**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**](https://arxiv.org/pdf/2603.28049) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_35) · [PDF](https://arxiv.org/pdf/2603.28049)
  - **Focus:** Hybrid AR prediction and iterative visual decoding.
  - **Mechanism:** Entropy-guided speculation and one-step drifting decoder.
  - **Source:** [Paper](https://arxiv.org/pdf/2603.28049#page=13), PDF p. 13.

<a id="paper-farmer"></a>

- [**FARMER: Flow AutoRegressive Transformer over Pixels**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf)
  - **Focus:** Pixel-level autoregressive normalizing-flow sampling.
  - **Mechanism:** Self-supervised dimension reduction reduces sequential sampling burden.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf#page=8), PDF p. 8.

<a id="paper-core2reviewcandidate"></a>

- [**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**](https://arxiv.org/pdf/2503.09662v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) · [PDF](https://arxiv.org/pdf/2503.09662v1)
  - **Focus:** LlamaGen guidance computation.
  - **Mechanism:** Weak-model training supports guidance and later replacement of expensive computation.
  - **Source:** [Paper](https://arxiv.org/pdf/2503.09662v1#page=16), PDF p. 16.

<a id="paper-interactiveavatarvideo"></a>

- [**InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars**](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37032-7_37) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf)
  - **Focus:** Sampling steps in a causal Wan2.2-5B talking-avatar generator.
  - **Mechanism:** Apply causal ODE initialization and Self-Forcing DMD to form a few-step AR generator. Use KV caching and separate DiT/VAE devices for streaming execution.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf), PDF p. 11, Sections 3.4 and 4.1; pp. 13–14, Tables 1–2.

<a id="paper-liveavatarvideo"></a>

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf)
  - **Focus:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Mechanism:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf), PDF pp. 2–3, streaming definition; PDF pp. 9–11, execution and setup; PDF p. 13, Table 3.

<a id="paper-marval"></a>

- [**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf)
  - **Focus:** MAR iterative conditional sampling.
  - **Mechanism:** Distills a faster sampler while retaining a masked AR generation organization.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf#page=7), PDF p. 7.

<a id="paper-omniforcingvideo"></a>

- [**OmniForcing: Unleashing Real-Time Joint Audio-Visual Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf)
  - **Focus:** Causal audio-video block generation and conditional denoising updates.
  - **Mechanism:** Distill a bidirectional LTX-2 teacher into a streaming AR student with block-causal modality alignment and rolling KV caches.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf), PDF pp. 5–11, method; pp. 12 and 14, timing protocol and Tables 1–2. Tables.

<a id="paper-xyzflow"></a>

- [**XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/liu26ck.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf)
  - **Focus:** MAR conditional-head sampling and AR teachers.
  - **Mechanism:** Shortcut flow modeling with multidimensional prediction.
  - **Source:** [Paper](https://proceedings.mlr.press/v306/liu26ck.html#page=6), PDF p. 6.

<a id="paper-energyar"></a>

- [**Continuous Visual Autoregressive Generation via Score Maximization**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/shao25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf)
  - **Focus:** Continuous AR per-position conditional sampling.
  - **Mechanism:** Models continuous conditionals with score maximization instead of iterative diffusion.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf#page=7), PDF p. 7.

<a id="paper-dd1"></a>

- [**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**](https://arxiv.org/pdf/2412.17153v3) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67d3805a7b01672c1c2dcb30f6d5290f-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2412.17153v3)
  - **Focus:** Complete VAR and LlamaGen latent generation.
  - **Mechanism:** Distills AR sampling into a few-step flow generator.
  - **Source:** [Paper](https://arxiv.org/pdf/2412.17153v3#page=10), PDF p. 10.

<a id="paper-dd2"></a>

- [**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/085f2a21d3f0cef1585fceaa6dacdc15-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf)
  - **Focus:** Complete VAR and LlamaGen latent generation.
  - **Mechanism:** Conditional score distillation trains a one-step replacement.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf#page=1), PDF p. 1.

## Other efficient generator designs

<a id="paper-tmlroufnxesoco"></a>

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026). [Paper](https://openreview.net/forum?id=OuFNXESoCO) · [PDF](https://arxiv.org/pdf/2412.07720)
  - **Focus:** Image and video block-AR conditional diffusion.
  - **Mechanism:** Block-causal denoising with reusable past context.
  - **Source:** [Paper](https://arxiv.org/pdf/2412.07720#page=10), PDF p. 10.

<a id="paper-ccfsemantic1d"></a>

- [**End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chu26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf)
  - **Focus:** AR prior over 1D image tokens.
  - **Mechanism:** Jointly learns semantic 1D representation and AR generation.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf#page=13), PDF p. 13.

<a id="paper-infinity"></a>

- [**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) · [Code](https://github.com/FoundationVision/Infinity)
  - **Focus:** High-resolution next-scale AR generation.
  - **Mechanism:** Bitwise prediction avoids a very large categorical classifier.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf#page=6), PDF p. 6.

<a id="paper-var"></a>

- [**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (NeurIPS, 2024). [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [Code](https://github.com/FoundationVision/VAR)
  - **Focus:** AR image generation sequence organization.
  - **Mechanism:** Next-scale prediction replaces raster next-token progression.
  - **Source:** [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf#page=7), PDF p. 7.

<a id="paper-songjacobi"></a>

- [**Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving**](https://proceedings.mlr.press/v139/song21a/song21a.pdf) (ICML, 2021). [Paper](https://proceedings.mlr.press/v139/song21a.html) · [PDF](https://proceedings.mlr.press/v139/song21a/song21a.pdf)
  - **Focus:** Deep AR image-model feedforward sampling.
  - **Mechanism:** Parallel nonlinear fixed-point solving.
  - **Source:** [Paper](https://proceedings.mlr.press/v139/song21a/song21a.pdf#page=7), PDF p. 7.

<a id="paper-blockwise"></a>

- [**Blockwise Parallel Decoding for Deep Autoregressive Models**](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) (NeurIPS, 2018). [Paper](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf)
  - **Focus:** AR image super-resolution decoding.
  - **Mechanism:** Predicts blocks provisionally and commits the prefix validated by a scoring model.
  - **Source:** [Paper](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html#page=7), PDF p. 7.
