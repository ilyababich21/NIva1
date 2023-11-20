import os

from PyQt6 import uic, QtWidgets

from address import resource_path

UI_errors = "resources\\view\\ifc\\toolbar\\notification errors.ui"


class NotificationErrors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(resource_path(UI_errors), self)
        self.clear_pushButton.clicked.connect(lambda:self.textEdit.clear())
