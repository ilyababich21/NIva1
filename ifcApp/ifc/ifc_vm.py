from PyQt6 import uic, QtWidgets

from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.dataSensors.data_sensors_vm import DataSensorsMainWindow
from ifcApp.dataSensors.settings_data_sensors import SettingsSensors

UI_ifc = "view/ifc version1.ui"


class ButtonForSection(QtWidgets.QPushButton):
    def __init__(self, number):
        super().__init__()
        self.id = number
        self.setFixedHeight(100)


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.size_of_button = ()
        self.settings_sensors = SettingsSensors()
        self.data_sensors = DataSensorsMainWindow()
        uic.loadUi(UI_ifc, self)
        self.show_button()

        self.v_action.triggered.connect(self.checked_action)
        self.zaz_action.triggered.connect(self.checked_action)
        self.pressure_stand1_action.triggered.connect(self.checked_action)
        self.pressure_stand2_action.triggered.connect(self.checked_action)
        self.shield_UGZ_action.triggered.connect(self.checked_action)
        self.shield_UGZ_sensor_approximation_action.triggered.connect(self.checked_action)
        self.shield_UGZ_angle_action.triggered.connect(self.checked_action)
        self.shield_UGZ_shifting_action.triggered.connect(self.checked_action)
        self.shield_UGZ_pressure_action.triggered.connect(self.checked_action)
        self.shield_UGZ_3rasp_abbr_action.triggered.connect(self.checked_action)
        self.top_drawer_action.triggered.connect(self.checked_action)
        self.top_drawer_shifting_action.triggered.connect(self.checked_action)
        self.visor_action.triggered.connect(self.checked_action)
        self.state_overlap_action.triggered.connect(self.checked_action)
        self.height_section_action1.triggered.connect(self.checked_action)
        self.height_section_action2.triggered.connect(self.checked_action)
        self.height_section_action3.triggered.connect(self.checked_action)

        self.change_setting_action.triggered.connect(self.show_settings_sensors)
        self.data_sensors_pushButton.clicked.connect(self.show_data_sensors)

        self.Ok_button.clicked.connect(self.show_button)
    def show_button(self):
        self.make_buttons(self.layout_100)
        self.make_buttons(self.layout_200)
        self.make_buttons(self.layout_300)
        self.make_buttons(self.layout_400)
        self.make_buttons(self.layout_500)
        self.make_buttons(self.layout_600)
        self.make_buttons(self.layout_700)
        self.make_buttons(self.layout_800)
        self.make_buttons(self.layout_900)
        self.make_buttons(self.layout_1000)
        self.make_buttons(self.layout_1100)
        self.make_buttons(self.layout_1200)
        self.make_buttons(self.layout_1300)
        self.make_buttons(self.layout_1400)
        self.make_buttons(self.layout_1500)
        self.make_buttons(self.layout_1600)
        self.make_buttons(self.layout_1700)


    def make_buttons(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().deleteLater()
        for elem in range(int(self.section_max_lineEdit.text())):
            btn = ButtonForSection(elem + 1)  # !!!
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
            self.settings_sensors.close()

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

        if self.top_drawer_action.isChecked():
            self.groupBox10.show()

        else:
            self.groupBox10.hide()

        if self.top_drawer_shifting_action.isChecked():
            self.groupBox11.show()

        else:
            self.groupBox11.hide()

        if self.shield_UGZ_3rasp_abbr_action.isChecked():
            self.groupBox12.show()

        else:
            self.groupBox12.hide()

        if self.visor_action.isChecked():
            self.groupBox13.show()

        else:
            self.groupBox13.hide()

        if self.state_overlap_action.isChecked():
            self.groupBox14.show()

        else:
            self.groupBox14.hide()

        if self.state_overlap_action.isChecked():
            self.groupBox14.show()

        else:
            self.groupBox14.hide()

        if self.height_section_action1.isChecked():
            self.groupBox15.show()

        else:
            self.groupBox15.hide()

        if self.height_section_action2.isChecked():
            self.groupBox16.show()

        else:
            self.groupBox16.hide()

        if self.height_section_action3.isChecked():
            self.groupBox17.show()

        else:
            self.groupBox17.hide()
