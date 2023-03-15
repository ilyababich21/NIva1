from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog

from serviceApp.service.service_model import session
from ifcApp.dataSensors.setting_data_sensors_model import SettingsSensorsTable

UI_settings_sensors = "view/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_settings_sensors, self)
        # self.setting = session.query(SettingsSensorsTable).all()
        # for n in self.setting:
        #     print(n.id)
        #self.color_error_sensors_pushButton.setStyleSheet('QPushButton { background-color: %s }'% self.setting.color_button_one)
        # for p in self.setting:
        self.color_error_sensors_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_error_sensors_pushButton))
        self.color_sensor_broken_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_sensor_broken_pushButton))
        self.color_sensor_CO_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_sensor_CO_pushButton))
        self.color_sensor_gaz_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_sensor_gaz_pushButton))
        self.color_sensor_dust_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_sensor_dust_pushButton))
        self.color_temperature_inside_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_temperature_inside_pushButton))
        self.color_wetness_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_wetness_pushButton))
        self.color_shifting_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_shifting_pushButton))
        self.color_shifting_height_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_shifting_height_pushButton))
        self.color_height__pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_height__pushButton))
        self.color_height_coal_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_height_coal_pushButton))
        self.color_height_section1_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_height_section1_pushButton))
        self.color_height_section2_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_height_section2_pushButton))
        self.color_height_section3_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_height_section3_pushButton))
        self.color_podzh_pressure_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_podzh_pressure_pushButton))
        self.color_podzh_position_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_podzh_position_pushButton))
        self.color_extention_top_shifting_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_extention_top_shifting_pushButton))
        self.color_extention_top_sensor_appr_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_extention_top_sensor_appr_pushButton))
        self.color_extention_top_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_extention_top_pushButton))
        self.color_shield_UGZ_pressure_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_shield_UGZ_pressure_pushButton))
        self.color_shield_angle_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_shield_angle_pushButton))
        self.color_shield_UGZ_sensor_appr_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_shield_UGZ_sensor_appr_pushButton))
        self.color_shield_UGZ_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_shield_UGZ_pushButton))
        self.color_CP_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_CP_pushButton))
        self.color_logitudinal_floor_slope_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_logitudinal_floor_slope_pushButton))
        self.color_transversal_slope_floor_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_transversal_slope_floor_pushButton))
        self.color_log_base_slope_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_log_base_slope_pushButton))
        self.color_transversal_slope_base_pushButton.clicked.connect(
            lambda: self.show_color_dialog(self.color_transversal_slope_base_pushButton))

    def show_color_dialog(self, button):
        color_dialog = QColorDialog.getColor()

        if color_dialog.isValid():
            button.setStyleSheet('QPushButton { background-color: %s }'
                                 % color_dialog.name())
        print(color_dialog.name())
