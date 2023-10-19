

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QMainWindow

from authorization.authorization_model import Users, Role
from connection_to_db import session
from ifcApp.ifc.users.groupbox_for_users import GroupBoxForUser

UI_user = "resources/view/ifc/user/user.ui"


class UserInIfc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qury_role = session.query(Role).filter(Role.id <= 2).all()
        self.users = None
        self.groupbox_in_users = None
        self.list_users_login = None
        self.list_groupbox_for_users = None
        self.load_UI()

    def load_UI(self):
        self.list_groupbox_for_users = []
        self.list_users_login = []
        uic.loadUi(UI_user, self)
        self.users = session.query(Users).filter(Users.role_id <= 2).all()
        for user in self.users:
            self.groupbox_in_users = GroupBoxForUser()
            if not len(self.users) == len(self.list_groupbox_for_users):
                self.list_groupbox_for_users.append(self.groupbox_in_users)
                self.list_users_login.append(user.login)
            self.groupbox_in_users.username_label.setText(user.login)
            match user.role.role:
                case "admin":
                    self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("resources/image/user/user_admin.png"))
                    self.groupbox_in_users.admin_pushButton.setStyleSheet(" background-color: #00ff00;")
                case "miner":
                    self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("resources/image/user/user_control.png"))
                    self.groupbox_in_users.pitman_pushButton.setStyleSheet(" background-color: #00ff00;")
                case _:
                    self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("resources/image/user/detect_person.png"))
                    self.groupbox_in_users.pitman_pushButton.setStyleSheet(" background-color: #00ff00;")

            self.layout_user_groupbox.addWidget(self.groupbox_in_users)
        self.add_user_pushButton.clicked.connect(self.show_add_user)
        self.delete_user_pushButton.clicked.connect(self.delete_user)

    def show_add_user(self):
        uic.loadUi("resources/view/ifc/user/add user.ui", self)
        for item in self.qury_role:
            self.law.addItem(item.description)
        self.add.clicked.connect(self.add_to_database_on_clicked)

    def add_to_database_on_clicked(self):
        for item in self.qury_role:
            if self.law.currentText() == item.description:
                print(item.id)
                session.add_all(
                    [Users(login=f"{self.username.text()}", password=f"{self.password.text()}", manufacture_id=1,
                           role_id=f"{item.id}")])
                session.commit()

            self.load_UI()

    def delete_user(self):
        try:
            for action in range(len(self.list_groupbox_for_users)):
                if self.list_groupbox_for_users[action].radioButton.isChecked():
                    delete_query = session.query(Users).filter(Users.login == self.list_users_login[action]).first()
                    session.delete(delete_query)
                    session.commit()
                    self.load_UI()
        except:
            print("you delete two users")

    # def change_user(self):
    #     uic.loadUi("view/ifc/add user.ui", self)
    #     self.label.setText("Изменение пользователя")
    #     for elem in range(len(self.list_groupbox_for_users)):
    #         self.username.setText(f"{self.list_users_login[elem]}")
