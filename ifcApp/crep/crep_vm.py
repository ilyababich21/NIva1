from PyQt6 import QtCore
from PyQt6 import uic, QtWidgets

from ifcApp.crep.graphicscene.graphicscene import CreateGraphicScene
from ifcApp.crep.progressbar.progressbar import ClickedProgressbar
from ifcApp.dataSensors.data_sensors_vm import DataSensorsSection

UI_crep = "view/ifc/ifc_crep.ui"


class CrepViewModel(QtWidgets.QMainWindow):
    def __init__(self, num):
        super().__init__()
        uic.loadUi(UI_crep, self)

        self.list_sensors_lineEdit = [self.sensors1_lineEdit, self.sensors2_lineEdit, self.sensors3_lineEdit,
                                      self.sensors4_lineEdit, self.sensors5_lineEdit, self.pozition_lineEdit,
                                      self.CP_lineEdit, self.prod_lineEdit, self.poper_lineEdit,
                                      self.end_section_lineEdit,
                                      self.poper_hieght_lineEdit]

        self.list_of_sensors_layouts = [self.gridLayout1, self.gridLayout2, self.gridLayout3, self.gridLayout4,
                                        self.gridLayout5, self.pozition_layout, self.CP_layout, self.prod_layout,
                                        self.poper_layout, self.end_section_layout, self.poper_hieght_layout]

        self.list_bar_layouts = [self.section_one_layout, self.section_two_layout, self.section_three_layout,
                                 self.poz_shifting_layout]

        self.list_bar_lineEdits = [self.section_one_lineEdit, self.section_two_lineEdit, self.section_three_lineEdit,
                                   self.poz_shifting_lineEdit]

        for lent in range(len(self.list_of_sensors_layouts)):
            speed = CreateGraphicScene(self)
            self.list_of_sensors_layouts[lent].addWidget(speed.graphicsView)
            self.list_of_sensors_layouts[lent].addWidget(self.list_sensors_lineEdit[lent])
            self.list_sensors_lineEdit[lent].textChanged.connect\
                (lambda ch, s=speed, l=self.list_sensors_lineEdit[lent]: s.valuechange(l))

        for bar in range(len(self.list_bar_layouts)):
            section1_progressBar = ClickedProgressbar()
            self.list_bar_layouts[bar].addWidget(section1_progressBar)
            self.list_bar_layouts[bar].addWidget(self.list_bar_lineEdits[bar])
            self.list_bar_lineEdits[bar].textChanged.connect(
                lambda ch, s=section1_progressBar, l=self.list_bar_lineEdits[bar]: s.diff_value_progress_bar(l, s))

        self.data_sensors_section = DataSensorsSection()
        self.num_crep.setText(str(num))
        self.control_pushbutton.clicked.connect(self.show_data_sensors_section)

    def show_data_sensors_section(self):
        self.data_sensors_section.show()

    def show_sensor1_data(self, lineEde):
        return lineEde.text()

    def show_sensor2_data(self):
        return self.sensors2_lineEdit.text()

    @QtCore.pyqtSlot(str)
    def setText1(self, string):
        self.sensors1_lineEdit.setText(string)

    @QtCore.pyqtSlot(str)
    def setText2(self, string):
        self.sensors2_lineEdit.setText(string)

    #
    @QtCore.pyqtSlot(str)
    def setText3(self, string):
        self.sensors3_lineEdit.setText(string)

    @QtCore.pyqtSlot(list)
    def setText1(self, lst):
        for lEd in range(len(self.list_sensors_lineEdit)):
            self.list_sensors_lineEdit[lEd].setText(str(lst[lEd]))
