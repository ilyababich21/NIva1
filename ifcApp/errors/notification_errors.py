from PyQt6 import uic, QtWidgets


UI_errors = "resources/view/ifc/notification errors.ui"


class NotificationErrors(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_errors, self)
        self.clear_pushButton.clicked.connect(lambda:self.textEdit.clear())
