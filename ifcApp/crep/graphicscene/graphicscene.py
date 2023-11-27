import os

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap, QIntValidator
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QVBoxLayout, QLineEdit, QLabel

from address import resource_path
from ifcApp.crep.graphics.graphic_for_sensors import GraphicsWindow


class ClickedGraphics(QGraphicsView):
    clicked = pyqtSignal()
    crep_id = 1
    id_dat = 1
    graf = None

    def __init__(self, database):
        super(ClickedGraphics, self).__init__()
        self.database = database

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.create_graphics()
        self.clicked.emit()

    def create_graphics(self):
        if self.graf:
            if self.graf.isVisible():
                self.graf.hide()
            else:
                self.graf.show()
        else:
            self.graf = GraphicsWindow(self.crep_id, self.id_dat, self.database)
            self.graf.show()


class CreateGraphicScene(QWidget):
    def __init__(self, max_value, database, parent=None):
        super().__init__(parent)
        self.max_value = max_value
        self.database = database
        layout = QVBoxLayout(self)
        scene = QGraphicsScene()
        scene.setSceneRect(-10, -12, self.width() - 41, self.height())
        self.pixmap = QPixmap(resource_path("resources/image/sensors/arrow1.png"))
        self.arrow = scene.addPixmap(self.pixmap)
        self.arrow.setTransformOriginPoint(20, 9)
        self.arrow.setRotation(-3)
        self.graphicsView = ClickedGraphics(self.database)
        # stroka = resource_path('resources/image/sensors/sensor_marco.png')
        self.graphicsView.setStyleSheet(f"background-image: url('resources/image/sensors/sensor_marco.png');\n"
                                        "background-repeat: no-repeat;\n"
                                        "border-radius: 1px;\n"
                                        "background-position: center;")
        self.lineedit = QLineEdit()
        self.lineedit.setFixedSize(57, 15)
        self.lineedit.setValidator(QIntValidator())
        self.lineedit.textChanged.connect(lambda: self.value_change(self.max_value))
        self.lineedit.setStyleSheet("margin-left:3px")
        self.label = QLabel()
        self.graphicsView.setScene(scene)
        layout.addWidget(self.graphicsView)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.label)
        layout.setSpacing(0)

    def value_change(self,max_value):
        angel = self.lineedit.text()
        if angel == '' or angel == ' ' or angel == "-":
            angel = 1
        else:
            angel = int(angel)
            if angel == 0:
                angel = 1
        if max_value == 0:
            max_value = 1
        self.coeff_angle = max_value / angel
        self.arrow.setRotation(240 / self.coeff_angle)
