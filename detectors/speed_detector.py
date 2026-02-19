import pytesseract
from detectors.base_detector import BaseDetector
import re

class SpeedDetector(BaseDetector):
    """
    Speed measurement detector - recognizes numbers using OCR
    """

    def __init__(self):
        super().__init__(roi_type=0, roi_name='Speed')
        self.last_speed = None

    def process(self):
        image = self.capture_roi()
        if image is None:
            return None

        text = pytesseract.image_to_string(
            image,
            lang='eng',
            config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789.'
        )

        numbers = re.findall(r'\d+\.?\d*', text.strip())

        if numbers:
            try:
                speed = float(numbers[0])
                self.last_speed = speed
            except ValueError:
                speed = self.last_speed
        else:
            speed = self.last_speed

        if speed is not None:
            return {"speed": speed}

        return None

    def _print_result(self, result):
        """Print result"""
        if result and "speed" in result:
            print(f"Current speed: {result['speed']:.2f} km/h")
        else:
            print("Speed could not be recognized")