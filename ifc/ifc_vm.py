from PyQt6 import uic, QtWidgets

UI_ifc = "view/ifc_model_view.ui"


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def load_ifc_UI(self):
        uic.loadUi(UI_ifc, self)
