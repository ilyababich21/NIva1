from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGroupBox, QLabel, QHBoxLayout, QGridLayout
from PyQt6.uic.uiparser import QtGui


class GroupBoxWidget(QGroupBox):
    list_icon = ["conveyor_distance.png", "conveyor_clearance.png",
                 "prop_pressure_1.png", "prop_pressure_2.png",
                 "articulated_cantilever_pos.png", "articulated_cantilever_pos.png",
                 "articulated_cantilever_switch.png", "articulated_cantilever_way.png",
                 "articulated_cantilever_pressure.png", "articulated_cantilever3.png",
                 "cantilever.png", "articulated_cantilever_way.png", "slidebar_pos.png",
                 "cantilever_state.png", "shield_height_1.png"]
    icon_paths = [f"resources/image/img tools/{i}" for i in list_icon]
    list_name_for_groupbox = ["ЦП", "Зазор цлиндра передвижки", "Давление в стойке левая",
                              "Давление в стойке правая", "Щит УГЗ", "Щит Угз Угол",
                              "Щит УГЗ ход", "Щит угз давление",
                              "9", "10", "11", "12", "13", "14", "15"]

    def __init__(self):
        super().__init__()

        self.setMinimumSize(0, 65)
        self.setMaximumSize(2000, 85)

        self.gridLayout = QGridLayout(self)

        self.setStyleSheet("QGroupBox{\n"
                           "                        background-color: #fff;\n"
                           "                        }")
        self.name_label = QLabel(self)

        font = QFont()
        font.setPointSize(9)
        font.setBold(1)
        self.name_label.setFont(font)
        self.name_label.setMinimumSize(200, 15)
        self.name_label.setMaximumSize(150, 40)
        self.gridLayout.addWidget(self.name_label, 0, 2)

        self.min_value = QLabel(self)
        self.min_value.setMinimumSize(40, 15)
        self.min_value.setMaximumSize(20, 20)
        self.gridLayout.addWidget(self.min_value, 3, 0)

        self.icon_label = QLabel(self)
        self.icon_label.setMaximumSize(21, 31)
        self.icon_label.setMinimumSize(21, 31)
        self.gridLayout.addWidget(self.icon_label, 1, 3)

        self.max_value = QLabel(self)
        self.max_value.setMinimumSize(40, 15)
        self.max_value.setMaximumSize(20, 20)
        self.gridLayout.addWidget(self.max_value, 0, 0)

        self.layoutWidget = QHBoxLayout(self)
        self.layoutWidget.setSpacing(0)
        self.gridLayout.addLayout(self.layoutWidget, 0, 1, 4, 2)
