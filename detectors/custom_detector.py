from detectors.base_detector import BaseDetector

class CustomDetector(BaseDetector):
    """
    Custom detector template
    """
    def __init__(self):
        super().__init__(roi_type=4, roi_name='Custom ROI')

    def process(self):
        """
        Perform user-defined processing in the ROI area
        Returns:
            any: user-defined result
        """
        image = self.capture_roi()
        if image is None:
            return None

        # TODO: Add custom logic here
        # Currently implemented as a placeholder

        return None

    def _print_result(self, result):
        """Print result"""
        if result is not None:
            print(f"Detection result: {result}")
        else:
            print("Custom ROI waiting (logic not implemented)")
