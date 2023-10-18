from PyQt6.QtCore import QObject

from connection_to_db import session
from serviceApp.service.service_model import Manufacture



class CountShieldModel(QObject):
    def __init__(self):
        super().__init__()
        self.value = None
        self.count_shield = None

    def get_count_shield(self):
        self.count_shield = session.query(Manufacture).first()
        self.value = self.count_shield.count_shield
        return self.value
