from PyQt6 import uic, QtWidgets
from crep.crep_vm import CrepViewModel

UI_ifc = "view/ifc version1.ui"


class ButtonForSection(QtWidgets.QPushButton):
    def __init__(self, number):
        super().__init__()
        self.id = number


class IfcViewModel(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi(UI_ifc, self)

        self.make_buttons(self.layout_600)
        self.make_buttons(self.layout_200)
        self.make_buttons(self.layout_1000)
        self.make_buttons(self.layout_10000)
        self.make_buttons(self.layout_250)
        self.make_buttons(self.layout_6)

    def make_buttons(self, layout):

        num = self.section_max_lineEdit.text()
        if num == "":
            num = 0
        num = int(num)
        for elem in range(num):
            btn = ButtonForSection(elem + 1)  # !!!
            btn.clicked.connect(lambda ch, b=btn: self.on_clicked(b))
            layout.addWidget(btn)

    def on_clicked(self, btn):
        self.crep = CrepViewModel(btn.id)
        self.crep.show()
