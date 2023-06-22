import sys

from PyQt6 import QtWidgets

from authorization.authorization_vm import Authorization
from ifcApp.ifc.ifc_vm import IfcViewModel


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = IfcViewModel()
    window.showMaximized()
    app.exec()


def main2():
    app = QtWidgets.QApplication(sys.argv)
    window = Authorization()
    window.show()
    app.exec()


if __name__ == '__main__':
    main2()
