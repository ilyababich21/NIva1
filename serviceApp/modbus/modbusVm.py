import sys

from PyQt6 import QtCore
from PyQt6 import QtWidgets, uic
from PyQt6.QtSerialPort import QSerialPortInfo
from pymodbus.client import ModbusSerialClient,ModbusTcpClient


UI_modbus = "view/service/modbus_view.ui"


class Changer(QtCore.QThread):
    nextValueOfText = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False

    text = ''

    def run(self):
        self.running = True
        while self.running == True:
            if client_modbus:
                self.text += str(
                    client_modbus.read_holding_registers(int(addressssio), int(countio), int(Slavik)).registers[0])
            else:
                self.text += str(
                    clientTCP.read_holding_registers(int(addressssio), int(countio), int(Slavik)).registers)
            self.text += '\n'
            self.nextValueOfText.emit(self.text)

            QtCore.QThread.msleep(1000)


class ModbusForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_modbus, self)  # доступные порты
        self.changer = Changer()
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portlist.append(port.portName())
        self.device_comboBox.addItems(portlist)
        self.RTU_checkBox.clicked.connect(self.choice_checkBox)
        self.TCP_checkBox.clicked.connect(self.choice_checkBox)
        self.changer.nextValueOfText.connect(self.setText)
        self.exit_pushButton.clicked.connect(self.stop)
        self.start_pushButton.clicked.connect(
            lambda: self.start(self.RTU_checkBox.isChecked(), self.device_comboBox.currentText(),
                               self.speed_comboBox.currentText(), self.stop_bit_comboBox.currentText(),
                               self.parity_comboBox.currentText(), self.address_device_comboBox.currentText(),
                               self.lineEdit_3.text(), self.number_comboBox.currentText(),
                               self.ip_modbus_lineEdit.text(), self.port_lineEdit.text()))

    def stop(self):
        self.changer.running = False
        if client_modbus:
            client_modbus.close()
        else:
            clientTCP.close()

    def start(self, shchk, com_port, baudrate, stopbits, parity, SlaveID, address, count, label7, label8):
        global clientRTU
        global client_modbus
        client_modbus=None
        global clientTCP
        if self.lineEdit_3.text() == '':
            self.textEdit.setText("Старт-регистр обязателен для заполнения")
        else:
            global Slavik, addressssio, countio
            addressssio = address
            countio = count
            Slavik = SlaveID
            if shchk:
                prt = parity
                if prt == "odd":
                    prt = "O"
                elif prt == "even":
                    prt = "E"
                else:
                    prt = "N"

                client_modbus = ModbusSerialClient(port=com_port, baudrate=int(baudrate), stopbits=int(stopbits), parity=prt)
                try:
                    client_modbus.connect()
                    print('norm')
                    self.changer.start()
                except:
                    print('No connection')

            else:

                clientTCP = ModbusTcpClient(host=label7, port=label8)
                try:
                    clientTCP.connect()
                    print('norm')
                    self.changer.start()
                except:
                    print('hueta')

    @QtCore.pyqtSlot(str)
    def setText(self, string):
        self.textEdit.setText(string)

    def choice_checkBox(self):
        if self.RTU_checkBox.isChecked():
            self.widget111.setEnabled(True)
            self.widget222.setEnabled(False)
        else:
            self.widget111.setEnabled(False)
            self.widget222.setEnabled(True)
