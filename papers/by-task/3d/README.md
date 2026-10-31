# 3D and Motion Generation Acceleration

[Home](../../../README.md) · [By output](../README.md) · [Mechanisms](../../README.md)

**9 acceleration papers.**

## 3D geometry

<a id="paper-supervoxelgpt"></a>

- [**SuperVoxelGPT: Adaptive and Ordered 3D Tokenization for Autoregressive Shape Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37577-3_22) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf)
  - **Focus:** Shape-token sequence length and sequential AR transformer evaluations.
  - **Mechanism:** Use adaptive ordered supervoxels and Jacobi decoding of a Qwen2.5-0.5B shape-token predictor, followed by SuperVoxelVAE decoding.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37577-3_22.pdf), PDF pp. 10–11, AR training and Jacobi decoding; PDF p. 12, Tables 1–2; PDF pp. 13–14, setup and generation efficiency.

## 3D human motion

<a id="paper-scalemogenmotion"></a>

- [**ScaleMoGen: Autoregressive Next-Scale Prediction for Human Motion Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37152-2_24) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf)
  - **Focus:** Seven scale-wise AR stages for motion synthesis.
  - **Mechanism:** Predicts each skeletal-temporal scale from text and completed coarser token maps.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37152-2_24.pdf), PDF pp. 5–8, Sections 3.1–3.2; pp. 15–16, Table 6 and Section 4.7.

## 3D layout

<a id="paper-lavigen3d"></a>

- [**Repurposing 3D Generative Model for Autoregressive Layout Generation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf)
  - **Focus:** Autoregressive 3D layout generation.
  - **Mechanism:** Repurposes a 3D diffusion model and uses dual-guidance self-rollout distillation.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Feng_Repurposing_3D_Generative_Model_for_Autoregressive_Layout_Generation_CVPR_2026_paper.pdf#page=8), PDF p. 8.

## 3D mesh

<a id="paper-flashmesh3d"></a>

- [**FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation**](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf)
  - **Focus:** AR mesh token decoding.
  - **Mechanism:** Trained face/point/coordinate proposal blocks with structured correction and backbone verification.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Shen_FlashMesh_Faster_and_Better_Autoregressive_Mesh_Synthesis_via_Structured_Speculation_CVPR_2026_paper.pdf#page=6), PDF p. 6, Table 1 and Sections 4.1–4.2; PDF p. 8, Tables 2–5.

<a id="paper-xspecmesh3d"></a>

- [**XSpecMesh: Quality-Preserving Auto-Regressive Mesh Generation Acceleration via Multi-Head Speculative Decoding**](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf) (ICML, 2026). [Paper](https://proceedings.mlr.press/v306/chen26dn.html) · [PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf)
  - **Focus:** AR mesh next-token decoding.
  - **Mechanism:** Multi-head proposals with backbone verification/resampling and head distillation.
  - **Source:** [Paper](https://raw.githubusercontent.com/mlresearch/v306/main/assets/chen26dn/chen26dn.pdf#page=8), PDF p. 8.

## 3D point cloud

<a id="paper-pointnsp3d"></a>

- [**PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction**](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf) (CVPR, 2026). [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.html) · [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf)
  - **Focus:** AR point-cloud sampling.
  - **Mechanism:** Next-scale level-of-detail prediction replaces next-point progression.
  - **Source:** [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Meng_PointNSP_Autoregressive_3D_Point_Cloud_Generation_with_Next-Scale_Level-of-Detail_Prediction_CVPR_2026_paper.pdf#page=7), PDF p. 7.

## 3D scene layout

<a id="paper-nalalayout"></a>

- [**NaLA: A 3D Native LLM Layout Agent for High-Quality 3D Scene Generation**](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37627-5_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf)
  - **Focus:** AR asset-pose output tokens and repeated optimization in 3D layout generation.
  - **Mechanism:** Encode room/asset point clouds, generate coarse discrete poses and refine them with a continuous regression head.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37627-5_16.pdf), PDF pp. 7–8, token construction; pp. 10 and 12–13, baseline setup, Section 5.6 and Figure 7d. Figure.

## 3D shape

<a id="paper-wag3d"></a>

- [**3D-WAG: Hierarchical Wavelet-Guided Autoregressive Generation for High-Fidelity 3D Shapes**](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf) (BMVC, 2025). [Paper](https://bmvc2025.bmva.org/proceedings/1064/) · [PDF](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf)
  - **Focus:** Autoregressive shape token sampling.
  - **Mechanism:** Wavelet hierarchy supports next-scale generation.
  - **Source:** [Paper](https://bmva-archive.org.uk/bmvc/2025/assets/papers/Paper_1064/paper.pdf#page=9), PDF p. 9.

## volumetric medical image synthesis

<a id="paper-mpadmri"></a>

- [**Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis**](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf) (ECCV, 2026). [Paper](https://link.springer.com/chapter/10.1007/978-3-032-37450-9_16) · [PDF](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf)
  - **Focus:** Volumetric denoising and cross-plane sampling in an AR MRI-synthesis generator.
  - **Mechanism:** Replace full 3D denoising with plane-wise 2D conditional diffusion. Reuse previous-plane volumes as priors for fewer subsequent-plane updates.
  - **Source:** [Paper](https://link.springer.com/content/pdf/10.1007/978-3-032-37450-9_16.pdf), PDF p. 2, Figure 1; p. 9, Section 4.2; pp. 14–15, reduced-refinement discussion. Figure 1.
