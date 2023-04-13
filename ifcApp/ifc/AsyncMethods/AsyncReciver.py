import asyncio
import time

from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QObject
from async_modbus import AsyncTCPClient
from pymodbus.client import ModbusTcpClient


class WorkerSignals(QObject):
    result = pyqtSignal(list)


class AsyncTcpReciver(QtCore.QObject):
    running = False
    prec=True
    all_signal = []

    def __init__(self, parent=None):
        super(AsyncTcpReciver, self).__init__(parent)
        print("start")

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
                stat = time.time()
                self.readSync(client)
                print("Time 1 iter:    ", time.time() - stat)
            except:
                print("neverno ukaazan address")
                break

    def readSync(self, client):

        for elem in range(len(self.all_signal)):
            # for elem in range(len(self.newTextAndColor)):
            result = client.read_holding_registers(address=0, count=7, slave=elem + 1)

            try:
                 self.all_signal[elem].result.emit(result.registers)

            except:
                print("ebaniy rot")

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
