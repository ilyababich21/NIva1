import sys
from PyQt6.QtWidgets import QApplication
from authorization.authorization_vm import Authorization
from ifcApp.ifc.ifc_vm import IfcViewModel


def main():
    app = QApplication(sys.argv)
    window = IfcViewModel()
    window.showMaximized()
    app.exec()


def main2():
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    app.exec()


if __name__ == '__main__':
    main2()
