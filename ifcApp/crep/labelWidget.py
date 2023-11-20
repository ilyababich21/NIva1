from PyQt6.QtWidgets import QLabel


class LabelWidget(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(140, 20)
