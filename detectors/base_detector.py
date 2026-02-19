from abc import ABC, abstractmethod
from PIL import ImageGrab
import time

# Parent class for Detector

class BaseDetector(ABC):
    """
    Common detector functionality
    """
    def __init__(self, roi_type, roi_name):
        """
        Args:
            roi_type (int): ROI type ID
            roi_name (str): ROI name
        """
        self.roi_type = roi_type
        self.roi_name = roi_name
        self.roi_coords = None  # (x, y, w, h)
        self.is_active = False

    def set_roi(self, x, y, w, h):
        """Set ROI coordinates"""
        self.roi_coords = (x, y, w, h)

    def get_roi(self):
        """Return ROI coordinates"""
        return self.roi_coords

    def has_roi(self):
        """Check if ROI is set"""
        return self.roi_coords is not None

    def capture_roi(self):
        """Capture the ROI area"""
        if not self.has_roi():
            return None

        x, y, w, h = self.roi_coords
        bbox = (x, y, x + w, y + h)
        return ImageGrab.grab(bbox=bbox)

    def activate(self):
        """Activate the detector"""
        self.is_active = True

    def deactivate(self):
        """Deactivate the detector"""
        self.is_active = False

    @abstractmethod
    def process(self):
        """
        Detection process (to be implemented in subclass)
        Returns:
            dict: detection result
        """
        pass

    def run(self):
        """
        Execute detection and return result
        Returns:
            dict: {'timestamp': str, 'result': any, 'error': str or None}
        """
        if not self.has_roi():
            return {
                'timestamp': time.strftime("%H:%M:%S"),
                'result': None,
                'error': 'ROI is not set'
            }

        if not self.is_active:
            return {
                'timestamp': time.strftime("%H:%M:%S"),
                'result': None,
                'error': 'Detector is inactive'
            }

        try:
            result = self.process()
            return {
                'timestamp': time.strftime("%H:%M:%S"),
                'result': result,
                'error': None
            }
        except Exception as e:
            return {
                'timestamp': time.strftime("%H:%M:%S"),
                'result': None,
                'error': str(e)
            }

    def format_output(self, result_dict):
        """
        Format and print the result
        Args:
            result_dict (dict): return value from run()
        """
        timestamp = result_dict['timestamp']
        result = result_dict['result']
        error = result_dict['error']

        # print(f"\n[{timestamp}] {self.roi_name} result:")
        # print("-" * 40)

        if error:
            print(f"error: {error}")
        elif result is not None:
            self._print_result(result)
        else:
            print("NO DETECTION")

        print("-" * 40)

    @abstractmethod
    def _print_result(self, result):
        pass
