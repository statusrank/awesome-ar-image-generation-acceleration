# All Core Acceleration Papers

[Home](../../README.md) · [Categories](../README.md) · [Source notes](../paper-notes.md)

**152 papers.**

- [3D geometry](#3d-geometry)
- [3D human motion](#3d-human-motion)
- [3D layout](#3d-layout)
- [3D mesh](#3d-mesh)
- [3D point cloud](#3d-point-cloud)
- [3D scene layout](#3d-scene-layout)
- [3D shape](#3d-shape)
- [image](#image)
- [image super-resolution](#image-super-resolution)
- [image; video](#image-video)
- [video](#video)
- [video / scene forecasts](#video--scene-forecasts)
- [video avatar](#video-avatar)
- [video view expansion](#video-view-expansion)
- [volumetric medical image synthesis](#volumetric-medical-image-synthesis)

## 3D geometry

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) · [Details](../paper-notes.md#supervoxelgpt)
  - **Accelerates:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Approach:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.

## 3D human motion

- [**ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_24) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf) · [Details](../paper-notes.md#scalemogenmotion)
  - **Accelerates:** Seven scale-wise AR stages for motion synthesis.
  - **Approach:** Section 3.2 conditions each skeletal-temporal scale on text and a prefix formed from completed coarser token maps. Section 4.7 specifies seven sequential scale stages. No Flow Matching head is part of the inspected next-scale bitwise-token prediction mechanism.

## 3D layout

- [**Repurposing 3D Generative Model for Autoregressive Layout Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#lavigen3d)
  - **Accelerates:** Autoregressive 3D layout generation.
  - **Approach:** Repurposes a 3D diffusion model and uses dual-guidance self-rollout distillation.

## 3D mesh

- [**FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#flashmesh3d)
  - **Accelerates:** AR mesh token decoding.
  - **Approach:** Trained face/point/coordinate proposal blocks with structured correction and backbone verification.

- [**XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26dn.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf) · [Details](../paper-notes.md#xspecmesh3d)
  - **Accelerates:** AR mesh next-token decoding.
  - **Approach:** Multi-head proposals with backbone verification/resampling and head distillation.

## 3D point cloud

- [**PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#pointnsp3d)
  - **Accelerates:** AR point-cloud sampling.
  - **Approach:** Next-scale level-of-detail prediction replaces next-point progression.

## 3D scene layout

- [**NaLA: A 3D Native LLM Layout Agent for High-Quality 3D Scene Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) · [Details](../paper-notes.md#nalalayout)
  - **Accelerates:** AR asset-pose output tokens and repeated optimization in 3D layout generation.
  - **Approach:** Encode room/asset point clouds, generate coarse discrete poses and refine them with a continuous regression head.

## 3D shape

- [**3D-WAG: Hierarchical Wavelet-Guided Autoregressive Generation for High-Fidelity 3D Shapes**](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf) (BMVC, 2025). [Paper](https://bmvc2025.bmva.org/proceedings/1064/) · [PDF](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf) · [Details](../paper-notes.md#wag3d)
  - **Accelerates:** Autoregressive shape token sampling.
  - **Approach:** Wavelet hierarchy supports next-scale generation.

## image

- [**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) (ICIC, 2027). [Paper](https://link.springer.com/chapter/10.1007/978-981-92-3378-6_16) · [Details](../paper-notes.md#dynamicvar)
  - **Accelerates:** High-resolution AR token-path computation.
  - **Approach:** Routes samples among discrete/hybrid/continuous representation paths.
  - Online 2026, proceedings imprint 2027.

- [**Accelerating Inference of Discrete Autoregressive Normalizing Flows by Selective Jacobi Decoding**](https://arxiv.org/pdf/2505.24791) (TMLR, 2026). [Paper](https://openreview.net/forum?id=xYATz9HpE7) · [PDF](https://arxiv.org/pdf/2505.24791) · [Details](../paper-notes.md#tmlrxyatz9hpe7)
  - **Accelerates:** Image generation by autoregressive normalizing flows.
  - **Approach:** Selective Jacobi iterations parallelize sequential flow inversions.

- [**Adaptive Visual Autoregressive Acceleration via Dual-Linkage Entropy Analysis**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26dq.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26dq/zhang26dq.pdf) · [Details](../paper-notes.md#nova)
  - **Accelerates:** Next-scale visual AR token processing.
  - **Approach:** Entropy-guided adaptive token reduction and cached residual reuse.

- [**AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers**](https://arxiv.org/pdf/2511.16047) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39936) · [PDF](https://arxiv.org/pdf/2511.16047) · [Details](../paper-notes.md#amskv)
  - **Accelerates:** Next-scale VAR KV memory and attention.
  - **Approach:** Retains condensed and local scales with adaptive cache allocation.

- [**Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation**](https://arxiv.org/pdf/2601.09212) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39489) · [PDF](https://arxiv.org/pdf/2601.09212) · [Details](../paper-notes.md#coolsd)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Anneals relaxed acceptance with a specified resampling distribution.

- [**ARVAR: Accelerating Visual Autoregressive Model via Attention Retrospect**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37429-5_9) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2002.pdf) · [Details](../paper-notes.md#arvar)
  - **Accelerates:** HART and Infinity next-scale inference.
  - **Approach:** Uses earlier attention for token selection and removes a late guidance branch.

- [**Autoregression with Self-Token Prediction**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26du.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) · [Details](../paper-notes.md#sar)
  - **Accelerates:** Grouped AR image generation.
  - **Approach:** Self-token prediction generates flexible token groups per step.

- [**Autoregressive Image Generation with Masked Bit Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/yu26z.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) · [Details](../paper-notes.md#barmbm)
  - **Accelerates:** Bitwise AR image generation.
  - **Approach:** Masked bit modeling supports efficient prediction of large-vocabulary image representations.

- [**Autoregressive Image Generation with Randomized Parallel Decoding**](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/267852def1fd0db257622892c7e3be2a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) · [Details](../paper-notes.md#arpg)
  - **Accelerates:** Random-order AR image decoding.
  - **Approach:** Decouples position guidance and content prediction for grouped decoding.

- [**CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration**](https://arxiv.org/pdf/2603.25463v1) (ICLR, 2026). [Paper](https://iclr.cc/virtual/2026/poster/10008851) · [PDF](https://arxiv.org/pdf/2603.25463v1) · [Details](../paper-notes.md#ciar)
  - **Accelerates:** Cloud-device AR image decoding.
  - **Approach:** On-device interval verification reduces cloud verification calls.

- [**Continuous Speculative Decoding for Autoregressive Image Generation**](https://arxiv.org/pdf/2411.11925) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_32) · [PDF](https://arxiv.org/pdf/2411.11925) · [Details](../paper-notes.md#cspd)
  - **Accelerates:** MAR continuous conditional sampling.
  - **Approach:** Uses continuous speculative proposals and approximate trajectory alignment.

- [**CSD: Content-aware Speculative Decoding for Efficient Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/wang26gi.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26gi/wang26gi.pdf) · [Details](../paper-notes.md#csd)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Uses content-dependent acceptance relaxation and resampling.

- [**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**](https://arxiv.org/pdf/2603.28049) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_35) · [PDF](https://arxiv.org/pdf/2603.28049) · [Details](../paper-notes.md#driftar)
  - **Accelerates:** Hybrid AR prediction and iterative visual decoding.
  - **Approach:** Entropy-guided speculation and one-step drifting decoder.

- [**Enabling 8B Bitwise Autoregressive Image Generation on Edge GPUs**](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) (ICPR, 2026). [Paper](https://doi.org/10.1007/978-3-032-31920-3_1) · [PDF](https://iris.unimore.it/bitstream/11380/1400428/4/2026icpr.pdf) · [Details](../paper-notes.md#varcompressor)
  - **Accelerates:** 8B bitwise AR image generation on edge GPUs.
  - **Approach:** Compresses inference memory for deployment.

- [**End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chu26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chu26b/chu26b.pdf) · [Details](../paper-notes.md#ccfsemantic1d)
  - **Accelerates:** AR prior over 1D image tokens.
  - **Approach:** Jointly learns semantic 1D representation and AR generation.

- [**Entropy-Aware Dynamic KV Cache Sparsification for Autoregressive Image Generation and Editing**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/tong26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/tong26k/tong26k.pdf) · [Details](../paper-notes.md#sparsear)
  - **Accelerates:** AR image KV attention.
  - **Approach:** Entropy-aware cache sparsification.

- [**EVAR: Edge Visual Autoregressive Models via Principled Pruning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37086-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) · [Details](../paper-notes.md#evar)
  - **Accelerates:** Next-scale VAR parameter and execution cost.
  - **Approach:** Structured pruning with scale-aware compensation and distillation.

- [**FARMER: Flow AutoRegressive Transformer over Pixels**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#farmer)
  - **Accelerates:** Pixel-level autoregressive normalizing-flow sampling.
  - **Approach:** Self-supervised dimension reduction reduces sequential sampling burden.

- [**FasterVAR: Plug-and-Play Acceleration for Visual Autoregressive Models**](https://arxiv.org/pdf/2512.16483) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26go.html) · [PDF](https://arxiv.org/pdf/2512.16483) · [Details](../paper-notes.md#fastervar)
  - **Accelerates:** Late-scale VAR execution.
  - **Approach:** Adaptive stage selection and reduced computation at costly scales.

- [**FastHybrid: Accelerating Hybrid Autoregressive Image Generation with Lookahead and Guided Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Jiang_FastHybrid_Accelerating_Hybrid_Autoregressive_Image_Generation_with_Lookahead_and_Guided_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#fasthybrid)
  - **Accelerates:** Hybrid AR image generator with diffusion decoder.
  - **Approach:** Lookahead and guided decoding reduce hybrid generation computation.

- [**From Prediction to Perfection: Introducing Refinement to Autoregressive Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0ef6ffcb85a2d238fc4761860c31ded4-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/0ef6ffcb85a2d238fc4761860c31ded4-Paper-Conference.pdf) · [Details](../paper-notes.md#ccfpredictionrefinement)
  - **Accelerates:** Causal AR image prediction unit.
  - **Approach:** Predicts overlapping tensors to refine previous discrete outputs.

- [**Generation then Reconstruction: Accelerating Masked Autoregressive Models via Two-Stage Sampling**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d9251dc20346dffe9b6db86dcc6f8cc9-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d9251dc20346dffe9b6db86dcc6f8cc9-Paper-Conference.pdf) · [Details](../paper-notes.md#gtr)
  - **Accelerates:** MAR stages and inner sampling budget.
  - **Approach:** Separates structure generation and detail reconstruction with frequency-weighted selection.

- [**Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2504.09261) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/39686) · [PDF](https://arxiv.org/pdf/2504.09261) · [Details](../paper-notes.md#hack)
  - **Accelerates:** VAR historical KV storage.
  - **Approach:** Head-dependent cache compression.

- [**Improved and Accelerated Text-to-Image Generation with Collect, Reflect, and Refine**](https://arxiv.org/pdf/2503.09662v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://scholars.hkbu.edu.hk/en/publications/improved-and-accelerated-text-to-image-generation-with-collect-re/) · [PDF](https://arxiv.org/pdf/2503.09662v1) · [Details](../paper-notes.md#core2reviewcandidate)
  - **Accelerates:** LlamaGen guidance computation.
  - **Approach:** Weak-model training supports guidance and later replacement of expensive computation.

- [**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#lactokgen)
  - **Accelerates:** High-resolution AR prior plus image reconstruction.
  - **Approach:** Compact discrete tokens with latent-consistency decoding.

- [**LazyVAR: Accelerating Visual Autoregressive Models via Scale-wise Token Pruning and Parallel Group Decoding**](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Mao_LazyVAR_Accelerating_Visual_Autoregressive_Models_via_Scale-wise_Token_Pruning_and_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#lazyvar)
  - **Accelerates:** VAR token processing and scale schedule.
  - **Approach:** Scale-dependent token pruning plus grouped scale decoding.

- [**Learning to Expand Images for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.15499v1) (ACM MM, 2026). [Paper](https://2026.acmmm.org/site/technical-programme.html) · [PDF](https://arxiv.org/pdf/2511.15499v1) · [Details](../paper-notes.md#ear)
  - **Accelerates:** AR image generation order and parallel groups.
  - **Approach:** Spiral expansion with length-adaptive parallel decoding.
  - Accepted

- [**LineAR: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens**](https://arxiv.org/pdf/2512.04857v1) (ECCV, 2026). [Paper](https://doi.org/10.1007/978-3-032-37035-8_33) · [PDF](https://arxiv.org/pdf/2512.04857v1) · [Details](../paper-notes.md#linear)
  - **Accelerates:** Causal visual AR KV storage.
  - **Approach:** Progressively evicts historical lines outside retained dependency regions.

- [**LISA: Locality-Informed Speculative Decoding for Accelerating Autoregressive Image Generation**](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37255-0_20) · [PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1222.pdf) · [Details](../paper-notes.md#lisa)
  - **Accelerates:** Visual AR speculative verification.
  - **Approach:** Locality-informed verifier modifies acceptance behavior.

- [**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**](https://arxiv.org/pdf/2507.01957v2) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/02687e7b22abc64e651be8da74ec610e-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2507.01957v2) · [Details](../paper-notes.md#lpd)
  - **Accelerates:** AR position grouping and inference schedule.
  - **Approach:** Position query tokens and locality-aware parallel generation order.

- [**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/7cdf000d22c6cda21f3cbd7467aaf26f-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) · [Details](../paper-notes.md#madformer)
  - **Accelerates:** AR/diffusion hybrid block computation.
  - **Approach:** Allocates AR conditioning layers and iterative diffusion layers.

- [**MARché: Fast Masked Autoregressive Image Generation with Cache-Aware Attention**](https://arxiv.org/pdf/2506.12035) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_34) · [PDF](https://arxiv.org/pdf/2506.12035) · [Details](../paper-notes.md#marche)
  - **Accelerates:** MAR attention and feed-forward recomputation.
  - **Approach:** Cache-aware attention and selective KV refresh.

- [**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#markovvar)
  - **Accelerates:** VAR historical context and memory.
  - **Approach:** Compressed history state and limited scale context.

- [**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#marval)
  - **Accelerates:** MAR iterative conditional sampling.
  - **Approach:** Distills a faster sampler while retaining a masked AR generation organization.

- [**MoSs: Mixture of Scales for Efficient High-Resolution Autoregressive Image Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37611) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37611/41573) · [Details](../paper-notes.md#moss)
  - **Accelerates:** High-resolution next-scale transformer execution.
  - **Approach:** Mixes scale work and dispatches late refinement selectively.

- [**Multi-Scale Local Speculative Decoding for Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#mulosd)
  - **Accelerates:** High-resolution AR image speculative generation.
  - **Approach:** Low-resolution proposals with upsampling and spatially local verification.

- [**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/37c6d0bc4d2917dcbea693b18504bd87-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) · [Details](../paper-notes.md#mvar)
  - **Accelerates:** VAR spatial and scale context.
  - **Approach:** Restricts conditioning to adjacent scales and local neighborhoods.

- [**OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_6) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) · [Details](../paper-notes.md#omnimamba)
  - **Accelerates:** Autoregressive image-token prediction with a Mamba-2 state-space backbone.
  - **Approach:** Train a unified next-token image/text generator with Mamba-2 and modality-specific vocabularies and adapters.

- [**Parallel Jacobi Decoding for Fast Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liao_Parallel_Jacobi_Decoding_for_Fast_Autoregressive_Image_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#pjd)
  - **Accelerates:** AR image Jacobi candidate refinement.
  - **Approach:** Spatial parallel drafts with adaptive attention masks.

- [**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26gy.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) · [Details](../paper-notes.md#prismmoe)
  - **Accelerates:** Dense visual AR predictor computation.
  - **Approach:** Dense-to-MoE conversion with sparse expert activation.

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkCTCXo1a9) · [PDF](https://arxiv.org/pdf/2602.03811) · [Details](../paper-notes.md#tmlrwkctcxo1a9)
  - **Accelerates:** Multiscale AR serial sampling schedule.
  - **Approach:** Progressive checkerboards permit parallel positions within scales.

- [**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.16546) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Progressive_Supernet_Training_for_Efficient_Visual_Autoregressive_Modeling_CVPR_2026_paper.html) · [PDF](https://arxiv.org/pdf/2511.16546) · [Details](../paper-notes.md#variant)
  - **Accelerates:** VAR inference depth and memory.
  - **Approach:** Progressive supernet training permits scale-dependent subnet execution.

- [**PTQ4ARVG: Post-Training Quantization for AutoRegressive Visual Generation Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/81a28be483155f802ddef448d6fc4b57-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/81a28be483155f802ddef448d6fc4b57-Paper-Conference.pdf) · [Details](../paper-notes.md#ptq4arvg)
  - **Accelerates:** AR visual predictor arithmetic.
  - **Approach:** Post-training weight/activation quantization and calibration.

- [**RADAR: VQ-VAE Decoder of VAR is a Good Student for Restoring Against Degradation by Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_RADAR_VQ-VAE_Decoder_of_VAR_is_a_Good_Student_for_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#radar)
  - **Accelerates:** VAR sparse attention plus decoded images.
  - **Approach:** Cost-constrained sparse prediction and decoder adaptation.

- [**SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) (AAAI, 2026). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/37400) · [PDF](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) · [Details](../paper-notes.md#scan)
  - **Accelerates:** AR coarse image prediction and selected refinement.
  - **Approach:** Coarse generation followed by calibrated local refinement.

- [**Shift-and-Sum Quantization for Visual Autoregressive Models**](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/89379d5fc6eb34ff98488202fb52b9d0-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/89379d5fc6eb34ff98488202fb52b9d0-Paper-Conference.pdf) · [Details](../paper-notes.md#shiftsum)
  - **Accelerates:** VAR quantized matrix computation.
  - **Approach:** Shift-and-sum value quantization with calibration resampling.

- [**SJD++: Improved Speculative Jacobi Decoding for Training-free Acceleration of Discrete Auto-regressive Text-to-Image Generation**](https://arxiv.org/pdf/2512.07503v1) (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2026). [Paper](https://doi.org/10.1109/TPAMI.2026.3700227) · [PDF](https://arxiv.org/pdf/2512.07503v1) · [Details](../paper-notes.md#sjdplus)
  - **Accelerates:** AR text-to-image Jacobi candidate reuse.
  - **Approach:** Retains high-confidence unaccepted draft states.

- [**SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Kang_SJD-PAC_Accelerating_Speculative_Jacobi_Decoding_via_Proactive_Drafting_and_Adaptive_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#sjdpac)
  - **Accelerates:** AR image Jacobi candidate generation.
  - **Approach:** Proactive drafting and adaptive continuation.

- [**SJD-SV: Speculative Jacobi Decoding with Semantics Verification for Autoregressive Image Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhang26fd.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhang26fd/zhang26fd.pdf) · [Details](../paper-notes.md#sjdsv)
  - **Accelerates:** AR image speculative verification.
  - **Approach:** Semantic subsequence verification changes the tested/committed positions.

- [**SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_SparVAR_Exploring_Sparsity_in_Visual_AutoRegressive_Modeling_for_Training-Free_Acceleration_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#sparvar)
  - **Accelerates:** Next-scale VAR attention.
  - **Approach:** Predicts sparse attention patterns from earlier scales.

- [**StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models**](https://arxiv.org/pdf/2603.01757) (ACM ICMR, 2026). [Paper](https://doi.org/10.1145/3805622.3810814) · [PDF](https://arxiv.org/pdf/2603.01757) · [Details](../paper-notes.md#stepvar)
  - **Accelerates:** High-resolution VAR token evaluation.
  - **Approach:** Structural and texture criteria select retained tokens.

- [**ToProVAR: Efficient Visual Autoregressive Modeling via Tri-Dimensional Entropy-Aware Semantic Analysis and Sparsity Optimization**](https://arxiv.org/pdf/2602.22948) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8edb116d5b288b6a9bba4c16ab647702-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2602.22948) · [Details](../paper-notes.md#toprovar)
  - **Accelerates:** VAR tokens, layers and scale computation.
  - **Approach:** Entropy-guided sparse execution.

- [**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d649dd586dba64672a96beff24178125-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) · [Details](../paper-notes.md#proceedings215)
  - **Accelerates:** AR generation with aligned compact visual tokens.
  - **Approach:** Causal decoder constrains tokenizer dependencies.

- [**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#ccfunicompress)
  - **Accelerates:** Unified-model AR image output sequences.
  - **Approach:** Token compression/decompression shortens visual generation.

- [**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/peng26k.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) · [Details](../paper-notes.md#uniar)
  - **Accelerates:** Unified AR image-generation token decoding.
  - **Approach:** Channel-bitwise prediction reduces serial autoregressive steps.

- [**VAR-Turbo: Unlocking the Potential of Visual Autoregressive Models Through Dual Redundancy**](https://doi.org/10.1109/hpca68181.2026.11408607) (HPCA, 2026). [Paper](https://doi.org/10.1109/hpca68181.2026.11408607) · [Details](../paper-notes.md#varturbo)
  - **Accelerates:** VAR execution and dedicated accelerator.
  - **Approach:** Parallel decoding, token aggregation and bypass with hardware support.

- [**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#ccfvibetoken)
  - **Accelerates:** Resolution-flexible AR image prior.
  - **Approach:** Resolution-agnostic 1D tokenization bounds AR sequence burden.

- [**Visual Implicit Autoregressive Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/jiang26ah.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) · [Details](../paper-notes.md#viar)
  - **Accelerates:** Next-scale visual AR stack.
  - **Approach:** Implicit equilibrium layer with variable inference iterations.

- [**VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping**](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Dong_VVS_Accelerating_Speculative_Decoding_for_Visual_Autoregressive_Generation_via_Partial_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#vvs)
  - **Accelerates:** AR visual speculative verification.
  - **Approach:** Skips verification for selected provisional positions.

- [**XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/liu26ck.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) · [Details](../paper-notes.md#xyzflow)
  - **Accelerates:** MAR conditional-head sampling and AR teachers.
  - **Approach:** Shortcut flow modeling with multidimensional prediction.

- [**Accelerating Auto-regressive Text-to-Image Generation with Training-free Speculative Jacobi Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e45c8d054739d31676619e7e11327f68-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/e45c8d054739d31676619e7e11327f68-Paper-Conference.pdf) · [Code](https://github.com/tyshiwo1/Accelerating-T2I-AR-with-SJD) · [Details](../paper-notes.md#sjd)
  - **Accelerates:** AR text-to-image next-token execution.
  - **Approach:** Jacobi candidate reuse with stochastic verification.

- [**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#xar)
  - **Accelerates:** AR image prediction units and conditional sampling.
  - **Approach:** Next-X prediction over flexible entities.

- [**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**](https://arxiv.org/pdf/2411.17787) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2411.17787) · [Details](../paper-notes.md#code)
  - **Accelerates:** Next-scale VAR computation and memory.
  - **Approach:** Large model predicts coarse scales and a smaller model refines later scales.

- [**Continuous Visual Autoregressive Generation via Score Maximization**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/shao25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) · [Details](../paper-notes.md#energyar)
  - **Accelerates:** Continuous AR per-position conditional sampling.
  - **Approach:** Models continuous conditionals with score maximization instead of iterative diffusion.

- [**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#dcar)
  - **Accelerates:** Hybrid masked AR text-to-image generator.
  - **Approach:** Deep-compression hybrid tokenizer reduces spatial sequence burden.

- [**Denoising Token Prediction in Masked Autoregressive Models**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#ccfdtp)
  - **Accelerates:** Continuous MAR token prediction.
  - **Approach:** Adds denoising refinement of unmasked predictions.

- [**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**](https://arxiv.org/pdf/2412.17153v3) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67d3805a7b01672c1c2dcb30f6d5290f-Abstract-Conference.html) · [PDF](https://arxiv.org/pdf/2412.17153v3) · [Details](../paper-notes.md#dd1)
  - **Accelerates:** Complete VAR and LlamaGen latent generation.
  - **Approach:** Distills AR sampling into a few-step flow generator.

- [**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/085f2a21d3f0cef1585fceaa6dacdc15-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) · [Details](../paper-notes.md#dd2)
  - **Accelerates:** Complete VAR and LlamaGen latent generation.
  - **Approach:** Conditional score distillation trains a one-step replacement.

- [**Effective and Efficient Masked Image Generation Models**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/you25d.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/you25d/you25d.pdf) · [Details](../paper-notes.md#emigm)
  - **Accelerates:** Continuous masked image generation including MAR.
  - **Approach:** Revises masking, sampling schedule and conditional token modeling.

- [**FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning**](https://arxiv.org/pdf/2503.23367) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_FastVAR_Linear_Visual_Autoregressive_Modeling_via_Cached_Token_Pruning_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.23367) · [Details](../paper-notes.md#fastvar)
  - **Accelerates:** High-resolution next-scale token processing.
  - **Approach:** Cached token pruning forwards selected tokens and recovers omitted states.

- [**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d0d75da30e2d81b928d793afe389ad4-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) · [Details](../paper-notes.md#flexvar)
  - **Accelerates:** Next-scale generator schedule.
  - **Approach:** Ground-truth scale prediction supports variable inference-stage budgets.

- [**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/95cb60b65d9f2c0cd78b567ffebde9e6-Abstract-Conference.html) · [PDF](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) · [Details](../paper-notes.md#freqexit)
  - **Accelerates:** VAR transformer depth at inference.
  - **Approach:** Trains frequency-aware early-exit behavior.

- [**Frequency-Aware Autoregressive Modeling for Efficient High-Resolution Image Synthesis**](https://arxiv.org/pdf/2507.20454) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Frequency-Aware_Autoregressive_Modeling_for_Efficient_High-Resolution_Image_Synthesis_ICCV_2025_paper.html) · [PDF](https://arxiv.org/pdf/2507.20454) · [Details](../paper-notes.md#sparsevar)
  - **Accelerates:** Late-scale VAR spatial computation.
  - **Approach:** Frequency-guided token omission and recovery.

- [**Grouped Speculative Decoding for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/So_Grouped_Speculative_Decoding_for_Autoregressive_Image_Generation_ICCV_2025_paper.pdf) · [Details](../paper-notes.md#gsd)
  - **Accelerates:** AR image speculative decoding.
  - **Approach:** Groups spatially related token candidates for verification.

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ab4e1e704c68b0f476c265996f08d283-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) · [Details](../paper-notes.md#hart)
  - **Accelerates:** High-resolution AR image generator.
  - **Approach:** Discrete AR structure with a small residual diffusion module.

- [**Hawk: Leveraging Spatial Context for Faster Autoregressive Text-to-Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.nips.cc/paper_files/paper/2025/hash/cba5f2c37ed6599fb9338e470a05e05a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/cba5f2c37ed6599fb9338e470a05e05a-Paper-Conference.pdf) · [Details](../paper-notes.md#hawk)
  - **Accelerates:** AR text-to-image speculative proposals.
  - **Approach:** Spatial-context drafting improves candidate prediction.

- [**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**](https://arxiv.org/pdf/2505.20288v1) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/zheng25i.html) · [PDF](https://arxiv.org/pdf/2505.20288v1) · [Details](../paper-notes.md#himar)
  - **Accelerates:** Hierarchical continuous masked AR image generation.
  - **Approach:** Low-resolution pivots condition later high-resolution groups.

- [**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**](https://arxiv.org/pdf/2506.04421v1) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.html) · [PDF](https://arxiv.org/pdf/2506.04421v1) · [Details](../paper-notes.md#hmar)
  - **Accelerates:** Hierarchical next-scale masked AR execution.
  - **Approach:** Hierarchical ordering and IO-aware block-sparse attention kernels.

- [**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) · [Code](https://github.com/FoundationVision/Infinity) · [Details](../paper-notes.md#infinity)
  - **Accelerates:** High-resolution next-scale AR generation.
  - **Approach:** Bitwise prediction avoids a very large categorical classifier.

- [**LANTERN: Accelerating Visual Autoregressive Models with Relaxed Speculative Decoding**](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5e1c255653eb98cef13f45b2d337c882-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e1c255653eb98cef13f45b2d337c882-Paper-Conference.pdf) · [Details](../paper-notes.md#lantern)
  - **Accelerates:** Visual AR speculative acceptance.
  - **Approach:** Latent-neighborhood relaxed acceptance.

- [**LazyMAR: Accelerating Masked Autoregressive Models via Feature Caching**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yan_LazyMAR_Accelerating_Masked_Autoregressive_Models_via_Feature_Caching_ICCV_2025_paper.pdf) · [Code](https://github.com/feihongyan1/LazyMAR) · [Details](../paper-notes.md#lazymar)
  - **Accelerates:** MAR repeated feature computation and guidance.
  - **Approach:** Caches stable token features and branch differences.

- [**Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression**](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/14550b451b65682b09f9080026d00a7e-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/14550b451b65682b09f9080026d00a7e-Paper-Conference.pdf) · [Details](../paper-notes.md#scalekv)
  - **Accelerates:** Next-scale VAR KV cache.
  - **Approach:** Layer-dependent retention of scales and cache entries.

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24aa1508f9bdb2c2894c00963ce39f18-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) · [Details](../paper-notes.md#nfig)
  - **Accelerates:** Next-scale AR frequency stages.
  - **Approach:** Generates low-frequency structure before higher-frequency detail.

- [**Numerical Pruning for Efficient Autoregressive Models**](https://arxiv.org/pdf/2412.12441) (AAAI, 2025). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/34249) · [PDF](https://arxiv.org/pdf/2412.12441) · [Details](../paper-notes.md#numericalpruning)
  - **Accelerates:** Decoder-only AR transformer parameters.
  - **Approach:** Numerical-score structured pruning.

- [**Plug-and-Play Context Feature Reuse for Efficient Masked Generation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e628a90ac4accdbcc67e8c960c1817f-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2e628a90ac4accdbcc67e8c960c1817f-Paper-Conference.pdf) · [Details](../paper-notes.md#recap)
  - **Accelerates:** MAR context-feature recomputation.
  - **Approach:** Alternates full evaluations with low-cost cached-context steps.

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

- [**Towards Better & Faster Autoregressive Image Generation: From the Perspective of Entropy**](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2d1c26fa38f31aca8712055758194bac-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/2d1c26fa38f31aca8712055758194bac-Paper-Conference.pdf) · [Details](../paper-notes.md#entropydecoding)
  - **Accelerates:** Visual AR sampling and speculation.
  - **Approach:** Entropy controls temperature and relaxed acceptance.

- [**ZipAR: Parallel Autoregressive Image Generation through Spatial Locality**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/he25b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/he25b/he25b.pdf) · [Details](../paper-notes.md#zipar)
  - **Accelerates:** Causal visual AR decoding.
  - **Approach:** Spatially parallel decoding with local context windows.

- [**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (NeurIPS, 2024). [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) · [Code](https://github.com/FoundationVision/VAR) · [Details](../paper-notes.md#var)
  - **Accelerates:** AR image generation sequence organization.
  - **Approach:** Next-scale prediction replaces raster next-token progression.

- [**Efficient-VQGAN: Towards High-Resolution Image Generation with Efficient Vision Transformers**](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) (ICCV, 2023). [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Efficient-VQGAN_Towards_High-Resolution_Image_Generation_with_Efficient_Vision_Transformers_ICCV_2023_paper.pdf) · [Details](../paper-notes.md#efficientvqgan)
  - **Accelerates:** High-resolution AR image attention and local code generation.
  - **Approach:** Local tokenization with blockwise parallel generation.

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) · [Details](../paper-notes.md#mqvae)
  - **Accelerates:** AR image sequence redundancy.
  - **Approach:** Masks less-important regions and predicts selected/content positions with Stackformer.

- [**Reject Decoding via Language-Vision Models for Text-to-Image Synthesis**](https://ojs.aaai.org/index.php/AAAI/article/view/25379) (AAAI, 2023). [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/25379) · [Details](../paper-notes.md#rejectdecoding)
  - **Accelerates:** Multi-path AR text-to-image search.
  - **Approach:** Tiny visual-language scorer terminates poor partial paths early.

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023). [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) · [Details](../paper-notes.md#dqvae)
  - **Accelerates:** AR image code length and decoding.
  - **Approach:** Dynamic quantization plus coarse-to-fine position/content prediction.

- [**Autoregressive Diffusion Models**](https://arxiv.org/pdf/2110.02037) (ICLR, 2022). [Paper](https://iclr.cc/virtual/2022/poster/6228) · [PDF](https://arxiv.org/pdf/2110.02037) · [Details](../paper-notes.md#ardm2022)
  - **Accelerates:** Order-agnostic AR image model evaluations.
  - **Approach:** Parallel generation under a selected network-evaluation budget.

- [**Autoregressive Image Generation Using Residual Quantization**](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) (CVPR, 2022). [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) · [Details](../paper-notes.md#rqtransformer)
  - **Accelerates:** AR image spatial sequence and depth code prediction.
  - **Approach:** Residual quantization compresses spatial maps and predicts code stacks.

- [**Accelerating Feedforward Computation via Parallel Nonlinear Equation Solving**](https://proceedings.mlr.press/v139/song21a/song21a.pdf) (ICML, 2021). [Paper](https://proceedings.mlr.press/v139/song21a.html) · [PDF](https://proceedings.mlr.press/v139/song21a/song21a.pdf) · [Details](../paper-notes.md#songjacobi)
  - **Accelerates:** Deep AR image-model feedforward sampling.
  - **Approach:** Parallel nonlinear fixed-point solving.

## image super-resolution

- [**Blockwise Parallel Decoding for Deep Autoregressive Models**](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) (NeurIPS, 2018). [Paper](https://papers.nips.cc/paper_files/paper/2018/hash/c4127b9194fe8562c64dc0f5bf2c93bc-Abstract.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) · [Details](../paper-notes.md#blockwise)
  - **Accelerates:** AR image super-resolution decoding.
  - **Approach:** Predicts blocks provisionally and commits the prefix validated by a scoring model.

## image; video

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026). [Paper](https://openreview.net/forum?id=OuFNXESoCO) · [PDF](https://arxiv.org/pdf/2412.07720) · [Details](../paper-notes.md#tmlroufnxesoco)
  - **Accelerates:** Image and video block-AR conditional diffusion.
  - **Approach:** Block-causal denoising with reusable past context.

- [**Speculative Coupled Decoding for Training-Free Lossless Acceleration of Autoregressive Visual Generation**](https://arxiv.org/pdf/2510.24211v2) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/so26a.html) · [PDF](https://arxiv.org/pdf/2510.24211v2) · [Details](../paper-notes.md#scd)
  - **Accelerates:** AR image stochastic speculative execution.
  - **Approach:** Couples proposal/verification randomness.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://arxiv.org/pdf/2503.10696) (ICCV, 2025). [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) · [PDF](https://arxiv.org/pdf/2503.10696) · [Details](../paper-notes.md#nar)
  - **Accelerates:** Image and video AR position decoding.
  - **Approach:** Neighbor expansion with dimension-oriented parallel prediction heads.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) · [Details](../paper-notes.md#par)
  - **Accelerates:** Image and video AR sequential decoding.
  - **Approach:** Generates spatially distant groups concurrently.

- [**Parallel Multiscale Autoregressive Density Estimation**](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) (ICML, 2017). [Paper](https://proceedings.mlr.press/v70/reed17a.html) · [PDF](https://proceedings.mlr.press/v70/reed17a/reed17a.pdf) · [Details](../paper-notes.md#parallelmultiscale2017)
  - **Accelerates:** Pixel AR sampling dependency depth.
  - **Approach:** Parallel multiscale density factorization.

## video

- [**AAD-1: Asymmetric Adversarial Distillation for One-Step Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/li26iw.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26iw/li26iw.pdf) · [Details](../paper-notes.md#aad1video)
  - **Accelerates:** AR video denoising evaluation budget.
  - **Approach:** Asymmetric adversarial distillation trains a one-NFE causal student.

- [**Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Nan_Accelerating_Autoregressive_Video_Diffusion_via_History-Guided_Cache_and_Residual_Correction_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#arcachevideo)
  - **Accelerates:** AR video diffusion recomputation.
  - **Approach:** History-guided cache timing with enhanced residual correction.

- [**Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/zhu26bf.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhu26bf/zhu26bf.pdf) · [Details](../paper-notes.md#causalforcingvideo)
  - **Accelerates:** Few-step causal video diffusion generator.
  - **Approach:** AR-teacher ODE initialization followed by distribution-matching distillation.

- [**Context Forcing: Consistent Autoregressive Video Generation with Long Context**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26eu.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26eu/chen26eu.pdf) · [Details](../paper-notes.md#contextforcingvideo)
  - **Accelerates:** AR video context-memory growth.
  - **Approach:** Bounded slow/fast memory retains selected historical frames.

- [**Deep Forcing: Training-Free Long Video Generation with Deep Sink and Participative Compression**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/yi26c.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yi26c/yi26c.pdf) · [Details](../paper-notes.md#deepforcingvideo)
  - **Accelerates:** AR video historical KV storage.
  - **Approach:** Persistent sink context with importance-aware KV pruning.

- [**FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/samuel26a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/samuel26a/samuel26a.pdf) · [Details](../paper-notes.md#fastarvideo)
  - **Accelerates:** AR video self/cross-attention and KV cache.
  - **Approach:** Temporal cache compression and approximate-neighbor sparse attention.

- [**Fastcar: Cache Attentive Replay for Fast Auto-Regressive Video Generation on the Edge**](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8488454077cb0fd9d31772274c78115d-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/8488454077cb0fd9d31772274c78115d-Paper-Conference.pdf) · [Details](../paper-notes.md#fastcarvideo)
  - **Accelerates:** AR video decoder MLP computation.
  - **Approach:** Replays cached MLP outputs with temporal attention-based selection and FPGA scheduling.

- [**FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis**](https://arxiv.org/pdf/2603.07192) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37098-3_12) · [PDF](https://arxiv.org/pdf/2603.07192) · [Details](../paper-notes.md#faststarvideo)
  - **Accelerates:** InfinityStar spatiotemporal token refinement.
  - **Approach:** Prunes converged spatial/temporal tokens with partial residual updates.

- [**Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/ma26b.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/ma26b/ma26b.pdf) · [Details](../paper-notes.md#flexforcingvideo)
  - **Accelerates:** AR video generation execution schedule.
  - **Approach:** Flexible chunks with bidirectional planning and autoregressive within-chunk inference.

- [**Flow Caching for Autoregressive Video Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/85dc8f85ff978b9c606d3b2f5b0da69a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/85dc8f85ff978b9c606d3b2f5b0da69a-Paper-Conference.pdf) · [Details](../paper-notes.md#flowcachevideo)
  - **Accelerates:** AR video denoising and KV storage.
  - **Approach:** Independent chunk cache policies with bounded KV compression.

- [**HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_13) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_13.pdf) · [Details](../paper-notes.md#hiarvideo)
  - **Accelerates:** Hierarchical denoising and pipelined execution of AR video blocks.
  - **Approach:** Generate each block using context at the same noise level, enabling pipelined parallel inference across denoising levels.

- [**InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars**](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37032-7_37) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37032-7_37.pdf) · [Details](../paper-notes.md#interactiveavatarvideo)
  - **Accelerates:** Sampling steps in a causal Wan2.2-5B talking-avatar generator.
  - **Approach:** Apply causal ODE initialization and Self-Forcing DMD to form a few-step AR generator. Use KV caching and separate DiT/VAE devices for streaming execution.

- [**Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/lv26i.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/lv26i/lv26i.pdf) · [Details](../paper-notes.md#lightforcingvideo)
  - **Accelerates:** AR video attention.
  - **Approach:** Chunk-aware sparsity allocation with hierarchical sparse attention.

- [**Live Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite Length**](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37135-5_5) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37135-5_5.pdf) · [Details](../paper-notes.md#liveavatarvideo)
  - **Accelerates:** Denoising updates and multi-GPU streaming execution in an AR talking-avatar generator.
  - **Approach:** Distill WanS2V into a causal few-step generator and pipeline denoising timesteps, with VAE parallelization and kernel optimizations.

- [**Lumos-1: On Autoregressive Video Generation with Discrete Diffusion from a Unified Model Perspective**](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/59ad89d72559dd4ce557d56f36313724-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/59ad89d72559dd4ce557d56f36313724-Paper-Conference.pdf) · [Details](../paper-notes.md#lumos1video)
  - **Accelerates:** LLM-based AR video generation.
  - **Approach:** Frame-causal masked parallel decoding with KV cache.

- [**Motion-Aware Caching for Efficient Autoregressive Video Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/xu26an.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xu26an/xu26an.pdf) · [Details](../paper-notes.md#motioncachevideo)
  - **Accelerates:** AR video diffusion denoising computation.
  - **Approach:** Motion-weighted token updates after a full-computation warmup.

- [**OmniForcing: Unleashing Real-Time Joint Audio-Visual Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37271-0_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37271-0_31.pdf) · [Details](../paper-notes.md#omniforcingvideo)
  - **Accelerates:** Causal audio-video block generation and conditional denoising updates.
  - **Approach:** Distill a bidirectional LTX-2 teacher into a streaming AR student with block-causal modality alignment and rolling KV caches.

- [**PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference**](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37464-6_31) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37464-6_31.pdf) · [Details](../paper-notes.md#packforcingvideo)
  - **Accelerates:** Stored historical KV entries and historical attention in a Wan2.1-based AR video generator.
  - **Approach:** Separate sink, compressed middle and recent history. Compress middle blocks and route selected historical blocks into attention, with incremental temporal RoPE adjustment.

- [**Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/xi26f.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/xi26f/xi26f.pdf) · [Details](../paper-notes.md#quantvideogen)
  - **Accelerates:** AR video KV storage.
  - **Approach:** Semantic smoothing and progressive residual cache quantization.

- [**Real-Time Motion-Controllable Autoregressive Video Diffusion**](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/71c1d6ec1f0003d8ea10bbea4291002d-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/71c1d6ec1f0003d8ea10bbea4291002d-Paper-Conference.pdf) · [Details](../paper-notes.md#ardragvideo)
  - **Accelerates:** Motion-controlled AR video diffusion.
  - **Approach:** Few-step causal distillation with motion conditioning.

- [**Reward Forcing: Efficient Streaming Video Generation with Rewarded Distribution Matching Distillation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lu_Reward_Forcing_Efficient_Streaming_Video_Generation_with_Rewarded_Distribution_Matching_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#rewardforcing)
  - **Accelerates:** Streaming AR video attention and conditional denoising.
  - **Approach:** Few-step causal distillation with a smaller attention window and fixed-size EMA sink state.

- [**Rolling Forcing: Autoregressive Long Video Diffusion in Real Time**](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/935151cc6cb5d8b6816133b75233775a-Paper-Conference.pdf) · [Details](../paper-notes.md#rollingforcingvideo)
  - **Accelerates:** Streaming AR video denoising.
  - **Approach:** Rolling-frame generation and few-step distillation with extended windows.

- [**SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer**](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/41b93c59da0d0f835907fd661d419db2-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/41b93c59da0d0f835907fd661d419db2-Paper-Conference.pdf) · [Details](../paper-notes.md#sanavideo)
  - **Accelerates:** Long-video AR attention and cache growth.
  - **Approach:** Linear attention with constant-memory block-causal state.

- [**Streaming Autoregressive Video Generation via Diagonal Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d899eabc6c8fefd0d4064762aba407e2-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d899eabc6c8fefd0d4064762aba407e2-Paper-Conference.pdf) · [Details](../paper-notes.md#diagonaldistillvideo)
  - **Accelerates:** Streaming AR video diffusion.
  - **Approach:** Diagonal distillation restructures few-step frame synthesis.

- [**Surprise Forcing: What to Remember, When to Skip in Long Video Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37419-6_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_16.pdf) · [Details](../paper-notes.md#surpriseforcingvideo)
  - **Accelerates:** Conditional denoising updates per AR video chunk and retained historical frames.
  - **Approach:** Adapt the denoising budget to chunk difficulty and retain selected evicted frames in a bounded memory bank.

- [**Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific Parametric Absorption**](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37026-6_25) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37026-6_25.pdf) · [Details](../paper-notes.md#ispavideo)
  - **Accelerates:** KV-cache storage and attention computation in streaming AR video generators.
  - **Approach:** Replace selected full-attention layers with local attention after instance-specific closed-form weight modulation absorbs historical context.

- [**Towards One-step Causal Video Generation via Adversarial Self-Distillation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) (ICLR, 2026). [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3ae86071c169649bff21188c536163dc-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/3ae86071c169649bff21188c536163dc-Paper-Conference.pdf) · [Details](../paper-notes.md#asdcausalvideo)
  - **Accelerates:** AR video conditional denoising evaluations.
  - **Approach:** Adversarial self-distillation with extra first-frame updates.

- [**Autoregressive Video Generation without Vector Quantization**](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6e5112eaa45f8c30b242c5f576213a92-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e5112eaa45f8c30b242c5f576213a92-Paper-Conference.pdf) · [Details](../paper-notes.md#novavideo)
  - **Accelerates:** Temporal/spatial AR video generation.
  - **Approach:** Frame-wise temporal causality and set-wise spatial generation with continuous tokens.

- [**Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/gao25m.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25m/gao25m.pdf) · [Details](../paper-notes.md#ca2vdmvideo)
  - **Accelerates:** AR video conditional-frame recomputation.
  - **Approach:** Causal feature computation and cache sharing across denoising steps.

- [**From Slow Bidirectional to Fast Autoregressive Video Diffusion Models**](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Yin_From_Slow_Bidirectional_to_Fast_Autoregressive_Video_Diffusion_Models_CVPR_2025_paper.pdf) · [Details](../paper-notes.md#causvidvideo)
  - **Accelerates:** Causal video diffusion inference.
  - **Approach:** Distills a bidirectional many-step teacher into a KV-cached causal few-step generator.

- [**MarDini: Masked Auto-regressive Diffusion for Video Generation at Scale**](https://arxiv.org/pdf/2410.20280) (TMLR, 2025). [Paper](https://openreview.net/forum?id=fuOHI59rUW) · [PDF](https://arxiv.org/pdf/2410.20280) · [Details](../paper-notes.md#mardinivideo)
  - **Accelerates:** Masked-AR video planning and spatial diffusion.
  - **Approach:** Low-resolution planning with a lightweight high-resolution diffusion model.

- [**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) (NeurIPS, 2025). [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f4823f831af67a3ef15e41a85434422a-Abstract-Conference.html) · [PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/f4823f831af67a3ef15e41a85434422a-Paper-Conference.pdf) · [Details](../paper-notes.md#selfforcingvideo)
  - **Accelerates:** Few-step streaming AR video generator.
  - **Approach:** Self-generated training rollouts with rolling KV-cache inference.

- [**Efficiency-optimized Video Diffusion Models**](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) (ACM MM, 2023). [Paper](https://dl.acm.org/doi/10.1145/3581783.3612406) · [PDF](https://hexiangteng.github.io/papers/ACM%20MM%202023%20EVDM.pdf) · [Details](../paper-notes.md#evdmacmmm2023)
  - **Accelerates:** Convolution and attention cost of the MCVD conditional video denoiser used for block-autoregressive generation.
  - **Approach:** Train smaller denoisers with bottleneck residual paths, channel splitting and a mixed attention algorithm.

## video / scene forecasts

- [**Doe-2: 3D Representation World Model for Unified Driving Scene Forecasting**](https://link.springer.com/content/pdf/10.1007/978-3-032-37235-2_29.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37235-2_29) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37235-2_29.pdf) · [Details](../paper-notes.md#doe2world)
  - **Accelerates:** Compact 3D latent prediction with an AR predictor and conditional DiT head.
  - **Approach:** Section 3.4 conditions next-scene prediction on historical latents Z_{<=t} and ego-actions a_{<=t}; Eqs. (7)–(8) specify historical cross-attention and coarse future-latent prediction. A three-layer conditional DiT head uses Rectified Flow, Eq. (11), to sample the next-scene latent; the temporal AR predictor supplies its conditioning features.

- [**GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors**](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_22.pdf) · [Details](../paper-notes.md#geoflowdriving)
  - **Accelerates:** Geometry-aligned initialization and fewer denoising steps for autoregressive driving-video chunks.
  - **Approach:** Section 3.5 explicitly specifies short-horizon frame autoregression: each six-frame chunk contains one reference frame and five newly generated frames. Conditional latent Flow Matching inside each video chunk; geometry-warped historical content initializes its source distribution.

- [**ShotStream: Streaming Multi-shot Video Generation for Interactive Storytelling**](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_12.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37261-1_12) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_12.pdf) · [Details](../paper-notes.md#shotstreamvideo)
  - **Accelerates:** Four-step causal multi-shot video generation replacing a multi-step bidirectional teacher.
  - **Approach:** Section 4.2 and Figure 4 generate shots from previous shots and each shot chunk-by-chunk. Global and local caches store historical context and recently generated frames. A few-step conditional video denoiser operates within the causal chunk-generation procedure; distribution matching distillation replaces the slow teacher.

## video avatar

- [**Avatar Forcing: Real-Time Interactive Head Avatar Generation for Natural Conversation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ki_Avatar_Forcing_Real-Time_Interactive_Head_Avatar_Generation_for_Natural_Conversation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#avatarforcing)
  - **Accelerates:** Causal avatar-motion generation latency.
  - **Approach:** Blockwise causal diffusion forcing with KV reuse replaces a bidirectional motion generator.

## video view expansion

- [**CubeComposer: Spatio-Temporal Autoregressive 4K 360deg Video Generation from Perspective Video**](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CubeComposer_Spatio-Temporal_Autoregressive_4K_360deg_Video_Generation_from_Perspective_Video_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#cubecomposervideo)
  - **Accelerates:** Autoregressive cubemap video synthesis.
  - **Approach:** Sparse context across cube faces and temporal windows.

## volumetric medical image synthesis

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) · [Details](../paper-notes.md#mpadmri)
  - **Accelerates:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Approach:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.
