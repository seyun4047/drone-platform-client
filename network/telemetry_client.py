import requests
from aws.sts_s3_uploader import DroneS3Uploader

class TelemetryClient:
    """
    Clients for communicating with the main control server
    """
    def __init__(self, client_url, serial, device_name):
        self.client_url = client_url
        self.serial = serial
        self.device_name = device_name

        self.token = None
        self.connected = False

    # ------------------------
    # CONNECT
    # ------------------------
    def connect(self):
        try:
            res = requests.post(
                f"{self.client_url}/auth/connect",
                json={
                    "serial": self.serial,
                    "device_name": self.device_name
                },
                timeout=5
            )
            result = res.json()
            print(result)
            if not result.get("status"):
                print("Connection failed:", result)
                return False

            self.token = result["token"]
            self.connected = True
            self.sts = result["sts"]
            self.uploader = DroneS3Uploader(self.sts)
            print("Connected successfully")
            print("TOKEN:", self.token)
            return True

        except Exception as e:
            print("Connection error:", e)
            return False

    # ------------------------
    # DISCONNECT
    # ------------------------
    def disconnect(self):
        if not self.connected:
            return

        try:
            res = requests.post(
                f"{self.client_url}/auth/disconnect",
                json={
                    "serial": self.serial,
                    "device_name": self.device_name,
                    "token": self.token
                },
                timeout=5
            )
            print("Disconnected:", res.json())

        except Exception as e:
            print("Disconnect failed:", e)

        self.connected = False

    # ------------------------
    # TELEMETRY
    # ------------------------
    def send_telemetry(self, data):
        if not self.connected:
            return

        payload = {
            "event": 0,
            "serial": self.serial,
            "device": self.device_name,
            "token": self.token,
            "data": data
        }

        try:
            res = requests.post(
                f"{self.client_url}/api/telemetry",
                json=payload,
                timeout=5
            )
            if not res.json()["status"]:
                print("RETRY!!!", res)
                self.disconnect()
                self.connect()
            else:
                print("Telemetry:", res.json())

        except Exception as e:
            print("Telemetry send failed:", e)

    # ------------------------
    # EVENT
    # ------------------------
    def send_event(self, telemetry_data, event_detail):
        if not self.connected:
            return
        img_path = event_detail.get("image")
        event_detail["image"] = self.uploader.upload_image_path(self.serial, img_path)
        payload = {
            "event": 1,
            "serial": self.serial,
            "device": self.device_name,
            "token": self.token,
            "data": {
                **telemetry_data,
                "event_detail": event_detail
            }
        }

        try:
            res = requests.post(
                f"{self.client_url}/api/telemetry",
                json=payload,
                timeout=5
            )
            if not res.json()["status"]:
                print("RETRY!!!", res)
                self.disconnect()
                self.connect()
            else:
                print("Event:", res.json())

        except Exception as e:
            print("Event send failed:", e)
