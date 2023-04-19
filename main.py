import sys

from PyQt6 import QtWidgets

from ifcApp.ifc.ifc_vm import IfcViewModel
from serviceApp.service.service_vm import ServiceViewModel


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = IfcViewModel()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
