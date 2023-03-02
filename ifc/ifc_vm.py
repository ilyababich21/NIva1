from PyQt6 import uic, QtWidgets

UI_ifc = "view/ifc_model_view.ui"


class ButtonForSection(QtWidgets.QMainWindow):
    def __init__(self, number):
        super().__init__()


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_ifc, self)
