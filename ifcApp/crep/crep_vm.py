from PyQt6 import uic, QtWidgets
from PyQt6 import QtCore
import asyncio


from pymodbus.client import AsyncModbusSerialClient
UI_crep = "view/ifc_crep.ui"



class Changer(QtCore.QThread):
    nextValueOfText = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

        self.running = False

    text = ''

    def run(self):
        self.running = True
        asyncio.run(self.get_var_modbus())
        # loop = asyncio.get_event_loop()
        # loop.create_task(self.get_var_modbus(loop))
        # loop.run_forever()

    async def get_var_modbus(self):
        self.client = await AsyncModbusSerialClient(port="COM9", baudrate=9600)

        while True:
            if self.client:
                self.text = str(
                    await self.client.read_holding_registers(0,1, unit=1).registers[0])
            self.text += '\n'
            self.nextValueOfText.emit(self.text)
            await QtCore.QThread.msleep(1000)


class CrepViewModel(QtWidgets.QMainWindow):
    def __init__(self, num):
        super().__init__()

        uic.loadUi(UI_crep, self)
        self.num_crep.setText(str(num))

        self.tracker = Changer()
        self.tracker.nextValueOfText.connect(self.setText)
        self.tracker.start()

    @QtCore.pyqtSlot(str)
    def setText(self, string):
        self.sensors1_lineEdit.setText(string)
