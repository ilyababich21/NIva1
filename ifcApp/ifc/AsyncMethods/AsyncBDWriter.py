import csv

import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer

from serviceApp.service.service_model import engine


class AsyncBDWriter(QtCore.QObject):
    columns = ["id_dat", "value", "crep_id"]

    def __init__(self, parent=None):
        super(AsyncBDWriter, self).__init__(parent)

        self.timer = QTimer()

        self.timer.timeout.connect(self.to_bd)
        self.timer.start(25000)

    def to_bd(self):
        print("pognali")
        for chunk in pd.read_csv("data.csv", chunksize=10000):
            chunk.to_sql("sensors", engine, if_exists="append", index=False)
        with open("data.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, self.columns, restval='Unknown', extrasaction='ignore')
            writer.writeheader()
