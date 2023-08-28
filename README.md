# KNU 실시간 주차 관리 서비스
`Yolov5 모델을 활용한 이미지 기반 실시간 주차 공간 모니터링 시스템` `2023-01 종합설계프로젝트 2`

<img width="412" alt="image" src="https://github.com/meeeeju/KNU-parking-lot-monitoring-service/assets/68631158/9d4b3a85-5687-400a-8ac7-904c08b55318">



## 프로젝트 소개
자동차 등록대수 증가에 비해 주차공간 부족으로 주차 불편을 겪고 있습니다. 이에 따른 불법 주차, 교통 혼잡 등 부가적인 문제들도 발생합니다.  교내 캠퍼스 내에서도 주차 공간 문제가 심각해지고있습니다. 경북대학교 재학생으로서, 본 문제점을 인식하고 주차공간의 효율적인 관리의 필요성을 인지하여 실시간 주차공간 모니터링 시스템을 구현해보았습니다. 

## 프로젝트 목표 
`서버에서 주차장의 빈 주차 공간 유무를 판별`하여 그 결과를 웹 페이지의 형태로 사용자에게 제공하는 것이 본 프로젝트의 주된 목표이자 내용입니다. 
이미지 기반의 주차 공간 인식을 위해 YoloV5 객체 인식 모델을 사용하였고, 이미지 인식 결과 값을 `주차 공간 매핑 알고리즘을 통해 실제 주차 공간에 매핑시킴으로써 주차공간의 빈 공간 유무를 판별`해 주었습니다. 

## 시스템 아키텍처 

<img width="638" alt="image" src="https://github.com/meeeeju/KNU-parking-lot-monitoring-service/assets/68631158/2e19fdf0-98d8-43b6-a657-dad2facb22ad">

<img width="988" alt="image" src="https://github.com/meeeeju/KNU-parking-lot-monitoring-service/assets/68631158/83cb9457-dc4c-4b6b-a71a-2140663304b3">


## 이미지 기반 주차 공간 인식 모델 학습 및 주차 공간 매핑 알고리즘 설계
<img src="https://github.com/meeeeju/KNU-parking-lot-monitoring-service/assets/68631158/384cebba-989c-430a-9b06-585c8ea32b56" width="60%" height="40%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img>
<img width="890" alt="image" src="https://github.com/meeeeju/KNU-parking-lot-monitoring-service/assets/68631158/384cebba-989c-430a-9b06-585c8ea32b56"> <br></br>
- 수집한 경북대학교 교내 주차장 사진(약 500장)과 외부 주차장 사진(약 4500장)을 사용하여 모델 학습을 진행 시켜주었습니다. Yolov5 모델로 학습 시키고 mAP@0.5 기준 최소 0.97 이상을 만족하는 결과를 이용해주었습니다.

<img src="https://github.com/meeeeju/KNU-parking-lot-monitoring-service/assets/68631158/41614de9-48f1-43e7-a943-bada9edb1cb3" width="60%" height="40%" title="px(픽셀) 크기 설정" alt="RubberDuck"></img> <br></br>
- 모델로부터 검출된 결과로 주차 여부를 판단하는 알고리즘은 촬영된 주차 공간 이미지에 따라 다르게 적용해주었습니다. (중심점 매핑 알고리즘과 인접변 우선 알고리즘)

## 서비스 미리보기 

<img width="992" alt="image" src="https://github.com/meeeeju/KNU-parking-lot-monitoring-service/assets/68631158/b0b659cc-1c98-480d-82b0-c49c3abef29c">



### 기대효과 및 한계점
- 이미지 기반의 모니터링을 통해 센서 기반 방식의 모니터링 장비 설치의 어려움 문제 극복했습니다.
- 주차 구역의 모양에 따라 주차공간 매핑 알고리즘을 달리 적용시켜 정확도를 높였습니다.
- 추가적인 알고리즘 설계와 모델 성능을 보완하게되면  시스템 정확성을 확보할 수 있을 것으로 기대됩니다.

### 사용 기술 및 라이브러리



