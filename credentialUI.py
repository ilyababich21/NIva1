# Form implementation generated from reading ui file 'credential.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CredentialUI(object):
    def credentialUI(self, CredentialUI):
        CredentialUI.setObjectName("CredentialUI")
        CredentialUI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CredentialUI)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fff;")
        self.log_in = QtWidgets.QPushButton(self.centralwidget)
        self.log_in.setGeometry(QtCore.QRect(370, 360, 171, 51))
        self.log_in.setObjectName("log_in")
        self.log_in.setStyleSheet(
            "background-color: #0d6efd; color: #fff;font-weight: 600;border-radius: 8px;border: 1px solid #0d6efd;padding: 5px 15px;margin-top: 10px;outline: 0px;")
        self.jpglabel = QtWidgets.QLabel(self.centralwidget)
        self.jpglabel.setGeometry(QtCore.QRect(220, 220, 141, 141))
        self.jpglabel.setText("")
        self.jpglabel.setPixmap(QtGui.QPixmap("image/logo-svg.svg"))
        self.jpglabel.setObjectName("jpglabel")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(360, 210, 181, 31))
        self.login_label.setObjectName("login_label")
        self.login_label.setStyleSheet( "color: #0f1925; font-size: 18px; margin-bottom: 10px;")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(360, 270, 191, 31))
        self.password_label.setObjectName("password_label")
        self.password_label.setStyleSheet( "color: #0f1925; font-size: 18px; margin-bottom: 10px;")
        self.login_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_lineEdit.setGeometry(QtCore.QRect(360, 240, 191, 31))
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.login_lineEdit.setStyleSheet("border-radius: 8px; border: 1px solid #e0e4e7; padding: 5px 15px;")
        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(360, 300, 191, 31))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lineEdit.setStyleSheet( "border-radius: 8px; border: 1px solid #e0e4e7; padding: 5px 15px;")
        self.one_user = QtWidgets.QPushButton(self.centralwidget)
        self.one_user.setGeometry(QtCore.QRect(30, 230, 101, 41))
        self.one_user.setText("")
        self.one_user.setStyleSheet(
            "background-color: #0d6efd; color: #fff;font-weight: 600;border-radius: 8px;border: 1px solid #0d6efd;padding: 5px 15px;margin-top: 10px;outline: 0px;")
        self.one_user.setObjectName("one_user")
        self.two_user = QtWidgets.QPushButton(self.centralwidget)
        self.two_user.setGeometry(QtCore.QRect(30, 300, 101, 41))
        self.two_user.setText("")
        self.two_user.setStyleSheet(
            "background-color: #0d6efd; color: #fff;font-weight: 600;border-radius: 8px;border: 1px solid #0d6efd;padding: 5px 15px;margin-top: 10px;outline: 0px;")
        self.two_user.setObjectName("two_user")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 340, 191, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        CredentialUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(CredentialUI)
        QtCore.QMetaObject.connectSlotsByName(CredentialUI)

    def retranslateUi(self, CredentialUI):
        _translate = QtCore.QCoreApplication.translate
        CredentialUI.setWindowTitle(_translate("CredentialUI", "Credential"))
        self.log_in.setText(_translate("CredentialUI", "Авторизироваться"))
        self.login_label.setText(_translate("CredentialUI", "Логин:"))
        self.password_label.setText(_translate("CredentialUI", "Пароль:"))
