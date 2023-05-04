![logo](https://raw.githubusercontent.com/ProtossDragoon/PlankHyundong/944c38802cfe392ed6ed194ccca6a083563add45/docs/images/logo.svg)

<br>

<div align="center">

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FProtossDragoon%2FPlankHyundong&count_bg=%23FFA217&title_bg=%2345FFDE&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 

</div>

<br>

# Plank Hyundong 3D

This is a 3D model of Hyundong, a fitness influencer, demonstrating the proper plank posture. For those who want to become fitness enthusiasts, why not exercise by carefully examining and comparing your posture with the **Hyundong figure extracted using the NeRF model**? 🏋🏻

[DataYanolja 2022 project description video](https://www.youtube.com/watch?v=s7k_cZi7hvw) / [Presentation material](https://drive.google.com/file/d/1XrWcYmuNC0rZVPC8ese5gtJTMicKKRcs/edit)

## Final result

<table>
<thead align="center">
  <tr>
    <th>Final result (actual figure), <a href="https://github.com/ProtossDragoon/PlankHyundong/blob/main/docs/GUIDELINE.md#evaluation">Qualitative evaluation</a> </th>
    <th>NeRF 3D representation</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img width="350" src="https://github.com/ProtossDragoon/PlankHyundong/blob/main/docs/images/figure_final.jpg"></td></th>
    <td><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/main/docs/images/hyundong360_removebg.gif"></td>
  </tr>
</tbody>
</table>

# Table of Contents

- [Quick Start](#quickstart)
- [Getting Started by Component](#start)
    - [1️⃣ Capturing Pseudo-depth Video](#step1)
    - [2️⃣ Sampling Images from Video](#step2)
    - [3️⃣ Calculating Camera Poses for Images](#step3)
    - [4️⃣ Training the NeRF Model](#step4)
    - [5️⃣ Creating and Refining Meshes from the NeRF Model](#step5)
    - [6️⃣ Printing and Post-processing the Figure](#step6)
- [Environment](#env)
- [Team](#team)

## Quick Start

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/nerf_quick_start.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

```
PlankHyundong/
├── nerf_quick_start.ipynb
├── notebooks
│   ├── nerf_colab.ipynb
│   ├── nerf_wandb_colab.ipynb
│   ├── colmap_colab.ipynb
│   ├── extract_mesh_colab.ipynb
│   └── sampling_colab.ipynb
└── data
    ├── video
    │   └── video.MOV
    ├── (images)
    │   └── ...
    └── (logs)
        └── ...
```

- The **notebooks** folder contains notebooks for each step of the pipeline needed to create the final result.
- A single notebook, **`nerf_quick_start.ipynb`**, is provided for quickly reviewing the entire workflow.
- The **data** folder contains the pseudo-depth video and the results of each step of the pipeline.

| Step | Content |
|:--:|:-----:|
| 1️⃣ | [Video Sampling: Sampling Images from a Video](#step1) |
| 2️⃣ | [Run COLMAP to get camera pose: Obtaining Camera Pose for Images](#step2) |
| 3️⃣ | [Run NeRF: Training the NeRF Model](#step3) |
| 4️⃣ | [Get Mesh file: Creating and Refining Mesh from the NeRF Model](#step4) |

- The required data can be found at `data/video/video.MOV`.
- A cell to clone the folder has been added at the beginning.
- Create subfolders named `images` and `logs` in the above folder. Each folder will store sampled images, config, mesh, weight, video files, etc.

<a name="start"></a>
# Getting Started by Component

![Pipeline](https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/pipeline.png)

|    | Output | Description |
|:--:|:------:|:-----------|
| 1️⃣ | RGB video | Collect video by rotating around the object. |
| 2️⃣ | N * RGB image set | Sample the video to obtain a set of images. |
| 3️⃣ | N * camera pose set | Camera poses are necessary for NeRF training.<br>Perform LLFF on the sampled images from 2️⃣. |
| 4️⃣ | Trained NeRF model file | Train the NeRF model.<br>The 3D representation contained in the NeRF model is called an **implicit 3D representation**. |
| 5️⃣ | Mesh object file | Apply a mesh to the implicit 3D representation.<br>Convert to the form of an **'explicit' 3D representation**. |
| 6️⃣ | 3D printer print file | Use slicer software.<br>Set the parameters of the 3D printer and prepare for printing. |
| 7️⃣ | 3D printed figure | Print the final product using a 3D printer. |

Below is an explanation of each step in the pipeline.

<br>

<a name="step1"></a>
## 1️⃣ Capture the Object on Video

<table>
<thead align="center">
  <tr>
    <th>Recommended, 360 degree capture</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/c466d902d2ec4d276452b78fdf258d2e73a0da13/docs/images/collecting_video.gif"></td>
  </tr>
  <tr>
    <td>Method used in this project</td>
  </tr>
</tbody>
</table>

➕ Please check the <a href="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/GUIDELINE.md#step1">following link</a> for recommended shooting practices and precautions.

<br>

<a name="step2"></a>
## 2️⃣ Sampling Images from Videos

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/sampling_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

<p align="center"><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/7fe9587f7c9c2752f5898dd41df171b86fe962d6/docs/images/video_sampling.gif" width="400" height="225"></p>

- This script samples images from a video taken by a camera with a fixed time interval.
- ✅ If the camera trajectory is long, it is better to sample images more frequently.
- ❗ If the camera trajectory is short and the time the lens is open is also short, sampling images too frequently from the video may negatively impact the performance.

➕ For more details on parameters, please check <a href="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/GUIDELINE.md#step2">here</a>!

<br>

<a name="step3"></a>
## 3️⃣ Estimating Camera Poses for Images

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/colmap_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

**NOTE:** You must use a GPU runtime.

<p align="center"><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/85638bda940f10d00839e656b4f9f487f9742aa8/docs/images/camera_poses.png"></p>

- The input for NeRF is a set of (image, camera pose) pairs.
- To compute the camera pose corresponding to each image in a custom dataset, we use the script developed by the author of [LLFF](https://github.com/Fyusion/LLFF) that is based on [COLMAP](https://github.com/colmap/colmap).
- When the script is finished, a `poses_bounds.npy` file necessary for running the NeRF model is created in the dataset folder.

➕ If you encounter difficulties in setting up the LLFF environment, please check <a href="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/GUIDELINE.md#step3">here</a> for more information.

<br>

<a name="step4"></a>
## 4️⃣ Training the NeRF Model

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/nerf_wandb_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

**NOTE:** You must use a GPU runtime.

### Training Options

|       Option      | Function |
|:---------------:|:---:|
| `--no_ndc`, `--spherify`, `--lindisp` | These flags are not necessary for forward-facing scenes, but are required for 360 scenes.|

### Results
<table>
<thead align="center">
  <tr>
    <th>RGB</th>
    <th>RGB_still</th>
    <th>disparity</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/7fe9587f7c9c2752f5898dd41df171b86fe962d6/docs/images/nerf_rgb.gif"></td>
    <td><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/7fe9587f7c9c2752f5898dd41df171b86fe962d6/docs/images/nerf_rgb_still.gif"></td>
      <td><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/7fe9587f7c9c2752f5898dd41df171b86fe962d6/docs/images/nerf_disp.gif"></td>
  </tr>
</tbody>
</table>

➕ If you want to know about the wandb integration and the results of the NeRF parameter experiments, check <a href="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/GUIDELINE.md#step4">here</a>!

<a name="step5"></a>
## 5️⃣ Creating and Refining Mesh from NeRF Model

### Creating Mesh

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/extract_mesh_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

**NOTE:** You must use a GPU runtime.

<p align="center"><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/7fe9587f7c9c2752f5898dd41df171b86fe962d6/docs/images/meshed_representation.gif" width="400" height="225"></p>

- This step involves loading the model trained using the NeRF model, extracting the surface (iso-surface) through the `PyMCubes` package, and saving the resulting `3d.obj` file. This is done to visualize the 3D representation of the trained NeRF model using `pyrender` and generate the `turntable.mp4` video.
- The source of this notebook is from the [official NeRF repository](https://github.com/bmild/nerf/blob/master/extract_mesh.ipynb).

### Refining Mesh

<p align="center"><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/7fe9587f7c9c2752f5898dd41df171b86fe962d6/docs/images/trim_mesh_case_without_background.jpg" width="400" height="225"></p>

- As the NeRF model is trained using data collected directly rather than through a simulator, the extracted mesh may have a lot of noise. In this case, it is necessary to remove the noise using Blender before printing the 3D object.
- If you want to know about experimental results and considerations for mesh creation parameters and mesh refinement depending on the data, please check <a href="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/GUIDELINE.md#step5">here</a>!

<a name="step6"></a>
## 6️⃣ Printing and Post-Processing the Figure

### Printing the Figure
<table>
<thead align="center">
  <tr>
    <th>Slicer Software</th>
    <th>Printing in Progress</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/28540b734f3da1462d97e85ab46dcc206ad1ff70/docs/images/slicer_sw.gif" width="480" width="640" height="360"></td>
    <td><img src="https://github.com/ProtossDragoon/PlankHyundong/blob/28540b734f3da1462d97e85ab46dcc206ad1ff70/docs/images/printing_figure.gif" width="270" height="360"></td>
  </tr>
</tbody>
</table>

➕ To learn about the experimental results of the 3D printer options, please check <a href="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/GUIDELINE.md#step6">here</a>!

### Post-Processing the Printed Figure
<table>
<thead align="center">
  <tr>
    <th></th>
    <th>Before</th>
    <th>After</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>Removing Raft</td>
    <td><img width="300" src="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/figure_postprocessing_before.jpg"></td>
    <td><img width="300" src="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/figure_postprocessing_ongoing.jpg"></td>
  </tr>
</tbody>
</table>

<br>

# Environment

- **Google COLAB**
    - All experiments by the PlankHyundong team were conducted on Google COLAB Pro and Google COLAB Pro+.
    - Notebook files of the PlankHyundong team are available on [GitHub](https://github.com/ProtossDragoon/PlankHyundong/tree/main/notebooks), where all dependencies are already defined as scripts for worry-free execution.
- **Weight and Bias ([wandb](https://wandb.ai/))**
- **Local Light Field Fusion ([LLFF](https://github.com/Fyusion/LLFF)), [COLMAP](https://github.com/colmap/colmap)**
- **Tensorflow 1.15**
    - The official [NeRF repository](https://github.com/bmild/nerf) and the [modified NeRF repository](https://github.com/ProtossDragoon/nerf-wandb) with wandb integration both use TensorFlow 1.15.

<table>
<thead align="center">
  <tr>
    <th>Google COLAB</th>
    <th>WandB</th>
    <th>Tensorflow (1.15.x)</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img width="200" src="https://github.com/ProtossDragoon/PlankHyundong/blob/0337fbe609c45dbc6a7fbefdd9ae87408d699468/docs/images/colab.png"></td>
    <td><img width="200" src="https://github.com/ProtossDragoon/PlankHyundong/blob/0337fbe609c45dbc6a7fbefdd9ae87408d699468/docs/images/wandb.png"></td>
    <td><img width="200" src="https://github.com/ProtossDragoon/PlankHyundong/blob/0337fbe609c45dbc6a7fbefdd9ae87408d699468/docs/images/tensorflow.png"></td>
  </tr>
</tbody>
</table>

<table>
<thead align="center">
  <tr>
    <th>Blender</th>
    <th>Sindoh</th>
    <th>3DWOX1/DP203</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img width="200" src="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/logo_blender.png"></td>
    <td><img width="200" src="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/logo_sindoh.png"></td>
    <td><img width="200" src="https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/printer_3DWOX1.png"></td>
  </tr>
</tbody>
</table>

<br>

<a name="team"></a>
# Team

<a name="team"></a>
# Team

- This project follows the [all-contributors specification](https://github.com/all-contributors/all-contributors) and welcomes any contributions!
- [Sejong University Artificial Intelligence Club (SAI)](https://github.com/sju-coml/SAI)
- [Project Kanban](https://www.notion.so/janghoo/21fcf2a58bd0412d98750e92156b728b?v=fb1550801bd94e748c1f13bc2c12c51b)

![logo-color.png](https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/logo_background.png )
