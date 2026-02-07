import pytesseract
from detectors.base_detector import BaseDetector
import re

class LatitudeDetector(BaseDetector):
    """
    Latitude measurement detector - recognizes numbers using OCR
    """

    def __init__(self):
        super().__init__(roi_type=1, roi_name='Latitude')
        self.last_latitude = None

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
                latitude = float(numbers[0])
                self.last_latitude = latitude
            except ValueError:
                latitude = self.last_latitude
        else:
            latitude = self.last_latitude

        if latitude is not None:
            return {"latitude": latitude}

        return None

    def _print_result(self, result):
        """Print result"""
        if result is not None:
            print(f"Current Latitude: {result['latitude']:}")
        else:
            print("Latitude could not be recognized")
