from datetime import datetime, timedelta

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from ifcApp.crep.graphics.select_graphics import SelectedGraphic

UI_select_date = "resources/view/ifc/crep/select_date.ui"


class SelectDate(QMainWindow):
    def __init__(self, num_crep, num_sensors):
        self.num_crep = num_crep
        self.num_sensors = num_sensors
        super().__init__()
        uic.loadUi(UI_select_date, self)
        self.draw_pushButton.clicked.connect(self.create_graphic)
        self.from_dateTimeEdit.setDateTime(datetime.now() - timedelta(days=1))
        self.before_dateTimeEdit.setDateTime(datetime.now())

    def create_graphic(self):
            from_datetime = self.from_dateTimeEdit.dateTime()
            before_datetime = self.before_dateTimeEdit.dateTime()
            self.select_graphic = SelectedGraphic(self.num_crep, self.num_sensors)
            self.select_graphic.draw_graphic(from_datetime, before_datetime)
            self.select_graphic.show()



