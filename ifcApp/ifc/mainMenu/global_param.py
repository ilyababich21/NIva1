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
        self.save_pushButton.clicked.connect(self.save_on_clicked_information)

        self.query_in_global_param_table = session.query(GlobalParamTable).all()

        if self.query_in_global_param_table == []:
            insert_into_setting_sensor_table1 = GlobalParamTable(id=1, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table2 = GlobalParamTable(id=2, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table3 = GlobalParamTable(id=3,min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table4 = GlobalParamTable(id=4, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table6 = GlobalParamTable(id=5,min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table7 = GlobalParamTable(id=6,min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table8 = GlobalParamTable(id=7, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table9 = GlobalParamTable(id=8, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table10 = GlobalParamTable(id=9, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table11 = GlobalParamTable(id=10, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table12 = GlobalParamTable(id=11, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table13 = GlobalParamTable(id=12, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table14 = GlobalParamTable(id=13, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table15 = GlobalParamTable(id=14, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            insert_into_setting_sensor_table5 = GlobalParamTable(id=15, min_value=0, max_value=600, from_normal_value=300,to_normal_value = 400,units = "bar")
            session.add_all([insert_into_setting_sensor_table1, insert_into_setting_sensor_table2,
                             insert_into_setting_sensor_table3, insert_into_setting_sensor_table4,
                             insert_into_setting_sensor_table6, insert_into_setting_sensor_table7,
                             insert_into_setting_sensor_table8, insert_into_setting_sensor_table9,
                             insert_into_setting_sensor_table10, insert_into_setting_sensor_table11,
                             insert_into_setting_sensor_table12, insert_into_setting_sensor_table13,
                             insert_into_setting_sensor_table14, insert_into_setting_sensor_table15,
                             insert_into_setting_sensor_table5])
            session.commit()
        row = 1
        for one_row_in_table in self.query_in_global_param_table:
            self.all_param_tableWidget.setItem(row, 0, QTableWidgetItem(f"{one_row_in_table.min_value}"))
            self.all_param_tableWidget.setItem(row, 1, QTableWidgetItem(f"{one_row_in_table.max_value}"))
            self.all_param_tableWidget.setItem(row, 2, QTableWidgetItem(f"{one_row_in_table.from_normal_value}"))
            self.all_param_tableWidget.setItem(row, 3, QTableWidgetItem(f"{one_row_in_table.to_normal_value}"))
            self.all_param_tableWidget.setItem(row, 4, QTableWidgetItem(f"{one_row_in_table.units}"))
            row += 1

    def save_on_clicked_information(self):
        for row in range(len(self.query_in_global_param_table)):
            self.query_in_global_param_table[row].update_globalParamTable(
                self.all_param_tableWidget.item(row + 1, 0).text(),
                self.all_param_tableWidget.item(row + 1, 1).text(),
                self.all_param_tableWidget.item(row + 1, 2).text(),
                self.all_param_tableWidget.item(row + 1, 3).text(),
                self.all_param_tableWidget.item(row + 1, 4).text())
            self.list_groupbox[row].min_value.setText(
                f"{self.query_in_global_param_table[row].min_value}")
            self.list_groupbox[row].max_value.setText(
                f"{self.query_in_global_param_table[row].max_value}")
            row += 1
        self.close()

