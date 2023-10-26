from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from connection_to_db import session
from serviceApp.service.service_model import Modbus

UI_Modbus = "resources/view/ifc/modbus_connect.ui"


def query_in_modbus_table():
    query = session.get(Modbus, 1)
    return query


class ModbusConnectViewModel(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_Modbus, self)
        self.port_lineEdit.setText(str(query_in_modbus_table().port))
        self.ip_lineEdit.setText(query_in_modbus_table().ip_address)
