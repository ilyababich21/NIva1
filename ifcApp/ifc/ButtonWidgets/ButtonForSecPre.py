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
        if self.rectangle_height == "-":
            self.rectangle_height = 0
        else:
            self.rectangle_height = int(self.rectangle_height)

        self.rectangle_height *= self.coefficient

        self.update()

    def errors_sensors(self, sensors, lineedit, dat, num, pushbutton):
        if sensors == "":
            self.rectangle_height = 150
            self.rectangle = QColor(139, 0, 255)  # Purple
            time = datetime.datetime.now()
            t = time.strftime("%d/%m/%Y %H:%M")
            lineedit.append(f"{t},pizda datchiku {dat} v crepi {num} ")
            pushbutton.setStyleSheet("background-color: #ff0000;")
        else:
            pushbutton.setStyleSheet("background-color: #e9e9e9;")

    def change_color(self, from_normal, to_normal):
        if self.rectangle_height < from_normal * self.coefficient:
            self.rectangle = QColor(255, 140, 0)  # Orange
        elif from_normal * self.coefficient <= self.rectangle_height < to_normal * self.coefficient:
            self.rectangle = QColor(0, 100, 0)  # Green
        else:
            self.rectangle = QColor(255, 0, 0)  # Red

    def ubdateColorAndHeight(self, value, notificationLineEdit, min_normal, max_normal, dat_name, num_crep, errorButton):
        try :
            self.rectangle_height=int(value)
            self.coefficient = self.height() / self.value
            self.rectangle_height  *= self.coefficient
            if self.rectangle_height < min_normal * self.coefficient:
                self.rectangle = QColor(100, 230, 200)  # Orange ?no, its beaurisoviy
            elif min_normal * self.coefficient <= self.rectangle_height < max_normal * self.coefficient:
                self.rectangle = QColor(0, 100, 0)  # Green
            else:
                self.rectangle = QColor(255, 0, 0)  # Red
        except ValueError:
            self.rectangle_height = 150
            self.rectangle = QColor(139, 0, 255)  # Purple
            time = datetime.datetime.now()
            t = time.strftime("%d/%m/%Y %H:%M")
            notificationLineEdit.append(f"{t},pizda datchiku {dat_name} v crepi {num_crep} ")
            errorButton.setStyleSheet("background-color: #ff0000;")

        except Exception as e:
            print(e)
        self.update()


        # if value == '':
        #     self.rectangle_height = 150
        #     self.rectangle = QColor(139, 0, 255)  # Purple
        #     time = datetime.datetime.now()
        #     t = time.strftime("%d/%m/%Y %H:%M")
        #     notificationLineEdit.append(f"{t},pizda datchiku {dat_name} v crepi {num_crep} ")
        #     errorButton.setStyleSheet("background-color: #ff0000;")
        # # else:
        # #     errorButton.setStyleSheet("background-color: #e9e9e9;")
        # else:
        #     self.coefficient = self.height() / self.value
        #     self.rectangle_height = int(int(value)*self.coefficient)
        #     if self.rectangle_height < min_normal * self.coefficient:
        #         self.rectangle = QColor(100, 230, 200)  # Orange ?no, its beaurisoviy
        #     elif min_normal * self.coefficient <= self.rectangle_height < max_normal * self.coefficient:
        #         self.rectangle = QColor(0, 100, 0)  # Green
        #     else:
        #         self.rectangle = QColor(255, 0, 0)  # Red

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.clicked.emit()
