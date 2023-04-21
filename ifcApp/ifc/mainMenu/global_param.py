from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

from ifcApp.ifc.mainMenu.globalparam_model import GlobalParamTable
from serviceApp.service.service_model import session

UI_all_parameter = "view/ifc/all parameter.ui"


class GlobalParam(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_all_parameter, self)
        self.exit_main_pushButton.clicked.connect(lambda: self.close())
        self.save_pushButton.clicked.connect(self.save_on_clicked_information)
        self.query_one = session.query(GlobalParamTable).all()
        print()
        if self.query_one == []:
            insert_into_setting_sensor_table1 = GlobalParamTable(id = 1,min_value=1, max_value=600, normal_value=300)
            insert_into_setting_sensor_table2 = GlobalParamTable(id = 2,min_value=2, max_value=600, normal_value=400)
            insert_into_setting_sensor_table3 = GlobalParamTable(id = 3,min_value=3, max_value=600, normal_value=500)
            insert_into_setting_sensor_table4 = GlobalParamTable(id = 4,min_value=4, max_value=600, normal_value=600)
            insert_into_setting_sensor_table5 = GlobalParamTable(id = 5,min_value=5, max_value=600, normal_value=700)
            session.add_all([insert_into_setting_sensor_table1, insert_into_setting_sensor_table2,
                             insert_into_setting_sensor_table3, insert_into_setting_sensor_table4,
                             insert_into_setting_sensor_table5])
            session.commit()
        row = 1
        for one_row_in_table in self.query_one:
            self.all_param_tableWidget.setItem(row, 0, QTableWidgetItem(f"{one_row_in_table.min_value}"))
            self.all_param_tableWidget.setItem(row, 1, QTableWidgetItem(f"{one_row_in_table.max_value}"))
            self.all_param_tableWidget.setItem(row, 2, QTableWidgetItem(f"{one_row_in_table.normal_value}"))
            row += 1

    def save_on_clicked_information(self):
        for row in range(len(self.query_one)):
            self.query_one[row].update_globalParamTable(self.all_param_tableWidget.item(row + 1, 0).text(),
                                                        self.all_param_tableWidget.item(row + 1, 1).text(),
                                                        self.all_param_tableWidget.item(row + 1, 2).text())
            row += 1
