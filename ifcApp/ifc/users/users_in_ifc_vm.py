from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QMainWindow

from authorization.authorization_model import Users
from ifcApp.ifc.users.groupbox_for_users import GroupBoxForUser
from serviceApp.service.service_model import session

UI_user = "view/ifc/user.ui"


class UserInIfc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.list_groupbox_radiobutton = []
        self.list_users_login = []

        self.load_UI()

    def load_UI(self):
        uic.loadUi(UI_user, self)
        self.users = session.query(Users).all()
        for user in self.users:
            self.groupbox_in_users = GroupBoxForUser()
            if not len(self.users) == len(self.list_groupbox_radiobutton):
                self.list_groupbox_radiobutton.append(self.groupbox_in_users.radioButton)
                self.list_users_login.append(user.login)
            self.groupbox_in_users.username_label.setText(user.login)
            if user.role_id == 3:
                self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("image/user/user_admin.png"))
            elif user.role_id == 4:
                self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("image/user/user_control.png"))
            self.layout_user_groupbox.addWidget(self.groupbox_in_users)
        self.add_user_pushButton.clicked.connect(self.show_add_user)
        self.delete_user_pushButton.clicked.connect(self.delete_user)

    def show_add_user(self):
        uic.loadUi("view/ifc/add user.ui", self)
        self.add.clicked.connect(self.add_to_database_on_clicked)

    def add_to_database_on_clicked(self):
        session.add_all([Users(login=f"{self.username.text()}", password=f"{self.password.text()}", manufacture_id=1,
                               role_id=f"{int(self.law.text())}")])
        session.commit()

        self.load_UI()
        print(self.list_groupbox_radiobutton)

    def delete_user(self):
        print(f"leng{self.list_groupbox_radiobutton}")
        for action in range(len(self.list_groupbox_radiobutton)):
            if self.list_groupbox_radiobutton[action].isChecked():
                delete_query = session.query(Users).filter(Users.login == self.list_users_login[action]).first()
                session.delete(delete_query)
                session.commit()
                self.load_UI()
