from PyQt6 import uic, QtWidgets


UI_errors = "view/ifc/notification errors.ui"


class NotificationErrors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_errors, self)
