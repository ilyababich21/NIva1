import datetime

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QColor


class ButtonForSectionWidget(QtWidgets.QFrame):
    value = 1
    coefficient = 1
    clicked = pyqtSignal()

    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setMaximumHeight(85)

        self.rectangle_height = 0
        self.rectangle = QColor(0, 0, 0)

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setBrush(self.rectangle)
        painter.drawRect(0, self.height(), int(self.width()), int(-self.rectangle_height))

    def change_rectangle_size(self, value):
        self.coefficient = self.height() / self.value
        self.rectangle_height = value
        if self.rectangle_height == '':
            self.rectangle_height = 0
        else:
            self.rectangle_height = int(self.rectangle_height)

        self.rectangle_height *= self.coefficient

        self.update()

    def errors_sensors(self,sensors, lineedit, dat, num,pushbutton):
        if sensors == "":
            self.rectangle_height = 150
            self.rectangle = QColor(139, 0, 255)
            time = datetime.datetime.now()
            t = time.strftime("%d/%m/%Y %H:%M")
            lineedit.append(f"{t},pizda datchiku {dat} v crepi {num} ")
            pushbutton.setStyleSheet("background-color: #ff0000;")
        else:
            pushbutton.setStyleSheet("background-color: #e9e9e9;")

    def change_color(self, normal):
        if self.rectangle_height < normal * self.coefficient:
            self.rectangle = QColor(255, 140, 0)
        elif normal * self.coefficient <= self.rectangle_height < (normal * self.coefficient) + 12:
            self.rectangle = QColor(0, 100, 0)
        else:
            self.rectangle = QColor(255, 0, 0)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()

    def notification_error(self, sensors, lineedit, dat, num):
        time = datetime.datetime.now()
        t = time.strftime("%d/%m/%Y %H:%M")
        if sensors == "":
            lineedit.append(f"{t},pizda {dat} v crepi {num} ")
