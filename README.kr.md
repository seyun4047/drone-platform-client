Original English Document: [https://github.com/seyun4047/drone-platform-client/blob/main/README.md](https://github.com/seyun4047/drone-platform-client/blob/main/README.md)

---

해당 문서는 gemini-2.5-flash-lite 로 자동 번역되어 부자연스러운 부분이 있을 수 있으니,<br>정확한 내용을 여기서 확인해주세요. : [영어 문서](https://github.com/seyun4047/drone-platform-{component}/blob/main/README.md)

---

# 드론 데이터 전송 및 Multi-ROI 감지 클라이언트

---
## 리포지토리 개요
- 이 클라이언트 애플리케이션은 드론에서 텔레메트리 데이터를 수집하여 실시간으로 중앙 서버로 전송합니다.
- 이 시스템은 드론의 영상 피드와 화면상의 텔레메트리 데이터를 지속적으로 모니터링할 수 있는 환경에서 작동하도록 설계되었습니다.
- 일반적으로 텔레메트리 정보는 속도 및 기타 비행 데이터가 표시되는 드론 컨트롤러 디스플레이에서 직접 캡처됩니다.

---

## 작동 방식

### 설정
| 1. 서버 연결 | 2. ROI 선택 | 3. 분석 |
|:---:|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/e5336103-6f95-4023-8e5e-401f4d8cf3f1" width="200">|<img src="https://github.com/user-attachments/assets/548a50ed-01da-4236-8501-cd21056c22e1" width="200">|<img src="https://github.com/user-attachments/assets/c9b7026f-c56a-4f4b-a8da-818017d658ca" width="200">|
|인증된 드론 시리얼 및 장치 이름을 입력한 후 연결합니다.|원하는 정보를 모니터링할 화면 영역을 선택합니다.|데이터가 감지되면 처리되어 메인 서버로 전송됩니다.|

### 데이터 전송
| 사람 감지 | 이벤트 데이터 전송 |
|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/2c66ff16-f5ff-43eb-b082-97bfa7bc7d7c" width="300">|<img width="300" alt="스크린샷 2026-02-08 22 53 30" src="https://github.com/user-attachments/assets/b4f43752-97c3-4c60-ae6d-424b73721697" />|
|사람을 자동으로 감지합니다.|이벤트 데이터를 서버로 전송합니다.<br>(이미지는 서버가 클라이언트로부터 받은 이벤트 데이터를 나타냅니다.)|

| 텔레메트리 데이터 전송 |
|:---:|
|<img width="300" alt="스크린샷 2026-02-08 22 53 55" src="https://github.com/user-attachments/assets/7356d83b-f2e8-42fd-8b9a-6096556ff142" />|
|아무것도 감지되지 않으면 텔레메트리 데이터를 서버로 전송합니다.<br>(이미지는 서버가 클라이언트로부터 받은 텔레메트리 데이터를 나타냅니다.)|


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
| 카테고리         | 기술                      | 버전      | 목적                             |
|------------------|---------------------------------|-------------|-------------------------------------|
| 언어         | Python                          | 3.x         | 핵심 애플리케이션 로직              |
| 숫자 OCR         | Tesseract (pytesseract)         | 0.3.13      | 속도 및 텔레메트리 숫자 추출 |
| 사람 감지 | YOLOv8 (Ultralytics)            | 8.4.12      | 실시간 사람 감지          |
| 컴퓨터 비전  | OpenCV                          | 4.12.0.88   | 이미지 처리                    |
| GUI              | PyQt5                           | 5.15.11     | 데스크톱 인터페이스                   |
| 딥러닝           | PyTorch (torch, torchvision)    | 2.10.0 / 0.25.0 | 모델 추론 엔진          |

---
## 이벤트 처리
영상 피드에서 사람이 감지되면 이벤트가 생성됩니다.
이벤트 데이터는 서버로 전송됩니다.
서버와 클라이언트 모두 이러한 이벤트를 실시간으로 모니터링할 수 있습니다.

---
## 흐름
| 전체 흐름 | AWS S3 업로드 흐름 |
|:---:|:---:|
|<img height="1000" alt="Untitled diagram-2026-02-08-201750" src="https://github.com/user-attachments/assets/2d25b82b-3ebd-41e1-b0af-b928de5fdcc8" />|<img height="1000" alt="Untitled diagram-2026-02-08-201847" src="https://github.com/user-attachments/assets/2217b0cb-2b20-4789-b53f-d8443c5c4e76" />|
---
## 주의 사항
이 시스템은 드론의 비디오 정보를 실시간으로 모니터링할 수 있는 환경에서 작동해야 합니다.
드론 텔레메트리 데이터는 일반적으로 카메라 드론의 리모트 컨트롤러 화면에서 얻습니다.
화면에는 속도 및 기타 비행 정보가 표시되어야 합니다.
좌표 감지를 위해서는 간단한 GPS 모듈이 연결되어야 하며, 해당 데이터는 화면에 표시되어 실시간으로 감지될 수 있어야 합니다.

---