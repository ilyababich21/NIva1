

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QMainWindow

from ifcApp.ifc.users.groupbox_for_users import GroupBoxForUser

UI_user = "resources/view/ifc/user/user.ui"


class UserInIfc(QMainWindow):
    def __init__(self,database):
        super().__init__()
        self.database = database
        self.query_role = self.database.roles_in_ifc()
        self.groupbox_in_users = None
        self.list_users_login = None
        self.list_groupbox_for_users = None
        self.load_UI()

    def load_UI(self):
        self.list_groupbox_for_users = []
        self.list_users_login = []
        uic.loadUi(UI_user, self)
        self.users = self.database.users_in_ifc()
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
        for item in self.query_role:
            self.law.addItem(item.description)
        self.add.clicked.connect(self.add_to_database)

    def add_to_database(self):
        for item in self.query_role:
            if self.law.currentText() == item.description:
                print(item.id)
                self.database.add_user(username=self.username.text(),password= self.password.text(),role_id= item.id)

            self.load_UI()

    def delete_user(self):
        try:
            for action in range(len(self.list_groupbox_for_users)):
                if self.list_groupbox_for_users[action].radioButton.isChecked():
                    self.database.remove_user(self.list_users_login[action])
                    self.load_UI()
        except:
            print("you delete two users")

    # def change_user(self):
    #     uic.loadUi("view/ifc/add user.ui", self)
    #     self.label.setText("Изменение пользователя")
    #     for elem in range(len(self.list_groupbox_for_users)):
    #         self.username.setText(f"{self.list_users_login[elem]}")
