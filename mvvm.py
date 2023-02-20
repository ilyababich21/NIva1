import subprocess
import sys

import psycopg2
from PyQt6 import QtCore, QtWidgets, uic
from PyQt6.QtSerialPort import QSerialPortInfo
from pymodbus.client import ModbusSerialClient as ModbusClient, ModbusTcpClient

UI_autoriation = "fileUI/authorization.ui"
UI_main = "fileUI/main.ui"
UI_ping = "fileUI/ping.ui"
UI_modbus = "fileUI/modbus.ui"


class Button(QtWidgets.QPushButton):
    def __init__(self, text, size):  # !!!
        super().__init__()

        self.setText(f'{text}')  # !!! {text} {num}
        self.setFixedSize(*size)  # !!! (*size)
        self.setStyleSheet(
            "  background-color: #0d6efd;color: #fff;font-weight: 1000;font-weight: 1000;"
            "border-radius: 8px;border: 1px "
            "solid #0d6efd;padding: 5px 15px; margin-top: 10px;")


class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.modbusForm = ModbusForm()
        self.ping = Ping()
        uic.loadUi(UI_autoriation, self)
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="1111", host="127.0.0.1")
        cursor = conn.cursor()

        conn.autocommit = True
        # команда для создания базы данных metanit
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'niva1'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute('CREATE DATABASE niva1')

        cursor.close()
        conn.close()

        con = psycopg2.connect(dbname='niva1', user='postgres', password='1111', host='127.0.0.1')

        cursor = con.cursor()
        con.autocommit = True
        cursor.execute("CREATE TABLE IF NOT EXISTS credential (id SERIAL PRIMARY KEY, login text,  password text)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS network_interface (id SERIAL PRIMARY KEY, device text  ,"
            " addressing text  , ip_address text  , subnet_mask text  )")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS setting_network (id SERIAL PRIMARY KEY, host_name text  ,"
            "domain_name text  ,primary_name_server text  ,secondary_name_server text ,default_gateway text)")

        cursor.execute("SELECT 1 FROM credential")
        exists = cursor.fetchone()
        if not exists:
            users = [("server", "1111"), ("IFC", "ifc")]
            cursor.executemany("INSERT INTO credential (login, password) VALUES (%s, %s)", users)

        cursor.execute("SELECT 1 FROM setting_network")
        exists = cursor.fetchone()
        if not exists:
            settings = ["Niva", "Niva main", "main", "main2", "127.0.0.1"]
            cursor.execute(
                "INSERT INTO setting_network (host_name, domain_name ,"
                " primary_name_server, secondary_name_server, default_gateway) VALUES (%s, %s, %s, %s, %s)",
                settings)

        cursor.execute("SELECT * FROM credential")

        size = (100, 60)  # размер кнопки, например 150х150

        layout = self.layoutButton

        num = 0
        for elem in cursor.fetchall():
            btn = Button(f'{elem[1]}', size)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.onClicked(b))
            layout.addWidget(btn)
            num = num + 1
        self.log_in_button.clicked.connect(lambda: self.NewUI(cursor))

    def onClicked(self, btn):

        self.login_lineEdit.setText(btn.text())

    def NewUI(self, cursor):
        check = 0

        cursor.execute("SELECT * FROM credential")
        if self.password_lineEdit.text() == '':
            self.label.setText("Введите пароль!!!")
            return
        for elem in cursor.fetchall():
            if self.login_lineEdit.text() == f"{elem[1]}" and self.password_lineEdit.text() == f"{elem[2]}":
                check = 1

                uic.loadUi(UI_main, self)

                cursor.execute("SELECT * FROM setting_network")
                id, host_name, domain_name, primary_name_server, secondary_name_server, default_gateway = cursor.fetchone()
                self.host_name_edit.setText(host_name)
                self.domain_name_edit.setText(domain_name)
                self.primary_server_edit.setText(primary_name_server)
                self.secondary_server_edit.setText(secondary_name_server)
                self.default_gateway_edit.setText(default_gateway)

                cursor.execute("SELECT * FROM network_interface")
                ip_d, device, addressing, ip_address, subnet_mask = cursor.fetchone()
                print(ip_d, device, addressing, ip_address, subnet_mask)
                if device:
                    for elem in range(self.device_combobox.count()):
                        if device == self.device_combobox.itemText(elem):
                            self.device_combobox.setCurrentIndex(elem)

                print(device, addressing, ip_address, subnet_mask)
                if addressing:
                    for elem in range(self.adressing_combobox.count()):
                        if addressing == self.adressing_combobox.itemText(elem):
                            self.adressing_combobox.setCurrentIndex(elem)

                self.ip_address_edit.setText(ip_address)
                self.mask_edit.setText(subnet_mask)

                self.pushButton_22.clicked.connect(self.Ping)
                self.pushButton_39.clicked.connect(self.Modbusssss)
                self.pushButton_48.clicked.connect(lambda: self.PingTest(self.pushButton_48, self.lineEdit_12))
                self.pushButton_49.clicked.connect(lambda: self.PingTest(self.pushButton_49, self.lineEdit_13))
                self.pushButton_50.clicked.connect(lambda: self.PingTest(self.pushButton_50, self.lineEdit_14))
                self.checkBox_2.clicked.connect(self.check_timezone)
                self.checkBox_3.clicked.connect(self.check_timezone)
                self.exit_pushButton.clicked.connect(lambda: self.VIhod(cursor))

        if check == 0:
            self.label.setText("Логин или пароль введен неверно")
        elif check == 2:
            pass

    def VIhod(self, cursor):
        print(self.host_name_edit.text(), self.domain_name_edit.text(), self.primary_server_edit.text(),
              self.secondary_server_edit.text(), self.default_gateway_edit.text())
        people = [self.host_name_edit.text(), self.domain_name_edit.text(), self.primary_server_edit.text(),
                  self.secondary_server_edit.text(), self.default_gateway_edit.text()]
        cursor.execute(
            "UPDATE setting_network SET host_name =%s, domain_name =%s,"
            " primary_name_server =%s, secondary_name_server =%s, default_gateway =%s  WHERE id=1",
            people)

        print(self.device_combobox.currentText(), self.adressing_combobox.currentText(),
              self.ip_address_edit.text(), self.mask_edit.text())
        people = [self.device_combobox.currentText(), self.adressing_combobox.currentText(),
                  self.ip_address_edit.text(), self.mask_edit.text()]
        cursor.execute(
            "UPDATE network_interface SET device =%s, addressing =%s, ip_address =%s, subnet_mask =%s  WHERE id=1",
            people)

        uic.loadUi(UI_autoriation, self)
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="1111", host="127.0.0.1")
        cursor = conn.cursor()

        conn.autocommit = True
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'niva1'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute('CREATE DATABASE niva1')

        cursor.close()
        conn.close()

        con = psycopg2.connect(dbname='niva1', user='postgres', password='1111', host='127.0.0.1')

        cursor = con.cursor()
        con.autocommit = True
        cursor.execute("CREATE TABLE IF NOT EXISTS credential (id SERIAL PRIMARY KEY, login text,  password text)")

        cursor.execute("SELECT 1 FROM credential")
        exists = cursor.fetchone()
        if not exists:
            users = [("server", "1111"), ("IFC", "ifc")]
            cursor.executemany("INSERT INTO credential (login, password) VALUES (%s, %s)", users)

        cursor.execute("SELECT * FROM credential")
        size = (100, 60)  # размер кнопки, например 150х150

        layout = self.layoutButton

        num = 0
        for elem in cursor.fetchall():
            btn = Button(f'{elem[1]}', size)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.onClicked(b))
            layout.addWidget(btn)
            num = num + 1
        self.log_in_button.clicked.connect(lambda: self.NewUI(cursor))

    def check_timezone(self):
        if self.checkBox_2.isChecked():
            self.label_13.setEnabled(True)
            self.lineEdit_8.setEnabled(True)
            self.label_14.setEnabled(False)
            self.label_15.setEnabled(False)
            self.label_16.setEnabled(False)
            self.label_17.setEnabled(False)
            self.label_18.setEnabled(False)
            self.comboBox_6.setEnabled(False)
            self.comboBox_7.setEnabled(False)
            self.comboBox_8.setEnabled(False)
            self.comboBox_9.setEnabled(False)
            self.comboBox_10.setEnabled(False)
        else:
            self.label_13.setEnabled(False)
            self.lineEdit_8.setEnabled(False)
            self.label_14.setEnabled(True)
            self.label_15.setEnabled(True)
            self.label_16.setEnabled(True)
            self.label_17.setEnabled(True)
            self.label_18.setEnabled(True)
            self.comboBox_6.setEnabled(True)
            self.comboBox_7.setEnabled(True)
            self.comboBox_8.setEnabled(True)
            self.comboBox_9.setEnabled(True)
            self.comboBox_10.setEnabled(True)

    def Ping(self):
        self.ping.show()

    def Modbusssss(self):
        self.modbusForm.show()

    def PingTest(self, btn, line):

        ip = line.text()
        if ip == '':
            btn.setStyleSheet('background-color: rgb(255,0,0);')
            return

        retcode = subprocess.call("ping -n 1 " + str(ip))
        if retcode != 0:
            btn.setStyleSheet('background-color: rgb(255,0,0);')
        else:
            btn.setStyleSheet('background-color: rgb(0,255,0);')


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

        self.checkBox.clicked.connect(self.Vibor)

        self.checkBox_2.clicked.connect(self.Vibor)
        self.changer = Changer()

        self.pushButton.clicked.connect(
            lambda: self.START(self.checkBox.isChecked(), self.comboBox.currentText(), self.comboBox_3.currentText(),
                               self.comboBox_2.currentText(),
                               self.comboBox_4.currentText(), self.comboBox_6.currentText(),
                               self.lineEdit_2.text(), self.comboBox_7.currentText(), self.lineEdit.text(),
                               self.lineEdit.text()))

        self.changer.nextValueOfText.connect(self.setText)
        self.pushButton_2.clicked.connect(self.STOP)

    def STOP(self):
        self.changer.running = False
        if client:
            client.close()
        else:
            clientTCP.close()

    def START(self, shchk, com_port, baudrate, stopbits, parity, SlaveID, address, count, label7, label8):
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

    def Vibor(self):
        if self.checkBox.isChecked():
            self.widget111.setEnabled(True)
            self.widget222.setEnabled(False)
        else:
            self.widget111.setEnabled(False)
            self.widget222.setEnabled(True)


class Ping(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()

        uic.loadUi(UI_ping, self)
        self.check_pushButton.clicked.connect(self.PingTest)

    def PingTest(self):

        ip = self.ip_lineEdit.text()
        if ip == '':
            self.check_pushButton.setStyleSheet('background-color: rgb(255,0,0);')
            return

        retcode = subprocess.call("ping -n 1 " + str(ip))
        if retcode != 0:
            self.check_pushButton.setStyleSheet('background-color: rgb(255,0,0);')
        else:
            self.check_pushButton.setStyleSheet('background-color: rgb(0,255,0);')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    # serial = QSerialPort()
    # serial.setBaudRate(9600)
    # portlist = []
    # ports = QSerialPortInfo().availablePorts()
    # for port in ports:
    #     portlist.append(port.portName())
    # window.comL.addItems(portlist)
    # text=''
    # window.closeB.isEnabledTo(False)
    # window.ReadB.isEnabledTo(False)
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение
