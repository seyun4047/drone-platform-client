"""
ROI Manager - Handles ROI selection, overlays, and detectors
"""
from ui.roi_overlay import ROIOverlay
from detectors.speed_detector import SpeedDetector
from detectors.person_detector import PersonDetector
from detectors.latitude_detector import LatitudeDetector
from detectors.longitude_detector import LongitudeDetector


class ROIManager:
    """Manages ROI detectors and overlays"""

    def __init__(self, num_rois=4):
        self.num_rois = num_rois

        # Initialize detectors
        self.detectors = {
            0: SpeedDetector(),
            1: PersonDetector(),
            2: LongitudeDetector(),
            3: LatitudeDetector(),
        }

        # Initialize ROI overlays
        self.overlays = {
            0: ROIOverlay(0),
            1: ROIOverlay(1),
            2: ROIOverlay(2),
            3: ROIOverlay(3),
        }

    def set_roi_coordinates(self, roi_type, x, y, w, h):
        """Set ROI coordinates for a specific detector"""
        self.detectors[roi_type].set_roi(x, y, w, h)
        self.overlays[roi_type].set_position(x, y, w, h)
        return True

    def has_any_roi(self):
        """Check if at least one ROI is set"""
        return any(detector.has_roi() for detector in self.detectors.values())

    def activate_all(self):
        """Activate all detectors that have ROI set and show overlays"""
        for roi_type, detector in self.detectors.items():
            if detector.has_roi():
                detector.activate()
                self.overlays[roi_type].show()

    def deactivate_all(self):
        """Deactivate all detectors and hide overlays"""
        for roi_type, detector in self.detectors.items():
            detector.deactivate()
            self.overlays[roi_type].hide()

    def get_detector(self, roi_type):
        """Get a specific detector"""
        return self.detectors.get(roi_type)

    def get_all_detectors(self):
        """Get all detectors"""
        return self.detectors

    def close_all_overlays(self):
        """Close all overlay windows"""
        for overlay in self.overlays.values():
            overlay.close()