from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QProgressBar


class ClickedProgressbar(QProgressBar):
    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.setFixedSize(61, 50)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()