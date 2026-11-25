# Designing Efficient Autoregressive Generators

[Home](../../README.md) · [Categories](../README.md)

Generator design changes inference computation and its distribution across generation stages.

**56 papers.**

## 5.1 Efficient Conditional Predictors

- [**DynamicVAR: Multimodal-Routing-Based Adaptive Visual Autoregressive Image Generation**](https://link.springer.com/content/pdf/10.1007/978-981-92-3378-6_16.pdf) (ICIC 2026, proceedings 2027).
  Routes generation through discrete, hybrid or continuous representation paths to reduce inference cost relative to a fixed-path configuration.

- [**EVAR: Edge Visual Autoregressive Models via Principled Pruning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37086-0_31.pdf) (ECCV, 2026).
  Structured pruning with scale-aware compensation and distillation.

- [**OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models**](https://link.springer.com/content/pdf/10.1007/978-3-032-37419-6_6.pdf) (ECCV, 2026).
  Uses a state-space autoregressive predictor with measured image-generation timing. headline long-sequence gains concern text output.

- [**Prism-MoE: Efficient Dense-to-MoE Conversion for Visual Autoregressive Generation**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26gy/li26gy.pdf) (ICML, 2026).
  Dense-to-MoE conversion with sparse expert activation.

- [**Progressive Supernet Training for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.16546) (CVPR, 2026).
  Progressive supernet training permits scale-dependent subnet execution.

- [**Visual Implicit Autoregressive Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/jiang26ah/jiang26ah.pdf) (ICML, 2026).
  Implicit equilibrium layer with variable inference iterations.

- [**Collaborative Decoding Makes Visual Auto-Regressive Modeling Efficient**](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Collaborative_Decoding_Makes_Visual_Auto-Regressive_Modeling_Efficient_CVPR_2025_paper.pdf) (CVPR, 2025).
  Large model predicts coarse scales and a smaller model refines later scales.

- [**Denoising Token Prediction in Masked Autoregressive Models**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yao_Denoising_Token_Prediction_in_Masked_Autoregressive_Models_ICCV_2025_paper.pdf) (ICCV, 2025).
  Redesigns masked and unmasked token prediction in MAR to improve the inference-time and image-quality trade-off.

- [**FreqExit: Enabling Early-Exit Inference for Visual Autoregressive Models via Frequency-Aware Guidance**](https://papers.neurips.cc/paper_files/paper/2025/file/95cb60b65d9f2c0cd78b567ffebde9e6-Paper-Conference.pdf) (NeurIPS, 2025).
  Trains frequency-aware early-exit behavior.

- [**Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis**](https://openaccess.thecvf.com/content/CVPR2025/papers/Han_Infinity_Scaling_Bitwise_AutoRegressive_Modeling_for_High-Resolution_Image_Synthesis_CVPR_2025_paper.pdf) (CVPR, 2025).
  Bitwise prediction avoids a very large categorical classifier.

- [**Numerical Pruning for Efficient Autoregressive Models**](https://arxiv.org/pdf/2412.12441) (AAAI, 2025).
  Numerical-score structured pruning.

- [**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf) (NeurIPS, 2024).
  Next-scale prediction replaces raster next-token progression.

- [**Blockwise Parallel Decoding for Deep Autoregressive Models**](https://proceedings.neurips.cc/paper_files/paper/2018/file/c4127b9194fe8562c64dc0f5bf2c93bc-Paper.pdf) (NeurIPS, 2018).
  Predicts blocks provisionally and commits the prefix validated by a scoring model.

## 5.2 Learned Generation Schedules and Conditioning Structures

- [**ACDiT: Interpolating Autoregressive Conditional Modeling and Diffusion Transformer**](https://arxiv.org/pdf/2412.07720) (TMLR, 2026).
  Caches completed blocks under block-causal attention and samples within each block by diffusion. image and video timings are reported separately.

- [**Autoregression with Self-Token Prediction**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26du/chen26du.pdf) (ICML, 2026).
  Self-token prediction generates flexible token groups per step.

- [**Autoregressive Image Generation with Randomized Parallel Decoding**](https://proceedings.iclr.cc/paper_files/paper/2026/file/267852def1fd0db257622892c7e3be2a-Paper-Conference.pdf) (ICLR, 2026).
  Decouples position guidance and content prediction for grouped decoding.

- [**Learning to Expand Images for Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2511.15499v1) (ACM MM, 2026).
  Spiral expansion with length-adaptive parallel decoding.

- [**Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation**](https://arxiv.org/pdf/2507.01957v2) (ICLR, 2026).
  Position query tokens and locality-aware parallel generation order.

- [**MADFormer: Mixed Autoregressive and Diffusion Transformers for Continuous Image Generation**](https://proceedings.iclr.cc/paper_files/paper/2026/file/7cdf000d22c6cda21f3cbd7467aaf26f-Paper-Conference.pdf) (ICLR, 2026).
  Allocates AR conditioning layers and iterative diffusion layers.

- [**Markovian Scale Prediction: A New Era of Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Markovian_Scale_Prediction_A_New_Era_of_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  Compressed history state and limited scale context.

- [**MVAR: Visual Autoregressive Modeling with Scale and Spatial Markovian Conditioning**](https://proceedings.iclr.cc/paper_files/paper/2026/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf) (ICLR, 2026).
  Restricts conditioning to adjacent scales and local neighborhoods.

- [**Progressive Checkerboards for Autoregressive Multiscale Image Generation**](https://arxiv.org/pdf/2602.03811) (TMLR, 2026).
  Combines cross-scale conditioning with progressive checkerboard groups to reduce sequential sampling rounds.

- [**SCAN: Self-Calibrated AutoregressioN for High-Quality Visual Generation**](https://ojs.aaai.org/index.php/AAAI/article/download/37400/41362) (AAAI, 2026).
  Uses next-set prediction for fast initial generation and adds selective token refinement at additional inference cost.

- [**XYZFlow: Scaling Multidimensional Shortcut Flows for Efficient Generative Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/liu26ck/liu26ck.pdf) (ICML, 2026).
  Shortcut flow modeling with multidimensional prediction.

- [**Beyond Next-Token: Next-X Prediction for Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Ren_Beyond_Next-Token_Next-X_Prediction_for_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Next-X prediction over flexible entities.

- [**Hierarchical Masked Autoregressive Models with Low-Resolution Token Pivots**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zheng25i/zheng25i.pdf) (ICML, 2025).
  Low-resolution pivots condition later high-resolution groups.

- [**HMAR: Efficient Hierarchical Masked Auto-Regressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Kumbong_HMAR_Efficient_Hierarchical_Masked_Auto-Regressive_Image_Generation_CVPR_2025_paper.pdf) (CVPR, 2025).
  Hierarchical ordering and IO-aware block-sparse attention kernels.

- [**Neighboring Autoregressive Modeling for Efficient Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/He_Neighboring_Autoregressive_Modeling_for_Efficient_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Neighbor expansion with dimension-oriented parallel prediction heads.

- [**NFIG: Multi-Scale Autoregressive Image Generation via Frequency Ordering**](https://proceedings.neurips.cc/paper_files/paper/2025/file/24aa1508f9bdb2c2894c00963ce39f18-Paper-Conference.pdf) (NeurIPS, 2025).
  Organizes multiscale autoregressive generation from low to high frequencies. reported runtime comparisons also vary model capacity.

- [**Parallelized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Parallelized_Autoregressive_Visual_Generation_CVPR_2025_paper.pdf) (CVPR, 2025).
  Generates spatially distant groups concurrently.

- [**RandAR: Decoder-only Autoregressive Visual Generation in Random Orders**](https://openaccess.thecvf.com/content/CVPR2025/papers/Pang_RandAR_Decoder-only_Autoregressive_Visual_Generation_in_Random_Orders_CVPR_2025_paper.pdf) (CVPR, 2025).
  Position instruction tokens enable parallel decoding.

- [**Randomized Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Randomized_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Randomized-order training yields an AR generator evaluated with KV-cached serving.

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Uses compact spectral tokens with sequential or grouped prediction. grouped configurations trade generation time against image quality.

- [**Locally Hierarchical Auto-Regressive Modeling for Image Generation**](https://proceedings.neurips.cc/paper_files/paper/2022/file/67d60c2694f4fecd18fa04d1fa8c0a5c-Paper-Conference.pdf) (NeurIPS, 2022).
  Models local code pyramids and samples fine-code groups in parallel after their coarse code is generated.

- [**PixelPyramids: Exact Inference Models from Lossless Image Pyramids**](https://openaccess.thecvf.com/content/ICCV2021/papers/Mahajan_PixelPyramids_Exact_Inference_Models_From_Lossless_Image_Pyramids_ICCV_2021_paper.pdf) (ICCV, 2021).
  Uses lossless image pyramids and local conditional dependencies to parallelize block-autoregressive pixel generation.

## 5.3 Efficient Visual Representations and Reconstruction

- [**Autoregressive Image Generation with Masked Bit Modeling**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/yu26z/yu26z.pdf) (ICML, 2026).
  Masked bit modeling supports efficient prediction of large-vocabulary image representations.

- [**BitDance: Scaling Autoregressive Generative Models with Binary Tokens**](https://arxiv.org/pdf/2602.14041) (NeurIPS, 2026, to appear).
  Combines binary visual tokens with a diffusion head and next-patch prediction to generate multiple image tokens in parallel.

- [**FARMER: Flow AutoRegressive Transformer over Pixels**](https://openaccess.thecvf.com/content/CVPR2026/papers/Zheng_FARMER_Flow_AutoRegressive_Transformer_over_Pixels_CVPR_2026_paper.pdf) (CVPR, 2026).
  Self-supervised dimension reduction reduces sequential sampling burden.

- [**LacTokGen: Latent Consistency Tokenizer for 1024-pixel Image Generation by 256 Tokens**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xie_LacTokGen_Latent_Consistency_Tokenizer_for_1024-pixel_Image_Generation_by_256_CVPR_2026_paper.pdf) (CVPR, 2026).
  Compact discrete tokens with latent-consistency decoding.

- [**Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model**](https://proceedings.iclr.cc/paper_files/paper/2026/file/d649dd586dba64672a96beff24178125-Paper-Conference.pdf) (ICLR, 2026).
  Trains a tokenizer with a causal decoder for efficient autoregressive prediction. throughput comparisons concern separately trained generators.

- [**UniCompress: Token Compression for Unified Vision-Language Understanding and Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_UniCompress_Token_Compression_for_Unified_Vision-Language_Understanding_and_Generation_CVPR_2026_paper.pdf) (CVPR, 2026).
  Shortens the main autoregressive visual sequence and expands it with a smaller autoregressive decompressor before image decoding.

- [**Unified Multimodal Autoregressive Modeling with Shared Context—Visual Tokenizer is Key to Unification**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/peng26k/peng26k.pdf) (ICML, 2026).
  Channel-bitwise prediction reduces serial autoregressive steps.

- [**VibeToken: Scaling 1D Image Tokenizers and Autoregressive Models for Dynamic Resolution Generations**](https://openaccess.thecvf.com/content/CVPR2026/papers/Patel_VibeToken_Scaling_1D_Image_Tokenizers_and_Autoregressive_Models_for_Dynamic_CVPR_2026_paper.pdf) (CVPR, 2026).
  Uses short resolution-agnostic codes to reduce autoregressive prediction FLOPs. image reconstruction remains a separate cost.

- [**DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer**](https://openaccess.thecvf.com/content/ICCV2025/papers/Wu_DC-AR_Efficient_Masked_Autoregressive_Image_Generation_with_Deep_Compression_Hybrid_ICCV_2025_paper.pdf) (ICCV, 2025).
  Deep-compression hybrid tokenizer reduces spatial sequence burden.

- [**FlexVAR: Flexible Visual Autoregressive Modeling without Residual Prediction**](https://proceedings.neurips.cc/paper_files/paper/2025/file/0d0d75da30e2d81b928d793afe389ad4-Paper-Conference.pdf) (NeurIPS, 2025).
  Ground-truth scale prediction supports variable inference-stage budgets.

- [**HART: Efficient Visual Generation with Hybrid Autoregressive Transformer**](https://proceedings.iclr.cc/paper_files/paper/2025/file/ab4e1e704c68b0f476c265996f08d283-Paper-Conference.pdf) (ICLR, 2025).
  Combines discrete autoregressive structure prediction with lightweight continuous residual sampling. residual sampling adds work relative to discrete-only generation.

- [**ImageFolder: Autoregressive Image Generation with Folded Tokens**](https://proceedings.iclr.cc/paper_files/paper/2025/file/82519a9d318f39096ea507615c61c340-Paper-Conference.pdf) (ICLR, 2025).
  Folds spatially aligned token streams and predicts paired codes from shared AR states, reducing inference FLOPs with latency close to VAR in the reported configuration.

- [**SpectralAR: Spectral Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_SpectralAR_Spectral_Autoregressive_Visual_Generation_ICCV_2025_paper.pdf) (ICCV, 2025).
  Uses compact spectral tokens with sequential or grouped prediction. grouped configurations trade generation time against image quality.

- [**Not All Image Regions Matter: Masked Vector Quantization for Autoregressive Image Generation**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Not_All_Image_Regions_Matter_Masked_Vector_Quantization_for_Autoregressive_CVPR_2023_paper.pdf) (CVPR, 2023).
  Omits redundant region codes, predicts retained codes and positions, and restores dense features before image decoding.

- [**Towards Accurate Image Coding: Improved Autoregressive Image Generation With Dynamic Vector Quantization**](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_Towards_Accurate_Image_Coding_Improved_Autoregressive_Image_Generation_With_Dynamic_CVPR_2023_paper.pdf) (CVPR, 2023).
  Allocates variable-length codes across image regions and predicts their positions and contents to reduce autoregressive sampling cost.

- [**Autoregressive Image Generation Using Residual Quantization**](https://openaccess.thecvf.com/content/CVPR2022/papers/Lee_Autoregressive_Image_Generation_Using_Residual_Quantization_CVPR_2022_paper.pdf) (CVPR, 2022).
  Reduces the spatial code grid through residual quantization and predicts code stacks. reported sampling times exclude image decoding.

- [**Anytime Sampling for Autoregressive Models via Ordered Autoencoding**](https://arxiv.org/pdf/2102.11495) (ICLR, 2021).
  Orders latent dimensions by reconstruction importance so AR sampling can stop before all codes are generated.

## 5.4 Learned Sampling Acceleration

- [**Drift-AR: Single-Step Visual Autoregressive Generation via Anti-Symmetric Drifting**](https://arxiv.org/pdf/2603.28049) (ECCV, 2026).
  Entropy-guided speculation and one-step drifting decoder.

- [**Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning**](https://openaccess.thecvf.com/content/CVPR2026/papers/Gu_Masked_Auto-Regressive_Variational_Acceleration_Fast_Inference_Makes_Practical_Reinforcement_Learning_CVPR_2026_paper.pdf) (CVPR, 2026).
  Distills a faster sampler while retaining a masked AR generation organization.

- [**Continuous Visual Autoregressive Generation via Score Maximization**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shao25b/shao25b.pdf) (ICML, 2025).
  Models continuous conditionals with score maximization instead of iterative diffusion.

- [**Distilled Decoding 1: One-step Sampling of Image Auto-regressive Models with Flow Matching**](https://arxiv.org/pdf/2412.17153v3) (ICLR, 2025).
  Distills AR sampling into a few-step flow generator.

- [**Distilled Decoding 2: One-step Sampling of Image Auto-regressive Models with Conditional Score Distillation**](https://proceedings.neurips.cc/paper_files/paper/2025/file/085f2a21d3f0cef1585fceaa6dacdc15-Paper-Conference.pdf) (NeurIPS, 2025).
  Conditional score distillation trains a one-step replacement.


## License

[CC BY 4.0](../../LICENSE.md). Linked papers retain their original licenses.
