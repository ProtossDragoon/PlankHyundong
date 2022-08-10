![logo](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0824bc5e-5361-4b1d-a1ea-4c223c52c136/logo-no-background.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T133739Z&X-Amz-Expires=86400&X-Amz-Signature=e7b104cd2f7696708f0f06cc5519d63530543733a790a76679b669fdc9e63aa7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22logo-no-background.svg%22&x-id=GetObject)

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
    - [NeRF 모델로부터 Mesh 만들기](#step5)
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

<a name="start"></a>
# 구성요소별로 시작하기

![파이프라인](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d6e5cc9e-5421-4d50-9973-5d521fa497cd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T121940Z&X-Amz-Expires=86400&X-Amz-Signature=dadc5bc8c5ae90768286a67b86b9e44a15183b5fffc0d56fff4e52a9a30447c7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

<table>
<thead align="center">
  <tr>
    <th>파이프라인 요소</th>
    <th>결과물</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>RGB video</td>
    <td><img src= alt=""></td>
  </tr>
  <tr>
    <td>image and pose</td>
    <td><img src=https://s3.us-west-2.amazonaws.com/secure.notion-static.com/573fa13f-da6a-4111-be17-9cf9e05695ee/wandb_show_pose.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T122452Z&X-Amz-Expires=86400&X-Amz-Signature=9ba9c1d7112eac7bc3a9ddbb6e1e41f844077d9168093ef5e73956721a6cc68f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22wandb_show_pose.gif%22&x-id=GetObject alt=""></td>
  </tr>
  <tr>
    <td>implicit 3d representation</td>
    <td><img src=https://s3.us-west-2.amazonaws.com/secure.notion-static.com/be8757ad-8f7b-4d82-965d-c564617fa84f/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB_%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8_2022-08-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6_58_16_AdobeExpress.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T122558Z&X-Amz-Expires=86400&X-Amz-Signature=7895a683de1348ca8991b5e129b75518f32df021dbbed178a666607a9fce1d7b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2592%25E1%2585%25AA%25E1%2584%2586%25E1%2585%25A7%25E1%2586%25AB_%25E1%2584%2580%25E1%2585%25B5%25E1%2584%2585%25E1%2585%25A9%25E1%2586%25A8_2022-08-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6_58_16_AdobeExpress.gif%22&x-id=GetObject alt=""></td>
  </tr>
  <tr>
    <td>3d representation<br>(mesh 3d model)</td>
    <td><img src=https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fe53287d-bd97-42ca-b21a-85a2812018c2/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB_%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8_2022-08-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6_27_50_AdobeExpress.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T122631Z&X-Amz-Expires=86400&X-Amz-Signature=61bac680552219b22c0dc941935508910b7b74ba4581ac41d3293df75bca6176&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2592%25E1%2585%25AA%25E1%2584%2586%25E1%2585%25A7%25E1%2586%25AB_%25E1%2584%2580%25E1%2585%25B5%25E1%2584%2585%25E1%2585%25A9%25E1%2586%25A8_2022-08-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6_27_50_AdobeExpress.gif%22&x-id=GetObject alt=""></td>
  </tr>
  <tr>
    <td>slicer SW</td>
    <td><img src=https://s3.us-west-2.amazonaws.com/secure.notion-static.com/94e55b44-2fca-49ea-9263-2015a11b9489/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB_%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8_2022-08-09_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8_57_11_AdobeExpress.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T122645Z&X-Amz-Expires=86400&X-Amz-Signature=5a9758ebb457b854c484b45b98a4feafc5fe413579a016e13b864b431994bcaf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2592%25E1%2585%25AA%25E1%2584%2586%25E1%2585%25A7%25E1%2586%25AB_%25E1%2584%2580%25E1%2585%25B5%25E1%2584%2585%25E1%2585%25A9%25E1%2586%25A8_2022-08-09_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_8_57_11_AdobeExpress.gif%22&x-id=GetObject alt=""></td>
  </tr>
  <tr>
    <td>figure</td>
    <td><img src= alt=""></td>
  </tr>
</tbody>
</table>

<a name="step1"></a>
## 피사체 동영상 촬영하기

### 촬영 권장사항

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
    <td align="center"><img src= alt=""></td>
    <td align="center"><img src=https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8591ab68-7922-4885-bfe7-1614ecf8b293/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB_%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8_2022-08-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7_06_02_AdobeExpress.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T123659Z&X-Amz-Expires=86400&X-Amz-Signature=e2d73df4e97c5113f04ca9b87c5ba095655e5ebc47863202e2389c8b311731aa&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2592%25E1%2585%25AA%25E1%2584%2586%25E1%2585%25A7%25E1%2586%25AB_%25E1%2584%2580%25E1%2585%25B5%25E1%2584%2585%25E1%2585%25A9%25E1%2586%25A8_2022-08-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_7_06_02_AdobeExpress.gif%22&x-id=GetObject alt=""></td>
  </tr>
</tbody>
</table>

- ❗ 피사체 주변에는 번들거리는 물체가 없도록 주의 
    - 피사체 주변에 차가 많을 때 결과가 좋지 않음을 확인함
- ❗ 피사체를 제외한 주변의 움직이는 사물이나 그림자 등이 등장하지 않도록 주의 
    - 촬영자의 팔이 나온 데이터를 제거했을 때 성능이 매우 향상됨을 확인함

<a name="step2"></a>
## 비디오로부터 이미지 샘플링하기

촬영한 비디오를 이미지로 등간격 샘플링한다. 플랭크현동 프로젝트에서는 피사체를 두고 360도를 60초만에 회전하며 촬영했다. 이때 100장을 샘플링했다.

**NOTE:** 카메라 트래젝토리가 길다면 더 잘게 잘라 주는 것이 좋다.

`TODO`

<a name="step3"></a>
## 이미지에 대한 카메라 포즈 구하기

NeRF 의 입력은 (이미지, 카메라포즈) 의 집합이다. 커스텀 이미지로부터 이미지 각각에 해당하는 카메라 포즈를 계산하기 위해서는 [COLMAP](https://github.com/colmap/colmap)을 기반으로 동작하는 [LLFF](https://github.com/Fyusion/LLFF) 저자의 스크립트를 사용해야 한다.

`TODO`

<a name="step4"></a>
## NeRF 모델 학습시키기

`TODO` run in colab

### 학습 옵션

<table>
<thead align="center">
  <tr>
    <th>정면 촬영 (Forward Facing)</th>
    <th>360도 촬영</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img src=https://github.com/Fyusion/LLFF/raw/master/imgs/capture.gif alt="source LLFF"></td>
    <td><img src=https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8591ab68-7922-4885-bfe7-1614ecf8b293/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB_%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8_2022-08-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7_06_02_AdobeExpress.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T123659Z&X-Amz-Expires=86400&X-Amz-Signature=e2d73df4e97c5113f04ca9b87c5ba095655e5ebc47863202e2389c8b311731aa&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2592%25E1%2585%25AA%25E1%2584%2586%25E1%2585%25A7%25E1%2586%25AB_%25E1%2584%2580%25E1%2585%25B5%25E1%2584%2585%25E1%2585%25A9%25E1%2586%25A8_2022-08-07_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_7_06_02_AdobeExpress.gif%22&x-id=GetObject alt=""></td>
  </tr>
</tbody>
</table>

|       옵션       |  파라미터 | 역할 |
|:---------------:|:------:|:---:|
| `--wandbproject`                      | wandb 프로젝트명    | 본 프로젝트에서는 필요한 Metric, 평가지표들을 시각화하기 위하여 실험 관리 도구인 wandb를 사용한다.|
| `--wandbentity`                       | wandb 팀 또는 유저명 | 본 프로젝트에서는 필요한 Metric, 평가지표들을 시각화하기 위하여 실험 관리 도구인 wandb를 사용한다.|
| `--no_ndc`, `--spherify`, `--lindisp` |                   | forward facing scene 에서는 필요하지 않지만, 360 scene 에 대해서는 반드시 사용해야 하는 플래그이다.|

<a name="step5"></a>
## NeRF 모델로부터 Mesh 만들기

`TODO` run in colab

NeRF 모델로 학습시킨 implicit representation 을 시각화 하기 위해, 모델 학습 과정에서의 가중치를 이용해 turntable.mp4 영상과 Mesh(.obj)를 생성해내는 과정이다. 학습시킨 모델을 로드한 뒤, PyMCubes 패키지를 통해 표면(iso-surface)을 추출하고, 그 결과물을 저장한다.

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

![wandb_experiment](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dc00483-d4c8-447c-8459-e6f1a5bcf9db/wandb_experiment.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220809T131040Z&X-Amz-Expires=86400&X-Amz-Signature=7fb358ef904c49fa1e3bdc49d49a2b5b764a045706253daa909f76ac047a00e3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22wandb_experiment.gif%22&x-id=GetObject)

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

- **Weight and Bias (wandb)**
    - 실험 관리 도구 [wandb](https://wandb.ai/) 계정을 준비한다.
- **Tensorflow 1.15**
    - [NeRF 공식 저장소](https://github.com/bmild/nerf)와 [NeRF 공식 저장소를 수정하여 wandb 가 자동으로 연결되도록 수정한 저장소](https://github.com/ProtossDragoon/nerf-wandb)는 TensorFlow 1.15 를 사용한다.
- **Google COLAB**
    - 플랭크현동팀의 모든 실험은 Google COLAB Pro, Google COLAB Pro+ 에서 진행되었다.
- Google COLAB 에서 환경에 대한 걱정 없이 실행할 수 있도록 이미 **의존성이 모두 스크립트로 정의**된 [플랭크현동팀의 노트북들](https://github.com/ProtossDragoon/PlankHyundong/tree/main/notebooks)을 실행하기를 권장한다.

<a name="usage"></a>
# 팀

|       학적       |  이름 | 역할 | 이메일 | 블로그 |
|:---------------:|:----:|:---:|:----:|:---:|
| 18, 컴퓨터공      | 이장후 |     |     | |
| 18, 컴퓨터공      | 조용재 |     |     | |
| 18, 지능기계      | 장수명 |     |     | |
| 19, 컴퓨터공      | 이현동 |     |     | |
| 19, 통계, 컴퓨터공 | 이연경 |     |     | |

- [세종대학교 인공지능 동아리 SAI](https://github.com/sju-coml/SAI)
- [프로젝트 칸반](https://www.notion.so/janghoo/21fcf2a58bd0412d98750e92156b728b?v=fb1550801bd94e748c1f13bc2c12c51b)
