import datetime

from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPainter, QColor


class ButtonForSectionWidget(QtWidgets.QFrame):
    value = 1
    coefficient = 1
    min_normal=1
    max_normal=1
    clicked = pyqtSignal()
    entry = pyqtSignal(int)

    def __init__(self, number,list):
        super().__init__()
        self.list = list
        self.id = number
        self.setMaximumHeight(85)

        self.rectangle_height = 0
        self.rectangle = QColor(0, 0, 0)

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setBrush(self.rectangle)
        painter.drawRect(0, self.height(), int(self.width()), int(-self.rectangle_height))

    def update_color_and_height(self, value):
        try:
            self.rectangle_height = int(value)
            self.coefficient = self.height() / self.value
            self.rectangle_height *= self.coefficient

            if self.rectangle_height < self.min_normal * self.coefficient:
                self.rectangle = QColor(self.list[1])  # Orange ?no, its beaurisoviy
            elif self.min_normal * self.coefficient <= self.rectangle_height < self.max_normal * self.coefficient:
                self.rectangle = QColor(self.list[0])  # Green
            else:
                self.rectangle = QColor(self.list[2])  # Red

        except ValueError:
            self.rectangle_height = 150
            self.rectangle = QColor(139, 0, 255)  # Purple
            time = datetime.datetime.now()
            t = time.strftime("%d/%m/%Y %H:%M")
            # text_edit.append(f"{t},Cломан датчик  {dat_name} в крепи {num_crep} ")
            # errorButton.setStyleSheet("background-color: #ff0000;")

        except Exception as e:
            print(e)
        self.update()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()
