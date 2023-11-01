import time

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog
from ifcApp.settingsSensors.settings_sensorsWidget import SettingsSensorsWidget

UI_settings_sensors = "resources/view/sensors/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self, user_id, database):
        super().__init__()
        self.database = database
        self.user_id = user_id
        query = database.get_setting_sensors(user_id)
        if not query:
            database.add_settings_sensors_of_user(user_id)
        query_global_param = database.get_setting_sensors(user_id)
        uic.loadUi(UI_settings_sensors, self)
        self.list = []
        self.setGeometry(500, 100, 600, 600)
        for elem, value in enumerate(query_global_param):
            self.widget = SettingsSensorsWidget(elem + 1, value.sensor.name)
            self.layout_for_sensors.addWidget(self.widget)
            self.widget.color_normal_pushButton.setStyleSheet(
                'QPushButton { background-color: %s }' % value.color_normal_pushButton)
            self.widget.color_reduced_pushButton.setStyleSheet(
                'QPushButton { background-color: %s }' % value.color_reduced_pushButton)
            self.widget.color_increased_pushButton.setStyleSheet(
                'QPushButton { background-color: %s }' % value.color_increased_pushButton)
            self.widget.min_size_lineEdit.setText(str(value.min_value))
            self.widget.max_size_lineEdit.setText(str(value.max_value))
            self.widget.color_normal_pushButton.released.connect(
                lambda sensor_id=elem + 1: self.show_color_dialog(sensor_id))
            self.widget.color_reduced_pushButton.clicked.connect(
                lambda sensor_id=elem + 1: self.show_color_dialog(sensor_id))
            self.widget.color_increased_pushButton.clicked.connect(
                lambda sensor_id=elem + 1: self.show_color_dialog(sensor_id))

    def show_color_dialog(self, sensor_id):
        color_dialog = QColorDialog.getColor()

        if color_dialog.isValid():
            self.sender().setStyleSheet('QPushButton { background-color: %s }'
                                        % color_dialog.name())
            sending_button = self.sender()
            print('%s Clicked!' % str(sending_button.objectName()), f"number {sensor_id}")
            # print(color_dialog.name(), number,self.sender())
            # self.database.update_settings_sensors(self.user_id, sensor_id, color_dialog.name())
