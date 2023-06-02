from PyQt6 import QtWidgets, uic

from authorization.authorization_model import Users
from ifcApp.ifc.ifc_vm import IfcViewModel
from serviceApp.service.service_model import session
from serviceApp.service.service_vm import ServiceViewModel

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


class Authorization(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.service = ServiceViewModel()
        self.ifc = IfcViewModel()

        self.size_of_user_button = (100, 60)

        uic.loadUi(UI_authorization, self)

        self.users = session.query(Users).all()

        if self.users == []:
            session.add_all([Users(login="service", password="1111", role="service"),
                             Users(login="IFC", password="ifc", role="user")])
            session.commit()
            self.users = session.query(Users).all()
        self.view_user_from_database()
        self.log_in_button.clicked.connect(self.check_credential)

    def view_user_from_database(self):
        layout = self.layoutButton
        num = 0
        for user in self.users:
            # print({user.role})
            # print(f"{user.id}.{user.login} ({user.password})")
            btn = Button(f'{user.login}', self.size_of_user_button)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.on_clicked(b))
            layout.addWidget(btn)
            num = num + 1

    def on_clicked(self, btn):
        self.login_lineEdit.setText(btn.text())
        self.password_lineEdit.setText("")
        self.password_lineEdit.setFocus()

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
            self.service.show()
        if role == 'user':
            self.ifc.showMaximized()
