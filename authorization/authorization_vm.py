from PyQt6 import QtWidgets, uic

from authorization.authorization_model import Users, Role_ifc
from ifcApp.ifc.ifc_vm import IfcViewModel
from serviceApp.service.service_model import session
from serviceApp.service.service_vm import ServiceViewModel

UI_authorization = "view/authorization_view.ui"
UI_main = "view/service/service_view.ui"


class ButtonForUserName(QtWidgets.QPushButton):
    def __init__(self, text, size):  # !!!
        super().__init__()

        self.setText(f'{text}')  # !!! {text} {num}
        self.setFixedSize(*size)  # !!! (*size)
        self.setStyleSheet(
            "  background-color: #0d6efd;color: #fff;font-weight: 1000;font-weight: 1000;"
            "border-radius: 8px;border: 1px "
            "solid #0d6efd;padding: 5px 15px; margin-top: 10px;")


class Authorization(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.service = ServiceViewModel()
        self.size_of_user_button = (100, 60)
        uic.loadUi(UI_authorization, self)
        self.query_from_database_users = session.query(Users).filter(Users.role_id <= 3).all()
        self.qury_role = session.query(Role_ifc).all()

        if self.qury_role == []:
            session.add_all([Role_ifc(role="admin", description="Администратор"),
                             Role_ifc(role="miner", description="Шахтёр")])
            session.commit()

        if self.query_from_database_users == []:
            session.add_all([Users(login="service", password="1111", manufacture_id=1, role_id=3),
                             Users(login="IFC", password="ifc", manufacture_id=1, role_id=1)])

            session.commit()
        self.query_from_database_users = session.query(Users).all()
        self.view_user_from_database()
        self.log_in_button.clicked.connect(self.check_credential)

    def view_user_from_database(self):
        for user in self.query_from_database_users:
            username_button = ButtonForUserName(f'{user.login}', self.size_of_user_button)  # !!!
            username_button.clicked.connect(
                lambda ch, one_button=username_button: self.clicked_button_username(one_button))
            self.layoutButton.addWidget(username_button)

    def clicked_button_username(self, btn):
        self.login_lineEdit.setText(btn.text())
        self.password_lineEdit.setText("")
        self.password_lineEdit.setFocus()

    def check_credential(self):
        username = self.login_lineEdit.text()
        password = self.password_lineEdit.text()
        check = 0
        if password == '':
            self.check_label.setText("Введите пароль!!!")
            return
        for user in self.query_from_database_users:
            if username == f"{user.login}" and password == f"{user.password}":
                match user.role.role:
                    case "admin":
                        ifc = IfcViewModel()
                        ifc.showMaximized()
                        del ifc
                    case "miner":
                        ifc = IfcViewModel()
                        ifc.role_for_miner()
                        ifc.showMaximized()
                        del ifc
                    case "service":
                        self.service.show()
                check = 1
        if check == 0:
            self.check_label.setText("Логин или пароль введен неверно")
        # self.close()

