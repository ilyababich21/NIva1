from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView

from ifcApp.graphics.graphics_vm import GraphicsWindow


class ClickedGraphics(QGraphicsView):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

        self.clicked.emit()


class CreateGraphicScene(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        scene = QGraphicsScene()
        # self.show_graphic_window = GraphicsWindow()
        scene.setSceneRect(-10, -12, self.width() - 41, self.height())
        self.pixmap = QPixmap("image/sensors/arrow1.png")
        self.arrow = scene.addPixmap(self.pixmap)
        self.arrow.setTransformOriginPoint(20, 9)
        self.arrow.setRotation(-3)
        self.graphicsView = ClickedGraphics()
        self.graphicsView.setStyleSheet("background-image:url(image/sensors/sensormarco.png);\n"
                                        "background-repeat:no-repeat;\n"
                                        "background-position: center;")
        self.graphicsView.setScene(scene)
        # self.graphicsView.clicked.connect(lambda: self.show_graphic_window.show())

    def valuechange(self, lineEdit):
        angel = lineEdit.text()
        if angel == '':
            angel = 0
        else:
            angel = int(angel)
        self.arrow.setRotation((angel * 2.5 - 10))