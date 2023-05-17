from PyQt6.QtWidgets import QGroupBox, QLabel, QHBoxLayout, QGridLayout


class GroupBoxWidget(QGroupBox):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(0, 65)
        self.setMaximumSize(2000, 85)

        self.gridLayout = QGridLayout(self)

        self.setStyleSheet("QGroupBox{\n"
                           "                        background-color: #fff;\n"
                           "                        }")
        self.name_label = QLabel(self)
        self.name_label.setMinimumSize(150,15)
        self.name_label.setMaximumSize(150, 40)
        self.gridLayout.addWidget(self.name_label, 0, 2)

        self.min_value = QLabel(self)
        self.min_value.setMaximumSize(20, 20)
        self.gridLayout.addWidget(self.min_value, 3, 0)

        self.icon_label = QLabel(self)
        self.icon_label.setMaximumSize(21, 31)
        self.icon_label.setMinimumSize(21, 31)
        self.gridLayout.addWidget(self.icon_label, 1, 3)

        self.max_value = QLabel(self)
        self.max_value.setMinimumSize(15,15)
        self.max_value.setMaximumSize(20, 20)
        self.gridLayout.addWidget(self.max_value, 0, 0)

        self.layoutWidget = QHBoxLayout(self)
        self.layoutWidget.setSpacing(0)
        self.gridLayout.addLayout(self.layoutWidget, 0, 1, 4, 2)



