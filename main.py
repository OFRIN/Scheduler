
import sys
from PyQt5.QtWidgets import QApplication

from core.scheduler_v1_1 import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

