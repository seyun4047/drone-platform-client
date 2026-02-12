해당 문서는 gemini-2.5-flash 로 자동 번역되었습니다.<br>정확한 내용은 여기서 확인해주세요: [English Document](https://github.com/seyun4047/drone-platform-client/blob/main/README.md)

---

# Drone Data Transmission & Multi-ROI Detection Client

---
## Repository Overview
- This client application collects telemetry data from a drone and transmits it to a central server in real time.
- The system is designed to operate in an environment where the drone’s video feed and on-screen telemetry data can be continuously monitored.
- Typically, telemetry information is captured directly from the drone controller’s display, where speed and other flight data are shown.

---

## How It Works

### SETUP
| 1. CONNECT TO THE SERVER | 2. SELECT ROI | 3. ANALYSIS |
|:---:|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/e5336103-6f95-4023-8e5e-401f4d8cf3f1" width="200">|<img src="https://github.com/user-attachments/assets/548a50ed-01da-4236-8501-cd21056c22e1" width="200">|<img src="https://github.com/user-attachments/assets/c9b7026f-c56a-4f4b-a8da-818017d658ca" width="200">|
|Enter the authorized drone serial and device name, then connect.|Select the regions on the screen to monitor the desired information.|When data is detected, it is processed and sent to the main server.|

### SEND DATA
| DETECT HUMAN | SEND EVENT DATA |
|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/2c66ff16-f5ff-43eb-b082-97bfa7bc7d7c" width="300">|<img width="300" alt="스크린샷 2026-02-08 22 53 30" src="https://github.com/user-attachments/assets/b4f43752-97c3-4c60-ae6d-424b73721697" />|
|Automatically detect human.|Send event data to the server.<br>(The image represents event data received from the client by the server.)|

| SEND TELEMETRY DATA |
|:---:|
|<img width="300" alt="스크린샷 2026-02-08 22 53 55" src="https://github.com/user-attachments/assets/7356d83b-f2e8-42fd-8b9a-6096556ff142" />|
|If nothing is detected, send telemetry data to the server.<br>(The image represents telemetry data received from the client by the server.)|


---
## Installation
Install the required dependencies:
```bash
pip install -r requirements.txt
```
---
## Usage
Run the application:
```bash
python3 main.py
```
---
## Stack
| Category         | Technology                      | Version      | Purpose                             |
|------------------|---------------------------------|-------------|-------------------------------------|
| Language         | Python                          | 3.x         | Core application logic              |
| Numeric OCR      | Tesseract (pytesseract)         | 0.3.13      | Extract speed and telemetry numbers |
| Human Detection | YOLOv8 (Ultralytics)            | 8.4.12      | Real-time human detection          |
| Computer Vision  | OpenCV                          | 4.12.0.88   | Image processing                    |
| GUI              | PyQt5                           | 5.15.11     | Desktop interface                   |
| Deep Learning    | PyTorch (torch, torchvision)    | 2.10.0 / 0.25.0 | Model inference engine          |

---
## Event Handling
When a human is detected in the video feed, an event is generated.
The event data is transmitted to the server.
Both the server and the client can monitor these events in real time.

---
## FLOW
| OVERALL FLOW | AWS S3 UPLOAD FLOW |
|:---:|:---:|
|<img height="1000" alt="Untitled diagram-2026-02-08-201750" src="https://github.com/user-attachments/assets/2d25b82b-3ebd-41e1-b0af-b928de5fdcc8" />|<img height="1000" alt="Untitled diagram-2026-02-08-201847" src="https://github.com/user-attachments/assets/2217b0cb-2b20-4789-b53f-d8443c5c4e76" />|
---
## Caution
The system must operate in an environment where the drone’s video information can be monitored in real time.
Drone telemetry data is typically obtained from the camera drone’s remote controller screen.
The screen must display speed and other flight information.
For coordinate detection, a simple GPS module should be attached, and its data must be visible on the screen so it can be detected in real time.

---

---

