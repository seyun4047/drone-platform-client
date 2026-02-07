import pytesseract
from detectors.base_detector import BaseDetector
import re


class LongitudeDetector(BaseDetector):
    """
    Longitude measurement detector - recognizes numbers using OCR
    """

    def __init__(self):
        super().__init__(roi_type=1, roi_name='Longitude')
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
                longitude = float(numbers[0])
                self.last_longitude = longitude
            except ValueError:
                longitude = self.last_longitude
        else:
            longitude = self.last_longitude

        if longitude is not None:
            return {"longitude": longitude}

        return None

    def _print_result(self, result):
        """Print result"""
        if result is not None:
            print(f"Current Longitude: {result['longitude']:}")
        else:
            print("Longitude could not be recognized")
