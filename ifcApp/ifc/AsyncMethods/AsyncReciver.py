import asyncio
import csv
import datetime
import time
import os
import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QObject
from async_modbus import AsyncTCPClient
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException

from serviceApp.service.service_model import engine


class WorkerSignals(QObject):
    result = pyqtSignal(list)


class AsyncTcpReciver(QtCore.QObject):
    brokeSignalsId=[]
    running = False
    prec = True
    emitValue = []
    all_signal = []
    state_info = []
    data = {
        "id_dat": None,
        "value": None,
        "crep_id": None,
        "create_date": None
    }
    columns = ["id_dat", "value", "crep_id","create_date"]


    def __init__(self, parent=None):
        super(AsyncTcpReciver, self).__init__(parent)
        csv_count=len(os.listdir('CSV_History'))
        print(os.listdir('CSV_History'))
        print(csv_count)
        with open("CSV_History\\data"+str(csv_count+1)+".csv", "w", newline="") as file:
            writer = csv.DictWriter(file, self.columns, restval='Unknown', extrasaction='ignore')
            writer.writeheader()

        print("start")

    def run(self):
        self.RunSync()
        # asyncio.run(self.RunRead())

    def RunSync(self):
        try:
            client = ModbusTcpClient("127.0.0.1", port=502)
        except:
            print("Net podklychenia")

        while self.prec:
            try:
                time.sleep(0.5)
                stat = time.time()
                print('poexali')
                self.readSync(client)
            except:
                print("neverno ukaazan address")
                # break

    def readSync(self, client):
        # ЧТЕНИЕ КАЖДОГО ДАТЧИКА КАЖДОЙ КРЕПИ
        for elem in range(len(self.all_signal)):
            print("НОМЕР ТЕКУЩЕЙ ИТЕРАЦИИ")
            self.emitValue=[]
            if elem in self.brokeSignalsId: continue
            try:
                for addr in range(15):
                    result = client.read_holding_registers(address=addr, count=1, slave=elem + 1)
                    print(type(result))
                    if type(result) is ModbusIOException:
                        print("emae")
                        self.emitValue=[" " for i in range(15)]
                        self.brokeSignalsId.append(elem)
                        break
                    elif result.isError():
                        print('Ошибка чтения регистров:', result,"\n"+str(elem))
                        self.emitValue.append(" ")
                        print("nO DATCHIK")
                    else:
                        print("ock")
                        self.emitValue.append(result.registers[0])
                        print(self.emitValue)
                else:
                    print("ПРОХОД ПО ВНУТРЕННЕМУ ЦИКЛУ ЗАКОНЧЕН")

            except:
                print("hello mir manera krutit mir")
                break
            # self.EntryValueForCSV(elem)
            try:
                # ОТПРАВИТЬ ЛИСТ НА ОТРИСОВКУ
                print(self.emitValue)
                self.all_signal[elem].result.emit(self.emitValue)
            except:
                print("ebaniy rot")

            self.EntryValueForCSV(elem)


        with open("CSV_History\\"+os.listdir('CSV_History')[-1], "a", newline="") as file:
            writer = csv.DictWriter(file, self.columns, restval='Unknown', extrasaction='ignore')
            # writer.writeheader()

            # запись нескольких строк
            writer.writerows(self.state_info)
        self.state_info = []

    def EntryValueForCSV(self,elem):

        for dat in range(len(self.emitValue)):
            self.data = {
                "id_dat": dat + 1,
                "value": int(self.emitValue[dat]),
                "crep_id": elem+1,
                "create_date":datetime.datetime.now()
            }
            self.state_info.append(self.data)

    async def RunRead(self):
        try:
            reader = await asyncio.open_connection('127.0.0.1', 502)

            client = AsyncTCPClient(reader)
            print("zhopa")
        except:
            self.running = False
            print("zhopa2")
        while True:
            # await asyncio.wait([read(client,i) for i in range(1,8)])
            try:
                stat = time.time()

                await self.read(client)
                print("Time 1 iter:    ", time.time() - stat)
                print("zhopa3")

            except:
                print("zhopa4")

                break

            # await asyncio.sleep(0.5)

            # print(list)

    async def read(self, client):

        for elem in range(len(self.all_signal)):
            # for elem in range(len(self.all_signal)):
            result = await client.read_holding_registers(slave_id=1, starting_address=0, quantity=1)
            print(result[0])
