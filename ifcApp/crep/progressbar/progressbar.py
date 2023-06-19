from pathlib import Path
import statsmodels.api as sm

import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QProgressBar
from matplotlib import pyplot as plt


class ClickedProgressbar(QProgressBar):
    clicked = pyqtSignal()
    id_dat = 1
    crep_id = 1
    def __init__(self):
        super().__init__()
        self.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.setFixedSize(61, 50)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)
        self.create_grafic()
        self.clicked.emit()

    def create_grafic(self):
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

        mod = sm.tsa.statespace.SARIMAX(df,
                                        order=(1, 0, 1),
                                        seasonal_order=(1, 1, 0, 30)
                                        )
        results = mod.fit()
        try:

            results.plot_diagnostics(figsize=(18, 8))
        except:
            print("MALO DANNIX")
        predict = results.get_forecast(steps=20)

        ax = df.plot(label='Текущие данные', figsize=(15, 12), title="Прогноз методом SARIMA")
        # results.fittedvalues.plot(ax=ax, style='--', color='red',label='Прогewfsvdbbdbноз')
        predict.predicted_mean.plot(ax=ax, style='--', color='green', label='Прогноз')
        ax.set_xlabel('Время')
        plt.legend()
        plt.grid(color='green', linestyle='--', linewidth=0.5)
        plt.show()
    def diff_value_progress_bar(self, lineEdit):
        value = lineEdit.text()
        if value == '':
            value = 0
        else:
            value = int(value)

        self.setValue(value)
