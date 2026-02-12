해당 문서는 gemini-2.5-flash 로 자동 번역되었습니다.<br>정확한 내용은 여기서 확인해주세요: [English Document](https://github.com/seyun4047/drone-platform-client/blob/main/README.md)

---

# 드론 데이터 전송 및 다중 ROI 감지 클라이언트

---
## 저장소 개요
- 이 클라이언트 애플리케이션은 드론에서 텔레메트리 데이터를 수집하여 중앙 서버로 실시간 전송합니다.
- 이 시스템은 드론의 비디오 피드와 화면상의 텔레메트리 데이터를 지속적으로 모니터링할 수 있는 환경에서 작동하도록 설계되었습니다.
- 일반적으로 텔레메트리 정보는 드론 컨트롤러 디스플레이에서 직접 캡처되며, 이곳에 속도 및 기타 비행 데이터가 표시됩니다.

---

## 작동 방식

### 설정
| 1. 서버 연결 | 2. ROI 선택 | 3. 분석 |
|:---:|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/e5336103-6f95-4023-8e5e-401f4d8cf3f1" width="200">|<img src="https://github.com/user-attachments/assets/548a50ed-01da-4236-8501-cd21056c22e1" width="200">|<img src="https://github.com/user-attachments/assets/c9b7026f-c56a-4f4b-a8da-818017d658ca" width="200">|
|승인된 드론 시리얼과 장치 이름을 입력한 후 연결합니다.|원하는 정보를 모니터링할 화면 영역을 선택합니다.|데이터가 감지되면 처리되어 메인 서버로 전송됩니다.|

### 데이터 전송
| 사람 감지 | 이벤트 데이터 전송 |
|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/2c66ff16-f5ff-43eb-b082-97bfa7bc7d7c" width="300">|<img width="300" alt="스크린샷 2026-02-08 22 53 30" src="https://github.com/user-attachments/assets/b4f43752-97c3-4c60-ae6d-424b73721697" />|
|자동으로 사람을 감지합니다.|서버로 이벤트 데이터를 전송합니다.<br>(이 이미지는 클라이언트로부터 서버가 수신한 이벤트 데이터를 나타냅니다.)|

| 텔레메트리 데이터 전송 |
|:---:|
|<img width="300" alt="스크린샷 2026-02-08 22 53 55" src="https://github.com/user-attachments/assets/7356d83b-f2e8-42fd-8b9a-6096556ff142" />|
|아무것도 감지되지 않으면 서버로 텔레메트리 데이터를 전송합니다.<br>(이 이미지는 클라이언트로부터 서버가 수신한 텔레메트리 데이터를 나타냅니다.)|


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
| 카테고리 | 기술 | 버전 | 목적 |
|------------------|---------------------------------|-------------|-------------------------------------|
| 언어 | Python | 3.x | 핵심 애플리케이션 로직 |
| 숫자 OCR | Tesseract (pytesseract) | 0.3.13 | 속도 및 텔레메트리 숫자 추출 |
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
|<img height="1000" alt="Untitled diagram-2026-02-08-201750" src="https://github.com/user-attachments/assets/2d25b82b-3ebd-41e1-b0af-b928de5fdcc8" />|<img height="1000" alt="Untitled diagram-2026-02-08-201847" src="https://github.com/user-attachments/assets/2217b0cb-2b20-4789-b53f-d8443c5c4e76" />|
---
## 주의사항
이 시스템은 드론의 비디오 정보를 실시간으로 모니터링할 수 있는 환경에서 작동해야 합니다.
드론 텔레메트리 데이터는 일반적으로 카메라 드론의 리모컨 화면에서 얻습니다.
화면에는 속도 및 기타 비행 정보가 표시되어야 합니다.
좌표 감지를 위해서는 간단한 GPS 모듈이 부착되어야 하며, 해당 데이터가 실시간으로 감지될 수 있도록 화면에 표시되어야 합니다.


---

# PROJECT OVERVIEW
# Manufacturer-Independent Drone Platform

---
It is a **manufacturer-independent integrated drone monitoring platform.**

It is designed to manage various drones within a single environment,
enabling both **high-end professional drones and commercially available hobby camera drones**
to be used for lifesaving and disaster response.

---

## Project Structure

This platform consists of multiple independent repositories:

| Component | Description                                       | Repository                                                              |
|---------|---------------------------------------------------|-------------------------------------------------------------------------|
| Server | Core drone platform server (API, Auth, Telemetry) | [GitHub](https://github.com/seyun4047/drone-platform-server)            |
| Monitoring Server | Real-time Drone health check monitoring service   | [GitHub](https://github.com/seyun4047/drone-platform-monitoring-server) |
| Drone Data Tester | Test client for drone telemetry & data simulation | [GitHub](https://github.com/seyun4047/drone-platform-trans-tester)       |
| Drone Client | Drone Data Collection, Transmission & Analysis | [GitHub](https://github.com/seyun4047/drone-platform-client)            |
| Docs | Platform Documents | [GitHub](https://github.com/seyun4047/drone-platform-docs)|

---

## Background

Although custom drones, commercial drones, and consumer drones share similar basic control mechanisms,
their operational methods and **command-and-control structures** in real-world environments vary significantly.

In practice, drones are often utilized as tools that depend heavily on:
- Specific equipment
- Highly trained personnel

Recently, many institutions and companies have attempted to build drone systems integrated with AI technologies.  
However, these systems have clear limitations. They typically rely on tuning specific drone models or operating a single type of custom-built drone, which results in strong dependency on specialized personnel and proprietary technologies.

Such dependency is particularly critical in **life-saving and disaster response operations**.

---
## Project Goal
- A manufacturer-independent drone monitoring platform that supports lifesaving and disaster response operations.

---
## Objectives

- A drone monitoring and management system deployable regardless of drone model or manufacturer
- A system that can be immediately deployed in the field without complex control procedures
- A system that does not rely on the performance capabilities of specific drone hardware
- A system that allows non-professional drone hobbyists to contribute effectively in emergency situations

---

## Expected Impact

In life-saving and disaster response scenarios, before professional equipment or rescue teams arrive on site,  
any available drone—if operable by anyone—can be immediately deployed to:
- Assess victims
- Identify hazards
- Estimate damage

By securing this critical **golden time**, the system enables faster decision-making and more effective deployment of advanced rescue resources, ultimately leading to more sophisticated and impactful drone-assisted emergency response systems.

---

## System Architecture

### Overall System Architecture
<img height="900" alt="Untitled diagram-2026-02-11-182634" src="https://github.com/user-attachments/assets/8842dd09-471e-4a75-8804-674f9cff675a" />


---

## Core System Flows

|                                                                           Auth Logic                                                                            |                                          Control Data From Drone                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|  <img width="450" alt="Redis Token Connection Flow-2026-02-01-182619" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />  | <img src="https://github.com/user-attachments/assets/669647c6-ee30-4bfb-baea-d02e306070ea" width="450"/>  |
|                                                   **Redis-based authentication and connection control flow.**                                                   |                    **Processing of control and telemetry data after authentication.**                     |

|                                             Token Validation                                              |                                             Monitoring Server                                             |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" width="450"/>  |<img width="450" alt="Untitled diagram-2026-02-11-173920" src="https://github.com/user-attachments/assets/6eea1ba2-663d-4bf1-be1d-c729e3bda2f7" />|
|                          **Validation of Redis tokens for incoming drone data.**                          |                              **Periodic drone connection state monitoring.**                             |

---
