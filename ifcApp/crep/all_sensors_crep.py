from PyQt6 import uic, QtWidgets

UI_sernsors = "view/ifc/sensors crep.ui"


class AllSensorsCrep(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_sernsors, self)
