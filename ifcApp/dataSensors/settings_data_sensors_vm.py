from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QColorDialog



UI_settings_sensors = "resources/view/sensors/settings_sensors.ui"


class SettingsSensors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_settings_sensors, self)

    def show_color_dialog(self, button):
        color_dialog = QColorDialog.getColor()

        if color_dialog.isValid():
            button.setStyleSheet('QPushButton { background-color: %s }'
                                 % color_dialog.name())
        print(color_dialog.name())
