import os
import sys

from pathlib import Path


import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow,  QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt6.QtCore import QTimer


class GraphicsWindow(QMainWindow):
    def __init__(self, num_crep,num_dat):
        self.num_crep=num_crep
        self.num_dat=num_dat
        super().__init__()

        # Создание фигуры и осей графика
        self.figure = Figure(figsize=(16, 9), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Создание вертикального layout и добавление в него графика и toolbar
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # Создание виджета и установка layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        # Добавление данных из csv-файлов
        data_dir = Path("D:\\PythonProjects\\NIva1\\CSV_History\\"+str(self.num_crep))
        self.df = pd.concat([pd.read_csv(f) for f in data_dir.glob("*.csv")], ignore_index=True)
        self.df['create_date'] = self.df['create_date'].apply(lambda x: x.split(".")[0])
        self.df = self.df[(self.df['id_dat'] == int(self.num_dat))]
        self.df['create_date'] = pd.to_datetime(self.df['create_date'], format="%Y-%m-%d %H:%M:%S")
        self.df = self.df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
        self.df = pd.DataFrame(self.df).set_index(['create_date'])
        # Создание таймера для обновления графика каждую секунду
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(1000)

        # Создание массивов данных для графика
        # self.x = [0]
        # self.y = [random.randint(0, 10)]

        # Создание линии графика
        self.ax = self.figure.add_subplot(111)
        # self.ax.set_facecolor('#155270')
        self.line, = self.ax.plot(self.df, linewidth=0.8, color='red')
        # grid(color='green', linestyle='--', linewidth=0.5)
        self.ax.grid(color='green', linestyle='-', linewidth=0.8)
    def update_plot(self):
        # Добавление новых данных в массивы
        # self.df.combine_first(self.preobrazovanie())
        self.df =self.df.combine_first(self.preobrazovanie())
        # Обновление данных линии графика
        self.line.set_data(self.df.index, self.df['value'])
        # Автоматическое масштабирование осей графика
        self.ax.relim()
        self.ax.autoscale_view()
        # Обновление графика на canvas
        self.canvas.draw()




    def preobrazovanie(self):
        data_dir = Path("D:\\PythonProjects\\NIva1\\CSV_History\\"+str(self.num_crep))
        data_dir=sorted(data_dir.glob("*.csv"), key=lambda x: x.stat().st_mtime)
        print(data_dir)
        if len(data_dir) == 1:
            df = pd.concat([pd.read_csv(f) for f in data_dir], ignore_index=True)
        else:
            df = pd.concat([pd.read_csv(f) for f in data_dir[-2:]], ignore_index=True)
        df['create_date'] = df['create_date'].apply(lambda x: x.split(".")[0])
        df = df[(df['id_dat'] == int(self.num_dat))]
        df['create_date'] = pd.to_datetime(df['create_date'], format="%Y-%m-%d %H:%M:%S")
        df = df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
        df = pd.DataFrame(df).set_index(['create_date'])
        return df

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphicsWindow(1,1)
    window.showMaximized()
    app.exec()