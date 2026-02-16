"""
DRONE COMMAND CORE - Futuristic Edition
Deep Space Black & Neon Cyan HUD Theme
"""

import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QMessageBox, QGroupBox
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import pytesseract

from config.config import TESSERACT_PATH, ROI_NAMES, DEFAULT_INTERVAL
from config.env_config import (
    TELEMETRY_SERVER_URL, DEFAULT_SERIAL, DEFAULT_DEVICE_NAME
)
from network.telemetry_client import TelemetryClient
from ui.selection_window import SelectionWindow
from managers.roi_manager import ROIManager
from managers.detection_manager import DetectionManager


class OCRApp(QWidget):
    """
    High-End Drone Command Center UI
    """

    def __init__(self):
        super().__init__()

        # Tesseract config
        try:
            pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
        except Exception as e:
            QMessageBox.critical(None, "SYSTEM ERROR", f"Tesseract Missing.\n{e}")
            sys.exit(1)

        self.roi_manager = ROIManager(num_rois=5)
        self.detection_manager = DetectionManager(self.roi_manager)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_detection_timer)

        self.is_running = False
        self.telemetry_client = None

        self.init_ui()
        self.apply_modern_styles()

    # ===============================
    # FUTURISTIC STYLE
    # ===============================
    def apply_modern_styles(self):
        self.setStyleSheet("""

        QWidget {
            background-color: #050B14;
            color: #EAF6FF;
            font-family: 'Segoe UI', 'Malgun Gothic', sans-serif;
        }

        QGroupBox {
            background-color: rgba(15, 25, 45, 0.9);
            border: 1px solid #0E2A47;
            border-radius: 14px;
            margin-top: 18px;
            font-weight: bold;
            color: #00E5FF;
            padding: 10px;
        }

        QGroupBox::title {
            subcontrol-origin: margin;
            left: 20px;
            padding: 0 6px;
        }

        QPushButton {
            background-color: #0E1625;
            border: 1px solid #00E5FF;
            border-radius: 8px;
            padding: 10px;
            color: #00E5FF;
            font-weight: 600;
        }

        QPushButton:hover {
            background-color: #00E5FF;
            color: #050B14;
        }

        QPushButton:pressed {
            background-color: #00B8D4;
        }

        QPushButton:disabled {
            border: 1px solid #1C3A5F;
            color: #355C7D;
            background-color: #08111E;
        }

        #RunButton[running="true"] {
            border: 1px solid #FF3B3B;
            color: #FF3B3B;
        }

        #RunButton[running="true"]:hover {
            background-color: #FF3B3B;
            color: white;
        }

        QLineEdit {
            background-color: #08111E;
            border: 1px solid #0E2A47;
            border-radius: 6px;
            padding: 6px;
            color: #EAF6FF;
            selection-background-color: #00E5FF;
        }

        QLineEdit:focus {
            border: 1px solid #00E5FF;
        }

        QLabel#StatusLabel {
            background-color: #08111E;
            border: 1px solid #0E2A47;
            border-radius: 10px;
            padding: 14px;
            font-family: 'Consolas';
            font-size: 12px;
            color: #00E5FF;
        }

        """)

    # ===============================
    # UI LAYOUT
    # ===============================
    def init_ui(self):
        self.setWindowTitle("MAIN-DRONE CLIENT")
        self.setMinimumWidth(520)

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(18)

        # ===== HEADER =====
        title = QLabel("MAIN-DRONE CLIENT")
        title.setFont(QFont("Consolas", 20, QFont.Bold))
        title.setStyleSheet("color: #00E5FF; letter-spacing: 4px;")
        layout.addWidget(title)

        # ===== ROI CONFIG =====
        roi_group = QGroupBox(" ROI CONFIGURATION ")
        roi_layout = QVBoxLayout()

        self.roi_buttons = {}
        self.roi_labels = {}

        for i in range(self.roi_manager.num_rois):
            row = QHBoxLayout()

            btn = QPushButton(f"SET AREA {ROI_NAMES[i]}")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, rt=i: self.select_roi(rt))

            lbl = QLabel(f"[{ROI_NAMES[i]}] :: STANDBY")
            lbl.setStyleSheet("color: #6C8CA3; font-size: 11px;")

            row.addWidget(btn)
            row.addWidget(lbl)
            roi_layout.addLayout(row)

            self.roi_buttons[i] = btn
            self.roi_labels[i] = lbl

        roi_group.setLayout(roi_layout)
        layout.addWidget(roi_group)

        # ===== SCAN PARAMETERS =====
        scan_group = QGroupBox(" SCAN PARAMETERS ")
        scan_layout = QVBoxLayout()

        freq_row = QHBoxLayout()
        freq_row.addWidget(QLabel("UPDATE FREQUENCY (SEC):"))

        self.interval_input = QLineEdit(str(DEFAULT_INTERVAL))
        self.interval_input.setFixedWidth(70)
        self.interval_input.setAlignment(Qt.AlignCenter)

        freq_row.addWidget(self.interval_input)
        freq_row.addStretch()
        scan_layout.addLayout(freq_row)

        self.btn_run = QPushButton("INITIATE SCAN")
        self.btn_run.setObjectName("RunButton")
        self.btn_run.setProperty("running", "false")
        self.btn_run.setEnabled(False)
        self.btn_run.clicked.connect(self.toggle_detection)

        scan_layout.addWidget(self.btn_run)
        scan_group.setLayout(scan_layout)
        layout.addWidget(scan_group)

        # ===== STATUS PANEL =====
        self.status_label = QLabel("> SYSTEM IDLE :: WAITING CONFIG")
        self.status_label.setObjectName("StatusLabel")
        layout.addWidget(self.status_label)

        # ===== TERMINAL LINK =====
        conn_group = QGroupBox(" TERMINAL LINK ")
        conn_layout = QHBoxLayout()

        self.serial_input = QLineEdit(DEFAULT_SERIAL)
        self.device_input = QLineEdit(DEFAULT_DEVICE_NAME)

        self.btn_connect = QPushButton("LINK")
        self.btn_connect.setFixedWidth(90)
        self.btn_connect.clicked.connect(self.connect_drone)

        conn_layout.addWidget(self.serial_input)
        conn_layout.addWidget(self.device_input)
        conn_layout.addWidget(self.btn_connect)

        conn_group.setLayout(conn_layout)
        layout.addWidget(conn_group)

        # ===== EXIT =====
        btn_exit = QPushButton("CLOSE TERMINAL")
        btn_exit.setStyleSheet("border: 1px solid #233554; color: #355C7D;")
        btn_exit.clicked.connect(self.close)
        layout.addWidget(btn_exit)

        self.setLayout(layout)

    # ===============================
    # LOGIC
    # ===============================
    def connect_drone(self):
        serial = self.serial_input.text().strip()
        device_name = self.device_input.text().strip()

        self.telemetry_client = TelemetryClient(
            client_url=TELEMETRY_SERVER_URL,
            serial=serial,
            device_name=device_name
        )

        if self.telemetry_client.connect():
            self.status_label.setText(f"> LINK ESTABLISHED :: {device_name.upper()}")
            self.status_label.setStyleSheet("""
                border: 1px solid #00E5FF;
                color: #00E5FF;
                background-color: #08111E;
            """)
            self.detection_manager.set_telemetry_client(self.telemetry_client)
        else:
            self.status_label.setText("> LINK FAILURE :: CONNECTION REFUSED")
            self.status_label.setStyleSheet("""
                border: 1px solid #FF3B3B;
                color: #FF3B3B;
                background-color: #08111E;
            """)

    def select_roi(self, roi_type):
        self.hide()
        self.selection_window = SelectionWindow(parent=self, roi_type=roi_type)
        self.selection_window.show()

    def set_roi_coordinates(self, roi_type, x, y, w, h):
        self.roi_manager.set_roi_coordinates(roi_type, x, y, w, h)
        self.roi_labels[roi_type].setText(f"LOCKED :: {x},{y} ({w}x{h})")
        self.roi_labels[roi_type].setStyleSheet(
            "color: #00E5FF; font-weight: bold;"
        )
        self.btn_run.setEnabled(True)
        self.show()

    def toggle_detection(self):
        if self.is_running:
            self.stop_detection()
        else:
            self.start_detection()

    def start_detection(self):
        try:
            interval = float(self.interval_input.text())
            self.timer.start(int(interval * 1000))
            self.is_running = True
            self.roi_manager.activate_all()

            self.btn_run.setText("TERMINATE SCAN")
            self.btn_run.setProperty("running", "true")
            self.btn_run.setStyle(self.btn_run.style())

            self.status_label.setText(f"> SCANNING ACTIVE :: {interval} SEC")
        except:
            pass

    def stop_detection(self):
        self.timer.stop()
        self.is_running = False
        self.roi_manager.deactivate_all()

        self.btn_run.setText("INITIATE SCAN")
        self.btn_run.setProperty("running", "false")
        self.btn_run.setStyle(self.btn_run.style())

        self.status_label.setText("> SCAN TERMINATED")

    def on_detection_timer(self):
        self.detection_manager.perform_detection()

    def closeEvent(self, event):
        if self.is_running:
            self.stop_detection()

        self.roi_manager.close_all_overlays()

        if self.telemetry_client:
            self.telemetry_client.disconnect()

        event.accept()
