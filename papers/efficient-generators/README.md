# Learning Efficient Generators

[Home](../../README.md) · [All categories](../../papers/README.md) · [By year](../../papers/by-year.md)

Efficient predictors and representations, including learned sampling procedures.

**63 papers.** Titles link to recorded PDFs or the official paper page.

## Contents

- [Efficient Conditional Predictors](#efficient-conditional-predictors)
- [Learning Generation Orders and Conditioning Structures](#learning-generation-orders-and-conditioning-structures)
- [Hierarchy and Compact Representations](#hierarchy-and-compact-representations)
- [Distillation and Shorter Sampling Processes](#distillation-and-shorter-sampling-processes)
- [Other efficient generator designs](#other-efficient-generator-designs)

## Efficient Conditional Predictors

- [**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) (ICIC, 2027). [Paper](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) · [Details](../paper-notes.md#dynamicvar)
  - **Accelerates:** High-resolution AR token-path computation.
  - **Approach:** Routes samples among discrete/hybrid/continuous representation paths.
  - Online 2026, proceedings imprint 2027.

- [**EVAR: Edge Visual Autoregressive Models via Principled Pruning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37086-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) · [Details](../paper-notes.md#evar)
  - **Accelerates:** Next-scale VAR parameter and execution cost.
  - **Approach:** Structured pruning with scale-aware compensation and distillation.

- [**NaLA: A 3D Native LLM Layout Agent for High-Quality 3D Scene Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) · [Details](../paper-notes.md#nalalayout)
  - **Accelerates:** AR asset-pose output tokens and repeated optimization in 3D layout generation.
  - **Approach:** Encode room/asset point clouds, generate coarse discrete poses and refine them with a continuous regression head.

- [**OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_6) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) · [Details](../paper-notes.md#omnimamba)
  - **Accelerates:** Autoregressive image-token prediction with a Mamba-2 state-space backbone.
  - **Approach:** Train a unified next-token image/text generator with Mamba-2 and modality-specific vocabularies and adapters.

- [**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26gy.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) · [Details](../paper-notes.md#prismmoe)
  - **Accelerates:** Dense visual AR predictor computation.
  - **Approach:** Dense-to-MoE conversion with sparse expert activation.

- [**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.16546) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Progressive_Supernet_Training_for_Efficient_Visual_Autoregressive_Modeling_CVPR_2026_paper.html) · [PDF](https://arxiv.org/pdf/2511.16546) · [Details](../paper-notes.md#variant)
  - **Accelerates:** VAR inference depth and memory.
  - **Approach:** Progressive supernet training permits scale-dependent subnet execution.

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) · [Details](../paper-notes.md#mpadmri)
  - **Accelerates:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Approach:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.

- [**Visual Implicit Autoregressive Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/jiang26ah.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) · [Details](../paper-notes.md#viar)
  - **Accelerates:** Next-scale visual AR stack.
  - **Approach:** Implicit equilibrium layer with variable inference iterations.

- [**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**](https://arxiv.org/pdf/2411.17787) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2411.17787) · [Details](../paper-notes.md#code)
  - **Accelerates:** Next-scale VAR computation and memory.
  - **Approach:** Large model predicts coarse scales and a smaller model refines later scales.

- [**Denoising Token Prediction in Masked Autoregressive Models**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#ccfdtp)
  - **Accelerates:** Continuous MAR token prediction.
  - **Approach:** Adds denoising refinement of unmasked predictions.

- [**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/95cb60b65d9f2c0cd78b567ffebde9e6-Abstract-Conference.html) · [PDF](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) · [Details](../paper-notes.md#freqexit)
  - **Accelerates:** VAR transformer depth at inference.
  - **Approach:** Trains frequency-aware early-exit behavior.

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) · [Details](../paper-notes.md#hart)
  - **Accelerates:** High-resolution AR image generator.
  - **Approach:** Discrete AR structure with a small residual diffusion module.

- [**Numerical Pruning for Efficient Autoregressive Models**](https://arxiv.org/pdf/2412.12441) (AAAI, 2025). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/34249) · [PDF](https://arxiv.org/pdf/2412.12441) · [Details](../paper-notes.md#numericalpruning)
  - **Accelerates:** Decoder-only AR transformer parameters.
  - **Approach:** Numerical-score structured pruning.

- [**Efficiency-optimized Video Diffusion Models**](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) (ACM MM, 2023). [Paper](https://dl.acm.org/doi/10.1145/3581783.3612406) · [PDF](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) · [Details](../paper-notes.md#evdmacmmm2023)
  - **Accelerates:** Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation.
  - **Approach:** Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm.

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023). [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) · [Details](../paper-notes.md#efficientvqgan)
  - **Accelerates:** High-resolution AR image attention and local code generation.
  - **Approach:** Local tokenization with blockwise parallel generation.

## Learning Generation Orders and Conditioning Structures

- [**Autoregression with Self-Token Prediction**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26du.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) · [Details](../paper-notes.md#sar)
  - **Accelerates:** Grouped AR image generation.
  - **Approach:** Self-token prediction generates flexible token groups per step.

- [**Autoregressive Image Generation with Randomized Parallel Decoding**](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/267852def1fd0db257622892c7e3be2a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) · [Details](../paper-notes.md#arpg)
  - **Accelerates:** Random-order AR image decoding.
  - **Approach:** Decouples position guidance and content prediction for grouped decoding.

- [**From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) · [Details](../paper-notes.md#ccfpredictionrefinement)
  - **Accelerates:** Causal AR image prediction unit.
  - **Approach:** Predicts overlapping tensors to refine previous discrete outputs.

- [**Learning to Expand Images for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.15499v1) (ACM MM, 2026). [Paper](https://2026.acmmm.org/site/technical-programme.html) · [PDF](https://arxiv.org/pdf/2511.15499v1) · [Details](../paper-notes.md#ear)
  - **Accelerates:** AR image generation order and parallel groups.
  - **Approach:** Spiral expansion with length-adaptive parallel decoding.
  - Accepted

- [**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**](https://arxiv.org/pdf/2507.01957v2) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2507.01957v2) · [Details](../paper-notes.md#lpd)
  - **Accelerates:** AR position grouping and inference schedule.
  - **Approach:** Position query tokens and locality-aware parallel generation order.

- [**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7cdf000d22c6cda21f3cbd7467aaf26f-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) · [Details](../paper-notes.md#madformer)
  - **Accelerates:** AR/diffusion hybrid block computation.
  - **Approach:** Allocates AR conditioning layers and iterative diffusion layers.

- [**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#markovvar)
  - **Accelerates:** VAR historical context and memory.
  - **Approach:** Compressed history state and limited scale context.

- [**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37c6d0bc4d2917dcbea693b18504bd87-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) · [Details](../paper-notes.md#mvar)
  - **Accelerates:** VAR spatial and scale context.
  - **Approach:** Restricts conditioning to adjacent scales and local neighborhoods.

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkCTCXo1a9) · [PDF](https://arxiv.org/pdf/2602.03811) · [Details](../paper-notes.md#tmlrwkctcxo1a9)
  - **Accelerates:** Multiscale AR serial sampling schedule.
  - **Approach:** Progressive checkerboards permit parallel positions within scales.

- [**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#xar)
  - **Accelerates:** AR image prediction units and conditional sampling.
  - **Approach:** Next-X prediction over flexible entities.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.10696) · [Details](../paper-notes.md#nar)
  - **Accelerates:** Image and video AR position decoding.
  - **Approach:** Neighbor expansion with dimension-oriented parallel prediction heads.

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) · [Details](../paper-notes.md#nfig)
  - **Accelerates:** Next-scale AR frequency stages.
  - **Approach:** Generates low-frequency structure before higher-frequency detail.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) · [Details](../paper-notes.md#par)
  - **Accelerates:** Image and video AR sequential decoding.
  - **Approach:** Generates spatially distant groups concurrently.

- [**RandAR: Decoder-only Autoregressive Visual Generation in Random Orders**](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) · [Code](https://github.com/ziqipang/RandAR) · [Details](../paper-notes.md#randar)
  - **Accelerates:** Random-order AR image inference.
  - **Approach:** Position instruction tokens enable parallel decoding.

- [**Randomized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#rar)
  - **Accelerates:** AR image generator execution at a quality target.
  - **Approach:** Randomized-order training yields an AR generator evaluated with KV-cached serving.

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#spectralar)
  - **Accelerates:** AR spectral image-token generation.
  - **Approach:** Orders tokens by increasing spectral detail.

- [**Speculative Jacobi-Denoising Decoding for Accelerating Autoregressive Text-to-image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/726ab29b61a749b36d2593648716ae3c-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf) · [Details](../paper-notes.md#sjd2)
  - **Accelerates:** AR text-to-image Jacobi refinement.
  - **Approach:** Fine-tunes noisy embeddings for next-clean-token prediction.

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) · [Details](../paper-notes.md#mqvae)
  - **Accelerates:** AR image sequence redundancy.
  - **Approach:** Masks less-important regions and predicts selected/content positions with Stackformer.

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) · [Details](../paper-notes.md#dqvae)
  - **Accelerates:** AR image code length and decoding.
  - **Approach:** Dynamic quantization plus coarse-to-fine position/content prediction.

## Hierarchy and Compact Representations

- [**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#lactokgen)
  - **Accelerates:** High-resolution AR prior plus image reconstruction.
  - **Approach:** Compact discrete tokens with latent-consistency decoding.

- [**SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37400) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) · [Details](../paper-notes.md#scan)
  - **Accelerates:** AR coarse image prediction and selected refinement.
  - **Approach:** Coarse generation followed by calibrated local refinement.

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) · [Details](../paper-notes.md#supervoxelgpt)
  - **Accelerates:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Approach:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.

- [**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) · [Details](../paper-notes.md#proceedings215)
  - **Accelerates:** AR generation with aligned compact visual tokens.
  - **Approach:** Causal decoder constrains tokenizer dependencies.

- [**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#ccfunicompress)
  - **Accelerates:** Unified-model AR image output sequences.
  - **Approach:** Token compression/decompression shortens visual generation.

- [**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/peng26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) · [Details](../paper-notes.md#uniar)
  - **Accelerates:** Unified AR image-generation token decoding.
  - **Approach:** Channel-bitwise prediction reduces serial autoregressive steps.

- [**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#ccfvibetoken)
  - **Accelerates:** Resolution-flexible AR image prior.
  - **Approach:** Resolution-agnostic 1D tokenization bounds AR sequence burden.

- [**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#dcar)
  - **Accelerates:** Hybrid masked AR text-to-image generator.
  - **Approach:** Deep-compression hybrid tokenizer reduces spatial sequence burden.

- [**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d0d75da30e2d81b928d793afe389ad4-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) · [Details](../paper-notes.md#flexvar)
  - **Accelerates:** Next-scale generator schedule.
  - **Approach:** Ground-truth scale prediction supports variable inference-stage budgets.

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) · [Details](../paper-notes.md#hart)
  - **Accelerates:** High-resolution AR image generator.
  - **Approach:** Discrete AR structure with a small residual diffusion module.

- [**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**](https://arxiv.org/pdf/2505.20288v1) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/zheng25i.html) · [PDF](https://arxiv.org/pdf/2505.20288v1) · [Details](../paper-notes.md#himar)
  - **Accelerates:** Hierarchical continuous masked AR image generation.
  - **Approach:** Low-resolution pivots condition later high-resolution groups.

- [**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**](https://arxiv.org/pdf/2506.04421v1) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.html) · [PDF](https://arxiv.org/pdf/2506.04421v1) · [Details](../paper-notes.md#hmar)
  - **Accelerates:** Hierarchical next-scale masked AR execution.
  - **Approach:** Hierarchical ordering and IO-aware block-sparse attention kernels.

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#spectralar)
  - **Accelerates:** AR spectral image-token generation.
  - **Approach:** Orders tokens by increasing spectral detail.

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023). [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) · [Details](../paper-notes.md#efficientvqgan)
  - **Accelerates:** High-resolution AR image attention and local code generation.
  - **Approach:** Local tokenization with blockwise parallel generation.

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) · [Details](../paper-notes.md#mqvae)
  - **Accelerates:** AR image sequence redundancy.
  - **Approach:** Masks less-important regions and predicts selected/content positions with Stackformer.

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) · [Details](../paper-notes.md#dqvae)
  - **Accelerates:** AR image code length and decoding.
  - **Approach:** Dynamic quantization plus coarse-to-fine position/content prediction.

- [**Autoregressive Image Generation Using Residual Quantization**](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) (CVPR, 2022). [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) · [Details](../paper-notes.md#rqtransformer)
  - **Accelerates:** AR image spatial sequence and depth code prediction.
  - **Approach:** Residual quantization compresses spatial maps and predicts code stacks.

## Distillation and Shorter Sampling Processes

- [**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**](https://arxiv.org/pdf/2603.28049) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_35) · [PDF](https://arxiv.org/pdf/2603.28049) · [Details](../paper-notes.md#driftar)
  - **Accelerates:** Hybrid AR prediction and iterative visual decoding.
  - **Approach:** Entropy-guided speculation and one-step drifting decoder.

- [**FARMER: Flow AutoRegressive Transformer over Pixels**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#farmer)
  - **Accelerates:** Pixel-level autoregressive normalizing-flow sampling.
  - **Approach:** Self-supervised dimension reduction reduces sequential sampling burden.

- [**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**](https://arxiv.org/pdf/2503.09662v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) · [PDF](https://arxiv.org/pdf/2503.09662v1) · [Details](../paper-notes.md#core2reviewcandidate)
  - **Accelerates:** LlamaGen guidance computation.
  - **Approach:** Weak-model training supports guidance and later replacement of expensive computation.

- [**InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars**](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37032-7_37) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) · [Details](../paper-notes.md#interactiveavatarvideo)
  - **Accelerates:** Sampling steps in a causal Wan2.2-5B talking-avatar generator.
  - **Approach:** Apply causal ODE initialization and Self-Forcing DMD to form a few-step AR generator. Use KV caching and separate DiT/VAE devices for streaming execution.

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) · [Details](../paper-notes.md#liveavatarvideo)
  - **Accelerates:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Approach:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.

- [**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#marval)
  - **Accelerates:** MAR iterative conditional sampling.
  - **Approach:** Distills a faster sampler while retaining a masked AR generation organization.

- [**OmniForcing: Unleashing Real-Time Joint Audio-Visual Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) · [Details](../paper-notes.md#omniforcingvideo)
  - **Accelerates:** Causal audio-video block generation and conditional denoising updates.
  - **Approach:** Distill a bidirectional LTX-2 teacher into a streaming AR student with block-causal modality alignment and rolling KV caches.

- [**XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/liu26ck.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) · [Details](../paper-notes.md#xyzflow)
  - **Accelerates:** MAR conditional-head sampling and AR teachers.
  - **Approach:** Shortcut flow modeling with multidimensional prediction.

- [**Continuous Visual Autoregressive Generation via Score Maximization**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/shao25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) · [Details](../paper-notes.md#energyar)
  - **Accelerates:** Continuous AR per-position conditional sampling.
  - **Approach:** Models continuous conditionals with score maximization instead of iterative diffusion.

- [**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**](https://arxiv.org/pdf/2412.17153v3) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67d3805a7b01672c1c2dcb30f6d5290f-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2412.17153v3) · [Details](../paper-notes.md#dd1)
  - **Accelerates:** Complete VAR and LlamaGen latent generation.
  - **Approach:** Distills AR sampling into a few-step flow generator.

- [**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/085f2a21d3f0cef1585fceaa6dacdc15-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) · [Details](../paper-notes.md#dd2)
  - **Accelerates:** Complete VAR and LlamaGen latent generation.
  - **Approach:** Conditional score distillation trains a one-step replacement.

## Other efficient generator designs

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026). [Paper](https://openreview.net/forum?id=OuFNXESoCO) · [PDF](https://arxiv.org/pdf/2412.07720) · [Details](../paper-notes.md#tmlroufnxesoco)
  - **Accelerates:** Image and video block-AR conditional diffusion.
  - **Approach:** Block-causal denoising with reusable past context.

- [**End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chu26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) · [Details](../paper-notes.md#ccfsemantic1d)
  - **Accelerates:** AR prior over 1D image tokens.
  - **Approach:** Jointly learns semantic 1D representation and AR generation.

- [**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) · [Code](https://github.com/FoundationVision/Infinity) · [Details](../paper-notes.md#infinity)
  - **Accelerates:** High-resolution next-scale AR generation.
  - **Approach:** Bitwise prediction avoids a very large categorical classifier.

- [**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (NeurIPS, 2024). [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [Code](https://github.com/FoundationVision/VAR) · [Details](../paper-notes.md#var)
  - **Accelerates:** AR image generation sequence organization.
  - **Approach:** Next-scale prediction replaces raster next-token progression.

- [**Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving**](https://proceedings.mlr.press/v139/song21a/song21a.pdf) (ICML, 2021). [Paper](https://proceedings.mlr.press/v139/song21a.html) · [PDF](https://proceedings.mlr.press/v139/song21a/song21a.pdf) · [Details](../paper-notes.md#songjacobi)
  - **Accelerates:** Deep AR image-model feedforward sampling.
  - **Approach:** Parallel nonlinear fixed-point solving.

- [**Blockwise Parallel Decoding for Deep Autoregressive Models**](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) (NeurIPS, 2018). [Paper](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) · [Details](../paper-notes.md#blockwise)
  - **Accelerates:** AR image super-resolution decoding.
  - **Approach:** Predicts blocks provisionally and commits the prefix validated by a scoring model.
