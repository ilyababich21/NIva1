from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QProgressBar, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel

from ifcApp.crep.graphics.graphic_for_sensors import GraphicsWindow


class ClickedProgressbar(QWidget):
    clicked = pyqtSignal()
    id_dat = 1
    crep_id = 1

    def __init__(self, max_value, database):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel()
        self.database = database
        self.progressBar = QProgressBar()
        self.progressBar.setMaximum(max_value)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar.setFixedSize(53, 50)
        self.lineedit = QLineEdit()
        self.lineedit.setValidator(QIntValidator())
        self.lineedit.textChanged.connect(lambda: self.diff_value_progress_bar(max_value))
        layout.addWidget(self.progressBar)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.label)
        layout.setSpacing(0)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.graf = GraphicsWindow(self.crep_id, self.id_dat, self.database)
        self.graf.show()
        self.clicked.emit()

    def diff_value_progress_bar(self, max_value):
        value = self.lineedit.text()
        if value == ' ' or value == '':
            value = 0
        elif int(value) > max_value:
            value = max_value
        else:
            value = int(value)

        self.progressBar.setValue(value)
