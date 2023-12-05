import os

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

from address import resource_path

UI_data_sensors = resource_path("resources\\view\\sensors\\data_sensors.ui")
UI_data_sensors_section = resource_path("resources\\view\\ifc\\crep\\data_sensors_section.ui")


class DataSensorsMainWindow(QtWidgets.QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        uic.loadUi(UI_data_sensors, self)
        glob_param=self.database.get_global_params()
        RowCount=len(glob_param)
        self.tableWidget = QTableWidget(RowCount, self.database.get_count_shield(), self)
        for i in range(RowCount):
            self.tableWidget.setVerticalHeaderItem(i,QTableWidgetItem(glob_param[i].name))
        self.setCentralWidget(self.tableWidget)


class DataSensorsSection(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_data_sensors_section, self)
