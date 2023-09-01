from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QProgressBar

from ifcApp.crep.graphics.graphic_for_sensors import GraphicsWindow


class ClickedProgressbar(QProgressBar):
    clicked = pyqtSignal()
    id_dat = 1
    crep_id = 1
    def __init__(self):
        super().__init__()
        self.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.setFixedSize(61, 50)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.graf = GraphicsWindow(self.crep_id, self.id_dat)
        self.graf.show()
        self.clicked.emit()


    def diff_value_progress_bar(self, lineEdit):
        value = lineEdit.text()
        if value == ' ' or value=='':
            value = 0
        elif int(value)>self.maximum():
            value=self.maximum()
        else:
            value = int(value)

        self.setValue(value)
