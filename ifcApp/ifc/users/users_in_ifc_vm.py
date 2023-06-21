from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QMainWindow

from authorization.authorization_model import Users
from ifcApp.ifc.users.groupbox_for_users import GroupBoxForUser
from serviceApp.service.service_model import session

UI_user = "view/ifc/user.ui"


class UserInIfc(QMainWindow):
    def __init__(self):
        super().__init__()

        self.users = None
        self.groupbox_in_users = None
        self.list_users_login = None
        self.list_groupbox_for_users = None
        self.load_UI()

    def load_UI(self):
        self.list_groupbox_for_users = []
        self.list_users_login = []
        uic.loadUi(UI_user, self)
        self.users = session.query(Users).filter(Users.role_id > 2).all()
        for user in self.users:
            self.groupbox_in_users = GroupBoxForUser()
            if not len(self.users) == len(self.list_groupbox_for_users):
                self.list_groupbox_for_users.append(self.groupbox_in_users)
                self.list_users_login.append(user.login)
            self.groupbox_in_users.username_label.setText(user.login)
            if user.role_id == 3:
                self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("image/user/user_admin.png"))
                self.groupbox_in_users.admin_pushButton.setStyleSheet(" background-color: #00ff00;")
            elif user.role_id == 4:
                self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("image/user/user_control.png"))
                self.groupbox_in_users.pitman_pushButton.setStyleSheet(" background-color: #00ff00;")
            self.layout_user_groupbox.addWidget(self.groupbox_in_users)
        self.add_user_pushButton.clicked.connect(self.show_add_user)
        self.delete_user_pushButton.clicked.connect(self.delete_user)

    def show_add_user(self):
        uic.loadUi("view/ifc/add user.ui", self)
        self.add.clicked.connect(self.add_to_database_on_clicked)

    def add_to_database_on_clicked(self):
        if self.law.currentText() == "Администратор":
            value = 3
        else:
            value = 4
        session.add_all([Users(login=f"{self.username.text()}", password=f"{self.password.text()}", manufacture_id=1,
                               role_id=f"{value}")])
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
