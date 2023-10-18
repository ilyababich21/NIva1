from PyQt6 import uic, QtWidgets
from ifcApp.ifc.globalParam.global_param import GlobalParam

UI_menu = "resources/view/ifc/general menu.ui"


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_menu, self)
        self.global_param = GlobalParam()
        self.general_menu_pushButton.clicked.connect(lambda : self.global_param.show())



