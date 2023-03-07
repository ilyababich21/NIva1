from PyQt6 import uic, QtWidgets

UI_crep = "view/ifc_crep.ui"


class CrepViewModel(QtWidgets.QMainWindow):
    def __init__(self, num):
        super().__init__()

        uic.loadUi(UI_crep, self)
        self.num_crep.setText(str(num))
