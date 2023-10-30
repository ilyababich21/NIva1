import time

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog
from ifcApp.settingsSensors.settings_sensorsWidget import SettingsSensorsWidget

UI_settings_sensors = "resources/view/sensors/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self, user_id, database):
        super().__init__()
        print(user_id)
        query = database.get_setting_sensors(user_id)
        if not query:
            database.add_settings_sensors_of_user(user_id)
        query_global_param = database.get_setting_sensors(user_id)
        uic.loadUi(UI_settings_sensors, self)
        self.setGeometry(500, 100, 600, 600)
        for elem, value in enumerate(query_global_param):
            self.widget = SettingsSensorsWidget(self, value.sensor.name)
            self.layout_for_sensors.addWidget(self.widget)
            self.widget.color_normal_pushButton.setStyleSheet(
                'QPushButton { background-color: %s }' % value.color_normal_pushButton)
            self.widget.color_reduced_pushButton.setStyleSheet(
                'QPushButton { background-color: %s }' % value.color_reduced_pushButton)
            self.widget.color_increased_pushButton.setStyleSheet(
                'QPushButton { background-color: %s }' % value.color_increased_pushButton)
            self.widget.min_size_lineEdit.setText(str(value.min_value))
            self.widget.max_size_lineEdit.setText(str(value.max_value))

    @staticmethod
    def show_color_dialog(button):
        color_dialog = QColorDialog.getColor()

        if color_dialog.isValid():
            button.setStyleSheet('QPushButton { background-color: %s }'
                                 % color_dialog.name())
        print(color_dialog.name(),)
