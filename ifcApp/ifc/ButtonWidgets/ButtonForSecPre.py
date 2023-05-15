from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QColor


class ButtonForPressureSection(QtWidgets.QFrame):
    coefficient = 1
    clicked = pyqtSignal()

    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMinimumHeight(40)
        self.setMaximumHeight(65)

        self.rectangle_height = 0
        self.rectangle = QColor(0, 0, 0)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setBrush(self.rectangle)
        painter.drawRect(5, self.height(), int(self.width() - 10), int(-self.rectangle_height))

    def change_rectangle_size(self, value):
        self.rectangle_height = value
        if self.rectangle_height == '':
            self.rectangle_height = 0
        else:
            self.rectangle_height = int(self.rectangle_height)

        self.rectangle_height *= self.coefficient

        self.update()

    def change_color(self):
        if self.rectangle_height < 20:
            self.rectangle = QColor(0, 100, 0)
        elif 20 <= self.rectangle_height < 45:
            self.rectangle = QColor(255, 140, 0)
        else:
            self.rectangle = QColor(255, 0, 0)
