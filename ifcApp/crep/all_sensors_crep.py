import os

from PyQt6 import uic, QtWidgets

from address import resource_path

UI_sernsors = resource_path("resources\\view\\ifc\\crep\\sensors crep.ui")


class AllSensorsCrep(QtWidgets.QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        self.label1 = None

        uic.loadUi(UI_sernsors, self)
        self.list_progressBar = [self.voltage_progressBar, self.current_sensors_progressBar, self.current_valve_progressBar,
                                 self.current_POE_progressBar, self.A1_progressBar, self.F1_progressBar,
                                 self.amperage_progressBar, self.amperage_valve_progressBar, self.CP_progressBar,
                                 self.zaz_CP_progressBar, self.max_zaz_progressBar]


