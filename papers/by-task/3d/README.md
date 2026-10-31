# 3D and Motion Generation Acceleration

[Home](../../../README.md) · [By output](../README.md) · [By mechanism](../../README.md) · [Background](../../background/README.md) · [Pending](../../pending/README.md)

**9 core papers.** A study with verified image and video applications appears in both task lists. Counts must not be added to obtain unique papers.

Geometry, scene layouts and human motion remain separate output labels below. Volumetric medical synthesis has its own label. Their metrics and timing results are not pooled.

## 3D geometry

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) · [Details](../../paper-notes.md#supervoxelgpt)
  - **Accelerates:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Approach:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.
  - **Original-source evidence:** Sections 3.3–4.1 explicitly apply Jacobi decoding to the AR token predictor, capped at 30 iterations. Tables 1–2 report seconds per shape. Section 4.2 decomposes total image-to-3D inference into saliency prediction, CVT, AR prediction and decoding.
  - **Source location:** PDF pp. 10–11, AR training and Jacobi decoding; PDF p. 12, Tables 1–2; PDF pp. 13–14, setup and generation efficiency · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf).
  - **Measured scope:** Complete reported shape-generation time on one RTX 4090. Text-to-3D AR comparisons use different resolutions. The headline 10x averages heterogeneous image-to-3D baselines. Reading extent: selected primary PDF passages.

## 3D human motion

- [**ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_24) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf) · [Details](../../paper-notes.md#scalemogenmotion)
  - **Accelerates:** Seven scale-wise AR stages for motion synthesis.
  - **Approach:** Section 3.2 conditions each skeletal-temporal scale on text and a prefix formed from completed coarser token maps. Section 4.7 specifies seven sequential scale stages. No Flow Matching head is part of the inspected next-scale bitwise-token prediction mechanism.
  - **Original-source evidence:** Retain as efficient AR 3D human-motion generation. Its output is motion, not static RGB images or a mesh-generation task. Single RTX 4090, SnapMoGen: seven stages and 0.071 s/sample versus T2M-GPT 40 stages and 0.239 s. MoMask++ reports 0.051 s. The source table does not establish that the fewest stages gives the fastest method.
  - **Source location:** Original PDF pp. 5–8, Sections 3.1–3.2; pp. 15–16, Table 6 and Section 4.7 · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf).
  - **Measured scope:** Single RTX 4090, SnapMoGen: seven stages and 0.071 s/sample versus T2M-GPT 40 stages and 0.239 s. MoMask++ reports 0.051 s. The source table does not establish that the fewest stages gives the fastest method. Reading extent: selected primary PDF passages.

## 3D layout

- [**Repurposing 3D Generative Model for Autoregressive Layout Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#lavigen3d)
  - **Accelerates:** Autoregressive 3D layout generation.
  - **Approach:** Repurposes a 3D diffusion model and uses dual-guidance self-rollout distillation.
  - **Original-source evidence:** Original performance and ablation passages compare generation time.
  - **Source location:** PDF p. 8 · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf#page=8).
  - **Measured scope:** 3D layout generation, not static-image latency. Reading extent: selected primary PDF passages.

## 3D mesh

- [**FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#flashmesh3d)
  - **Accelerates:** AR mesh token decoding.
  - **Approach:** Trained face/point/coordinate proposal blocks with structured correction and backbone verification.
  - **Original-source evidence:** Table 1 reports mesh-token throughput on H20 for Meshtron and Mesh-RFT variants with learned speculation modules.
  - **Source location:** PDF p. 6, Table 1 and Sections 4.1–4.2; PDF p. 8, Tables 2–5 · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf#page=6).
  - **Measured scope:** Mesh tokens per generation second, parameter counts increase with the added modules. No independent sampling-law guarantee checked. Reading extent: selected primary PDF passages.

- [**XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26dn.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf) · [Details](../../paper-notes.md#xspecmesh3d)
  - **Accelerates:** AR mesh next-token decoding.
  - **Approach:** Multi-head proposals with backbone verification/resampling and head distillation.
  - **Original-source evidence:** Table 3 and efficiency experiments report step latency and actual sampling speedup on RTX 3090.
  - **Source location:** PDF p. 8 · [Original source](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf#page=8).
  - **Measured scope:** Mesh decoding runtime, no new preservation theorem certified. Reading extent: selected primary PDF passages.

## 3D point cloud

- [**PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf) · [Details](../../paper-notes.md#pointnsp3d)
  - **Accelerates:** AR point-cloud sampling.
  - **Approach:** Next-scale level-of-detail prediction replaces next-point progression.
  - **Original-source evidence:** Table 3 reports sampling seconds separately from training GPU hours.
  - **Source location:** PDF p. 7 · [Original source](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf#page=7).
  - **Measured scope:** 3D sampling time, not training-time acceleration. Reading extent: selected primary PDF passages.

## 3D scene layout

- [**NaLA: A 3D Native LLM Layout Agent for High-Quality 3D Scene Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) · [Details](../../paper-notes.md#nalalayout)
  - **Accelerates:** AR asset-pose output tokens and repeated optimization in 3D layout generation.
  - **Approach:** Encode room/asset point clouds, generate coarse discrete poses and refine them with a continuous regression head.
  - **Original-source evidence:** Section 4 describes AR pose codes followed by continuous refinement. Section 5.6 and Figure 7d compare inference time against asset count for NaLA, LayoutGPT, Holodeck and LayoutVLM, and show lower reported generation time for NaLA. The baseline methods are run with their official configurations.
  - **Source location:** Official ECCV PDF pp. 7–8, token construction; pp. 10 and 12–13, baseline setup, Section 5.6 and Figure 7d. Figure visually checked · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf).
  - **Measured scope:** Source-reported layout-generation runtime curves for different complete agents. The figure does not isolate token representation from backbone or optimization changes. No numeric ratio is inferred from plotted points. Reading extent: selected primary PDF passages.

## 3D shape

- [**3D-WAG: Hierarchical Wavelet-Guided Autoregressive Generation for High-Fidelity 3D Shapes**](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf) (BMVC, 2025). [Paper](https://bmvc2025.bmva.org/proceedings/1064/) · [PDF](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf) · [Details](../../paper-notes.md#wag3d)
  - **Accelerates:** Autoregressive shape token sampling.
  - **Approach:** Wavelet hierarchy supports next-scale generation.
  - **Original-source evidence:** Original Table 2 reports shape sampling time; the abstract uses a different hardware setting.
  - **Source location:** PDF p. 9 · [Original source](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf#page=9).
  - **Measured scope:** 3D shape inference, hardware-specific results remain separate. Reading extent: selected primary PDF passages.

## volumetric medical image synthesis

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) · [Details](../../paper-notes.md#mpadmri)
  - **Accelerates:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Approach:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.
  - **Original-source evidence:** Figure 1 compares LDM-3D, ALDM and MPAD on ADNI. MPAD reports 23.6 TFLOPs per volume, 4.6 s and 3.0 GB peak memory, versus LDM-3D's 68.4 TFLOPs, 5.2 s and 18.1 GB. Section 4.2 uses ten DDIM steps for the first plane and two for later planes.
  - **Source location:** Official ECCV PDF p. 2, Figure 1; p. 9, Section 4.2; pp. 14–15, reduced-refinement discussion. Figure 1 visually checked · [Original source](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf).
  - **Measured scope:** Efficient learned AR generator compared with volumetric diffusion baselines. The approximately threefold FLOPs reduction is distinct from the much smaller reported runtime difference. Task is cross-contrast MRI synthesis, not general text-to-image generation. Reading extent: selected primary PDF passages.
