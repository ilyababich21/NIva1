import asyncio
import time

from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, QObject
from async_modbus import AsyncTCPClient
from pymodbus.client import ModbusTcpClient


class WorkerSignals(QObject):
    result = pyqtSignal(str)


class AsyncTcpReciver(QtCore.QObject):
    running = False
    num = None

    # sigOnal = pyqtSignal(str)
    all_signal = []
    all_signal2 = []

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
            self.running = False
        while True:
            try:
                stat = time.time()
                self.readSync(client)
                print("Time 1 iter:    ", time.time() - stat)
            except:
                print("neverno ukaazan address")
                break

    def readSync(self, client):
        list = []
        list2 = []
        start = time.time()
        for elem in range(len(self.all_signal)):
            # for elem in range(len(self.newTextAndColor)):
            result = client.read_holding_registers(address=0, count=2, slave=elem + 1)
            list.append(result.registers[0])
            list2.append(result.registers[1])

            # print(result.registers[0])
        print("Time to search:    ", time.time() - start)

        crinzh = time.time()
        for elem in range(len(self.all_signal)):
            self.all_signal[elem].result.emit(str(list[elem]))
            self.all_signal2[elem].result.emit(str(list2[elem]))
        print("Time to emit all signals:    ------", time.time() - crinzh)

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
