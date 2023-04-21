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
        self.object_database = session.get(GlobalParamTable, 1)
        if self.query_one == []:
            insert_into_setting_sensor_table1 = GlobalParamTable(min_value=0, max_value=600, normal_value=300)
            session.add_all([insert_into_setting_sensor_table1])
            session.commit()
        for one_row_in_table in self.query_one:
            if one_row_in_table.id == 1:
                self.all_param_tableWidget.setItem(1, 0, QTableWidgetItem(f"{one_row_in_table.min_value}"))
                self.all_param_tableWidget.setItem(1, 1, QTableWidgetItem(f"{one_row_in_table.max_value}"))
                self.all_param_tableWidget.setItem(1, 2, QTableWidgetItem(f"{one_row_in_table.normal_value}"))

    def save_on_clicked_information(self):
        self.object_database.update_globalParamTable(self.all_param_tableWidget.item(1, 0).text(),
                                                     self.all_param_tableWidget.item(1, 1).text(),
                                                     self.all_param_tableWidget.item(1, 2).text())

        session.refresh(self.object_database)
