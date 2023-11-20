import os

from PyQt6 import uic, QtWidgets

from address import resource_path

UI_data_sensors = "resources\\view\\sensors\\data_sensors.ui"
UI_data_sensors_section = "resources\\view\\ifc\\crep\\data_sensors_section.ui"


class DataSensorsMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(resource_path(UI_data_sensors), self)


class DataSensorsSection(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(resource_path(UI_data_sensors_section), self)
