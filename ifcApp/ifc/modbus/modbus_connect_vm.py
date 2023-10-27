from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


UI_Modbus = "resources/view/ifc/modbus_connect.ui"





class ModbusConnectViewModel(QMainWindow):
    def __init__(self,database):
        super().__init__()
        uic.loadUi(UI_Modbus, self)
        self.port_lineEdit.setText(str(database.query_modbus().port))
        self.ip_lineEdit.setText(database.query_modbus().ip_address)
