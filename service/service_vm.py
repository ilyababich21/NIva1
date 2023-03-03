import subprocess
from PyQt6 import QtWidgets, uic
import service.service_model as model
from service.service_model import session, Users, SettingNetwork, NetworkInterface
from modbus.modbusVm import ModbusForm
from ping.pingVm import Ping
from ifc.ifc_vm import IfcViewModel

UI_authorization = "view/authorization_view.ui"
UI_main = "view/service/service_view.ui"


class Button(QtWidgets.QPushButton):
    def __init__(self, text, size):  # !!!
        super().__init__()

        self.setText(f'{text}')  # !!! {text} {num}
        self.setFixedSize(*size)  # !!! (*size)
        self.setStyleSheet(
            "  background-color: #0d6efd;color: #fff;font-weight: 1000;font-weight: 1000;"
            "border-radius: 8px;border: 1px "
            "solid #0d6efd;padding: 5px 15px; margin-top: 10px;")


class ServiceViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ifc = IfcViewModel()
        self.modbusForm = ModbusForm()
        self.ping = Ping()
        self.size_of_user_button = (100, 60)

        uic.loadUi(UI_authorization, self)

        self.users = session.query(Users).all()
        if self.users == []:
            session.add_all([Users(login="service", password="1111", role="service"),
                             Users(login="IFC", password="ifc", role="user")])
            session.commit()
            self.users = session.query(model.Users).all()
        self.setting_network = self.check_first_load(SettingNetwork)
        self.network_interface = self.check_first_load(NetworkInterface)

        self.get_user_from_database()
        self.log_in_button.clicked.connect(self.check_credential)

    def check_first_load(self, model_object):
        object_database = session.get(model_object, 1)
        if object_database is None:
            session.add(model_object())
            session.commit()
            object_database = session.get(model_object, 1)
        return object_database

    def check_credential(self):

        check = 0
        if self.password_lineEdit.text() == '':
            self.check_label.setText("Введите пароль!!!")
            return
        for user in self.users:
            if self.login_lineEdit.text() == f"{user.login}" \
                    and self.password_lineEdit.text() == f"{user.password}":
                role = user.role
                check = 1
        if check == 0:
            self.check_label.setText("Логин или пароль введен неверно")
            return
        if role == 'service':
            self.load_main_service_UI()
        if role == 'user':
            self.ifc.show()

    def load_main_service_UI(self):
        uic.loadUi(UI_main, self)
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
        self.exit_pushButton.clicked.connect(self.exit_from_menu)
        self.save_change_pushButton.clicked.connect(self.save_on_clicked_data)

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

    def exit_from_menu(self):
        print(self.host_name_edit.text(), self.domain_name_edit.text(), self.primary_server_edit.text(),
              self.secondary_server_edit.text(), self.default_gateway_edit.text())

        uic.loadUi(UI_authorization, self)

        self.get_user_from_database()

        self.log_in_button.clicked.connect(self.check_credential)

    def ping_show(self):
        self.ping.show()

    def on_clicked(self, btn):
        self.login_lineEdit.setText(btn.text())
        self.password_lineEdit.setFocus()

    def get_user_from_database(self):
        layout = self.layoutButton
        num = 0
        for user in self.users:
            print(f"{user.id}.{user.login} ({user.password})")
            btn = Button(f'{user.login}', self.size_of_user_button)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.on_clicked(b))
            layout.addWidget(btn)
            num = num + 1

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
