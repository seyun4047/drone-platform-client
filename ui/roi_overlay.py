from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from config.config import ROI_COLORS


class ROIOverlay(QWidget):
    """
    Transparent overlay that displays color-coded borders for ROI areas
    """

    def __init__(self, roi_type):
        """
        Args:
            roi_type (int): ROI type (0–4)
        """
        super().__init__()
        self.roi_type = roi_type

        # Window settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Set color based on ROI type
        self.color = ROI_COLORS.get(roi_type, (255, 0, 0))

        self.hide()

    def paintEvent(self, event):
        """Draw border"""
        painter = QPainter(self)

        # Draw border with ROI-specific color
        r, g, b = self.color
        painter.setPen(QPen(QColor(r, g, b), 2, Qt.SolidLine))
        painter.setBrush(Qt.NoBrush)

        # Draw border rectangle
        rect = self.rect().adjusted(1, 1, -1, -1)
        painter.drawRect(rect)

    def set_position(self, x, y, w, h):
        """Set overlay position and size"""
        self.setGeometry(x, y, w, h)
