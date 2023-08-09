import csv
import datetime
import os
import time

from PyQt6.QtCore import QObject, pyqtSignal, QThread
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException


class WorkerSignals(QObject):
    result = pyqtSignal(list)


class AsyncTCPThread(QThread):
    all_signal = None  # На самом деле 1 сигнал
    slaveID = None
    state_info = []

    def __init__(self, parent=None):
        super(AsyncTCPThread, self).__init__(parent)
        self.running = False  # Флаг выполнения

    def run(self) -> None:
        self.running = True
        try:
            client = ModbusTcpClient("127.0.0.1", port=502)
        except:
            print("Net podklychenia")
        while self.running:
            num = self.slaveID
            # print("СЕЙЧАС РАБОТАЕТ ПОТОК НОМЕР: ", {self.slaveID})
            self.emitValue = []
            try:
                for addr in range(15):
                    result = client.read_holding_registers(address=addr, count=1, slave=self.slaveID)
                    # print(type(result))

                    if type(result) is ModbusIOException:
                        print("emae")
                        self.emitValue = [" " for i in range(15)]
                        break
                    elif result.isError():
                        print('Ошибка чтения регистров:', result, "\n" + str(addr))
                        self.emitValue.append(" ")
                        print("nO DATCHIK")
                    else:
                        # print("ock")
                        self.emitValue.append(result.registers[0])
                        # print(self.emitValue)

                    # print(self.emitValue)
            except Exception as e:
                print("vs` huina  ", {e})

            try:
                # ОТПРАВИТЬ ЛИСТ НА ОТРИСОВКУ
                # print(self.emitValue)
                self.state_info = []
                self.all_signal.result.emit(self.emitValue)

                # self.msleep(500)
            except:
                print("ebaniy rot")

            self.EntryValueForCSV(num)
            addr = "CSV_History\\" + str(self.slaveID)
            with open(addr + "\\" + str(len(os.listdir(addr))) + ".csv", "a", newline="") as file:
                writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                        extrasaction='ignore')
                # writer.writeheader()

                # запись нескольких строк
                writer.writerows(self.state_info)
            # self.state_info = []
            # print(f"ЗАПИСЬ ПОТОКА НОМЕР {self.slaveID} \n:  ",  self.state_info, "\n" )
            # self.state_info=[]
            self.msleep(200)

    def EntryValueForCSV(self, num):

        for dat in range(len(self.emitValue)):
            self.data = {
                "id_dat": dat + 1,
                "value": self.emitValue[dat],
                "crep_id": self.slaveID,
                "create_date": datetime.datetime.now()
            }
            self.state_info.append(self.data)
