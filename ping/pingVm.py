import subprocess
from ping.pingModel import session
from ping.pingModel import PingTable
from PyQt6 import QtWidgets, uic
import ping.pingModel as ping

UI_ping = "view/service/ping_requst_view.ui"





class Ping(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()

        uic.loadUi(UI_ping, self)
        self.ping_table = session.get(ping.PingTable, 1)
        self.check_pushButton.clicked.connect(self.ping_test)
        self.pings = session.query(ping.PingTable).all()
        if self.pings == []:
            session.add(PingTable(ping="127.0.0.1"))
            session.commit()
        self.ip_lineEdit.setText(self.ping_table.ping)
        self.ping_table.update_pingTable(self.ip_lineEdit.text())

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
