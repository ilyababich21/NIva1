import csv
import datetime
import os
import time
from threading import Thread

from PyQt6.QtCore import QObject, pyqtSignal, QThread
from pymodbus.client import ModbusTcpClient


class WorkerSignals(QObject):
    result = pyqtSignal(list)


class AsyncThread(Thread):
    brokeSignalsId = []
    emitValue = []
    all_signal = []
    state_info = []
    play_pause = False

    def __init__(self, parent=None):
        super(AsyncThread, self).__init__(parent)
        self.running = False  # Флаг выполнения
        print("start")

    def run(self) -> None:
        self.running = True
        try:
            self.client = ModbusTcpClient("127.0.0.1", port=502)
        except Exception as e:
            print(e)

        while self.running:
            if self.play_pause:
                try:
                    self.read_sync()
                except Exception as e:
                    print("neverno ukaazan address ", e)
            else:
                time.sleep(1)

    def read_sync(self):
        self.emitValue = []
        self.result_trap = []
        max_reg = 120
        cur_dat=15
        num_of_creps = len(self.all_signal)
        # print(num_of_creps)
        crep_iter=max_reg//cur_dat
        reg_iter=crep_iter*cur_dat
        puf = num_of_creps // crep_iter  # 8- max count read registers/ count sensor
        ostatok = num_of_creps % crep_iter
        try:
            if puf == 0 and ostatok != 0:
                result = self.client.read_holding_registers(address=0, count=ostatok * cur_dat, slave=1)
                self.emitValue += result.registers
            elif puf != 0 and ostatok == 0:
                for addr in range(puf):
                    result = self.client.read_holding_registers(address=addr * reg_iter, count=reg_iter, slave=1)
                    self.emitValue += result.registers
            elif puf != 0 and ostatok != 0:
                for addr in range(puf):
                    result = self.client.read_holding_registers(address=addr * reg_iter, count=reg_iter, slave=1)
                    self.emitValue += result.registers
                else:
                    result = self.client.read_holding_registers(address=(addr + 1) * reg_iter, count=ostatok * cur_dat, slave=1)
                    self.emitValue += result.registers
        except Exception as e:
            print(e)

        # print(self.emitValue)
        self.result_trap = [self.emitValue[i:i + cur_dat] for i in range(0, len(self.emitValue), cur_dat)]
        # print(self.result_trap)
        for elem in range(len(self.all_signal)):
            self.state_info = []
            self.all_signal[elem].result.emit(self.result_trap[elem])
            self.EntryValueForCSV(elem)

            folder = "CSV_History\\" + str(elem + 1)
            with open(folder + "\\" + str(len(os.listdir(folder))) + ".csv", "a", newline="") as file:
                writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                        extrasaction='ignore')
                # запись нескольких строк
                writer.writerows(self.state_info)

    def EntryValueForCSV(self, elem):

        for register in range(len(self.result_trap[elem])):
            self.data = {
                "id_dat": register + 1,
                "value": int(self.result_trap[elem][register]),
                "crep_id": elem + 1,
                "create_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.state_info.append(self.data)
