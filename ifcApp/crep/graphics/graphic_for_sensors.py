import os
import pandas as pd
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt6.QtCore import QTimer

from ifcApp.crep.graphics.select_date import SelectDate

UI_graphic = "resources/view/ifc/crep/graphics_view/graphics.ui"


class GraphicsWindow(QMainWindow):
    def __init__(self, num_crep, id_dat,database):
        self.database=database
        self.num_crep = num_crep
        self.num_sensors = id_dat
        super().__init__()
        uic.loadUi(UI_graphic, self)
        self.open_pushButton.clicked.connect(self.open_date_window)
        # Создание фигуры и осей графика
        self.figure = Figure(figsize=(16, 9), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Создание вертикального layout и добавление в него графика и toolbar
        self.canvas_layout.addWidget(self.toolbar)
        self.canvas_layout.addWidget(self.canvas)

        directory_crep = 'CSV_History' + "\\" + str(self.num_crep)

        # Добавление данных из csv-файлов
        path = []
        for files in os.listdir(directory_crep):
            path.append(os.path.join(directory_crep, files))
        self.df = pd.concat([pd.read_csv(f) for f in path], ignore_index=True)
        self.df['create_date'] = self.df['create_date'].apply(lambda x: x.split(".")[0])
        self.df = self.df[(self.df['id_dat'] == int(self.num_sensors))]
        self.df['create_date'] = pd.to_datetime(self.df['create_date'], format="%Y-%m-%d %H:%M:%S")
        self.df = self.df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
        self.df = pd.DataFrame(self.df).set_index(['create_date'])

        # Создание таймера для обновления графика каждую секунду
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)
        self.stop_pushButton.clicked.connect(lambda: self.timer.stop())
        self.start_pushButton.clicked.connect(lambda: self.timer.start(1000))
        # Создание линии графика
        self.ax = self.figure.add_subplot(111)
        self.line, = self.ax.plot(self.df, linewidth=0.8, color='red')
        self.ax.grid(color='green', linestyle='-', linewidth=0.8)

    def update_plot(self):
        # Добавление новых данных в массивы
        self.df = self.df.combine_first(self.preobrazovanie())
        # Обновление данных линии графика
        self.line.set_data(self.df.index, self.df['value'])
        # Автоматическое масштабирование осей графика
        self.ax.relim()
        self.ax.autoscale_view()

        # Обновление графика на canvas
        self.canvas.draw()

    def preobrazovanie(self):
        path = []
        directory_crep = 'CSV_History' + "\\" + str(self.num_crep)

        for files in os.listdir(directory_crep):
            path.append(os.path.join(directory_crep, files))

        path = sorted(path, key=lambda x: int(x.split('.')[0].split('\\')[-1]))

        if len(path) == 1:
            df = pd.concat([pd.read_csv(f) for f in path], ignore_index=True)
        else:
            df = pd.concat([pd.read_csv(f) for f in path[-2:]], ignore_index=True)
        df['create_date'] = df['create_date'].apply(lambda x: x.split(".")[0])
        df = df[(df['id_dat'] == int(self.num_sensors))]
        df['create_date'] = pd.to_datetime(df['create_date'], format="%Y-%m-%d %H:%M:%S")
        df = df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
        df = pd.DataFrame(df).set_index(['create_date'])
        return df
    def open_date_window(self):
        self.select_date_for_graphics = SelectDate(self.num_crep, self.num_sensors,self.database)
        self.select_date_for_graphics.show()



