from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

from ifcApp.countShield.count_shield_model import CountShieldModel

UI_count_shield = "resources/view/ifc/toolbar/count shield.ui"


class CountShieldVM(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.model = CountShieldModel()
        uic.loadUi(UI_count_shield, self)
        self.count_shield_lineEdit.setText(str(self.model.get_count_shield()))
        regex = QRegularExpression("[1-9]|[1-9][0-9]|1[0-9]{2}|200")
        validator = QRegularExpressionValidator(regex, self.count_shield_lineEdit)
        self.count_shield_lineEdit.setValidator(validator)

    def get_and_save_number_from_lineedit(self):
        self.model.count_shield.update_manufacture(self.count_shield_lineEdit.text())
        self.close()
