import random
from pathlib import Path
import statsmodels.api as sm

import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QTimer
from PyQt6.QtWidgets import QProgressBar
from PySide6.QtCharts import QLineSeries, QChart, QChartView
from matplotlib import pyplot as plt
import pyqtgraph as pg

from ifcApp.crep.graphicscene.Bard import GraphicsWindow


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
        self.graf = GraphicsWindow(self.crep_id, self.id_dat)
        self.graf.show()
        self.clicked.emit()


    def diff_value_progress_bar(self, lineEdit):
        value = lineEdit.text()
        if value == ' ' or value=='':
            value = 0
        elif int(value)>self.maximum():
            value=self.maximum()
        else:
            value = int(value)

        self.setValue(value)
