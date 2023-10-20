import csv
import datetime
import os
import time
from PyQt6 import QtCore
from PyQt6.QtCore import QObject, pyqtSignal
from pymodbus.client import ModbusTcpClient


class WorkerSignals(QObject):
    result = pyqtSignal(list)


class AsyncThread(QtCore.QObject):
    brokeSignalsId = []
    running = False
    emitValue = []
    all_signal = []
    state_info = []
    play_pause = False

    def __init__(self, parent=None):
        super(AsyncThread, self).__init__(parent)
        print("start")

    def run(self):
        # Переписать!!!
        self.client = ModbusTcpClient("127.0.0.1", port=502)

        while True:
            if self.play_pause:
                try:
                    # time.sleep(1)
                    self.read_sync()
                except Exception as e:
                    print("neverno ukaazan address ", e)
            else:
                time.sleep(1)

    def read_sync(self):
        self.emitValue = []
        num_of_creps = len(self.all_signal)
        puf = num_of_creps // 8
        ostatok = num_of_creps % 8
        try:
            if puf == 0 and ostatok != 0:
                result = self.client.read_holding_registers(address=0, count=ostatok * 15, slave=1)
                self.emitValue += result.registers
            elif puf != 0 and ostatok == 0:
                for addr in range(puf):
                    result = self.client.read_holding_registers(address=addr * 120, count=120, slave=1)
                    self.emitValue += result.registers
            elif puf != 0 and ostatok != 0:
                for addr in range(puf):
                    result = self.client.read_holding_registers(address=addr * 120, count=120, slave=1)
                    self.emitValue += result.registers
                else:
                    result = self.client.read_holding_registers(address=(addr + 1) * 120, count=ostatok * 15, slave=1)
                    self.emitValue += result.registers
        except Exception as e:
            print(e)

        # print(self.emitValue)
        self.result_trap = [self.emitValue[i:i + 15] for i in range(0, len(self.emitValue), 15)]
        # print(self.result_trap)
        self.state_info = []
        for elem in range(len(self.all_signal)):
            self.all_signal[elem].result.emit(self.result_trap[elem])
            self.EntryValueForCSV(elem)

            folder = "CSV_History\\" + str(elem + 1)
            with open(folder + "\\" + str(len(os.listdir(folder))) + ".csv", "a", newline="") as file:
                writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                        extrasaction='ignore')
                # запись нескольких строк
                writer.writerows(self.state_info)

    def EntryValueForCSV(self, elem):

        for dat in range(len(self.result_trap[elem])):
            self.data = {
                "id_dat": dat + 1,
                "value": int(self.result_trap[elem][dat]),
                "crep_id": elem + 1,
                "create_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.state_info.append(self.data)
