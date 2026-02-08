"""
Environment-based configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Server Configuration
TELEMETRY_SERVER_URL = os.getenv("TELEMETRY_SERVER_URL", "http://127.0.0.1:8080")

# Default Drone Connection Settings
DEFAULT_SERIAL = os.getenv("DRONE_SERIAL", "drone-serial")
DEFAULT_DEVICE_NAME = os.getenv("DRONE_DEVICE_NAME", "drone-device-name")

# Detection Settings (can be overridden)
DEFAULT_DETECTION_INTERVAL = float(os.getenv("DETECTION_INTERVAL", "1.0"))
MIN_DETECTION_INTERVAL = float(os.getenv("MIN_DETECTION_INTERVAL", "0.1"))

# AWS SETTING
# API Gateway URL
SERVER_URL = os.getenv(
    "SERVER_URL",
    "https://XXX.execute-api.ap-northeast-2.amazonaws.com"
)
SERVER_REGION = os.getenv(
    "SERVER_REGION",
)