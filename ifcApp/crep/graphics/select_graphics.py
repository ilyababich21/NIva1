from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from ifcApp.crep.graphics.selected_graphic_model import SelectedGraphicModel

UI_selected_graphic = "resources/view/ifc/crep/graphics_view/selected graphic.ui"


class SelectedGraphic(QMainWindow):
    def __init__(self, num_crep, num_sensors,model):
        self.num_crep = num_crep
        self.num_sensors = num_sensors
        self.model = model
        super().__init__()
        uic.loadUi(UI_selected_graphic, self)
        self.figure = plt.figure(figsize=(16, 9), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)

    def draw_graphic(self, from_datetime, before_datetime):
        df = self.model.get_data(from_datetime, before_datetime)
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax.plot(df, linewidth=0.8, color='red')
        self.ax.grid(color='green', linestyle='-', linewidth=0.8)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()
