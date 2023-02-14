import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
# Hello world
# ghbrffhb
from pymodbus.client import ModbusSerialClient as ModbusClient, ModbusTcpClient
import sqlite3
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo
import time
import qtishka  # Это наш конвертированный файл дизайна
import proba
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import start
import ping
import Modbus
import subprocess
import psycopg2




class Button(QtWidgets.QPushButton):
    def __init__(self, text, size):  # !!!
        super().__init__()

        self.setText(f'{text}')  # !!! {text} {num}
        self.setFixedSize(*size)  # !!! (*size)


class ExampleApp(QtWidgets.QMainWindow, start.Ui_MainWindow, proba.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()

        self.modbusForm = ModbusForm()
        self.ping = Ping()

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        conn = psycopg2.connect(dbname="postgres", user="postgres", password="1111", host="127.0.0.1")
        cursor = conn.cursor()

        conn.autocommit = True
        # команда для создания базы данных metanit
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'niva1'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute('CREATE DATABASE niva1')
        # rest of the script
        # sql = "SELECT ‘CREATE DATABASE Niva’ WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = ‘Niva’)\gexec"
        #
        # # выполняем код sql
        # cursor.execute(sql)
        # print("База данных успешно создана")


        cursor.close()
        conn.close()


        con = psycopg2.connect(dbname='niva1', user='postgres', password='1111', host='127.0.0.1')

        cursor = con.cursor()
        con.autocommit = True
        cursor.execute("CREATE TABLE IF NOT EXISTS registr (id SERIAL PRIMARY KEY, login text,  password text)")

        cursor.execute("SELECT 1 FROM registr")
        exists = cursor.fetchone()
        if not exists:
            people = [("server", "1111"), ("Ilya", "1234"), ("Kate", "25")]
            cursor.executemany("INSERT INTO registr (login, password) VALUES (%s, %s)", people)

        cursor = con.cursor()
        cursor.execute("SELECT * FROM registr")

        # many_buttons = 16  # хотим создать 16 кнопок
        column = 2  # хотим разместить эти кнопки в 2 колонки
        size = (50, 50)  # размер кнопки, например 150х150

        layout = QtWidgets.QGridLayout(self.centralwidget)
        num = 0
        for elem in cursor.fetchall():
            btn = Button(f'{elem[1]}', size)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.onClicked(b))
            layout.addWidget(btn, num // column, num % column)
            num = num + 1
        self.pushButton.clicked.connect(lambda: self.NewUI(cursor))

    def onClicked(self, btn):
        # тут выполняются какие-то действия по нажатию на кнопку
        # допустим мы хотим скрыть кнопку, на которуй нажали
        # btn.hide()

        self.lineEdit.setText(btn.text())

        # for elem in cursor.fetchall():
        # self.pushButton0 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton0.setGeometry(QtCore.QRect(300, point, 75, 23))
        # self.pushButton0.setObjectName(f"pushButton{num}")
        # self.pushButton0.setText(f"{elem[0]}")
        # point=point+1
        # num=num+1

        # self.pushButton.clicked.connect(self.NewUI)

    def NewUI(self, cursor):
        check = 0
        cursor.execute("SELECT * FROM registr")
        if self.lineEdit_2.text() == '':
            self.label_3.setText("Введите пароль!!!")
            return
        for elem in cursor.fetchall():
            if self.lineEdit.text() == f"{elem[1]}" and self.lineEdit_2.text() == f"{elem[2]}":
                self.initUi(self)
                self.pushButton_22.clicked.connect(self.Ping)
                self.pushButton_39.clicked.connect(self.Modbusssss)
                self.pushButton_48.clicked.connect(lambda:self.PingTest(self.pushButton_48,self.lineEdit_12))
                self.pushButton_49.clicked.connect(lambda:self.PingTest(self.pushButton_49,self.lineEdit_13))
                self.pushButton_50.clicked.connect(lambda:self.PingTest(self.pushButton_50,self.lineEdit_14))
                self.checkBox_2.clicked.connect(self.Chicks)
                self.checkBox_3.clicked.connect(self.Chicks)
                self.pushButton_2.clicked.connect(self.VIhod)

                check = 1
        if check == 0:
            self.label_3.setText("Логин или пароль введен неверно")


    def VIhod(self):
        self.setupUi(self)
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="1111", host="127.0.0.1")
        cursor = conn.cursor()

        conn.autocommit = True
        # команда для создания базы данных metanit
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'niva1'")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute('CREATE DATABASE niva1')
        # rest of the script
        # sql = "SELECT ‘CREATE DATABASE Niva’ WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = ‘Niva’)\gexec"
        #
        # # выполняем код sql
        # cursor.execute(sql)
        # print("База данных успешно создана")

        cursor.close()
        conn.close()

        con = psycopg2.connect(dbname='niva1', user='postgres', password='1111', host='127.0.0.1')

        cursor = con.cursor()
        con.autocommit = True
        cursor.execute("CREATE TABLE IF NOT EXISTS registr (id SERIAL PRIMARY KEY, login text,  password text)")

        cursor.execute("SELECT 1 FROM registr")
        exists = cursor.fetchone()
        if not exists:
            people = [("server", "1111"), ("Ilya", "1234"), ("Kate", "25")]
            cursor.executemany("INSERT INTO registr (login, password) VALUES (%s, %s)", people)

        cursor = con.cursor()
        cursor.execute("SELECT * FROM registr")

        # many_buttons = 16  # хотим создать 16 кнопок
        column = 2  # хотим разместить эти кнопки в 2 колонки
        size = (50, 50)  # размер кнопки, например 150х150

        layout = QtWidgets.QGridLayout(self.centralwidget)
        num = 0
        for elem in cursor.fetchall():
            btn = Button(f'{elem[1]}', size)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.onClicked(b))
            layout.addWidget(btn, num // column, num % column)
            num = num + 1
        self.pushButton.clicked.connect(lambda: self.NewUI(cursor))


    def Chicks(self):
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

    def PingTest(self, btn,line):

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


class ModbusForm(QtWidgets.QMainWindow, Modbus.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()

        self.setupUi(self)
        # доступные порты
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
                               self.lineEdit_3.text(), self.comboBox_7.currentText(), self.lineEdit.text(),
                               self.lineEdit_2.text()))

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


class Ping(QtWidgets.QMainWindow, ping.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.PingTest)

    def PingTest(self):

        ip = self.lineEdit.text()
        if ip == '':
            self.pushButton.setStyleSheet('background-color: rgb(255,0,0);')
            return

        retcode = subprocess.call("ping -n 1 " + str(ip))
        if retcode != 0:
            self.pushButton.setStyleSheet('background-color: rgb(255,0,0);')
        else:
            self.pushButton.setStyleSheet('background-color: rgb(0,255,0);')


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


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
