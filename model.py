from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
import sqlalchemy




# <<<<<<< HEAD
# =======
# def connection_database():
#
#     engine = create_engine("postgresql://postgres:root@localhost/niva1")
# >>>>>>> 0888870d1909ee1481c401683cc5041a65c2d50d

def connection_database():
    pass


class Base(DeclarativeBase): pass


class Users(Base):
    __tablename__ = "credential"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String)
    password = Column(String)


class SettingNetwork(Base):
    __tablename__ = "setting_network"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    host_name = Column(String)
    domain_name = Column(String)
    primary_name_server = Column(String)
    secondary_name_server = Column(String)
    default_gateway = Column(String)

    def update_setting_network(self, host_name,domain_name,primary_name_server,secondary_name_server,default_gateway):
        self.host_name=host_name
        self.domain_name=domain_name
        self.primary_name_server=primary_name_server
        self.secondary_name_server=secondary_name_server
        self.default_gateway=default_gateway
        session.commit()





class NetworkInterface(Base):
    __tablename__ = "network_interface"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    device = Column(String)
    addressing = Column(String)
    ip_address = Column(String)
    subnet_mask = Column(String)

    def update_network_interface(self,device,addressing,ip_address,subnet_mask):
        self.device=device
        self.addressing=addressing
        self.ip_address=ip_address
        self.subnet_mask=subnet_mask
        session.commit()

engine = create_engine("postgresql://postgres:1111@localhost/niva1")
Base.metadata.create_all(bind=engine)

DBsession = sqlalchemy.orm.sessionmaker(bind=engine)
session = DBsession()

# class ConnectionDb(object):
#     def __init__(self):
#         super().__init__()
#         self.engine = create_engine("postgresql://postgres:1111@localhost/niva1")
#         Base.metadata.create_all(bind=self.engine)
#
#         DBsession = sqlalchemy.orm.sessionmaker(bind=self.engine)
#         self.session = DBsession()




































def work_users():

    with Session(autoflush=False, bind=connection_database()) as db:
        users = db.query(Users).all()
        if users==[]:
            service = Users(login="service", password="1111")
            ifc = Users(login="IFC", password="ifc")
            db.add_all([service, ifc])
            db.commit()
            users = db.query(Users).all()


    return users


def work_setting_network():
    with Session(autoflush=False, bind=connection_database()) as db:
        setting_network = db.get(SettingNetwork, 1)
    if setting_network is None:
        line = SettingNetwork()
        db.add(line)
        db.commit()
        setting_network = db.get(SettingNetwork, 1)

    return setting_network


def work_network_interface():
    with Session(autoflush=False, bind=connection_database()) as db:
        network_interface = db.get(NetworkInterface, 1)
    if network_interface is None:
        line = NetworkInterface()
        db.add(line)
        db.commit()
        network_interface = db.get(NetworkInterface, 1)

    return network_interface


# Base.metadata.create_all(bind=connection_database())
# work_users()