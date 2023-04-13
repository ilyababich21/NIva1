import time

from PyQt6 import QtCore
from PyQt6 import uic, QtWidgets
from ifcApp.crep.graphicscene.graphicscene import CreateGraphicScene
from ifcApp.dataSensors.data_sensors_vm import DataSensorsSection
from ifcApp.crep.progressbar.progressbar import ClickedProgressbar

UI_crep = "view/ifc/ifc_crep.ui"
class CrepViewModel(QtWidgets.QMainWindow):
    def __init__(self, num):
        super().__init__()
        uic.loadUi(UI_crep, self)


        speed = CreateGraphicScene(self)
        self.gridLayout1.addWidget(speed.graphicsView)
        self.gridLayout1.addWidget(self.sensors1_lineEdit)
        self.sensors1_lineEdit.textChanged.connect \
            (lambda: speed.valuechange(self.sensors1_lineEdit))

        speed2 = CreateGraphicScene(self)
        self.gridLayout2.addWidget(speed2.graphicsView)
        self.gridLayout2.addWidget(self.sensors2_lineEdit)
        self.sensors2_lineEdit.textChanged.connect \
            (lambda: speed2.valuechange(self.sensors2_lineEdit))

        speed3 = CreateGraphicScene(self)
        self.gridLayout3.addWidget(speed3.graphicsView)
        self.gridLayout3.addWidget(self.sensors3_lineEdit)
        self.sensors3_lineEdit.textChanged.connect \
            (lambda: speed3.valuechange(self.sensors3_lineEdit))

        speed4 = CreateGraphicScene(self)
        self.gridLayout4.addWidget(speed4.graphicsView)
        self.gridLayout4.addWidget(self.sensors4_lineEdit)
        self.sensors4_lineEdit.textChanged.connect \
            (lambda: speed4.valuechange(self.sensors4_lineEdit))

        speed5 = CreateGraphicScene(self)
        self.gridLayout5.addWidget(speed5.graphicsView)
        self.gridLayout5.addWidget(self.sensors5_lineEdit)
        self.sensors5_lineEdit.textChanged.connect \
            (lambda: speed5.valuechange(self.sensors5_lineEdit))

        speed6 = CreateGraphicScene(self)
        self.pozition_layout.addWidget(speed6.graphicsView)
        self.pozition_layout.addWidget(self.pozition_lineEdit)
        self.pozition_lineEdit.textChanged.connect \
            (lambda: speed6.valuechange(self.pozition_lineEdit))
        speed7 = CreateGraphicScene(self)
        self.CP_layout.addWidget(speed7.graphicsView)
        self.CP_layout.addWidget(self.CP_lineEdit)
        self.CP_lineEdit.textChanged.connect \
            (lambda: speed7.valuechange(self.CP_lineEdit))
        speed8 = CreateGraphicScene(self)
        self.prod_layout.addWidget(speed8.graphicsView)
        self.prod_layout.addWidget(self.prod_lineEdit)
        self.prod_lineEdit.textChanged.connect \
            (lambda: speed8.valuechange(self.prod_lineEdit))
        speed9 = CreateGraphicScene(self)
        self.poper_layout.addWidget(speed9.graphicsView)
        self.poper_layout.addWidget(self.poper_lineEdit)
        self.poper_lineEdit.textChanged.connect \
            (lambda: speed9.valuechange(self.poper_lineEdit))
        speed10 = CreateGraphicScene(self)
        self.end_section_layout.addWidget(speed10.graphicsView)
        self.end_section_layout.addWidget(self.end_section_lineEdit)
        self.end_section_lineEdit.textChanged.connect \
            (lambda: speed10.valuechange(self.end_section_lineEdit))
        speed11 = CreateGraphicScene(self)
        self.poper_hieght_layout.addWidget(speed11.graphicsView)
        self.poper_hieght_layout.addWidget(self.poper_hieght_lineEdit)
        self.poper_hieght_lineEdit.textChanged.connect \
            (lambda: speed11.valuechange(self.poper_hieght_lineEdit))


        list_section_layouts=[self.section_one_layout,self.section_two_layout,self.section_three_layout,self.poz_shifting_layout]
        list_section_Bar_lineEdits=[self.section_one_lineEdit,self.section_two_lineEdit,self.section_three_lineEdit,self.poz_shifting_lineEdit]


        # for bar in range(len(list_section_layouts)):
        #     section1_progressBar = ClickedProgressbar()
        #     list_section_layouts[bar].addWidget(section1_progressBar)
        #     list_section_layouts[bar].addWidget(list_section_Bar_lineEdits[bar])
        #     list_section_Bar_lineEdits[bar].textChanged.connect(
        #         lambda: self.diff_value_progress_bar( list_section_Bar_lineEdits[bar], section1_progressBar))

        self.section1_progressBar = ClickedProgressbar()
        self.section_one_layout.addWidget(self.section1_progressBar)
        self.section_one_layout.addWidget(self.section_one_lineEdit)
        self.section1_progressBar.clicked.connect(lambda: print("1"))
        self.section_one_lineEdit.textChanged.connect(lambda: self.diff_value_progress_bar(self.section_one_lineEdit,self.section1_progressBar))

        self.section2_progressBar = ClickedProgressbar()
        self.section_two_layout.addWidget(self.section2_progressBar)
        self.section_two_layout.addWidget(self.section_two_lineEdit)
        self.section2_progressBar.clicked.connect(lambda: print("2"))
        self.section_two_lineEdit.textChanged.connect(lambda: self.diff_value_progress_bar(self.section_two_lineEdit,self.section2_progressBar))

        self.section3_progressBar = ClickedProgressbar()
        self.section_three_layout.addWidget(self.section3_progressBar)
        self.section_three_layout.addWidget(self.section_three_lineEdit)
        self.section3_progressBar.clicked.connect(lambda: print("3"))
        self.section_three_lineEdit.textChanged.connect(lambda: self.diff_value_progress_bar(self.section_three_lineEdit,self.section3_progressBar))

        self.poz_shifting_progressBar = ClickedProgressbar()
        self.poz_shifting_layout.addWidget(self.poz_shifting_progressBar)
        self.poz_shifting_layout.addWidget(self.poz_shifting_lineEdit)
        self.poz_shifting_progressBar.clicked.connect(lambda: print("4"))
        self.poz_shifting_lineEdit.textChanged.connect(lambda: self.diff_value_progress_bar(self.poz_shifting_lineEdit,self.poz_shifting_progressBar))






        self.data_sensors_section = DataSensorsSection()
        self.num_crep.setText(str(num))
        self.control_pushbutton.clicked.connect(self.show_data_sensors_section)

    def diff_value_progress_bar(self,lineEdit,progressbar):
        value = lineEdit.text()
        if value == '':
            value = 0
        else:
            value = int(value)

        progressbar.setValue(value)

    def show_data_sensors_section(self):
        self.data_sensors_section.show()



    def show_sensor1_data(self):
        return self.sensors1_lineEdit.text()
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





