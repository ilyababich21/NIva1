from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QIntValidator
from pymodbus.client import ModbusTcpClient

from serviceApp.ping.pingVm import Ping

UI_service = "resources/view/service/service_view.ui"


class ServiceViewModel(QtWidgets.QMainWindow):
    def __init__(self,database):
        super().__init__()
        uic.loadUi(UI_service, self)

        self.modbus_query = database.query_modbus()

        self.list_value = [self.modbus_query.ip_address, self.modbus_query.port,
                           self.modbus_query.slave_id, self.modbus_query.start_register,
                           self.modbus_query.count_register]
        self.list_lineedit = [self.ip_modbus_lineEdit, self.port_lineEdit, self.slave_id_lineEdit,
                              self.start_reg_lineEdit, self.end_reg_lineEdit]

        for one_lineedit, value in zip(self.list_lineedit, self.list_value):
            if one_lineedit == self.ip_modbus_lineEdit:
                regex = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
                self.ip_modbus_lineEdit.setValidator(QRegularExpressionValidator(
                    QRegularExpression("^" + regex + "\\." + regex + "\\." + regex + "\\." + regex + "$")))
            else:
                one_lineedit.setValidator(QIntValidator())
            one_lineedit.setText(str(value))

        self.ping = Ping(database)

        self.ping_query_pushButton.clicked.connect(lambda: self.ping.show())
        self.auto_checkBox.clicked.connect(self.check_timezone)
        self.manually_checkBox.clicked.connect(self.check_timezone)
        self.exit_pushButton.clicked.connect(lambda: self.close())
        self.clientTCP = None
        self.start_pushButton.clicked.connect(
            lambda: self.start_modbus(self.ip_modbus_lineEdit.text(), self.port_lineEdit.text(),
                                      self.start_reg_lineEdit.text(), self.end_reg_lineEdit.text(),
                                      self.slave_id_lineEdit.text()))

    def save_on_clicked_data(self):
        self.modbus_query.update_modbus_table(self.ip_modbus_lineEdit.text(), self.port_lineEdit.text(),
                                              self.slave_id_lineEdit.text(), self.start_reg_lineEdit.text(),
                                              self.end_reg_lineEdit.text(), )

    def start_modbus(self, ip_address, port, start_register, end_register, slave_id):
        if self.start_reg_lineEdit.text() == '':
            self.textEdit.setText("Старт-регистр обязателен для заполнения")
        else:
            self.clientTCP = ModbusTcpClient(host=ip_address, port=port)
            self.clientTCP.connect()
            if self.clientTCP.is_socket_open():
                self.status_label.setText("Подключено")
                result = self.clientTCP.read_holding_registers(int(start_register), int(end_register),
                                                               int(slave_id))
                self.textEdit.setText(str(result.registers))
                self.save_on_clicked_data()
            if not self.clientTCP.is_socket_open():
                self.status_label.setText("Нет Подключения")

    def check_timezone(self):
        if self.auto_checkBox.isChecked():
            self.time_server_label.setEnabled(True)
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
            self.time_server_label.setEnabled(False)
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
