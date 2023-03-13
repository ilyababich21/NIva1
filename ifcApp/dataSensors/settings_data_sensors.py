from PyQt6 import uic, QtWidgets

UI_settings_sensors = "view/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_settings_sensors, self)
