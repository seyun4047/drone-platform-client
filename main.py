import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import OCRApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OCRApp()
    ex.show()
    sys.exit(app.exec_())