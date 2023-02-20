from PyQt6 import QtCore
from PyQt6 import QtWidgets, uic
from PyQt6.QtSerialPort import QSerialPortInfo
from pymodbus.client import ModbusSerialClient as ModbusClient, ModbusTcpClient

UI_modbus = "fileUI/modbus.ui"


class Changer(QtCore.QThread):
    nextValueOfText = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False  # Флаг выполнения

    text = ''

    def run(self):
        self.running = True
        while self.running == True:
            if client:
                self.text += str(
                    client.read_holding_registers(int(addressssio), int(countio), unit=int(Slavik)).registers[0])
            else:
                self.text += str(
                    clientTCP.read_holding_registers(int(addressssio), int(countio), unit=int(Slavik)).registers[0])
            self.text += '\n'
            self.nextValueOfText.emit(self.text)

            QtCore.QThread.msleep(1000)


class ModbusForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_modbus, self)  # доступные порты
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portlist.append(port.portName())
        self.comboBox.addItems(portlist)

        self.checkBox.clicked.connect(self.vibor)

        self.checkBox_2.clicked.connect(self.vibor)
        self.changer = Changer()

        self.pushButton.clicked.connect(
            lambda: self.start(self.checkBox.isChecked(), self.comboBox.currentText(), self.comboBox_3.currentText(),
                               self.comboBox_2.currentText(),
                               self.comboBox_4.currentText(), self.comboBox_6.currentText(),
                               self.lineEdit_2.text(), self.comboBox_7.currentText(), self.lineEdit.text(),
                               self.lineEdit.text()))

        self.changer.nextValueOfText.connect(self.setText)
        self.pushButton_2.clicked.connect(self.stop)

    def stop(self):
        self.changer.running = False
        if client:
            client.close()
        else:
            clientTCP.close()

    def start(self, shchk, com_port, baudrate, stopbits, parity, SlaveID, address, count, label7, label8):
        global client
        client = None
        global clientTCP
        if self.primary_server_edit.text() == '':
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

                client = ModbusClient(port=com_port, baudrate=int(baudrate), stopbits=int(stopbits), parity=prt)
                try:
                    client.connect()
                    print('norm')
                    self.changer.start()
                except:
                    print('hueta')

            else:

                clientTCP = ModbusTcpClient(host=label7, port=int(label8))
                try:
                    clientTCP.connect()
                    print('norm')
                    self.changer.start()
                except:
                    print('hueta')

    @QtCore.pyqtSlot(str)
    def setText(self, string):
        self.textEdit.setText(string)

    def vibor(self):
        if self.checkBox.isChecked():
            self.widget111.setEnabled(True)
            self.widget222.setEnabled(False)
        else:
            self.widget111.setEnabled(False)
            self.widget222.setEnabled(True)
