import asyncio
import csv
import datetime
import time
import os
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QObject
from async_modbus import AsyncTCPClient
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
        # ЧТЕНИЕ КАЖДОГО ДАТЧИКА КАЖДОЙ КРЕПИ
        for elem in range(len(self.all_signal)):
            self.emitValue = []
            if elem in self.brokeSignalsId: continue
            try:
                for addr in range(15):
                    result = self.client.read_holding_registers(address=addr, count=1, slave=elem + 1)
                    # print(type(result))
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
                        # print("ock")
                        self.emitValue.append(result.registers[0])
                        print(result.registers[0])
                        # print(self.emitValue)
                # else:
                #     # print("ПРОХОД ПО ВНУТРЕННЕМУ ЦИКЛУ ЗАКОНЧЕН")

            except Exception as e:
                print("pizda rulu ", e)
                break
            try:
                # ОТПРАВИТЬ ЛИСТ НА ОТРИСОВКУ
                self.state_info = []
                self.all_signal[elem].result.emit(self.emitValue)
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
