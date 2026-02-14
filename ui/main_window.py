"""
Main Application Window - UI Only
Delegates business logic to managers
"""
import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QMessageBox, QGroupBox
)
from PyQt5.QtCore import QTimer
import pytesseract

from config.config import TESSERACT_PATH, ROI_NAMES, DEFAULT_INTERVAL, MIN_INTERVAL
from config.env_config import (
    TELEMETRY_SERVER_URL, DEFAULT_SERIAL, DEFAULT_DEVICE_NAME
)
from network.telemetry_client import TelemetryClient
from ui.selection_window import SelectionWindow
from managers.roi_manager import ROIManager
from managers.detection_manager import DetectionManager


class OCRApp(QWidget):
    """
    Main application window - UI layer only
    """

    def __init__(self):
        super().__init__()

        # Set Tesseract path
        try:
            pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
        except Exception as e:
            QMessageBox.critical(
                None, "Error",
                f"Tesseract-OCR executable not found.\n{e}"
            )
            sys.exit(1)

        # Initialize managers
        self.roi_manager = ROIManager(num_rois=5)
        self.detection_manager = DetectionManager(self.roi_manager)

        # Initialize timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_detection_timer)
        self.is_running = False

        # Telemetry client (initialized on connect)
        self.telemetry_client = None

        self.init_ui()

    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle('Drone Video Multi-ROI Detection System')
        self.setGeometry(100, 100, 500, 600)

        main_layout = QVBoxLayout()

        # ROI settings group
        main_layout.addWidget(self._create_roi_group())

        # Detection control group
        main_layout.addWidget(self._create_control_group())

        # Status display
        self.status_label = QLabel("Status: Please set at least one ROI area")
        main_layout.addWidget(self.status_label)

        # Drone connection group
        main_layout.addWidget(self._create_connection_group())

        # Exit button
        btn_exit = QPushButton('Exit Program')
        btn_exit.clicked.connect(self.close)
        main_layout.addWidget(btn_exit)

        main_layout.addStretch(1)
        self.setLayout(main_layout)

    def _create_roi_group(self):
        """Create ROI settings group"""
        roi_group = QGroupBox("ROI Area Settings")
        roi_layout = QVBoxLayout()

        self.roi_buttons = {}
        self.roi_labels = {}

        for roi_type in range(self.roi_manager.num_rois):
            roi_name = ROI_NAMES[roi_type]

            h_layout = QHBoxLayout()

            # ROI selection button
            btn = QPushButton(f'Select {roi_name} Area')
            btn.clicked.connect(lambda checked, rt=roi_type: self.select_roi(rt))
            self.roi_buttons[roi_type] = btn
            h_layout.addWidget(btn)

            # Status label
            label = QLabel("Not set")
            label.setStyleSheet("color: gray;")
            self.roi_labels[roi_type] = label
            h_layout.addWidget(label)

            roi_layout.addLayout(h_layout)

        roi_group.setLayout(roi_layout)
        return roi_group

    def _create_control_group(self):
        """Create detection control group"""
        control_group = QGroupBox("Detection Settings")
        control_layout = QVBoxLayout()

        # Detection interval setting
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("Detection interval (seconds):"))
        self.interval_input = QLineEdit(str(DEFAULT_INTERVAL))
        self.interval_input.setMaximumWidth(100)
        interval_layout.addWidget(self.interval_input)
        interval_layout.addStretch(1)
        control_layout.addLayout(interval_layout)

        # Start/Stop button
        self.btn_run = QPushButton('Start Detection')
        self.btn_run.clicked.connect(self.toggle_detection)
        self.btn_run.setEnabled(False)
        control_layout.addWidget(self.btn_run)

        control_group.setLayout(control_layout)
        return control_group

    def _create_connection_group(self):
        """Create drone connection group"""
        conn_group = QGroupBox("Drone Connection")
        conn_layout = QVBoxLayout()

        # Serial input
        serial_layout = QHBoxLayout()
        serial_layout.addWidget(QLabel("Serial:"))
        self.serial_input = QLineEdit()
        self.serial_input.setText(DEFAULT_SERIAL)
        serial_layout.addWidget(self.serial_input)
        conn_layout.addLayout(serial_layout)

        # Device name input
        name_layout = QHBoxLayout()
        name_layout.addWidget(QLabel("Device Name:"))
        self.device_input = QLineEdit()
        self.device_input.setText(DEFAULT_DEVICE_NAME)
        name_layout.addWidget(self.device_input)
        conn_layout.addLayout(name_layout)

        # Connect button
        self.btn_connect = QPushButton("Connect")
        self.btn_connect.clicked.connect(self.connect_drone)
        conn_layout.addWidget(self.btn_connect)

        conn_group.setLayout(conn_layout)
        return conn_group

    def connect_drone(self):
        """Connect to drone telemetry server"""
        serial = self.serial_input.text().strip()
        device_name = self.device_input.text().strip()

        if not serial or not device_name:
            print("Connection failed: serial or device_name missing")
            QMessageBox.warning(self, "Warning", "Please enter serial and device name.")
            return

        self.telemetry_client = TelemetryClient(
            client_url=TELEMETRY_SERVER_URL,
            serial=serial,
            device_name=device_name
        )

        if self.telemetry_client.connect():
            print(f"[CONNECT SUCCESS] serial={serial}, device_name={device_name}")
            self.status_label.setText("Status: Drone connected")

            # Update detection manager with telemetry client
            self.detection_manager.set_telemetry_client(self.telemetry_client)
        else:
            print(f"[CONNECT FAILED] serial={serial}, device_name={device_name}")
            self.status_label.setText("Status: Connection failed")
            self.telemetry_client = None

    def select_roi(self, roi_type):
        """Open ROI selection window"""
        self.hide()
        self.selection_window = SelectionWindow(parent=self, roi_type=roi_type)
        self.selection_window.show()

    def set_roi_coordinates(self, roi_type, x, y, w, h):
        """Set ROI coordinates (called by SelectionWindow)"""
        # Delegate to ROI manager
        self.roi_manager.set_roi_coordinates(roi_type, x, y, w, h)

        # Update UI
        roi_name = ROI_NAMES[roi_type]
        self.roi_labels[roi_type].setText(f"Set: ({x}, {y}, {w}, {h})")
        self.roi_labels[roi_type].setStyleSheet("color: green;")

        # Enable run button if at least one ROI is set
        self.btn_run.setEnabled(True)

        self.show()

    def toggle_detection(self):
        """Toggle detection start/stop"""
        if self.is_running:
            self.stop_detection()
        else:
            self.start_detection()

    def start_detection(self):
        """Start detection"""
        # Check if at least one ROI is set
        if not self.roi_manager.has_any_roi():
            QMessageBox.warning(
                self, "Warning",
                "Please set at least one ROI area."
            )
            return

        try:
            interval = float(self.interval_input.text())
            if interval < MIN_INTERVAL:
                QMessageBox.warning(
                    self, "Warning",
                    f"Interval must be at least {MIN_INTERVAL} seconds."
                )
                return

            # Start timer
            self.timer.start(int(interval * 1000))
            self.is_running = True

            # Activate all ROI detectors and overlays
            self.roi_manager.activate_all()

            # Update UI
            self.btn_run.setText(f'Stop Detection (Interval: {interval}s)')
            self.status_label.setText("Status: Detection running... (check terminal)")

            print("\n" + "=" * 60)
            print("=== Multi-ROI Detection Started ===")
            print(f"=== Detection interval: {interval} seconds ===")
            print("=" * 60 + "\n")

        except ValueError:
            QMessageBox.warning(
                self, "Warning",
                "Please enter a valid number for the detection interval."
            )

    def stop_detection(self):
        """Stop detection"""
        self.timer.stop()
        self.is_running = False

        # Deactivate all detectors and overlays
        self.roi_manager.deactivate_all()

        # Update UI
        self.btn_run.setText('Start Detection')
        self.status_label.setText("Status: Detection stopped")

        print("\n" + "=" * 60)
        print("=== Multi-ROI Detection Stopped ===")
        print("=" * 60 + "\n")

    def on_detection_timer(self):
        """Timer callback - delegate to detection manager"""
        self.detection_manager.perform_detection()

    def closeEvent(self, event):
        """Window close event"""
        if self.is_running:
            self.stop_detection()

        # Close all overlays
        self.roi_manager.close_all_overlays()

        # Disconnect telemetry
        if self.telemetry_client:
            self.telemetry_client.disconnect()

        event.accept()