Korean version: [한국어 문서](https://github.com/seyun4047/drone-platform-client/blob/main/README.kr.md)

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
|<img width="200" alt="connect_to_the_server" src="https://github.com/user-attachments/assets/d15b80d3-28c8-4fd1-aefe-d77681471950" /> |<img width="200" alt="select_roi" src="https://github.com/user-attachments/assets/3c84c375-0ae8-4964-84a5-62a603ef8cde" /> | <img width="200" alt="analysis" src="https://github.com/user-attachments/assets/b39e6ae3-44a2-4e24-93ab-0ca1fdbc4222" /> |
|Enter the authorized drone serial and device name, then connect.|Select the regions on the screen to monitor the desired information.|When data is detected, it is processed and sent to the main server.|

### SEND DATA
| DETECT HUMAN | SEND EVENT DATA |
|:---:|:---:|
|<img alt="detect_human_ex" src="https://github.com/user-attachments/assets/2c66ff16-f5ff-43eb-b082-97bfa7bc7d7c" width="300">|<img width="500" height="83" alt="event_data" src="https://github.com/user-attachments/assets/c5db2f05-a378-4eae-acad-22f84dea28e1" /> |
|Automatically detect human.|Send event data to the server.<br>(The image represents event data received from the client by the server.)|

| SEND TELEMETRY DATA |
|:---:|
|<img  width="500" height="66" alt="telemetry_data" src="https://github.com/user-attachments/assets/bed9bc00-f311-4317-9bef-54cb4e3d6934"/> |
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
|<img height="1000" alt="overall flow" src="https://github.com/user-attachments/assets/187f25db-d82c-415c-9dc3-6aa01c0a374a" />|<img height="1000" alt="aws s3 upload flow" src="https://github.com/user-attachments/assets/0597c7c9-e2e1-4be7-ae5c-de554b0f88ff" />|
---
## Caution
The system must operate in an environment where the drone’s video information can be monitored in real time.
Drone telemetry data is typically obtained from the camera drone’s remote controller screen.
The screen must display speed and other flight information.
For coordinate detection, a simple GPS module should be attached, and its data must be visible on the screen so it can be detected in real time.

---


---

<div align="center">
 
# PROJECT OVERVIEW

  <a href="https://youtu.be/7IdtRp_fe1U" target="_blank">
    <img width="900" src="https://github.com/user-attachments/assets/7bc575a8-27f7-4e64-b04e-1e33d4a7848e" alt="MAIN_DRONE_LOGO"/>
  </a>
   <p><strong>Click & Watch the Introduction Video</strong></p> 

---


It is a **Manufacturer-Independent Drone Monitoring Platform.**

It is designed to manage various drones within a single environment, enabling both **high-end professional drones
<br>and commercially available hobby camera drones**
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
| Dashboard | Drone platform's front-end | [GitHub](https://github.com/seyun4047/drone-platform-dashboard)            |
| Docs | Platform Documents, API's | [GitHub](https://github.com/seyun4047/drone-platform-docs)|



---



## Background

</div>

Although custom drones, commercial drones, and consumer drones share similar basic control mechanisms,
<br>their operational methods and **command-and-control structures** in real-world environments vary significantly.

In practice, drones are often utilized as tools that depend heavily on:
- Specific equipment
- Highly trained personnel

Recently, many institutions and companies have attempted to build drone systems integrated with AI technologies.  
However, these systems have clear limitations.
<br>They typically rely on tuning specific drone models or operating a single type of custom-built drone,
<br>which results in strong dependency on specialized personnel and proprietary technologies.

Such dependency is particularly critical in **life-saving and disaster response operations**.

---

<div align="center">

 ## Project Goal

</div>

- A manufacturer-independent drone monitoring platform that supports lifesaving and disaster response operations.

---

<div align="center">
 
## Objectives

</div>

- A drone monitoring and management system deployable regardless of drone model or manufacturer
- A system that can be immediately deployed in the field without complex control procedures
- A system that does not rely on the performance capabilities of specific drone hardware
- A system that allows non-professional drone hobbyists to contribute effectively in emergency situations

---

<div align="center">

 ## Expected Impact

</div>

In life-saving and disaster response scenarios, before professional equipment<br>
or rescue teams arrive on site, any available drone—if operable by anyone—can be immediately deployed to:
- Assess victims
- Identify hazards
- Estimate damage

By securing this critical **golden time**, the system enables faster decision-making<br>
and more effective deployment of advanced rescue resources, ultimately leading to more sophisticated<br>
and impactful drone-assisted emergency response systems.

---
<div align="center">
 
## System Architecture

### Overall System Architecture

<img width="8192" height="6302" alt="AWS Upload Presigned URL-2026-02-20-144917" src="https://github.com/user-attachments/assets/687f81a5-f03c-4f28-acc3-338f4d78a00a" />

---

## Core System Flows
<details>
  <summary>Click to expand</summary>

|                                                                           Auth Logic                                                                            |                                          Control Data From Drone                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|  <img width="450" alt="Redis Token Connection Flow-2026-02-01-182619" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />  | <img width="450" alt="Redis Token Connection Flow-2026-02-01-182708" src="https://github.com/user-attachments/assets/a344e0c5-b12a-45ab-951c-0cefcc87bf2b" />
 |
|                                                   **Redis-based authentication and connection control flow.**                                                   |                    **Processing of control and telemetry data after authentication.**                     |

|                                             Token Validation                                              |                                             Monitoring Server                                             |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" width="450"/>  |<img width="450" alt="Untitled diagram-2026-02-11-173920" src="https://github.com/user-attachments/assets/6eea1ba2-663d-4bf1-be1d-c729e3bda2f7" />|
|                          **Validation of Redis tokens for incoming drone data.**                          |                              **Periodic drone connection state monitoring.**                             |

| Back-End <-> Front-End |
|:---:|
| <img width="700" alt="AWS Upload Presigned URL-2026-02-13-144904" src="https://github.com/user-attachments/assets/97c1dbf0-3e24-4b4d-8669-65f076a0ffe5" /> |
| **Communication between Back-End Server and Front-End Dashboard** |

</details>

</div>
