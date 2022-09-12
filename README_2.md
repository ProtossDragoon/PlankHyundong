![logo](https://raw.githubusercontent.com/ProtossDragoon/PlankHyundong/944c38802cfe392ed6ed194ccca6a083563add45/docs/images/logo.svg)

<br>

<div align="center">

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FProtossDragoon%2FPlankHyundong&count_bg=%23FFA217&title_bg=%2345FFDE&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 

</div>

<br>

# 플랭크 현동 3D
헬스보이 현동이가 알려주는 정확한 플랭크 자세!\
헬창이 되고 싶은 사람들은 **NeRF모델을 이용해 뽑은, 현동이 피규어**를 요리조리 살펴보고 자신과 비교하며 운동해보는건 어떨까? 🏋🏻

<br/>

## 최종 결과물
![image](https://user-images.githubusercontent.com/81481259/189610961-41ba1824-2332-48bd-98f6-45798a8c7c2f.png)
`TODO`: images 파일에 올리고 연결해줘야 함

<br/>

# 목차

- [빠른 시작](#quickstart)
- [구성요소별로 시작하기](#start)
    - [1️⃣ 피사체 동영상 촬영하기](#step1)
    - [2️⃣ 비디오로부터 이미지 샘플링하기](#step2)
    - [3️⃣ 이미지에 대한 카메라 포즈 구하기](#step3)
    - [4️⃣ NeRF 모델 학습시키기](#step4)
    - [5️⃣ NeRF 모델로부터 Mesh 만들고 다듬기](#step5)
    - [6️⃣ 피규어 인쇄하기](#step6)
- [환경](#env)
- [팀](#team)

<br/>

<a name="quickstart"></a>
# 빠른 시작
`TODO`

<a name="start"></a>
# 구성요소별로 시작하기
![파이프라인](https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/pipeline.png )
- 1️⃣ RGB Video: 피사체를 가운데에 두고 촬영자는 360도로 회전하며 영상을 수집한다.
- 2️⃣ N*RGB image: 영상을 샘플링하여 이미지들을 얻는다.
- 3️⃣ N*camera pose: 카메라 포즈는 NeRF 학습에 필요한 것으로, 이전 단계의 샘플링된 이미지로부터 LLFF를 수행함으로써 얻을 수 있다.
- 4️⃣ implicit 3D representation: NeRF 모델을 학습시켜 결과물을 얻어낸다.
- 5️⃣ 3D representation: implicit 3D representation을 시각화하기 위해 Mesh(.obj)를 생성한다.
- 6️⃣ slicer SW: 3D 프린터로 뽑기 전에 슬라이서에서 최적의 파라미터를 세팅한다.
- 6️⃣ figure: 3D 프린터로 최종 결과물을 뽑아낸다.

구체적인 내용은 아래에서 확인할 수 있다.

<br/>

<a name="step1"></a>
## 1️⃣ 피사체 동영상 촬영하기
<table>
<thead align="center">
  <tr>
    <th>권장, 360도 촬영</th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td><img src=https://github.com/ProtossDragoon/PlankHyundong/blob/docs/docs/images/non_forward_facing.gif></td>
  </tr>
  <tr>
    <td>이 프로젝트에서 사용한 방법</td>
  </tr>
</tbody>
</table>
