from PyQt6 import uic, QtWidgets

UI_data_sensors = "view/data_sensors.ui"
UI_data_sensors_section = "view/data_sensors_section.ui"


class DataSensorsMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_data_sensors, self)


class DataSensorsSection(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_data_sensors_section, self)
