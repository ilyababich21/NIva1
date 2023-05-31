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

    def diff_value_progress_bar(self, lineEdit):
        value = lineEdit.text()
        if value == '':
            value = 0
        else:
            value = int(value)

        self.setValue(value)
