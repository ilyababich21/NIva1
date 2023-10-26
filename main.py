import sys
import time

import sqlalchemy
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QSplashScreen
from sqlalchemy import create_engine

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


# def CheckDB():
#     from serviceApp.service.service_model import Manufacture
#     from ifcApp.crep.crep_model import Crep_ifc
#     engine = create_engine("postgresql://postgres:root@localhost/niva1")
#     db_session = sqlalchemy.orm.sessionmaker(bind=engine)
#     session = db_session()
#     if not session.query(Manufacture).count():
#         session.add(Manufacture(name='niva', discription='null', count_shield=20))
#         session.commit()
#
#     if not session.query(Modbus).count():
#         session.add(Modbus(ip_address="192.168.1.1", port=502, slave_id=1, start_register=1, count_register=15))
#         session.commit()
#
#     if not session.query(Crep_ifc).count():
#         for elem in range(1, 301):
#             number = Crep_ifc(num=elem, manufacture_id=1)
#
#             session.add(number)
#             session.commit()


if __name__ == '__main__':
    main2()
