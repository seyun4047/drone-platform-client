import requests


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

            if not result.get("status"):
                print("Connection failed:", result)
                return False

            self.token = result["token"]
            self.connected = True

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
            print("Telemetry:", res.json())

        except Exception as e:
            print("Telemetry send failed:", e)

    # ------------------------
    # EVENT
    # ------------------------
    def send_event(self, telemetry_data, event_detail):
        if not self.connected:
            return

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
            print("Event:", res.json())

        except Exception as e:
            print("Event send failed:", e)
