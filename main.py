import sys

from PyQt6 import QtWidgets

from service.service_vm import ServiceViewModel


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ServiceViewModel()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
