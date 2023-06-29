import sys

import sqlalchemy
from PyQt6 import QtWidgets
from sqlalchemy import create_engine

# import DBcreator
from PyQt6.QtWidgets import QApplication
from authorization.authorization_vm import Authorization
from ifcApp.crep.crep_model import Creps
from ifcApp.ifc.ifc_vm import IfcViewModel
from serviceApp.service.service_model import Manufacture, SettingNetwork


def main():
    app = QApplication(sys.argv)
    window = IfcViewModel()
    window.showMaximized()
    app.exec()


def main2():

    CheckDB()
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    app.exec()




def CheckDB():
    from serviceApp.service.service_model import Manufacture, SettingNetwork
    from ifcApp.crep.crep_model import Creps
    engine = create_engine("postgresql://postgres:root@localhost/niva1")
    db_session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = db_session()
    if not session.query(Manufacture).count():
        session.add(Manufacture(name='niva',discription='null'))
        session.commit()

    if not session.query(SettingNetwork).count():
        session.add(SettingNetwork( host_name="124", domain_name="453", manufacture_id=1))
        session.commit()

    if not session.query(Creps).count():
        for elem in range(1, 301):
            microsoft = Creps(num=elem, manufacture_id=1)

            session.add(microsoft)
            session.commit()






if __name__ == '__main__':
    main2()
