import subprocess

from PyQt6 import QtWidgets, uic

import serviceApp.ping.pingModel as ping
from connection_to_db import session
from serviceApp.ping.pingModel import PingTable

UI_ping = "resources/view/service/ping_requst_view.ui"


class Ping(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()

        uic.loadUi(UI_ping, self)
        self.ping_table = session.get(ping.PingTable, 1)
        if not self.ping_table:
            session.add(PingTable(ping="127.0.0.1"))
            session.commit()
            self.ping_table = session.get(ping.PingTable, 1)
        self.ip_lineEdit.setText(self.ping_table.ping)
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

        self.ping_table.update_pingTable(self.ip_lineEdit.text())
        session.commit()
        session.refresh(self.ping_table)
