from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIntValidator

from connection_to_db import session
from ifcApp.countShield.count_shield_model import CountShieldModel
from serviceApp.service.service_model import Manufacture

UI_count_shield = "view/ifc/count shield.ui"


class CountShieldVM(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.model = CountShieldModel()
        uic.loadUi(UI_count_shield, self)
        self.count_shield_lineEdit.setText(F"{self.model.get_count_shield()}")
        self.count_shield_lineEdit.setValidator(QIntValidator())

    def get_and_save_number_from_lineedit(self):
        print(self.model.get_count_shield())
        self.model.count_shield.update_manufacture(self.count_shield_lineEdit.text())
        self.close()
