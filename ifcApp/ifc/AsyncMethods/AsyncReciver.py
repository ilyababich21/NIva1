import asyncio
import csv
import datetime
import time
import os
import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QObject, QTimer
from async_modbus import AsyncTCPClient
from pymodbus.client import ModbusTcpClient

from serviceApp.service.service_model import engine


class WorkerSignals(QObject):
    result = pyqtSignal(list)


class AsyncTcpReciver(QtCore.QObject):
    running = False
    prec = True
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
        # self.timer = QTimer()
        #
        # self.timer.timeout.connect(self.to_bd)
        # self.timer.start(50000)
        print("start")

    # def to_bd(self):
    #
    #     for chunk in pd.read_csv("data.csv",chunksize=10000):
    #         chunk.to_sql("sensors",engine,if_exists="append",index=False)
    #     with open("data.csv", "w", newline="") as file:
    #         writer = csv.DictWriter(file, self.columns, restval='Unknown', extrasaction='ignore')
    #         writer.writeheader()


    # method which will execute algorithm in another thread
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

                self.readSync(client)
                # print("Time 1 iter:    ", time.time() - stat)
            except:
                print("neverno ukaazan address")
                break

    def readSync(self, client):

        for elem in range(len(self.all_signal)):
            # for elem in range(len(self.newTextAndColor)):
            result = client.read_holding_registers(address=0, count=15, slave=elem + 1)

            for dat in range(len(result.registers)):
                self.data = {
                    "id_dat": dat + 1,
                    "value": int(result.registers[dat]),
                    "crep_id": elem+1,
                    "create_date":datetime.datetime.now()
                    # "create_date":datetime.datetime.now().replace(microsecond=0)
                }
                self.state_info.append(self.data)



            try:
                self.all_signal[elem].result.emit(result.registers)

                # try:
                #     for reger in result.registers:

            except:
                print("ebaniy rot")

        with open("CSV_History\\"+os.listdir('CSV_History')[-1], "a", newline="") as file:
            writer = csv.DictWriter(file, self.columns, restval='Unknown', extrasaction='ignore')
            # writer.writeheader()

            # запись нескольких строк
            writer.writerows(self.state_info)
        self.state_info = []

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
