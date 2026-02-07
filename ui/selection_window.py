from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QCursor, QImage
from PyQt5.QtCore import Qt, QRect
from PIL import ImageGrab


class SelectionWindow(QWidget):
    """
    Capture the screen and select an ROI area by mouse drag
    """

    def __init__(self, parent=None, roi_type=0):
        """
        Args:
            parent: parent widget
            roi_type (int): ROI type
        """
        super().__init__()
        self.parent = parent
        self.roi_type = roi_type

        # Window settings
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Screen capture
        desktop = QApplication.desktop()
        screen_rect = desktop.screenGeometry()

        self.screenshot = ImageGrab.grab(bbox=(
            screen_rect.left(), screen_rect.top(),
            screen_rect.right(), screen_rect.bottom()
        ))

        # Convert PIL image to QPixmap
        data = self.screenshot.convert("RGBA").tobytes("raw", "BGRA")
        qimage = QImage(
            data,
            self.screenshot.size[0],
            self.screenshot.size[1],
            QImage.Format_ARGB32
        )
        self.pixmap = QPixmap.fromImage(qimage)

        self.setGeometry(screen_rect)

        # Initialize selection area
        self.begin = QCursor.pos()
        self.end = QCursor.pos()
        self.is_selecting = False

    def paintEvent(self, event):
        """Draw the screen"""
        painter = QPainter(self)

        # Draw background screenshot
        painter.setOpacity(1.0)
        painter.drawPixmap(self.rect(), self.pixmap)

        # Dark overlay
        painter.setOpacity(0.4)
        painter.fillRect(self.rect(), QColor(0, 0, 0))

        # Draw selection area
        if self.is_selecting:
            rect = QRect(self.begin, self.end).normalized()

            # Make selected area bright
            painter.setClipping(True)
            painter.setClipRect(rect)
            painter.setOpacity(1.0)
            painter.drawPixmap(self.rect(), self.pixmap)

            # Red border
            painter.setClipping(False)
            painter.setPen(QPen(QColor(255, 0, 0), 2, Qt.SolidLine))
            painter.setBrush(Qt.NoBrush)
            painter.drawRect(rect)

    def mousePressEvent(self, event):
        """Mouse press"""
        if event.button() == Qt.LeftButton:
            self.begin = event.pos()
            self.end = event.pos()
            self.is_selecting = True
            self.update()

    def mouseMoveEvent(self, event):
        """Mouse move"""
        if self.is_selecting:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        """Mouse release"""
        if event.button() == Qt.LeftButton and self.is_selecting:
            self.is_selecting = False
            rect = QRect(self.begin, self.end).normalized()

            # Minimum size check
            if rect.width() > 5 and rect.height() > 5:
                x, y, w, h = rect.x(), rect.y(), rect.width(), rect.height()
                self.parent.set_roi_coordinates(self.roi_type, x, y, w, h)

                from config.config import ROI_NAMES
                roi_name = ROI_NAMES.get(self.roi_type, 'Unknown')
                QMessageBox.information(
                    self, "ROI Selection Complete",
                    f"{roi_name} area has been selected.\nPosition: ({x}, {y}, {w}, {h})"
                )
            else:
                QMessageBox.warning(
                    self, "Warning",
                    "The selected area is too small. Please try again."
                )

            self.close()
