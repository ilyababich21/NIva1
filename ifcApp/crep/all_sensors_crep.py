from PyQt6 import uic, QtWidgets

from ifcApp.ifc.mainMenu.global_param import GlobalParam

UI_sernsors = "view/ifc/crep/sensors crep.ui"


class AllSensorsCrep(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label1 = None
        self.global_param = GlobalParam()

        uic.loadUi(UI_sernsors, self)
        self.list_progressBar = [self.voltage_progressBar, self.current_sensors_progressBar, self.current_valve_progressBar,
                                 self.current_POE_progressBar, self.A1_progressBar, self.F1_progressBar,
                                 self.amperage_progressBar, self.amperage_valve_progressBar, self.CP_progressBar,
                                 self.zaz_CP_progressBar, self.max_zaz_progressBar]

        for elem in range(len(self.list_progressBar)):
            self.list_progressBar[elem].setMaximum(self.global_param.query_in_global_param_table[elem].max_value)
