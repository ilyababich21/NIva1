from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog

from serviceApp.service.service_model import session
from ifcApp.dataSensors.setting_data_sensors_model import SettingsSensorsTable

UI_settings_sensors = "view/sensors/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_settings_sensors, self)

        self.setting_query_all = session.query(SettingsSensorsTable).all()

        if self.setting_query_all == []:
            insert_into_setting_sensor_table1 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table2 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table3 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table4 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table5 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table6 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table7 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table8 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table9 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                     color_button_two="#55aa00",
                                                                     color_button_three="#55aa00", min_value=1,
                                                                     max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table10 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table11 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table12 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table13 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table14 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table15 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table16 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table17 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)
            insert_into_setting_sensor_table18 = SettingsSensorsTable(color_button_one="#55aa00",
                                                                      color_button_two="#55aa00",
                                                                      color_button_three="#55aa00", min_value=1,
                                                                      max_value=2, coefficient_value=1)

            session.add_all([insert_into_setting_sensor_table1, insert_into_setting_sensor_table2,
                             insert_into_setting_sensor_table3, insert_into_setting_sensor_table4,
                             insert_into_setting_sensor_table5, insert_into_setting_sensor_table6,
                             insert_into_setting_sensor_table7, insert_into_setting_sensor_table8,
                             insert_into_setting_sensor_table9, insert_into_setting_sensor_table10,
                             insert_into_setting_sensor_table11, insert_into_setting_sensor_table12,
                             insert_into_setting_sensor_table13, insert_into_setting_sensor_table14,
                             insert_into_setting_sensor_table15, insert_into_setting_sensor_table16,
                             insert_into_setting_sensor_table17, insert_into_setting_sensor_table18])
            session.commit()
            self.setting_query_all = session.query(SettingsSensorsTable).all()
        for one_row_in_query in self.setting_query_all:
            if one_row_in_query.id == 1:
                self.color_error_sensors_pushButton.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
            if one_row_in_query.id == 2:
                self.color_sensor_broken_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
            if one_row_in_query.id == 3:
                self.distance_between_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 4:
                self.automatic_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.automatic_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.automatic_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 5:
                self.color_between_time_pushButton1.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.color_between_time_pushButton2.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.color_between_time_pushButton3.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.between_time_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.between_time_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.between_time_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 6:
                self.color_time_work_cycle_pushButton1.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.color_time_work_cycle_pushButton2.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.color_time_work_cycle_pushButton3.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.time_work_cycle_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.time_work_cycle_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.time_work_cycle_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 7:
                self.color_time_upload_pushButton1.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.color_time_upload_pushButton2.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.color_time_upload_pushButton3.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.time_upload_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.time_upload_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.time_upload_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 8:
                self.color_time_shifting_pushButton1.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.color_time_shifting_pushButton2.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.color_time_shifting_pushButton3.setStyleSheet(
                    'QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.time_shifting_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.time_shifting_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.time_shifting_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 9:
                self.color_time_thrust_pushButton1.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.color_time_thrust_pushButton2.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.color_time_thrust_pushButton3.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.time_thrust_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.time_thrust_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.time_thrust_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 10:
                self.time_upload_in_trust_pushButton1.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.time_upload_in_trust_pushButton2.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.time_upload_in_trust_pushButton3.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.time_upload_in_trust_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.time_upload_in_trust_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.time_upload_in_trust_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 11:
                self.time_upload_in_location_pushButton1.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.time_upload_in_location_pushButton2.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.time_upload_in_location_pushButton3.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.time_upload_in_location_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.time_upload_in_location_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.time_upload_in_location_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 12:
                self.time_trust_height_pressure_pushButton1.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.time_trust_height_pressure_pushButton2.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.time_trust_height_pressure_pushButton3.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.time_trust_height_pressure_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.time_trust_height_pressure_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.time_trust_height_pressure_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 13:
                self.function_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.function_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.function_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 14:
                self.color_sound_light_pushButton1.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.color_sound_light_pushButton2.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_two)
                self.color_sound_light_pushButton3.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_three)
                self.sound_light_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.sound_light_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.sound_light_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 15:
                self.color_synch_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.synch_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.synch_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.synch_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 16:
                self.color_resist_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.resist_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.resist_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.resist_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 17:
                self.neighboring_section_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.neighboring_section_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.neighboring_section_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 18:
                self.color_current_cons_now_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.current_cons_now_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.current_cons_now_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.current_cons_now_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 19:
                self.color_current_cons_valve_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
                self.current_cons_valve_min_value_lineEdit.setText(str(one_row_in_query.min_value))
                self.current_cons_valve_max_value_lineEdit.setText(str(one_row_in_query.max_value))
                self.current_cons_valve_coeff_lineEdit.setText(str(one_row_in_query.coefficient_value))
            if one_row_in_query.id == 20:
                self.color_current_all_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)

            if one_row_in_query.id == 21:
                self.color_sipply_voltage_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)

            if one_row_in_query.id == 22:
                self.color_sensor_sipply_voltage_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)

            if one_row_in_query.id == 23:
                self.color_valve_sipply_voltage_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
            # if one_row_in_query.id == 24:
            # if one_row_in_query.id == 25:
            # if one_row_in_query.id == 26:
            if one_row_in_query.id == 27:
                self.color_transversal_slope_base_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)
            if one_row_in_query.id == 28:
                self.color_log_base_slope_pushButton.setStyleSheet('QPushButton { background-color: %s }' % one_row_in_query.color_button_one)

            # if one_row_in_query.id == 29:
            # if one_row_in_query.id == 30:
            # if one_row_in_query.id == 31:
            # if one_row_in_query.id == 32:
            # if one_row_in_query.id == 33:
            # if one_row_in_query.id == 34:
            # if one_row_in_query.id == 34:
            # if one_row_in_query.id == 36:
            # if one_row_in_query.id == 37:
            # if one_row_in_query.id == 38:
            # if one_row_in_query.id == 39:
            # if one_row_in_query.id == 40:
            # if one_row_in_query.id == 41:
            # if one_row_in_query.id == 42:
            # if one_row_in_query.id == 43:
            # if one_row_in_query.id == 44:

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
