import pytesseract
from detectors.base_detector import BaseDetector
import re

class PowerDetector(BaseDetector):


    """
    Power measurement detector - recognizes numbers using OCR
    """

    def __init__(self):
        super().__init__(roi_type=4, roi_name='Longitude')
        self.last_longitude = None

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
                power = int(numbers[0])
                self.last_power = power
            except ValueError:
                power = self.last_power
        else:
            power = self.last_power

        if power is not None:
            return {"power": power}

        return None

    def _print_result(self, result):
        """Print result"""
        if result is not None:
            print(f"Current Power: {result['power']:}")
        else:
            print("Power could not be recognized")
