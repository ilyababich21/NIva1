from PyQt6 import QtCore
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGroupBox, QGridLayout, QPushButton, QLabel, QRadioButton

from address import resource_path


class GroupBoxForUser(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QGroupBox{\n"
                           "background-color:#fff; \n"
                           "}")
        self.setMinimumSize(0, 118)
        self.setMaximumSize(300, 118)

        self.gridLayout = QGridLayout(self)
        self.change_pushButton = QPushButton(self)
        self.change_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.change_pushButton.setIcon(QIcon(resource_path("resources\\image\\img tools\\addtext.png")))
        self.gridLayout.addWidget(self.change_pushButton, 3, 2)

        self.admin_pushButton = QPushButton(self)
        self.admin_pushButton.setIcon(QIcon(resource_path("resources\\image\\img tools\\perm_admin.png")))
        self.admin_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.gridLayout.addWidget(self.admin_pushButton, 3, 4)

        self.pitman_pushButton = QPushButton(self)
        self.pitman_pushButton.setIcon(QIcon(resource_path("resources\\image\\img tools\\parameter.png")))
        self.pitman_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.gridLayout.addWidget(self.pitman_pushButton, 3, 3)

        self.username_label = QLabel(self)
        self.gridLayout.addWidget(self.username_label, 0, 3)

        self.pixmap = QLabel(self)
        self.pixmap.setMaximumSize(QtCore.QSize(51, 61))
        self.pixmap.setTextFormat(QtCore.Qt.TextFormat.PlainText)

        self.gridLayout.addWidget(self.pixmap, 1, 1)
        self.radioButton = QRadioButton(self)
        self.radioButton.setMaximumSize(QtCore.QSize(16, 16))
        self.gridLayout.addWidget(self.radioButton, 1, 0)
