from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QColorDialog


class SettingsSensorsWidget(QWidget):
    def __init__(self, name):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.name_label = QLabel(self)
        self.name_label.setText(
            f"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">{name}</span></p></body></html>")

        self.color_increased_pushButton = QPushButton(self)
        self.color_increased_pushButton.setMaximumSize(30, 25)
        self.color_increased_pushButton.setToolTip("Повышенное давление")

        self.color_normal_pushButton = QPushButton(self)
        self.color_normal_pushButton.setMaximumSize(30, 25)
        self.color_normal_pushButton.setToolTip("Нормальное давление")

        self.color_reduced_pushButton = QPushButton(self)
        self.color_reduced_pushButton.setMaximumSize(30, 25)
        self.color_reduced_pushButton.setToolTip("Пониженное давление")




        self.min_size_lineEdit = QLineEdit(self)
        self.min_size_lineEdit.setMaximumSize(100, 25)
        self.max_size_lineEdit = QLineEdit(self)
        self.max_size_lineEdit.setMaximumSize(100, 25)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.color_increased_pushButton)
        self.layout.addWidget(self.color_reduced_pushButton)
        self.layout.addWidget(self.color_normal_pushButton)
        self.layout.addWidget(self.min_size_lineEdit)
        self.layout.addWidget(self.max_size_lineEdit)
