import subprocess
import sys

from PyQt6 import QtWidgets, uic

from modbus.modbusVm import ModbusForm
from model import connection_database
from model import work_network_interface
from model import work_setting_network
from model import work_users
from ping.pingVm import Ping

UI_authorization = "fileUI/authorization.ui"
UI_main = "fileUI/main.ui"


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
        uic.loadUi(UI_authorization, self)
        self.connectionDb = connection_database()
        size = (100, 60)  # размер кнопки, например 150х150
        layout = self.layoutButton
        self.users = work_users()
        self.settingNetwork = work_setting_network()
        self.networkInterface = work_network_interface()

        num = 0
        for p in self.users:
            btn = Button(f'{p.login}', size)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.on_clicked(b))
            layout.addWidget(btn)
            num = num + 1

        self.log_in_button.clicked.connect(self.NewUI)

    def on_clicked(self, btn):
        self.login_lineEdit.setText(btn.text())

    def NewUI(self):
        check = 0
        if self.password_lineEdit.text() == '':
            self.check_label.setText("Введите пароль!!!")
            return
        for user in self.users:
            if self.login_lineEdit.text() == f"{user.login}" \
                    and self.password_lineEdit.text() == f"{user.password}":
                check = 1

                uic.loadUi(UI_main, self)
                self.host_name_edit.setText(self.settingNetwork.host_name)
                self.domain_name_edit.setText(self.settingNetwork.domain_name)
                self.primary_server_edit.setText(self.settingNetwork.primary_name_server)
                self.secondary_server_edit.setText(self.settingNetwork.secondary_name_server)
                self.default_gateway_edit.setText(self.settingNetwork.default_gateway)

                for elem in range(self.device_combobox.count()):
                    if self.networkInterface.device == self.device_combobox.itemText(elem):
                        self.device_combobox.setCurrentIndex(elem)

                for elem in range(self.adressing_combobox.count()):
                    if self.networkInterface.addressing == self.adressing_combobox.itemText(elem):
                        self.adressing_combobox.setCurrentIndex(elem)

                self.ip_address_edit.setText(self.networkInterface.ip_address)
                self.mask_edit.setText(self.networkInterface.subnet_mask)

                self.ping_query_pushButton.clicked.connect(self.ping_show)
                self.scan_modbus_pushButton.clicked.connect(self.modbus_show)
                self.test_alz_pushButton.clicked.connect(
                    lambda: self.ping_test_for_button(self.test_alz_pushButton, self.ip_comp_lineEdit))
                self.main_drive_pushButton.clicked.connect(
                    lambda: self.ping_test_for_button(self.main_drive_pushButton, self.ip_main_comp_lineEdit))
                self.second_drive_pushButton.clicked.connect(
                    lambda: self.ping_test_for_button(self.second_drive_pushButton, self.second_drive_lineEdit))
                self.auto_checkBox.clicked.connect(self.check_timezone)
                self.manually_checkBox.clicked.connect(self.check_timezone)
                self.exit_pushButton.clicked.connect(self.exit_service)

        if check == 0:
            self.check_label.setText("Логин или пароль введен неверно")
        elif check == 2:
            pass

    def exit_service(self):
        self.settingNetwork.host_name = self.host_name_edit.text()
        self.settingNetwork.domain_name = self.domain_name_edit.text()
        self.settingNetwork.primary_name_server = self.primary_server_edit.text()
        self.settingNetwork.secondary_name_server = self.secondary_server_edit.text()
        self.settingNetwork.default_gateway = self.default_gateway_edit.text()
        self.networkInterface.device = self.device_combobox.currentText()
        self.networkInterface.addressing = self.adressing_combobox.currentText()
        self.networkInterface.ip_address = self.ip_address_edit.text()
        self.networkInterface.subnet_mask = self.mask_edit.text()

        uic.loadUi(UI_authorization, self)
        size = (100, 60)  # размер кнопки, например 150х150
        layout = self.layoutButton
        num = 0
        for p in self.users:
            btn = Button(f'{p.login}', size)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.on_clicked(b))
            layout.addWidget(btn)
            num = num + 1
        self.log_in_button.clicked.connect(self.NewUI)

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

    def ping_show(self):
        self.ping.show()

    def modbus_show(self):
        self.modbusForm.show()

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
