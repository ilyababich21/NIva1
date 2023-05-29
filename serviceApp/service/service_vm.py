import subprocess

from PyQt6 import QtWidgets, uic

from serviceApp.modbus.modbusVm import ModbusForm
from serviceApp.ping.pingVm import Ping
from serviceApp.service.service_model import session, SettingNetwork, NetworkInterface

UI_service = "view/service/service_view.ui"


class ServiceViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.modbusForm = ModbusForm()
        self.ping = Ping()
        uic.loadUi(UI_service, self)
        self.setting_network = self.check_first_load(SettingNetwork)
        self.network_interface = self.check_first_load(NetworkInterface)
        self.host_name_edit.setText(self.setting_network.host_name)
        self.domain_name_edit.setText(self.setting_network.domain_name)
        self.primary_server_edit.setText(self.setting_network.primary_name_server)
        self.secondary_server_edit.setText(self.setting_network.secondary_name_server)
        self.default_gateway_edit.setText(self.setting_network.default_gateway)

        for elem in range(self.device_combobox.count()):
            if self.network_interface.device == self.device_combobox.itemText(elem):
                self.device_combobox.setCurrentIndex(elem)

        for elem in range(self.adressing_combobox.count()):
            if self.network_interface.addressing == self.adressing_combobox.itemText(elem):
                self.adressing_combobox.setCurrentIndex(elem)

        self.ip_address_edit.setText(self.network_interface.ip_address)
        self.mask_edit.setText(self.network_interface.subnet_mask)

        self.ping_query_pushButton.clicked.connect(lambda: self.ping.show())
        self.scan_modbus_pushButton.clicked.connect(lambda: self.modbusForm.show())
        self.test_alz_pushButton.clicked.connect(
            lambda: self.ping_test_for_button(self.test_alz_pushButton, self.ip_comp_lineEdit))
        self.main_drive_pushButton.clicked.connect(
            lambda: self.ping_test_for_button(self.main_drive_pushButton, self.ip_main_comp_lineEdit))
        self.second_drive_pushButton.clicked.connect(
            lambda: self.ping_test_for_button(self.second_drive_pushButton, self.second_drive_lineEdit))
        self.auto_checkBox.clicked.connect(self.check_timezone)
        self.manually_checkBox.clicked.connect(self.check_timezone)
        self.exit_pushButton.clicked.connect(lambda: self.close())
        self.save_change_pushButton.clicked.connect(self.save_on_clicked_data)

    def check_first_load(self, model_object):
        object_database = session.get(model_object, 1)
        if object_database is None:
            session.add(model_object())
            session.commit()
            object_database = session.get(model_object, 1)
        return object_database

    def save_on_clicked_data(self):
        self.setting_network.update_setting_network(self.host_name_edit.text(),
                                                    self.domain_name_edit.text(),
                                                    self.primary_server_edit.text(),
                                                    self.secondary_server_edit.text(),
                                                    self.default_gateway_edit.text())

        self.network_interface.update_network_interface(self.device_combobox.currentText(),
                                                        self.adressing_combobox.currentText(),
                                                        self.ip_address_edit.text(), self.mask_edit.text())

        session.refresh(self.setting_network)
        session.refresh(self.network_interface)

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

    def ping_test_for_button(self, btn, line):
        ip = line.text()
        if ip == '':
            btn.setStyleSheet('background-color: rgb(255,0,0);')
            return
        retcode = subprocess.call("ping -n 1 " + str(ip))
        if retcode != 0:
            btn.setStyleSheet('background-color: rgb(255,0,0);')
        else:
            btn.setStyleSheet('background-color: rgb(0,255,0);')
