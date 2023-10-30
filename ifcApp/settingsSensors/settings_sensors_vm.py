from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog
from ifcApp.settingsSensors.settings_sensorsWidget import SettingsSensorsWidget

UI_settings_sensors = "resources/view/sensors/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self, user_id, database):
        super().__init__()
        print(user_id)
        uic.loadUi(UI_settings_sensors, self)
        query_global_param = database.get_global_params()
        for i in query_global_param:
            self.widget = SettingsSensorsWidget(i.name)
            self.layout_for_sensors.addWidget(self.widget)


