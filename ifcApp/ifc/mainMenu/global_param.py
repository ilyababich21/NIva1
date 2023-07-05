from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

from ifcApp.ifc.mainMenu.globalparam_model import GlobalParamTable
from serviceApp.service.service_model import session

UI_all_parameter = "view/ifc/global parameter.ui"


class GlobalParam(QtWidgets.QMainWindow):
    list_groupbox = []

    def __init__(self):
        super().__init__()
        uic.loadUi(UI_all_parameter, self)
        self.exit_main_pushButton.clicked.connect(lambda: self.close())

        self.query_in_global_param_table = session.query(GlobalParamTable).all()

        if self.query_in_global_param_table == []:
            session.add_all([GlobalParamTable(id=id, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar") for id in range(1,16)])
            session.commit()

        for row in range(len(self.query_in_global_param_table)):
            self.all_param_tableWidget.setItem(row+1, 0, QTableWidgetItem(f"{self.query_in_global_param_table[row].min_value}"))
            self.all_param_tableWidget.setItem(row+1, 1, QTableWidgetItem(f"{self.query_in_global_param_table[row].max_value}"))
            self.all_param_tableWidget.setItem(row+1, 2, QTableWidgetItem(f"{self.query_in_global_param_table[row].from_normal_value}"))
            self.all_param_tableWidget.setItem(row+1, 3, QTableWidgetItem(f"{self.query_in_global_param_table[row].to_normal_value}"))
            self.all_param_tableWidget.setItem(row+1, 4, QTableWidgetItem(f"{self.query_in_global_param_table[row].units}"))


    def save_on_clicked_information(self):
        for row in range(len(self.query_in_global_param_table)):
            self.query_in_global_param_table[row].update_globalParamTable([self.all_param_tableWidget.item(row + 1, num).text() for num in range(5)])
            self.list_groupbox[row].min_value.setText(
                f"{self.query_in_global_param_table[row].min_value}")
            self.list_groupbox[row].max_value.setText(
                f"{self.query_in_global_param_table[row].max_value}")
        self.close()

