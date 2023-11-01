from PyQt6 import QtWidgets, QtCore, uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QSplashScreen

from authorization.button_username import ButtonForUserName
from ifcApp.ifc.ifc_vm import IfcViewModel
from serviceApp.service.service_vm import ServiceViewModel

UI_authorization = "resources/view/authorization_view.ui"
UI_main = "resources/view/service/service_view.ui"


class Authorization(QtWidgets.QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.database = database
        self.load_ui_auth()

    def load_ui_auth(self):
        print("suka")
        self.size_of_user_button = (100, 60)
        uic.loadUi(UI_authorization, self)
        self.log_in_button.clicked.connect(self.login)
        self.view_user_from_database()

    def login(self):
        login = self.login_lineEdit.text()
        password = self.password_lineEdit.text()
        role,self.id_user = self.database.check_user(login, password)
        if role:
            self.on_login_successful(role)
        else:
            self.on_login_failed(password)

    def on_login_successful(self, role):
        if role == 'admin':
            self.open_admin_ui()
        elif role == "miner":
            self.open_miner_ui()
        elif role == "service":
            self.open_service_ui()

    def on_login_failed(self, password):
        if password == '':
            self.check_label.setText("Введите пароль!")
        else:
            self.check_label.setText("Логин или пароль введен неверно")
        self.password_lineEdit.setFocus()

    def open_service_ui(self):
        self.service = ServiceViewModel(self.database)
        self.service.show()

    def open_admin_ui(self):
        splash = QSplashScreen(QPixmap("resources/image/logotip-niva-pochti-bez-fona.png"))
        splash.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        splash.show()
        self.admin_ui = IfcViewModel(self, self.database)
        self.admin_ui.setWindowTitle("Niva-M" + f"  {self.login_lineEdit.text()}")
        splash.finish(self.admin_ui)
        self.admin_ui.showMaximized()
        self.close()

    def open_miner_ui(self):
        splash = QSplashScreen(QPixmap("resources/image/logotip-niva-pochti-bez-fona.png"))
        splash.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        splash.show()
        self.miner_ui = IfcViewModel(self, self.database)
        self.miner_ui.setWindowTitle("Niva-M" + f"  {self.login_lineEdit.text()}")
        self.miner_ui.role_for_miner()
        splash.finish(self.miner_ui)

        self.miner_ui.showMaximized()
        self.close()

    def view_user_from_database(self):
        for user in self.database.users_list():
            username_button = ButtonForUserName(f'{user.login}', self.size_of_user_button)  # !!!
            username_button.clicked.connect(
                lambda ch, one_button=username_button: self.clicked_button_username(one_button))
            self.layoutButton.addWidget(username_button)

    def clicked_button_username(self, btn):
        self.login_lineEdit.setText(btn.text())
        self.password_lineEdit.setText("")
        self.password_lineEdit.setFocus()
