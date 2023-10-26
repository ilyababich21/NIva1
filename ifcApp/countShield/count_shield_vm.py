from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator


UI_count_shield = "resources/view/ifc/toolbar/count shield.ui"


class CountShieldVM(QtWidgets.QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        uic.loadUi(UI_count_shield, self)
        self.count_shield_lineEdit.setText(str(self.database.get_count_shield()))
        regex = QRegularExpression("[1-9]|[1-9][0-9]|1[0-9]{2}|200")
        validator = QRegularExpressionValidator(regex, self.count_shield_lineEdit)
        self.count_shield_lineEdit.setValidator(validator)

    def get_and_save_number_from_lineedit(self):
        self.database.update_count_shield(self.count_shield_lineEdit.text())
        self.close()
