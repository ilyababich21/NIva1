from PyQt6 import QtCore
from PyQt6 import uic, QtWidgets

from ifcApp.crep.all_sensors_crep import AllSensorsCrep
from ifcApp.crep.graphicscene.graphicscene import CreateGraphicScene
from ifcApp.crep.progressbar.progressbar import ClickedProgressbar
from ifcApp.dataSensors.data_sensors_vm import DataSensorsSection
from ifcApp.ifc.mainMenu.global_param import GlobalParam

UI_crep = "view/ifc/crep/ifc_crep.ui"


class CrepViewModel(QtWidgets.QMainWindow):
    num = 1
    data={
        "id_dat":[],
    "value":[],
    "crep_id":[],
}
    def __init__(self, num):
        super().__init__()
        self.num=num
        self.all_sensors_crep = AllSensorsCrep()
        uic.loadUi(UI_crep, self)
        self.global_param = GlobalParam()

        self.list_sensors_lineEdit = [self.sensors1_lineEdit, self.sensors2_lineEdit, self.sensors3_lineEdit,
                                      self.sensors4_lineEdit, self.sensors5_lineEdit, self.pozition_lineEdit,
                                      self.CP_lineEdit, self.prod_lineEdit, self.poper_lineEdit,
                                      self.end_section_lineEdit,
                                      self.poper_hieght_lineEdit

                                      ,self.section_one_lineEdit, self.section_two_lineEdit, self.section_three_lineEdit,
                                      self.poz_shifting_lineEdit


                                      ]

        self.list_of_sensors_layouts = [self.gridLayout1, self.gridLayout2, self.gridLayout3, self.gridLayout4,
                                        self.gridLayout5, self.pozition_layout, self.CP_layout, self.prod_layout,
                                        self.poper_layout, self.end_section_layout, self.poper_hieght_layout,


                                        self.section_one_layout, self.section_two_layout, self.section_three_layout,
                                        self.poz_shifting_layout


                                        ]

        # self.list_bar_layouts = [self.section_one_layout, self.section_two_layout, self.section_three_layout,
        #                          self.poz_shifting_layout]
        #
        # self.list_bar_lineEdits = [self.section_one_lineEdit, self.section_two_lineEdit, self.section_three_lineEdit,
        #                            self.poz_shifting_lineEdit]

        for lent in range(11):
            # for lent in range(len(self.list_of_sensors_layouts)):
            speed = CreateGraphicScene(self)
            self.list_of_sensors_layouts[lent].addWidget(speed.graphicsView)
            self.list_of_sensors_layouts[lent].addWidget(self.list_sensors_lineEdit[lent])
            self.list_sensors_lineEdit[lent].textChanged.connect \
                (lambda ch, s=speed, l=self.list_sensors_lineEdit[lent]: s.valuechange(l))

        for bar in range(4):
            section1_progressBar = ClickedProgressbar()
            section1_progressBar.setMaximum(self.global_param.list_max_value[bar + 11])
            self.list_of_sensors_layouts[bar + 11].addWidget(section1_progressBar)
            self.list_of_sensors_layouts[bar + 11].addWidget(self.list_sensors_lineEdit[bar + 11])
            self.list_sensors_lineEdit[bar + 11].textChanged.connect(
                lambda ch, s=section1_progressBar, l=self.list_sensors_lineEdit[bar + 11]: s.diff_value_progress_bar(l,
                                                                                                                     s))

        self.data_sensors_section = DataSensorsSection()
        self.num_crep.setText(str(num))
        self.control_pushbutton.clicked.connect(self.show_data_sensors_section)
        self.all_sensors_pushButton.clicked.connect(lambda: self.all_sensors_crep.show())

    def show_data_sensors_section(self):
        self.data_sensors_section.show()

    def show_sensor1_data(self, lineEde):
        return lineEde.text()

    def setText_lineEdit_sensors(self, lst):
        for elem in range(len(lst)):
            self.list_sensors_lineEdit[elem].setText(str(lst[elem]))
