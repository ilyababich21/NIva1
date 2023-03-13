from PyQt6 import uic, QtWidgets

from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors import SettingsSensors

UI_ifc = "view/ifc version1.ui"


class ButtonForSection(QtWidgets.QPushButton):
    def __init__(self, number, size):
        super().__init__()
        self.id = number
        self.setFixedSize(*size)


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.size_of_button = (20, 100)
        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        uic.loadUi(UI_ifc, self)

        self.make_buttons(self.layout_100)
        self.make_buttons(self.layout_200)
        self.make_buttons(self.layout_300)
        self.make_buttons(self.layout_400)
        self.make_buttons(self.layout_500)
        self.make_buttons(self.layout_600)
        self.make_buttons(self.layout_700)
        self.make_buttons(self.layout_800)
        self.make_buttons(self.layout_900)

        self.v_action.triggered.connect(self.checked_action)
        self.zaz_action.triggered.connect(self.checked_action)
        self.pressure_stand1_action.triggered.connect(self.checked_action)
        self.pressure_stand2_action.triggered.connect(self.checked_action)
        self.shield_UGZ_action.triggered.connect(self.checked_action)
        self.shield_UGZ_sensor_approximation_action.triggered.connect(self.checked_action)
        self.shield_UGZ_angle_action.triggered.connect(self.checked_action)
        self.shield_UGZ_shifting_action.triggered.connect(self.checked_action)
        self.shield_UGZ_pressure_action.triggered.connect(self.checked_action)

        self.change_setting_action.triggered.connect(self.show_settings_sensors)
        self.data_sensors_pushButton.clicked.connect(self.show_data_sensors)

    def make_buttons(self, layout):
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
        if self.change_setting_action.isChecked():
            self.settings_sensors.show()
        else:
            self.settings_sensors.hide()

    def checked_action(self):
        if self.v_action.isChecked():
            self.groupBox1.show()
        else:
            self.groupBox1.hide()

        if self.zaz_action.isChecked():
            self.groupBox2.show()
        else:
            self.groupBox2.hide()

        if self.pressure_stand1_action.isChecked():
            self.groupBox3.show()
        else:
            self.groupBox3.hide()

        if self.pressure_stand2_action.isChecked():
            self.groupBox4.show()
        else:
            self.groupBox4.hide()

        if self.shield_UGZ_action.isChecked():
            self.groupBox5.show()
        else:
            self.groupBox5.hide()

        if self.shield_UGZ_sensor_approximation_action.isChecked():
            self.groupBox6.show()
        else:
            self.groupBox6.hide()

        if self.shield_UGZ_angle_action.isChecked():
            self.groupBox7.show()

        else:
            self.groupBox7.hide()

        if self.shield_UGZ_shifting_action.isChecked():
            self.groupBox8.show()

        else:
            self.groupBox8.hide()

        if self.shield_UGZ_pressure_action.isChecked():
            self.groupBox9.show()

        else:
            self.groupBox9.hide()


