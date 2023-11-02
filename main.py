import sys
import time

from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QSplashScreen

from authorization.authorization_vm import Authorization
from database import NivaStorage
from ifcApp.ifc.ifc_vm import IfcViewModel


def main():
    app = QApplication(sys.argv)
    window = IfcViewModel()
    window.showMaximized()
    app.exec()


def main2():
    # import logging
    # FORMAT = ('%(asctime)-15s %(threadName)-15s'
    #           ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    # logging.basicConfig(format=FORMAT)
    # log = logging.getLogger()
    # log.setLevel(logging.DEBUG)
    # CheckDB()
    database = NivaStorage()
    app = QApplication(sys.argv)
    start=time.time()
    splash = QSplashScreen(QPixmap("resources/image/logotip-niva-pochti-bez-fona.png"))
    splash.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    splash.show()
    while time.time() - start < 1:
        time.sleep(0.001)
        app.processEvents()
    window = Authorization(database)
    splash.finish(window)
    window.show()
    app.exec()


if __name__ == '__main__':
    main2()
