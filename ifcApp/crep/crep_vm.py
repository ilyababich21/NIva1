from PyQt6 import uic, QtWidgets
from ifcApp.dataSensors.data_sensors_vm import DataSensorsSection

UI_crep = "view/ifc_crep.ui"


class CrepViewModel(QtWidgets.QMainWindow):
    def __init__(self, num):
        super().__init__()

        uic.loadUi(UI_crep, self)
        self.data_sensors_section = DataSensorsSection()
        self.num_crep.setText(str(num))
        self.control_pushButton.clicked.connect(self.show_data_sensors_section)




    def show_data_sensors_section(self):
        self.data_sensors_section.show()

