import os

from PyQt6 import QtCore
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from PyQt6.QtWidgets import QTableWidgetItem

from address import resource_path
from ifcApp.crep.all_sensors_crep import AllSensorsCrep
from ifcApp.crep.graphicscene.graphicscene import CreateGraphicScene
from ifcApp.crep.labelWidget import LabelWidget
from ifcApp.crep.progressbar.progressbar import ClickedProgressbar
from ifcApp.dataSensors.data_sensors_vm import DataSensorsSection
from ifcApp.ifc.globalParam.global_param import GlobalParam

UI_crep = resource_path("resources\\view\\ifc\\crep\\ifc_crep.ui")


class CrepViewModel(QtWidgets.QMainWindow):
    num = 1
    data = {
        "id_dat": [],
        "value": [],
        "crep_id": [],
    }
    my_signal = QtCore.pyqtSignal(list, int)
    def __init__(self, num, database, pizda):
        super().__init__()
        self.num = num
        self.database = database
        # self.all_sensors_crep = AllSensorsCrep(self.database)
        uic.loadUi(UI_crep, self)
        self.global_param = pizda
        self.data_sensors_section = DataSensorsSection()

        self.list_sensors_lineEdit = []

        self.list_of_sensors_layouts = (self.CP_layout, self.gridLayout5, self.gridLayout1, self.gridLayout2,
                                        self.gridLayout3,
                                        self.gridLayout4,
                                        self.pozition_layout, self.prod_layout,
                                        self.poper_layout, self.end_section_layout, self.poper_hieght_layout,
                                        self.section_one_layout, self.section_two_layout, self.section_three_layout,
                                        self.poz_shifting_layout)

        for elem in range(11):
            speed = CreateGraphicScene(self.global_param[elem].max_value,self.database, self)
            speed.graphicsView.crep_id = self.num
            speed.graphicsView.id_dat = elem + 1
            speed.label.setText(f"{self.global_param[elem].name}")
            self.list_of_sensors_layouts[elem].addWidget(speed)
            self.list_sensors_lineEdit.append(speed.lineedit)

        for bar in range(4):
            section1_progressBar = ClickedProgressbar(self.global_param[bar + 11].max_value,self.database)
            self.list_sensors_lineEdit.append(section1_progressBar.lineedit)
            section1_progressBar.id_dat = bar + 11
            section1_progressBar.crep_id = self.num
            self.list_of_sensors_layouts[bar + 11].addWidget(section1_progressBar)
            section1_progressBar.label.setText(f"{self.global_param[bar + 11].name}")
        self.num_crep.setText(str(num))
        self.control_pushbutton.clicked.connect(lambda: self.data_sensors_section.show())
        # self.all_sensors_pushButton.clicked.connect(lambda: self.all_sensors_crep.show())

    @staticmethod
    def show_sensor_data(lineEdit):
        return lineEdit.text()

    @QtCore.pyqtSlot(list)
    def setText_lineEdit_sensors(self, lst):
        self.my_signal.emit(lst,self.num)
        for elem in range(len(lst)):
            # self.all_sensors_crep.label1.setText(str(lst[0]))
            # self.all_sensors_crep.list_progressBar[0].setValue(lst[0])
            self.data_sensors_section.tableWidget.setItem(elem, 0, QTableWidgetItem(str(lst[elem])))
            self.list_sensors_lineEdit[elem].setText(str(lst[elem]))
