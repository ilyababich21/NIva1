from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

UI_all_parameter = "resources/view/ifc/toolbar/global parameter.ui"


class GlobalParam(QtWidgets.QMainWindow):
    list_groupbox = []

    def __init__(self,database):
        super().__init__()
        self.database=database
        uic.loadUi(UI_all_parameter, self)
        self.exit_main_pushButton.clicked.connect(lambda: self.close())

        self.query_in_global_param_table = self.database.global_params()

        for row in range(len(self.query_in_global_param_table)):
            self.all_param_tableWidget.setItem(row + 1, 0,
                                               QTableWidgetItem(f"{self.query_in_global_param_table[row].min_value}"))
            self.all_param_tableWidget.setItem(row + 1, 1,
                                               QTableWidgetItem(f"{self.query_in_global_param_table[row].max_value}"))
            self.all_param_tableWidget.setItem(row + 1, 2, QTableWidgetItem(
                f"{self.query_in_global_param_table[row].from_normal_value}"))
            self.all_param_tableWidget.setItem(row + 1, 3, QTableWidgetItem(
                f"{self.query_in_global_param_table[row].to_normal_value}"))
            self.all_param_tableWidget.setItem(row + 1, 4,
                                               QTableWidgetItem(f"{self.query_in_global_param_table[row].units}"))

    def save_on_clicked_information(self):
        for row in range(len(self.query_in_global_param_table)):
            self.database.update_global_params(self.query_in_global_param_table[row],
                [self.all_param_tableWidget.item(row + 1, num).text() for num in range(5)])
            self.list_groupbox[row].min_value.setText(
                f"{self.query_in_global_param_table[row].min_value}")
            self.list_groupbox[row].max_value.setText(
                f"{self.query_in_global_param_table[row].max_value}")
        self.close()
