import subprocess

from PyQt6 import QtWidgets, uic

UI_ping = "fileUI/ping.ui"


class Ping(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()

        uic.loadUi(UI_ping, self)
        self.check_pushButton.clicked.connect(self.ping_test)

    def ping_test(self):

        ip = self.ip_lineEdit.text()
        if ip == '':
            self.check_pushButton.setStyleSheet('background-color: rgb(255,0,0);')
            return

        retcode = subprocess.call("ping -n 1 " + str(ip))
        if retcode != 0:
            self.check_pushButton.setStyleSheet('background-color: rgb(255,0,0);')
        else:
            self.check_pushButton.setStyleSheet('background-color: rgb(0,255,0);')
