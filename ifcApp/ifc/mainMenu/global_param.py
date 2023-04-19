from PyQt6 import uic, QtWidgets

UI_all_parameter = "view/ifc/all parameter.ui"


class GlobalParam(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_all_parameter, self)
        self.exit_main_pushButton.clicked.connect(lambda :self.close())