from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QIntValidator
from pymodbus.client import ModbusTcpClient

from serviceApp.ping.pingVm import Ping

UI_service = "resources/view/service/service_view.ui"


class ServiceViewModel(QtWidgets.QMainWindow):
    def __init__(self, database):
        super().__init__()
        uic.loadUi(UI_service, self)
        self.database = database
        self.modbus_query = self.database.query_modbus()
        self.manuf_query = self.database.query_manufacture()

        self.list_value = [self.manuf_query.ip_address,self.manuf_query.port,self.manuf_query.count_shield,
                           self.manuf_query.count_dat, self.modbus_query.ip_address, self.modbus_query.port,
                           self.modbus_query.slave_id, self.modbus_query.start_register,
                           self.modbus_query.count_register]
        self.list_lineedit = [self.ip_address, self.port, self.count_crep, self.count_dat, self.ip_modbus_lineEdit,
                              self.port_lineEdit, self.slave_id_lineEdit,
                              self.start_reg_lineEdit, self.end_reg_lineEdit]

        for one_lineedit, value in zip(self.list_lineedit, self.list_value):
            if one_lineedit == self.ip_modbus_lineEdit or one_lineedit==self.ip_address:
                regex = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
                one_lineedit.setValidator(QRegularExpressionValidator(
                    QRegularExpression("^" + regex + "\\." + regex + "\\." + regex + "\\." + regex + "$")))
            else:
                one_lineedit.setValidator(QIntValidator())
            one_lineedit.setText(str(value))

        self.ping = Ping(database)
        # ИСПРАВИТЬ НАХОЙ ЭТУ ХУЕТУ
        self.ping_query_pushButton.clicked.connect(lambda: self.ping.show())
        self.auto_checkBox.clicked.connect(self.check_timezone)
        self.manually_checkBox.clicked.connect(self.check_timezone)
        self.exit_pushButton.clicked.connect(lambda: self.close())
        self.clientTCP = None
        self.start_pushButton.clicked.connect(self.start_modbus)
        self.save_change_pushButton.clicked.connect(self.save)

    def save(self):
        self.database.update_manufacture_table(self.manuf_query,[self.ip_address.text(), int(self.port.text()), int(self.count_crep.text()), int(self.count_dat.text())])

    def save_on_clicked_data(self):
        self.database.update_modbus_table(self.modbus_query, [self.ip_modbus_lineEdit.text(), self.port_lineEdit.text(),
                                                              self.slave_id_lineEdit.text(),
                                                              self.start_reg_lineEdit.text(),
                                                              self.end_reg_lineEdit.text()])

    def start_modbus(self):
        if self.start_reg_lineEdit.text() == '':
            self.textEdit.setText("Старт-регистр обязателен для заполнения")
        else:
            self.clientTCP = ModbusTcpClient(host=self.ip_modbus_lineEdit.text(), port=self.port_lineEdit.text())
            if self.clientTCP.connect():
                self.status_label.setText("Подключено")
                result = self.clientTCP.read_holding_registers(int(self.start_reg_lineEdit.text()),
                                                               int(self.end_reg_lineEdit.text()),
                                                               int(self.slave_id_lineEdit.text()))
                self.textEdit.setText(str(result.registers))
                self.save_on_clicked_data()
            else:
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
