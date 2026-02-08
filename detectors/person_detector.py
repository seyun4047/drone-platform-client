import os
import cv2
import numpy as np
from datetime import datetime
from aws.presigned_upload_client import PresignedUploadClient
from detectors.base_detector import BaseDetector
from ultralytics import YOLO
from config.env_config import SERVER_URL

class PersonDetector(BaseDetector):
    """
    Person detection and logging
    """
    def __init__(self):
        super().__init__(roi_type=3, roi_name='Person Detection')
        self.detected_count = 0

        # YOLOv8 model
        self.model = YOLO('yolov8n.pt')

        # Detect only person class
        self.target_class = 0
        self.conf_threshold = 0.5

        # Log directory
        os.makedirs("log/pic", exist_ok=True)

        # Presigned upload client
        self.upload_client = PresignedUploadClient(SERVER_URL)

    def process(self):
        image = self.capture_roi()
        if image is None:
            return None

        # Convert PIL → OpenCV
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # YOLO inference
        results = self.model(
            frame,
            conf=self.conf_threshold,
            classes=[self.target_class],
            verbose=False
        )

        person = []

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                x, y, w, h = int(x1), int(y1), int(x2 - x1), int(y2 - y1)

                conf = float(box.conf[0])
                person.append((x, y, w, h, conf))

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f'{conf:.2f}',
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

        count = len(person)
        image_path = None
        s3_url = None

        if count > 0:
            image_path = self._save_event(frame, person)
            s3_url = self.upload_client.upload_file(image_path)

        return {
            "person_count": count,
            "image_path": image_path,
            "s3_url": s3_url
        }

    def _save_event(self, frame, person):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        img_path = f"log/pic/person_{timestamp}.jpg"
        log_path = "log/person_log.txt"

        cv2.imwrite(img_path, frame)

        with open(log_path, "a") as f:
            f.write(f"[{timestamp}] detected {len(person)} person: {person}\n")

        return img_path

    def _print_result(self, result):
        if result and "person_count" in result:
            print(f"detected: {result['person_count']} person")
        else:
            print("READY TO DETECT PERSON")
