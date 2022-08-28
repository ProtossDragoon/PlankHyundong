![logo](https://raw.githubusercontent.com/ProtossDragoon/PlankHyundong/944c38802cfe392ed6ed194ccca6a083563add45/docs/images/logo.svg)

<br>

<div align="center">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FProtossDragoon%2FPlankHyundong&count_bg=%23FFA217&title_bg=%2345FFDE&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 

</div>

<br>

# 플랭크 현동 3D

현동이가 플랭크를 흔들림 없이 버텨줄수록 프로젝트 난이도는 낮아지고, 현동이의 플랭크가 흔들흔들 불안정할수록 프로젝트 난이도가 매우 높아지는 "tradeoff" 상황에 놓이게 되는데... 헬스보이 현동이가 알려주는 정확한 플랭크 자세! **헬창이 되고 싶은 사람들은 그의 자세를 360도로 요리조리 살펴보고 자신과 비교해보면서 운동해보는건 어떨까?** 🏋🏻

## 최종 결과물

<table>
<thead align="center">
  <tr>
    <th>시각화</th>
    <th>최초 데이터셋</th>
    <th>노이즈 제거</th>
    <th>누끼 제거</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>RGB</td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result.gif alt="" width="200" height="200"></td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_2.gif alt="" width="200" height="200"></td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_3.gif alt="" width="200" height="200"></td>
  </tr>
  <tr>
    <td>disparity</td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_80_64_1.gif alt="" width="200" height="200"></td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_80_64_2.gif alt="" width="200" height="200"></td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_80_64_3.gif alt="" width="200" height="200"></td>
  </tr>
  <tr>
    <td>3D figure</td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_160_64_32_1b-30.gif alt="" width="200" height="200"></td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_160_64_32_1b-10.gif alt="" width="200" height="200"></td>
    <td><img src=https://github.com/ProtossDragoon/NeRF-TF2-Keras/blob/master/docs/result_160_64_32_1b_10.gif alt="" width="200" height="200"></td>
  </tr>
</tbody>
</table>

- 모든 실험 내역들을 [wandb 프로젝트](https://wandb.ai/plank-hyundong/plank-hyundong)에서 확인할 수 있습니다.

# 목차

- [빠른 시작](#quickstart)
- [구성요소별로 시작하기](#start)
    - [피사체 동영상 촬영하기](#step1)
    - [비디오로부터 이미지 샘플링하기](#step2)
    - [이미지에 대한 카메라 포즈 구하기](#step3)
    - [NeRF 모델 학습시키기](#step4)
    - [NeRF 모델로부터 Mesh 만들고 다듬기](#step5)
    - [피규어 인쇄하기](#step6)
    - [인쇄된 피규어 후가공하기](#step7)
- [실험 및 평가](#experiment)
    - [데이터셋 및 NeRF 모델 파라미터 실험](#dataandnerf)
    - [Mesh Renderer 파라미터 실험](#renderer)
    - [3D 프린터 옵션 실험](#printer)
- [개발 환경](#devenv)
- [팀](#team)

<a name="quickstart"></a>
# 빠른 시작

`TODO`

<a name="start"></a>
# 구성요소별로 시작하기

![파이프라인](https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/pipeline.png )

<table style="table-layout: fixed; width: 100%;">
<thead align="center" >
  <tr>
    <th>step</th>
    <th>1️⃣</th>
    <th>2️⃣</th>
    <th>3️⃣</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>output</td>
    <td>RGB 비디오</td>
    <td>이미지와 포즈</td>
    <td>뉴럴넷 기반 3d 표현</td>
  </tr>
  </tr>
    <td></td>
    <td><img width="230" src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/non_forward_facing.gif></td>
    <td><img width="230" src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/wandb_show_pose.gif></td>
    <td><img width="230" src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/wandb_visualize_implicit_representation.gif></td>
  </tr>
</tbody>
</table>

<table style="table-layout: fixed; width: 100%;">
<thead align="center">
  </tr>
    <th>step</th>
    <th>4️⃣</th>
    <th>5️⃣</th>
    <th>6️⃣</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>output</td>
    <td>메쉬가 적용된 3d 표현</td>
    <td>슬라이서 소프트웨어</td>
    <td>결과물 피규어</td>
  </tr>
  <tr>
    <td></td>
    <td><img width="230" src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/meshed_representation.gif></td>
    <td><img width="230" src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/slicer_sw.gif></td>
    <td><img width="230" src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/result_1.png></td>
  </tr>
</tbody>
</table>

<a name="step1"></a>
## 피사체 동영상 촬영하기

### 촬영 권장사항

<table>
<thead align="center">
  <tr>
    <th>권장, 360도 촬영</th>
    <th>정면촬영 (Forward Facing)</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/non_forward_facing.gif></td>
    <td><img src=https://github.com/Fyusion/LLFF/raw/master/imgs/capture.gif></td>
  </tr>
  <tr>
    <td>이 프로젝트에서 사용한 방법</td>
    <td>모델 학습은 가능하지만 피규어를 제작할 수 없음. 동영상 출처: <a href="https://github.com/Fyusion/LLFF">Google LLFF</a></td>
  </tr>
</tbody>
</table>

- ✅ 충분한 조명을 확보하여 충분히 짧은 셔터 속도를 사용할 수 있도록 준비
- ✅ 피사체를 가운데에 두고 촬영자는 360도로 돌면서 촬영
- ✅ 다양한 각도를 수집하기 위해 위 아래로 S자를 만들면서 촬영
- ✅ 각 각도에 대한 이미지를 동일하게 수집하기 위해 일정한 속도로 돌며 촬영
- ✅ 정적인 물체에 최적화된 NeRF 특성을 고려하여 피사체는 움직임을 최소화

### 촬영 주의사항

<table>
<thead align="center">
  <tr>
    <th>번들거리는 물체가 등장</th>
    <th>움직이는 신체가 등장</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align="center"><img src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/worse_practice_1.jpeg alt=""></td>
    <td align="center"><img src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/worse_practice_2.png alt=""></td>
  </tr>
</tbody>
</table>

- ❗ 피사체 주변에는 번들거리는 물체가 없도록 주의 
    - 실험을 통해 피사체 주변에 차가 많을 때 결과가 좋지 않음을 확인했습니다.
- ❗ 피사체를 제외한 주변의 움직이는 사물이나 그림자 등이 등장하지 않도록 주의 
    - 실험을 통해 촬영자의 팔이 나온 데이터를 제거했을 때 성능이 매우 향상됨을 확인했습니다.

<a name="step2"></a>
## 비디오로부터 이미지 샘플링하기

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/sampling_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

|   파라미터    |  설명  |
|:-----------:|:--------------:|
| `dir_path`  | 비디오 파일의 경로 |
| `frame`     | 비디오로부터 샘플링되는 이미지의 개수 |

스크립트를 이용하여 촬영한 비디오를 이미지로 등간격 샘플링합니다.

- ✅ 카메라 트래젝토리가 길다면 더 잘게 잘라 주는 것이 좋습니다.
- ❗ 카메라 트래젝토리가 짧고 렌즈를 열어두는 시간이 짧은 경우, 동영상으로부터 이미지를 너무 잘게 샘플링한다면 성능에 악영향을 미칠 수 있습니다.

<a name="step3"></a>
## 이미지에 대한 카메라 포즈 구하기

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/colmap_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

**NOTE:** 반드시 GPU 런타임을 사용해야 합니다.

NeRF 의 입력은 (이미지, 카메라포즈) 의 집합입니다. 커스텀 이미지로부터 이미지 각각에 해당하는 카메라 포즈를 계산하기 위해 [COLMAP](https://github.com/colmap/colmap)을 기반으로 동작하는 [LLFF](https://github.com/Fyusion/LLFF) 저자의 스크립트를 사용합니다. 하지만 LLFF 스크립트를 구동할 수 있는 환경을 구축하는 일은 꽤 까다롭습니다. 이러한 문제를 피하기 위해 [플랭크현동이 제공하는 노트북]()을 사용하세요. COLAB 클라우드 컴퓨터에서 모든 연산이 이루어집니다. 실행이 완료되면 데이터셋 폴더 안에 NeRF 모델을 실행시키는 데 필요한 `poses_bounds.npy` 파일이 생성됩니다.

<a name="step4"></a>
## NeRF 모델 학습시키기

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/nerf_wandb_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

**NOTE:** 반드시 GPU 런타임을 사용해야 합니다.

### 학습 옵션

|       옵션       |  파라미터 | 역할 |
|:---------------:|:------:|:---:|
| `--wandbproject`                      | wandb 프로젝트명      | 본 프로젝트에서는 필요한 Metric, 평가지표들을 시각화하기 위하여 실험 관리 도구인 wandb를 사용합니다.|
| `--wandbentity`                       | wandb 팀명 또는 유저명 | 본 프로젝트에서는 필요한 Metric, 평가지표들을 시각화하기 위하여 실험 관리 도구인 wandb를 사용합니다.|
| `--no_ndc`, `--spherify`, `--lindisp` |                    | forward facing scene 에서는 필요하지 않지만, 360 scene 에 대해서는 반드시 사용해야 하는 플래그입니다.|

<a name="step5"></a>
## NeRF 모델로부터 Mesh 만들고 다듬기

<p style="text-align:center;">
<a href="https://colab.research.google.com/github/ProtossDragoon/PlankHyundong/blob/main/notebooks/extract_mesh_colab.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></p>

**NOTE:** 반드시 GPU 런타임을 사용해야 합니다.

NeRF 모델로 학습시킨 implicit representation 을 시각화 하기 위해, 모델 학습 과정에서의 가중치를 이용해 turntable.mp4 영상과 Mesh(.obj)를 생성해내는 과정이다. 학습시킨 모델을 로드한 뒤, PyMCubes 패키지를 통해 표면(iso-surface)을 추출하고, 그 결과물을 저장한다.

<table>
<thead align="center">
  <tr>
    <th></th>
    <th>문제</th>
    <th>해결</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>제거</td>
    <td><img src="" alt=""></td>
    <td><img src="" alt=""></td>
  </tr>
  <tr>
    <td>생성</td>
    <td><img src="" alt=""></td>
    <td><img src="" alt=""></td>
  </tr>
</tbody>
</table>

이때 그 결과물의 상태가 좋지 않을 가능성이 높다. 

<a name="step6"></a>
## 피규어 인쇄하기

`TODO`

<a name="step7"></a>
## 인쇄된 피규어 후가공하기

`TODO`

<a name="experiment"></a>
# 실험 및 평가

<a name="dataandnerf"></a>
## 데이터셋 및 NeRF 모델 파라미터 실험

![wandb_experiment](https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/wandb_experiment.gif )

- 다양한 시행착오들과 인사이트는 [wandb 리포트](https://wandb.ai/plank-hyundong/plank-hyundong/reports/Hyperparameter-Experiment-Ablation-Study--VmlldzoyNDAzMDYz)에서 모두 확인할 수 있다.

<a name="renderer"></a>
## Mesh Renderer 파라미터 실험

`TODO`

<a name="printer"></a>
## 3D 프린터 옵션 실험

- 가장 중요한 옵션들은 레이어 높이, 노즐 두께, 출력 속도이다.
- 각각에 따라 결과물의 디테일이 달라진다.
- 목록을 리스트업하여 메이커에게 전달했다.

<a name="devenv"></a>
# 개발 환경

- **Weight and Bias ([wandb](https://wandb.ai/))**
- **Tensorflow 1.15**
    - [NeRF 공식 저장소](https://github.com/bmild/nerf)와 [NeRF 공식 저장소를 수정하여 wandb 가 자동으로 연결되도록 수정한 저장소](https://github.com/ProtossDragoon/nerf-wandb)는 TensorFlow 1.15 를 사용합니다.
- **Google COLAB**
    - 플랭크현동팀의 모든 실험은 Google COLAB Pro, Google COLAB Pro+ 에서 진행되었습니다.
    - 환경에 대한 걱정 없이 실행할 수 있도록 이미 **의존성이 모두 스크립트로 정의**되어 있는 [플랭크현동팀의 노트북들](https://github.com/ProtossDragoon/PlankHyundong/tree/main/notebooks)이 준비되어 있습니다.

<a name="usage"></a>
# 팀

- [세종대학교 인공지능 동아리 SAI](https://github.com/sju-coml/SAI)
- [프로젝트 칸반](https://www.notion.so/janghoo/21fcf2a58bd0412d98750e92156b728b?v=fb1550801bd94e748c1f13bc2c12c51b)

![logo-color.png](https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/logo_background.png )