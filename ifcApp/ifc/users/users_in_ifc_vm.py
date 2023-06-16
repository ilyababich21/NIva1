from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QMainWindow

from authorization.authorization_model import Users
from ifcApp.ifc.users.groupbox_for_users import GroupBoxForUser
from serviceApp.service.service_model import session

UI_user = "view/ifc/user.ui"


class UserInIfc(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_user, self)
        self.users = session.query(Users).all()
        for user in self.users:
            self.groupbox_in_users = GroupBoxForUser()
            self.groupbox_in_users.username_label.setText(user.login)
            if user.role == "service":
                self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("image/user/user_admin.png"))
            else:
                self.groupbox_in_users.pixmap.setPixmap(QtGui.QPixmap("image/user/user_control.png"))

            self.layout_user_groupbox.addWidget(self.groupbox_in_users)
