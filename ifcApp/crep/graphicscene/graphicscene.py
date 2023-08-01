import time
from pathlib import Path
import pandas as pd
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView


import matplotlib.pyplot as plt



class ClickedGraphics(QGraphicsView):
    clicked = pyqtSignal()
    id_dat = 1
    crep_id = 1

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.create_grafic()
        self.clicked.emit()

    def create_grafic(self):
        start_time = time.time()
        data_dir = Path("CSV_History")
        df = pd.concat([pd.read_csv(f) for f in data_dir.glob("*.csv")], ignore_index=True)
        df['create_date'] = df['create_date'].apply(lambda x: x.split(".")[0])
        df = df[(df['id_dat'] == self.id_dat) & (df['crep_id'] == self.crep_id)]
        print(df)
        df['create_date'] = pd.to_datetime(df['create_date'], format="%Y-%m-%d %H:%M:%S")

        df = df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
        print(df)
        print("EBAL VAS V ROT")
        print(df.index, df.columns)
        df = pd.DataFrame(df).set_index(['create_date'])

        print(df)
        print("Vremya operacii preobrazovania   ", time.time() - start_time)
        # mod = sm.tsa.statespace.SARIMAX(df,
        #                                 order=(1, 0, 1),
        #                                 seasonal_order=(1, 1, 0, 30)
        #                                 )
        # results = mod.fit()
        # try:
        #     pass
        #     # results.plot_diagnostics(figsize=(18, 8))
        # except:
        #
        #     print("MALO DANNIX")
        # predict = results.get_forecast(steps=20)

        ax = df.plot(label='Текущие данные', figsize=(15, 12), title="Прогноз методом SARIMA")
        # results.fittedvalues.plot(ax=ax, style='--', color='red',label='Прогewfsvdbbdbноз')

        # predict.predicted_mean.plot(ax=ax, style='--', color='green', label='Прогноз') emae

        ax.set_xlabel('Время')

        # plt.legend() emae

        # plt.grid(color='green', linestyle='--', linewidth=0.5)
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

    def value_change(self, lineEdit, max_value):
        angel = lineEdit.text()
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
