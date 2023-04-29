from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QColor




class ClickedGraphics(QtWidgets.QFrame):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()


class ButtonForPressureSection(ClickedGraphics):
    coefficient = 1
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(60)
        self.rectangle_height = 0
        self.rectangle = QColor(0, 0, 0)

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setBrush(self.rectangle)
        painter.drawRect(5, 60, int(self.width()-10), int(-self.rectangle_height))

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
            self.rectangle = QColor(0, 255, 0)
        elif 20 <= self.rectangle_height < 45:
            self.rectangle = QColor(230, 255, 0)
        else:
            self.rectangle = QColor(250, 64, 0)
