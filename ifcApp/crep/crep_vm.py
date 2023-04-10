import time

from PyQt6 import QtCore
from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView
from ifcApp.dataSensors.data_sensors_vm import DataSensorsSection
from ifcApp.graphics.graphics_vm import GraphicsWindow
UI_crep = "view/ifc/ifc_crep.ui"


class ClickedGraphics(QGraphicsView):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()


class CreateGraphicScene(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.show_graphic_window = GraphicsWindow()
        scene = QGraphicsScene()
        scene.setSceneRect(+10, -10, self.width() - 41, self.height())
        self.pixmap = QPixmap("image/sensors/sparaw.png")
        self.arrow = scene.addPixmap(self.pixmap)
        self.arrow.setTransformOriginPoint(38, 11)
        self.arrow.setRotation(-5)
        self.graphicsView = ClickedGraphics()
        self.graphicsView.setStyleSheet("background-image:url(image/sensors/sensors.png);\n"
                                        "background-repeat:no-repeat;\n"
                                        "background-position: center;")
        self.graphicsView.setScene(scene)
        self.graphicsView.clicked.connect(lambda: self.show_graphic_window.show())

    def valuechange(self, lineEdit):
        angel = lineEdit.text()
        if angel == '':
            angel = 0
        else:
            angel = int(angel)
        self.arrow.setRotation((angel * 2 - 5))




class CrepViewModel(QtWidgets.QMainWindow):
    def __init__(self, num):
        super().__init__()
        uic.loadUi(UI_crep, self)
        speed = CreateGraphicScene(self)
        self.gridLayout1.addWidget(speed.graphicsView)
        self.sensors1_lineEdit.textChanged.connect \
            (lambda: speed.valuechange(self.sensors1_lineEdit))

        speed2 = CreateGraphicScene(self)
        self.gridLayout2.addWidget(speed2.graphicsView)
        self.sensors2_lineEdit.textChanged.connect(lambda: speed2.valuechange(self.sensors2_lineEdit))

        speed3 = CreateGraphicScene(self)
        self.gridLayout3.addWidget(speed3.graphicsView)
        self.sensors3_lineEdit.textChanged.connect(lambda: speed3.valuechange(self.sensors3_lineEdit))

        self.data_sensors_section = DataSensorsSection()
        self.num_crep.setText(str(num))
        self.control_pushbutton.clicked.connect(self.show_data_sensors_section)

    def show_data_sensors_section(self):
        self.data_sensors_section.show()



    def show_sensor1_data(self):
        return self.sensors1_lineEdit.text()
    def show_sensor2_data(self):
        return self.sensors2_lineEdit.text()

    @QtCore.pyqtSlot(str)
    def setText1(self, string):
        str=time.time()
        self.sensors1_lineEdit.setText(string)
        # print("vremya peredechi 1 sensor:--------", time.time()-str)

    @QtCore.pyqtSlot(str)
    def setText2(self, string):
        self.sensors2_lineEdit.setText(string)

    #
    @QtCore.pyqtSlot(str)
    def setText3(self, string):
        self.sensors3_lineEdit.setText(string)





