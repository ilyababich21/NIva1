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
        x = deque([0], maxlen=npoints)
        y = deque([0], maxlen=npoints)
        fig, ax = plt.subplots()
        [line] = ax.step(x, y)

        def update(dy):
            x.append(x[-1] + 1)  # update data
            y.append(y[-1] + dy)

            line.set_xdata(x)  # update plot data
            line.set_ydata(y)

            ax.relim()  # update axes limits
            ax.autoscale_view(True, True, True)
            return line, ax

        def data_gen():
            while True:
                yield 1 if random.random() < 0.5 else -1

        ani = animation.FuncAnimation(fig, update, data_gen)
        plt.show()


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
                                        "border-radius: 1px;"
                                        "background-position: center;")
        self.graphicsView.setScene(scene)
        # self.graphicsView.clicked.connect(lambda: self.show_graphic_window.show())

    def valuechange(self, lineEdit, max_value):
        angel = lineEdit.text()
        if angel == '':
            angel = 1
        else:
            angel = int(angel)
            if angel == 0:
                angel = 1
        self.coeff_angle = max_value / angel
        self.arrow.setRotation(240 / self.coeff_angle)
