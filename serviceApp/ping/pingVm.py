import subprocess
from PyQt6 import QtWidgets, uic

from address import resource_path

UI_ping = "resources\\view\\service\\ping_requst_view.ui"


class Ping(QtWidgets.QMainWindow):
    def __init__(self,database):

        super().__init__()
        self.database=database
        uic.loadUi(resource_path(UI_ping), self)
        self.ip_lineEdit.setText(self.database.query_modbus().ip_address)
        self.check_pushButton.clicked.connect(self.ping_test)

    def ping_test(self):
        self.textEdit.clear()
        ip = self.ip_lineEdit.text()
        if ip == '':
            self.check_pushButton.setStyleSheet('background-color: rgb(255,0,0);')
            return
        ping = subprocess.Popen(['ping', str(ip)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        for out in ping.stdout:
            s = out.decode('cp866', 'ignore')
            self.textEdit.append(s)




