from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog
from ifcApp.settingsSensors.settings_sensorsWidget import SettingsSensorsWidget

UI_settings_sensors = "resources/view/sensors/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self, user_id, database):
        super().__init__()
        self.database = database
        self.user_id = user_id
        self.check_color_in_database()
        query_global_param = database.get_setting_sensors(user_id)
        uic.loadUi(UI_settings_sensors, self)
        self.setGeometry(500, 100, 600, 600)
        for elem, value in enumerate(query_global_param):
            self.widget = SettingsSensorsWidget(value.sensor.name)
            self.layout_for_sensors.addWidget(self.widget)
            self.set_param_from_database(value)
            self.push_in_button(query_global_param[elem].sensor_id)

    def show_color_dialog(self, num, sensor_id):
        color_dialog = QColorDialog.getColor()
        if color_dialog.isValid():
            self.sender().setStyleSheet('QPushButton { background-color: %s }'
                                        % color_dialog.name())
        query_one_row = self.database.get_one_row_settings_sensors(self.user_id, sensor_id)
        self.database.update_setting_sensors(query_one_row, num, color_dialog.name())

    def push_in_button(self, number_id):
        self.widget.color_normal_pushButton.clicked.connect(
            lambda ch, sensor_id=number_id: self.show_color_dialog(1, sensor_id))
        self.widget.color_reduced_pushButton.clicked.connect(
            lambda ch, sensor_id=number_id: self.show_color_dialog(2, sensor_id))
        self.widget.color_increased_pushButton.clicked.connect(
            lambda ch, sensor_id=number_id: self.show_color_dialog(3, sensor_id))

    def set_param_from_database(self, value):
        self.widget.color_normal_pushButton.setStyleSheet(
            'QPushButton { background-color: %s }' % value.color_normal)
        self.widget.color_reduced_pushButton.setStyleSheet(
            'QPushButton { background-color: %s }' % value.color_reduced)
        self.widget.color_increased_pushButton.setStyleSheet(
            'QPushButton { background-color: %s }' % value.color_increased)
        self.widget.min_size_lineEdit.setText(str(value.min_value))
        self.widget.max_size_lineEdit.setText(str(value.max_value))

    def check_color_in_database(self):
        check_user_id_table = self.database.get_setting_sensors(self.user_id)
        if not check_user_id_table:
            self.database.add_settings_sensors_of_user(self.user_id)
