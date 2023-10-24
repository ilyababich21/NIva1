import csv
import datetime
import os
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QObject
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException


class WorkerSignals(QObject):
    result = pyqtSignal(list)


class AsyncTcpReciver(QtCore.QObject):
    brokeSignalsId = []
    running = False
    emitValue = []
    all_signal = []
    state_info = []

    def __init__(self, parent=None):
        super(AsyncTcpReciver, self).__init__(parent)
        print("start")

    def run(self):
        self.client = ModbusTcpClient("127.0.0.1", port=502)
        while True:
            try:
                # time.sleep(1)
                self.readSync()
            except Exception as e:
                print("neverno ukaazan address ", e)

    def readSync(self):
        address = 0
        count = 15
        for elem in range(len(self.all_signal)):
            self.emitValue = []
            if elem in self.brokeSignalsId: continue
            try:
                result = self.client.read_holding_registers(address=address, count=count, slave=1)
                for i, value in enumerate(result.registers):
                    if type(result) is ModbusIOException:
                        print("emae")
                        self.emitValue = [" " for i in range(15)]
                        self.brokeSignalsId.append(elem)
                        break
                    elif result.isError():
                        print('Ошибка чтения регистров:', result, "\n" + str(elem))
                        self.emitValue.append(" ")
                        print("nO DATCHIK")
                    else:
                        self.emitValue.append(value)
                address += count
            except Exception as e:
                print("pizda rulu ", e)
                break
            try:
                self.state_info = []
                # print(self.emitValue)
                self.all_signal[elem].result.emit(self.emitValue)
                # print(f"отправляем на крепь {elem}")
            except:
                print("ebaniy rot")

            self.EntryValueForCSV(elem)
            folder = "CSV_History\\" + str(elem + 1)
            with open(folder + "\\" + str(len(os.listdir(folder))) + ".csv", "a", newline="") as file:
                writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                        extrasaction='ignore')
                # запись нескольких строк
                writer.writerows(self.state_info)

    def EntryValueForCSV(self, elem):

        for dat in range(len(self.emitValue)):
            self.data = {
                "id_dat": dat + 1,
                "value": int(self.emitValue[dat]),
                "crep_id": elem + 1,
                "create_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.state_info.append(self.data)
