from PyQt6 import uic, QtWidgets

UI_data_sensors = "view/data_sensors.ui"


class DataSensors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_data_sensors, self)
