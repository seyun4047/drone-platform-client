"""
Detection Manager - Handles detection execution and telemetry
"""


class DetectionManager:
    """Manages detection process and telemetry communication"""

    def __init__(self, roi_manager, telemetry_client=None):
        self.roi_manager = roi_manager
        self.telemetry_client = telemetry_client

    def set_telemetry_client(self, client):
        """Set telemetry client"""
        self.telemetry_client = client

    def perform_detection(self):
        """Execute detection on all active detectors and send telemetry"""
        telemetry_data = {}
        event_triggered = False
        event_detail = None

        for detector in self.roi_manager.get_all_detectors().values():
            if not detector.is_active:
                continue

            result_dict = detector.run()
            detector.format_output(result_dict)

            if result_dict is None:
                continue

            data = result_dict.get("result")

            if not data:
                continue

            # Handle person detection separately (triggers event)
            if "person_count" in data:
                count = int(data.get("person_count", 0))
                telemetry_data["person_count"] = count

                if count > 0:
                    event_triggered = True
                    event_detail = {
                        "message": "human detected",
                        # "positions": data.get("positions", []),
                        "image": data.get("image_path")
                    }
                continue

            # Add other telemetry data
            telemetry_data.update(data)

        # Send telemetry to server
        if not telemetry_data:
            return

        if self.telemetry_client is None:
            print("Telemetry not connected. Skipping send.")
            return

        if event_triggered:
            print("[EVENT TRIGGERED] sending event")
            self.telemetry_client.send_event(telemetry_data, event_detail)
        else:
            print("[TELEMETRY] sending normal telemetry")
            self.telemetry_client.send_telemetry(telemetry_data)