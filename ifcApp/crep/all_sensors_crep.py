from PyQt6 import uic, QtWidgets, QtCore

UI_sernsors = "view/ifc/crep/sensors crep.ui"


class AllSensorsCrep(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_sernsors, self)
        self.list_progressBar = [self.voltage_progressBar,self.current_sensors_progressBar,self.current_valve_progressBar,
                                 self.current_POE_progressBar,self.A1_progressBar,self.F1_progressBar,
                                 self.amperage_progressBar,self.amperage_valve_progressBar,self.CP_progressBar,
                                 self.zaz_CP_progressBar,self.max_zaz_progressBar]

    @QtCore.pyqtSlot(list)
    def setValue_progressBar(self, lst):
        for elem in range(len(lst)):
            self.list_progressBar[elem].setValue(lst[elem])
