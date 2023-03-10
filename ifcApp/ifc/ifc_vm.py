from PyQt6 import uic, QtWidgets

from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.data_sensors_vm import SettingsSensors

UI_ifc = "view/ifc version1.ui"


class ButtonForSection(QtWidgets.QPushButton):
    def __init__(self, number, size):
        super().__init__()
        self.id = number
        self.setFixedSize(*size)


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.size_of_button = (20, 150)
        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        uic.loadUi(UI_ifc, self)
        if self.hight_section_action1.isChecked():
            self.groupBox1.show()
        else:
            self.groupBox1.hide()
        self.make_buttons(self.layout1)
        self.make_buttons(self.layout2)
        # self.make_buttons(self.layout_1000)
        # self.make_buttons(self.layout_10000)
        # self.make_buttons(self.layout_200)
        # self.make_buttons(self.layout_6)
        self.change_setting_action

        self.data_sensors_pushButton.clicked.connect(self.show_data_sensors)

    def make_buttons(self, layout):
        # num = self.section_max_lineEdit.text()
        # if num == "":
        #     num = 0
        # num = int(num)
        num = 100

        for elem in range(num):
            btn = ButtonForSection(elem + 1, self.size_of_button)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.on_clicked(b))
            layout.addWidget(btn)

    def on_clicked(self, btn):
        self.crep = CrepViewModel(btn.id)
        self.crep.show()

    def show_data_sensors(self):
        self.data_sensors.show()

    def show_settings_sensors(self):
        self.settings_sensors.show()
