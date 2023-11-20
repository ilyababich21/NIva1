import os
from datetime import datetime, timedelta

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from address import resource_path
from ifcApp.crep.graphics.select_graphics import SelectedGraphic
from ifcApp.crep.graphics.selected_graphic_model import SelectedGraphicModel

UI_select_date = "resources\\view\\ifc\\crep\\graphics_view\\select_date.ui"


class SelectDate(QMainWindow):
    def __init__(self, num_crep, num_sensors,database):
        self.database = database
        self.num_crep = num_crep
        self.num_sensors = num_sensors
        super().__init__()
        uic.loadUi(resource_path(UI_select_date), self)
        self.draw_pushButton.clicked.connect(self.create_graphic)
        self.from_dateTimeEdit.setDateTime(datetime.now() - timedelta(days=1))
        self.before_dateTimeEdit.setDateTime(datetime.now())

    def create_graphic(self):
        model = SelectedGraphicModel(self.num_crep, self.num_sensors,self.database)
        from_datetime = self.from_dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        before_datetime = self.before_dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.select_graphic = SelectedGraphic(self.num_crep, self.num_sensors, model)
        self.select_graphic.draw_graphic(from_datetime, before_datetime)
        self.select_graphic.show()
