from PyQt6 import uic, QtWidgets


UI_data_sensors = "view/sensors/data_sensors.ui"
UI_data_sensors_section = "view/sensors/data_sensors_section.ui"


class DataSensorsMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_data_sensors, self)
        # column = 0
        # for one in range(5):
        #     for elem in range(5):
        #         self.tableWidget.setItem(elem, column, QTableWidgetItem(f"{elem}"))
        #     column += 1


class DataSensorsSection(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_data_sensors_section, self)


