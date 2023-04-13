from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QColor


class ClickedGraphics(QtWidgets.QFrame):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()


class ButtonForPressureSection(ClickedGraphics):
    rate = 1
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(90)
        self.h, self.b = 7, 7
        self.leftHand=QColor(0, 0, 0)
        self.rightHand=QColor(0, 0, 0)


    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setBrush(self.leftHand)
        painter.drawRect(0, 60, int(self.width()/2), int(-self.h))
        painter.setBrush(self.rightHand)
        painter.drawRect(int((self.width()/2)), 60, int(self.width()/2), int(-self.b))

    def change_rectangle_size(self, value):
        self.h = value
        if self.h == '':
            self.h = 0
        else:
            self.h = int(self.h)
            if self.h < 20:
                self.leftHand = QColor(0, 255, 0)
            elif self.h >= 20 and self.h < 45:
                self.leftHand = QColor(230, 255, 0)
            else:
                self.leftHand = QColor(250, 64, 0)

            self.h *= self.rate

        self.update()

    def change_rectangle_size1(self, value1):
        self.b = value1
        if self.b == '':
            self.b = 0
        else:
            self.b = int(self.b)
            if self.b < 30:
                self.rightHand = QColor(0, 255, 0)
            elif self.b >= 30 and self.b < 45:
                self.rightHand = QColor(230, 255, 0)
            else:
                self.rightHand = QColor(250, 64, 0)

            self.b *= self.rate

        self.update()


class ButtonForSection(ClickedGraphics):
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(90)
