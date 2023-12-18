from PyQt6 import QtCore
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QTableWidgetItem


class Urod(QObject):

    buts:list

    def __init__(self,buts,data_sensors,list_all_crep,elem):
        QObject.__init__(self)
        self.buts = buts
        self.data_sensors=data_sensors
        self.list_all_crep=list_all_crep
        self.kek=elem

    @QtCore.pyqtSlot(list)
    def setText(self,lst):
        for elem in range(len(lst)):
            self.buts[elem].update_color_and_height(lst[elem])
            self.data_sensors.tableWidget.setItem(elem, self.kek, QTableWidgetItem(str(lst[elem])))

        if self.list_all_crep.get(self.kek+1):
            self.list_all_crep[self.kek+1].setText_lineEdit_sensors(lst)


