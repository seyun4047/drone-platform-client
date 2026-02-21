해당 문서는 gemini-2.5-flash 로 자동 번역되었습니다.<br>정확한 내용은 여기서 확인해주세요: [English Document](https://github.com/seyun4047/drone-platform-client/blob/main/README.md)

---

# 드론 데이터 전송 및 다중 ROI 감지 클라이언트

---
## 저장소 개요
- 이 클라이언트 애플리케이션은 드론에서 원격 측정 데이터를 수집하여 중앙 서버로 실시간 전송합니다.
- 이 시스템은 드론의 비디오 피드 및 화면 상의 원격 측정 데이터를 지속적으로 모니터링할 수 있는 환경에서 작동하도록 설계되었습니다.
- 일반적으로 원격 측정 정보는 속도 및 기타 비행 데이터가 표시되는 드론 컨트롤러 디스플레이에서 직접 캡처됩니다.

---

## 작동 방식

### 설정
| 1. 서버 연결 | 2. ROI 선택 | 3. 분석 |
|:---:|:---:|:---:|
|<img width="200" alt="connect_to_the_server" src="https://github.com/user-attachments/assets/d15b80d3-28c8-4fd1-aefe-d77681471950" /> |<img width="200" alt="select_roi" src="https://github.com/user-attachments/assets/3c84c375-0ae8-4964-84a5-62a603ef8cde" /> | <img width="200" alt="analysis" src="https://github.com/user-attachments/assets/b39e6ae3-44a2-4e24-93ab-0ca1fdbc4222" /> |
|승인된 드론 시리얼과 장치 이름을 입력한 후 연결합니다.|원하는 정보를 모니터링할 화면 영역을 선택합니다.|데이터가 감지되면 처리되어 메인 서버로 전송됩니다.|

### 데이터 전송
| 사람 감지 | 이벤트 데이터 전송 |
|:---:|:---:|
|<img alt="detect_human_ex" src="https://github.com/user-attachments/assets/2c66ff16-f5ff-43eb-b082-97bfa7bc7d7c" width="300">|<img width="500" height="83" alt="event_data" src="https://github.com/user-attachments/assets/c5db2f05-a378-4eae-acad-22f84dea28e1" /> |
|자동으로 사람을 감지합니다.|이벤트 데이터를 서버로 전송합니다.<br>(이 이미지는 클라이언트로부터 서버가 수신한 이벤트 데이터를 나타냅니다.)|

| 원격 측정 데이터 전송 |
|:---:|
|<img  width="500" height="66" alt="telemetry_data" src="https://github.com/user-attachments/assets/bed9bc00-f311-4313-9bef-54cb4e3d6934"/> |
|아무것도 감지되지 않으면 원격 측정 데이터를 서버로 전송합니다.<br>(이 이미지는 클라이언트로부터 서버가 수신한 원격 측정 데이터를 나타냅니다.)|


---
## 설치
필요한 종속성을 설치합니다:
```bash
pip install -r requirements.txt
```
---
## 사용법
애플리케이션을 실행합니다:
```bash
python3 main.py
```
---
## 스택
| 범주 | 기술 | 버전 | 목적 |
|------------------|---------------------------------|-------------|-------------------------------------|
| 언어 | Python | 3.x | 핵심 애플리케이션 로직 |
| 숫자 OCR | Tesseract (pytesseract) | 0.3.13 | 속도 및 원격 측정 숫자 추출 |
| 사람 감지 | YOLOv8 (Ultralytics) | 8.4.12 | 실시간 사람 감지 |
| 컴퓨터 비전 | OpenCV | 4.12.0.88 | 이미지 처리 |
| GUI | PyQt5 | 5.15.11 | 데스크톱 인터페이스 |
| 딥러닝 | PyTorch (torch, torchvision) | 2.10.0 / 0.25.0 | 모델 추론 엔진 |

---
## 이벤트 처리
비디오 피드에서 사람이 감지되면 이벤트가 생성됩니다.
이벤트 데이터는 서버로 전송됩니다.
서버와 클라이언트 모두 이러한 이벤트를 실시간으로 모니터링할 수 있습니다.

---
## 흐름
| 전체 흐름 | AWS S3 업로드 흐름 |
|:---:|:---:|
|<img height="1000" alt="Overall flow" src="https://github.com/user-attachments/assets/8e1de094-ba4e-4340-bc16-c5660f0cc688" />|<img height="1000" alt="aws s3 upload flow" src="https://github.com/user-attachments/assets/0597c7c9-e2e1-4be7-ae5c-de554b0f88ff" />|
---
## 주의사항
이 시스템은 드론의 비디오 정보를 실시간으로 모니터링할 수 있는 환경에서 작동해야 합니다.
드론 원격 측정 데이터는 일반적으로 카메라 드론의 원격 조종기 화면에서 얻습니다.
화면에는 속도 및 기타 비행 정보가 표시되어야 합니다.
좌표 감지를 위해서는 간단한 GPS 모듈을 부착해야 하며, 해당 데이터는 실시간으로 감지할 수 있도록 화면에 표시되어야 합니다.

---

<div align="center">
 
# 프로젝트 개요

  <a href="https://youtu.be/7IdtRp_fe1U" target="_blank">
    <img width="900" src="https://github.com/user-attachments/assets/7bc575a8-27f7-4e64-b04e-1e33d4a7848e" alt="MAIN_DRONE_LOGO"/>
  </a>
   <p><strong>소개 영상 클릭 및 시청</strong></p> 

---


이것은 **제조사 독립적인 드론 모니터링 플랫폼**입니다.

단일 환경에서 다양한 드론을 관리하도록 설계되어, **고급 전문가용 드론<br>부터 시판되는 취미용 카메라 드론까지** 모두 인명 구조 및 재난 대응에 활용될 수 있습니다.



---

## 프로젝트 구조

이 플랫폼은 여러 독립적인 저장소로 구성됩니다:

| 구성 요소 | 설명                                       | 저장소                                                              |
|---------|---------------------------------------------------|-------------------------------------------------------------------------|
| 서버 | 핵심 드론 플랫폼 서버 (API, 인증, 텔레메트리) | [GitHub](https://github.com/seyun4047/drone-platform-server)            |
| 모니터링 서버 | 실시간 드론 상태 확인 모니터링 서비스   | [GitHub](https://github.com/seyun4047/drone-platform-monitoring-server) |
| 드론 데이터 테스터 | 드론 텔레메트리 및 데이터 시뮬레이션 테스트 클라이언트 | [GitHub](https://github.com/seyun4047/drone-platform-trans-tester)       |
| 드론 클라이언트 | 드론 데이터 수집, 전송 및 분석 | [GitHub](https://github.com/seyun4047/drone-platform-client)            |
| 대시보드 | 드론 플랫폼 프론트엔드 | [GitHub](https://github.com/seyun4047/drone-platform-dashboard)            |
| 문서 | 플랫폼 문서, API | [GitHub](https://github.com/seyun4047/drone-platform-docs)|



---



## 배경

</div>

맞춤형 드론, 상업용 드론, 소비자용 드론은 기본적인 제어 메커니즘을 공유하지만,<br>실제 환경에서의 운용 방식과 **명령 및 제어 구조**는 크게 다릅니다.

실제로 드론은 다음과 같은 요소에 크게 의존하는 도구로 활용됩니다:
- 특정 장비
- 고도로 훈련된 인력

최근 많은 기관과 기업들이 AI 기술과 통합된 드론 시스템을 구축하려 시도했습니다. <br>그러나 이러한 시스템에는 명확한 한계가 있습니다.<br>일반적으로 특정 드론 모델을 튜닝하거나 단일 유형의 맞춤 제작 드론을 운용하는 방식에 의존하여,<br>전문 인력과 독점 기술에 대한 의존성이 강합니다.

이러한 의존성은 특히 **인명 구조 및 재난 대응 작전**에서 매우 중요합니다.

---

<div align="center">

 ## 프로젝트 목표

</div>

- 인명 구조 및 재난 대응 작전을 지원하는 제조사 독립적인 드론 모니터링 플랫폼.

---

<div align="center">
 
## 목표

</div>

- 드론 모델이나 제조사에 관계없이 배포 가능한 드론 모니터링 및 관리 시스템
- 복잡한 제어 절차 없이 현장에 즉시 배포할 수 있는 시스템
- 특정 드론 하드웨어의 성능 기능에 의존하지 않는 시스템
- 비전문 드론 취미 사용자도 비상 상황에서 효과적으로 기여할 수 있도록 하는 시스템

---

<div align="center">

 ## 예상되는 영향

</div>

인명 구조 및 재난 대응 시나리오에서, 전문 장비<br>또는 구조팀이 현장에 도착하기 전에, 누구든 조작할 수 있는 모든 가용한 드론은 즉시 다음을 위해 배포될 수 있습니다:
- 희생자 파악
- 위험 요소 식별
- 피해 규모 추정

이 중요한 **골든 타임**을 확보함으로써, 시스템은 더 빠른 의사 결정<br>과 고급 구조 자원의 더 효과적인 배포를 가능하게 하여, 궁극적으로 더 정교하고<br>영향력 있는 드론 지원 비상 대응 시스템으로 이어집니다.

---
<div align="center">
 
## 시스템 아키텍처

### 전체 시스템 아키텍처

<img width="8192" height="6302" alt="AWS Upload Presigned URL-2026-02-20-144917" src="https://github.com/user-attachments/assets/687f81a5-f03c-4f28-acc3-338f4d78a00a" />

---

## 핵심 시스템 흐름
<details>
  <summary>클릭하여 확장</summary>

|                                                                           인증 로직                                                                            |                                          드론으로부터의 제어 데이터                                          |                                           드론 토큰 유효성 검사                                              |                                             모니터링 서버                                             |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|  <img width="450" alt="Auth logic flow" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />  |<img width="450" alt="Control data flow" src="https://github.com/user-attachments/assets/f8c4acf7-0cbe-4ca3-b7fe-6aee4f3e854c" /> | <img alr="Token validation flow" src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" width="450"/>  |<img width="450" alt="Monitoring server flow" src="https://github.com/user-attachments/assets/6eea1ba2-663d-4bf1-be1d-c729e3bda2f7" />|
|                                                   **Redis 기반 인증 및 연결 제어 흐름.**                                                   |                    **인증 후 제어 및 텔레메트리 데이터 처리.**                     |                         **수신 드론 데이터에 대한 Redis 토큰 유효성 검사.**                          |                              **주기적인 드론 연결 상태 모니터링.**                             |

| 백엔드 <-> 프론트엔드 |
|:---:|
| <img width="700" alt="AWS Upload Presigned URL-2026-02-13-144904" src="https://github.com/user-attachments/assets/97c1dbf0-3e24-4b4d-8669-65f076a0ffe5" /> |
| **백엔드 서버와 프론트엔드 대시보드 간 통신** |

</details>

</div>