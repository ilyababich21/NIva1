from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog
from ifcApp.settingsSensors.settings_sensorsWidget import SettingsSensorsWidget
UI_settings_sensors = "resources/view/sensors/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_settings_sensors, self)
        for i in range(15):
            self.wiget = SettingsSensorsWidget(i)
            self.layout_for_sensors.addWidget(self.wiget)
