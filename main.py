import sys

import sqlalchemy
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from sqlalchemy import create_engine


from PyQt6.QtWidgets import QApplication, QSplashScreen
from authorization.authorization_vm import Authorization
from ifcApp.crep.crep_model import Crep_ifc
from ifcApp.crep.crep_vm import CrepViewModel
from ifcApp.ifc.ifc_vm import IfcViewModel
from serviceApp.service.service_model import Manufacture, SettingNetwork


def main():
    app = QApplication(sys.argv)
    window = CrepViewModel()
    window.showMaximized()
    app.exec()


def main2():
    # import logging
    # FORMAT = ('%(asctime)-15s %(threadName)-15s'
    #           ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    # logging.basicConfig(format=FORMAT)
    # log = logging.getLogger()
    # log.setLevel(logging.DEBUG)
    CheckDB()
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap("resources/image/logotip-niva-pochti-bez-fona.png"))
    splash.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    splash.show()
    window = Authorization()
    splash.finish(window)
    window.show()
    app.exec()

def CheckDB():
    from serviceApp.service.service_model import Manufacture, SettingNetwork
    from ifcApp.crep.crep_model import Crep_ifc
    engine = create_engine("postgresql://postgres:root@localhost/niva1")
    db_session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = db_session()
    if not session.query(Manufacture).count():
        session.add(Manufacture(name='niva', discription='null',count_shield = 20))
        session.commit()


    if not session.query(SettingNetwork).count():
        session.add(SettingNetwork(host_name="124", domain_name="453", manufacture_id=1))
        session.commit()

    if not session.query(Crep_ifc).count():
        for elem in range(1, 301):
            number = Crep_ifc(num=elem, manufacture_id=1)

            session.add(number)
            session.commit()


if __name__ == '__main__':
    main2()
