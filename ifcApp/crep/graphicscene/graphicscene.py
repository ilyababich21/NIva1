from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView

from ifcApp.crep.graphics.graphic_for_sensors import GraphicsWindow


class ClickedGraphics(QGraphicsView):
    clicked = pyqtSignal()
    crep_id = 1
    id_dat = 1
    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.create_graphics()
        self.clicked.emit()

    def create_graphics(self):
        self.graf = GraphicsWindow(self.crep_id,self.id_dat)
        self.graf.show()


class CreateGraphicScene(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        scene = QGraphicsScene()
        scene.setSceneRect(-10, -12, self.width() - 41, self.height())
        self.pixmap = QPixmap("resources/image/sensors/arrow1.png")
        self.arrow = scene.addPixmap(self.pixmap)
        self.arrow.setTransformOriginPoint(20, 9)
        self.arrow.setRotation(-3)
        self.graphicsView = ClickedGraphics()
        self.graphicsView.setStyleSheet("background-image:url(resources/image/sensors/sensormarco.png);\n"
                                        "background-repeat:no-repeat;\n"
                                        "border-radius: 1px;"
                                        "background-position: center;")
        self.graphicsView.setScene(scene)

    def value_change(self, lineEdit, max_value):
        angel = lineEdit.text()
        if angel == '':
            angel = 1
        if angel == ' ':
            angel = 1
        if angel == "-":
            angel = 1
        else:
            angel = int(angel)
            if angel == 0:
                angel = 1
        self.coeff_angle = max_value / angel
        self.arrow.setRotation(240 / self.coeff_angle)
