from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QColor


class ClickedGraphics(QtWidgets.QFrame):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()


class ButtonForPressureSection(ClickedGraphics):
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(90)
        self.h, self.b = 7, 7

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setBrush(QColor(200, 0, 0))
        painter.drawRect(0, 60, int(10), int(-self.h))
        painter.setBrush(QColor(255, 80, 0, 160))
        painter.drawRect(10, 60, int(10), -self.b)

    def change_rectangle_size(self, value):
        self.h = value
        if self.h == '':
            self.h = 0
        else:
            self.h = int(self.h)

        self.update()

    def change_rectangle_size1(self, value1):
        self.b = value1
        if self.b == '':
            self.b = 0
        else:
            self.b = int(self.b)
        self.update()


class ButtonForSection(ClickedGraphics):
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(90)
