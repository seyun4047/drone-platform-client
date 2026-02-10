
# Manufacturer-Independent Drone Platform

The project aims to be a **manufacturer-independent drone platform**, connecting various drone devices with standardized interfaces and performing **Redis-based authentication and status management**.

---

## Project Structure

This platform consists of multiple independent repositories:

| Component | Description                                       | Repository                                                              |
|---------|---------------------------------------------------|-------------------------------------------------------------------------|
| Server | Core drone platform server (API, Auth, Telemetry) | [GitHub](https://github.com/seyun4047/drone-platform-server)            |
| Monitoring Server | Real-time Drone health check monitoring service   | [GitHub](https://github.com/seyun4047/drone-platform-monitoring-server) |
| Drone Data Tester | Test client for drone telemetry & data simulation | [GitHub](https://github.com/seyun4047/drone-platform-trans-tester)       |
| Drone Client | Drone Data Collection, Transmission & Analysis | [GitHub](https://github.com/seyun4047/drone-platform-client)            |

---

## Overview

This project focuses on building a universal drone control and monitoring platform that can operate independently of drone manufacturers and hardware-specific constraints.

---

## Background

Although custom drones, commercial drones, and consumer drones share similar basic control mechanisms,  
their operational methods and **command and control structures** in real-world environments vary significantly.

In practice, drones are often utilized as tools that depend heavily on:
- Specific equipment
- Highly trained personnel

Recently, many institutions and companies have attempted to build drone systems integrated with AI technologies.  
However, these systems have clear limitations. They typically rely on tuning specific drone models or operating a single type of custom-built drone, which results in strong dependency on specialized personnel and proprietary technologies.

Such dependency is particularly critical in **life-saving and disaster response operations**.

---
## Project Goal
- A manufacturer-independent drone control platform that supports life-saving operations and disaster response.

---
## Objectives

- A drone control and monitoring system deployable regardless of drone model or manufacturer
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
<img src="https://github.com/user-attachments/assets/2693c67c-8110-4f79-86f5-22768663c5ae" width="900"/>

---

## Core System Flows

|                                                                           Auth Logic                                                                            |                                          Control Data From Drone                                          |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|  <img width="450" alt="Redis Token Connection Flow-2026-02-01-182619" src="https://github.com/user-attachments/assets/cf0e6a9e-eeae-4525-aaf1-198c98e61c90" />  | <img src="https://github.com/user-attachments/assets/669647c6-ee30-4bfb-baea-d02e306070ea" width="450"/>  |
|                                                   **Redis-based authentication and connection control flow.**                                                   |                    **Processing of control and telemetry data after authentication.**                     |

|                                             Token Validation                                              |                                             Monitoring Server                                             |
|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
| <img src="https://github.com/user-attachments/assets/456dc993-64a0-4ac8-9138-0f5446aaad07" width="450"/>  | <img src="https://github.com/user-attachments/assets/592adb6b-9066-47ac-8f9d-d5117492a6af" width="450"/>  |
|                          **Validation of Redis tokens for incoming drone data.**                          |                              **Periodic drone connection state monitoring.**                              |

# Drone Data Transmission & Multi-ROI Detection Client

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
| DETECT PERSON | SEND EVENT DATA |
|:---:|:---:|
|<img src="https://github.com/user-attachments/assets/2c66ff16-f5ff-43eb-b082-97bfa7bc7d7c" width="300">|<img width="300" alt="스크린샷 2026-02-08 22 53 30" src="https://github.com/user-attachments/assets/b4f43752-97c3-4c60-ae6d-424b73721697" />|
|Automatically detect person.|Send event data to the server.<br>(The image represents event data received from the client by the server.)|

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
| Person Detection | YOLOv8 (Ultralytics)            | 8.4.12      | Real-time person detection          |
| Computer Vision  | OpenCV                          | 4.12.0.88   | Image processing                    |
| GUI              | PyQt5                           | 5.15.11     | Desktop interface                   |
| Deep Learning    | PyTorch (torch, torchvision)    | 2.10.0 / 0.25.0 | Model inference engine          |

---
## Event Handling
When a person is detected in the video feed, an event is generated.
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
