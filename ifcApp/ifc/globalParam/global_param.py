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
        self.all_param_tableWidget.setRowCount(len(self.query_in_global_param_table))
        self.all_param_tableWidget.setVerticalHeaderLabels([str(param.id) for param in self.query_in_global_param_table])
        self.add_button.clicked.connect(self.add_row)
        self.del_button.clicked.connect(self.del_row)



        for row in range(len(self.query_in_global_param_table)):
            self.all_param_tableWidget.setItem(row , 0,
                                               QTableWidgetItem(self.query_in_global_param_table[row].name))
            self.all_param_tableWidget.setItem(row , 1,
                                               QTableWidgetItem(f"{self.query_in_global_param_table[row].min_value}"))
            self.all_param_tableWidget.setItem(row , 2,
                                               QTableWidgetItem(f"{self.query_in_global_param_table[row].max_value}"))
            self.all_param_tableWidget.setItem(row , 3, QTableWidgetItem(
                f"{self.query_in_global_param_table[row].from_normal_value}"))
            self.all_param_tableWidget.setItem(row , 4, QTableWidgetItem(
                f"{self.query_in_global_param_table[row].to_normal_value}"))
            self.all_param_tableWidget.setItem(row , 5,
                                               QTableWidgetItem(f"{self.query_in_global_param_table[row].units}"))

    def add_row(self):
        pass

    def del_row(self):
        # print(self.all_param_tableWidget.selectedItems())
        print(self.all_param_tableWidget.currentRow())

    def save_on_clicked_information(self):
        for row in range(len(self.query_in_global_param_table)):
            self.database.update_global_params(self.query_in_global_param_table[row],
                [self.all_param_tableWidget.item(row, num).text() for num in range(6)])
            self.list_groupbox[row].min_value.setText(
                str(self.query_in_global_param_table[row].min_value))
            self.list_groupbox[row].max_value.setText(
                str(self.query_in_global_param_table[row].max_value))
            self.list_groupbox[row].name_label.setText(
                self.query_in_global_param_table[row].name)
        self.close()
