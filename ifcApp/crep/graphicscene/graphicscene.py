from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView

import random
from collections import deque

import matplotlib.pyplot as plt  # $ pip install matplotlib
import matplotlib.animation as animation
from ifcApp.graphics.graphics_vm import GraphicsWindow


class ClickedGraphics(QGraphicsView):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.create_grafic()
        self.clicked.emit()



    def create_grafic(self):
        npoints = 30
        self.x = deque([0], maxlen=npoints)
        self.y = deque([0], maxlen=npoints)
        self.fig, self.ax = plt.subplots()
        [self.line] = self.ax.step(self.x, self.y)



        ani = animation.FuncAnimation(self.fig, self.update, self.data_gen)
        plt.show()
    def update(self,dy):
        self.x.append(self.x[-1] + 1)  # update data
        self.y.append(self.y[-1] + dy)

        self.line.set_xdata(self.x)  # update plot data
        self.line.set_ydata(self.y)

        self.ax.relim()  # update axes limits
        self.ax.autoscale_view(True, True, True)
        return self.line, self.ax

    def data_gen(self):
        while True:
            yield 1 if random.random() < 0.5 else -1

class CreateGraphicScene(QWidget):
    num=0
    def __init__(self, parent=None):
        super().__init__(parent)
        scene = QGraphicsScene()

        # self.show_graphic_window = GraphicsWindow()
        scene.setSceneRect(-10, -12, self.width() - 41, self.height())
        self.pixmap = QPixmap("image/sensors/arrow1.png")
        self.arrow = scene.addPixmap(self.pixmap)
        self.arrow.setTransformOriginPoint(20, 9)
        self.arrow.setRotation(-3)
        self.graphicsView = QGraphicsView()
        self.graphicsView.setStyleSheet("background-image:url(image/sensors/sensormarco.png);\n"
                                        "background-repeat:no-repeat;\n"
                                        "background-position: center;")
        self.graphicsView.setScene(scene)
        # self.graphicsView.clicked.connect(lambda: self.show_graphic_window.show())

    def valuechange(self, lineEdit, max_value):
        angel = lineEdit.text()
        if angel == '':
            angel = 0.1
        else:
            angel = int(angel)
        self.coeff_angle = max_value / angel
        self.arrow.setRotation(240 / self.coeff_angle)
