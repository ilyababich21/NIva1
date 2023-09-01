import pandas as pd
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.dates import DateFormatter
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from connection_to_db import engine

UI_selected_graphic = "resources/view/ifc/crep/selected graphic.ui"


class SelectedGraphic(QMainWindow):
    def __init__(self, num_crep, num_sensors):
        self.query = None
        self.num_crep = num_crep
        self.num_sensors = num_sensors
        super().__init__()
        uic.loadUi(UI_selected_graphic, self)
        self.figure = plt.figure(figsize=(16, 9), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # self.pushButton.clicked.connect(self.clear)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)

    def draw_graphic(self, from_datetime, before_datetime):
        self.query = f"SELECT  create_date, value From sensors WHERE id_dat = {self.num_sensors} and crep_id = {self.num_crep}"
        self.df = pd.read_sql_query(self.query, engine)
        self.df.sort_values(by=['create_date'], inplace=True)
        self.df['value'] = self.df['value'].astype("int64")
        self.df = self.df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
        self.df = pd.DataFrame(self.df).set_index(['create_date'])
        from_value = from_datetime.toString("yyyy-MM-dd HH:mm:ss")
        before_value = before_datetime.toString("yyyy-MM-dd HH:mm:ss")
        self.df = self.df.loc[f"{from_value}": f"{before_value}"]
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax.plot(self.df, linewidth=0.8, color='red')
        self.ax.grid(color='green', linestyle='-', linewidth=0.8)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

