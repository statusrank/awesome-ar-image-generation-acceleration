# Pending Papers

[Home](../../README.md) · [Categories](../README.md) · [Source notes](../paper-notes.md)

**29 papers.**

These entries are separate from the core acceleration list. The outstanding check is stated beside each paper.

- [3D geometry](#3d-geometry)
- [3D human motion](#3d-human-motion)
- [3D mesh](#3d-mesh)
- [image](#image)
- [video](#video)
- [video / scene forecasts](#video--scene-forecasts)

## 3D geometry

- [**Grow3D: Hierarchical Next-Scale Octree Prediction for Fast and High-Fidelity 3D Shape Generation**](https://doi.org/10.1145/3820379) (ACM Transactions on Graphics, 2026). [Paper](https://doi.org/10.1145/3820379) · [Details](../paper-notes.md#grow3d)
  - **Context:** Next-scale octree prediction for efficient AR 3D-shape generation.
  - **To verify:** Retrieve the full paper and identify actual inference timing, baseline and hardware. Do not report a numerical speedup from secondary summaries
  - Online publication: 2026-09-14. The publisher metadata assigns volume 46(1) to the 2027 print issue. Listed under the verified online year.

## 3D human motion

- [**ActionPlan: Future-Aware Streaming Motion Synthesis via Frame-Level Action Planning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37225-3_30.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37225-3_30) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37225-3_30.pdf) · [Details](../paper-notes.md#actionplanmotion)
  - **Context:** Overlapping conditional-denoising updates for streaming motion tokens.
  - **To verify:** Inspect streaming attention masks and the treatment of clean historical versus provisional future motion latents in the official implementation or supplementary algorithm. Do not infer non-AR or algorithmic error from this missing check

- [**InterCMDM: Block-Causal Diffusion for Autoregressive Human Interaction Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_2.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37531-5_2) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37531-5_2.pdf) · [Details](../paper-notes.md#intercmdmmotion)
  - **Context:** Block-causal conditional sampling for streaming human-interaction motion.
  - **To verify:** Locate an efficiency comparison establishing the saved computation. Do not convert real-time feasibility into an acceleration ratio

- [**Language-Guided Transformer Tokenizer for Human Motion Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37041-9_17.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37041-9_17) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37041-9_17.pdf) · [Details](../paper-notes.md#lgtokmotion)
  - **Context:** Compact language-aligned discrete motion tokens.
  - **To verify:** Read the appendix timing and identify the evaluated generator family. Token-count reduction alone is not measured latency

- [**Practice Makes Perfect: From Explicit Decomposition to Reinforced Latent Planning in Text-to-Motion Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37174-4_27.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37174-4_27) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37174-4_27.pdf) · [Details](../paper-notes.md#lactmotion)
  - **Context:** Replace explicit reasoning text preceding AR motion decoding with continuous latent reasoning.
  - **To verify:** Retrieve the supplementary timing configuration and compare the same workload. Cross-source explicit-CoT timing is not a controlled speedup

## 3D mesh

- [**FACE: A Face-based Autoregressive Representation for High-Fidelity and Efficient Mesh Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_FACE_A_Face-based_Autoregressive_Representation_for_High-Fidelity_and_Efficient_Mesh_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#facemesh)
  - **Context:** Autoregressive mesh decoder.
  - **To verify:** Inspected tables concern representation length and geometric fidelity

- [**EdgeRunner: Auto-regressive Auto-encoder for Artistic Mesh Generation**](https://proceedings.iclr.cc/paper_files/paper/2025/file/58e6c003c9fb3992265005ff6aef1913-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/58e6c003c9fb3992265005ff6aef1913-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/58e6c003c9fb3992265005ff6aef1913-Paper-Conference.pdf) · [Details](../paper-notes.md#edgerunner3d)
  - **Context:** AR mesh sampling.
  - **To verify:** Source reports its own token throughput and time by face count, without an established acceleration comparison

- [**TreeMeshGPT: Artistic Mesh Generation with Autoregressive Tree Sequencing**](https://openaccess.thecvf.com/content/CVPR2025/papers/Lionar_TreeMeshGPT_Artistic_Mesh_Generation_with_Autoregressive_Tree_Sequencing_CVPR_2025_paper.pdf) (CVPR, 2025). [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lionar_TreeMeshGPT_Artistic_Mesh_Generation_with_Autoregressive_Tree_Sequencing_CVPR_2025_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Lionar_TreeMeshGPT_Artistic_Mesh_Generation_with_Autoregressive_Tree_Sequencing_CVPR_2025_paper.pdf) · [Details](../paper-notes.md#treemeshgpt3d)
  - **Context:** Mesh AR sequence length.
  - **To verify:** Inspected source reports compression and mesh quality. An inference-cost comparison was not located

## image

- [**31.4 VARSA: A Visual Autoregressive Generation Accelerator Using Performance-Scalable Multi-Precision PE-LUT and Grid-Similarity Attention Compression**](https://doi.org/10.1109/isscc49663.2026.11409066) (ISSCC, 2026). [Paper](https://doi.org/10.1109/isscc49663.2026.11409066) · [Details](../paper-notes.md#varsa)
  - **Context:** Claimed visual AR hardware inference.
  - **To verify:** Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established

- [**A 28nm 47.3TFLOPs/W 894mJ/Inference Visual Autoregressive Accelerator with Differential-Amplifier Speculation and Chain-Reaction-Like Parallel Generation**](https://doi.org/10.1109/isscc49663.2026.11409075) (ISSCC, 2026). [Paper](https://doi.org/10.1109/isscc49663.2026.11409075) · [Details](../paper-notes.md#issccvaraccelerator)
  - **Context:** Claimed visual AR hardware inference.
  - **To verify:** Formal publication exists. ISSCC eligibility under the supplied CCF directory is not established

- [**Autoregressive Image Generation with Frequency Progression**](https://arxiv.org/pdf/2503.05305) (TMLR, 2026). [Paper](https://openreview.net/forum?id=cEfd15ouQ1) · [PDF](https://arxiv.org/pdf/2503.05305) · [Details](../paper-notes.md#tmlrcefd15ouq1)
  - **Context:** Frequency-progressive continuous AR image generation.
  - **To verify:** AR mechanism confirmed. Inspected version reports stages and quality, without a verified timing/FLOPs comparison

- [**Breaking Codebook Redundancy for Faster Autoregressive Image Generation with Retrieval-Augmented Speculative Decoding**](https://doi.org/10.1109/icassp55912.2026.11461425) (ICASSP, 2026). [Paper](https://doi.org/10.1109/icassp55912.2026.11461425) · [Details](../paper-notes.md#retrievalspecicassp)
  - **Context:** Claimed retrieval-augmented AR image speculation.
  - **To verify:** Official ICASSP identity is established. Algorithm and cost-bearing result not yet retrieved

- [**CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization**](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_CaTok_Taming_Mean_Flows_for_One-Dimensional_Causal_Image_Tokenization_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_CaTok_Taming_Mean_Flows_for_One-Dimensional_Causal_Image_Tokenization_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_CaTok_Taming_Mean_Flows_for_One-Dimensional_Causal_Image_Tokenization_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#catok)
  - **Context:** AR image tokens and MeanFlow image reconstruction.
  - **To verify:** The inspected tables report tokens, reconstruction steps and quality. A measured AR inference-cost comparison was not located

- [**Depth Adaptive Efficient Visual Autoregressive Modeling**](https://arxiv.org/pdf/2604.17286) (CVPR Findings, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026F/html/Li_Depth_Adaptive_Efficient_Visual_Autoregressive_Modeling_CVPRF_2026_paper.html) · [PDF](https://arxiv.org/pdf/2604.17286) · [Details](../paper-notes.md#depthvar)
  - **Context:** VAR token-wise computational depth.
  - **To verify:** Acceleration evidence is present, but the confirmed publication is CVPR Findings. Main-track CCF equivalence is not established

- [**DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Srivastava_DPAR_Dynamic_Patchification_for_Efficient_Autoregressive_Visual_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Srivastava_DPAR_Dynamic_Patchification_for_Efficient_Autoregressive_Visual_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Srivastava_DPAR_Dynamic_Patchification_for_Efficient_Autoregressive_Visual_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#dpar)
  - **Context:** AR image token sequence.
  - **To verify:** The inspected efficiency result is training FLOPs. The paper calls generation-speed improvements a future direction

- [**Efficient High-Resolution Image Synthesis via Autoregressive Modeling in a Diffusion-Learned Continuous Latent Space**](https://openreview.net/forum?id=wkNwPZ0g3G) (TMLR, 2026). [Paper](https://openreview.net/forum?id=wkNwPZ0g3G) · [Details](../paper-notes.md#tmlrwknwpz0g3g)
  - **Context:** Claimed high-resolution continuous-latent AR generator.
  - **To verify:** Formal TMLR identity is established. Primary mechanism/cost passages remain inaccessible

- [**Enhancing Quantization for Visual Autoregressive Generation Via Uncertainty Identification**](https://doi.org/10.1109/icassp55912.2026.11462147) (ICASSP, 2026). [Paper](https://doi.org/10.1109/icassp55912.2026.11462147) · [Details](../paper-notes.md#uncertaintyquanticassp)
  - **Context:** Claimed visual AR quantization.
  - **To verify:** Official ICASSP identity is established. Quantization type and inference evidence remain unresolved

- [**SCALAR++: Efficient Controllable Generation via Scale-wise Visual Autoregressive Learning**](https://doi.org/10.1007/s11263-026-02984-z) (IJCV, 2026). [Paper](https://doi.org/10.1007/s11263-026-02984-z) · [Details](../paper-notes.md#scalarplus)
  - **Context:** Control-conditioned VAR adapter overhead.
  - **To verify:** Publisher abstract claims parameter and memory savings. Inference versus training-memory boundary needs confirmation

- [**Soft Tail-Dropping for Adaptive Visual Tokenization**](https://link.springer.com/content/pdf/10.1007/978-3-032-37553-7_24.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37553-7_24) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37553-7_24.pdf) · [Details](../paper-notes.md#stat)
  - **Context:** Adaptive-length AR image tokens.
  - **To verify:** Locate an actual inference-cost comparison before core admission. The token-count ratio is not a measured speedup

- [**TMXVAR: Twin Microscaling Floating-Point Quantization for Efficient Visual Autoregressive Model Inference on FPGA**](https://doi.org/10.1109/tcad.2026.3734745) (IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2026). [Paper](https://doi.org/10.1109/tcad.2026.3734745) · [Details](../paper-notes.md#tmxvar)
  - **Context:** Claimed VAR FPGA numerical inference.
  - **To verify:** Journal identity confirmed. Original technical result has not been retrieved

- [**Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation**](https://iiswc.org/iiswc2026/program.html) (IISWC, 2026). [Paper](https://iiswc.org/iiswc2026/program.html) · [Details](../paper-notes.md#diagonalsparsity)
  - **Context:** AR image attention and KV accesses.
  - **To verify:** Mechanism is relevant. The confirmed IISWC venue is not established under the requested CCF list

- [**A Dual Stream Visual Tokenizer for LLM Image Generation**](https://ijcai.org/proceedings/2025/0167.pdf) (IJCAI, 2025). [Paper](https://ijcai.org/proceedings/2025/167) · [PDF](https://ijcai.org/proceedings/2025/0167.pdf) · [Details](../paper-notes.md#dualstreamvisualtokenizer)
  - **Context:** Compact dual-stream visual representation for LLM image generation.
  - **To verify:** No original AR inference-cost result established. Shorter representation alone is insufficient for core admission

- [**FlexTok: Resampling Images into 1D Token Sequences of Flexible Length**](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachmann25a/bachmann25a.pdf) (ICML, 2025). [Paper](https://proceedings.mlr.press/v267/bachmann25a.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachmann25a/bachmann25a.pdf) · [Details](../paper-notes.md#flextok)
  - **Context:** GPT-style image generation with compact 1D codes.
  - **To verify:** The inspected source establishes AR use and code lengths. Complete inference-cost savings were not verified

- [**ImageFolder: Autoregressive Image Generation with Folded Tokens**](https://proceedings.iclr.cc/paper_files/paper/2025/file/82519a9d318f39096ea507615c61c340-Paper-Conference.pdf) (ICLR, 2025). [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/82519a9d318f39096ea507615c61c340-Abstract-Conference.html) · [PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/82519a9d318f39096ea507615c61c340-Paper-Conference.pdf) · [Details](../paper-notes.md#imagefolder)
  - **Context:** AR image token prediction.
  - **To verify:** Mechanism and AR use confirmed. A separate measured inference-cost comparison is still required

- [**Stable Control Visual AutoRegressive Model: Precise and Efficient Image Generation via Scale Alignment**](https://doi.org/10.1109/icassp49660.2025.10890268) (ICASSP, 2025). [Paper](https://doi.org/10.1109/icassp49660.2025.10890268) · [Details](../paper-notes.md#stablecontrolvar)
  - **Context:** Candidate scale-alignment method for controllable VAR image generation.
  - **To verify:** Retrieve the original abstract and full method/performance sections. Efficient in the title alone does not establish acceleration

## video

- [**DiCoDe: Diffusion-Compressed Deep Tokens for Autoregressive Video Generation with Language Models**](https://arxiv.org/pdf/2412.04446) (TMLR, 2026). [Paper](https://openreview.net/forum?id=B7a0IAIEXZ) · [PDF](https://arxiv.org/pdf/2412.04446) · [Details](../paper-notes.md#dicodevideo)
  - **Context:** AR prior over diffusion-compressed video tokens.
  - **To verify:** Inspected source establishes compressed tokens and training efficiency, not a comparative generation-inference cost result

- [**EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Xiong_EVATok_Adaptive_Length_Video_Tokenization_for_Efficient_Visual_Autoregressive_Generation_CVPR_2026_paper.pdf) · [Details](../paper-notes.md#evatokvideo)
  - **Context:** AR video token length.
  - **To verify:** Table 3 reports generation tokens and quality. Inference runtime or FLOPs savings have not been established

- [**TinyHistory: Lightweight Video History Embeddings Via Two-Stage Context Learning**](https://link.springer.com/content/pdf/10.1007/978-3-032-37189-8_10.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37189-8_10) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37189-8_10.pdf) · [Details](../paper-notes.md#tinyhistoryvideo)
  - **Context:** Historical conditioning-token count in AR video generation.
  - **To verify:** Establish runtime, FLOPs or actual inference-memory changes including the added history encoder

## video / scene forecasts

- [**SyncCache: Exploiting Asymmetric Dynamics for Fast Audio-Driven Portrait Animation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_34.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37261-1_34) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37261-1_34.pdf) · [Details](../paper-notes.md#synccachepending)
  - **Context:** Reuse DiT backbone residuals while refreshing lightweight audio blocks.
  - **To verify:** AR/chunk-generation dependency and actual cache lifetime across chunks require verification before core admission
