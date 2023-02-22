from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


def connection_database():
    engine = create_engine("postgresql://postgres:root@localhost/niva1")

    return engine


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


class NetworkInterface(Base):
    __tablename__ = "network_interface"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    device = Column(String)
    addressing = Column(String)
    ip_address = Column(String)
    subnet_mask = Column(String)


def work_users():
    Base.metadata.create_all(bind=connection_database())
    with Session(autoflush=False, bind=connection_database()) as db:
        users = db.query(Users).all()
        if not users:
            service = Users(login="service", password="1111")
            ifc = Users(login="IFC", password="ifc")
            db.add_all([service, ifc])
            db.commit()
            users = db.query(Users).all()

    return users


def work_setting_network():
    Base.metadata.create_all(bind=connection_database())
    with Session(autoflush=False, bind=connection_database()) as db:
        setting_network = db.get(SettingNetwork, 1)
    if setting_network is None:
        line = SettingNetwork()
        db.add(line)
        db.commit()
        setting_network = db.get(SettingNetwork, 1)

    return setting_network


def work_network_interface():
    Base.metadata.create_all(bind=connection_database())
    with Session(autoflush=False, bind=connection_database()) as db:
        network_interface = db.get(NetworkInterface, 1)
    if network_interface is None:
        line = NetworkInterface()
        db.add(line)
        db.commit()
        network_interface = db.get(NetworkInterface, 1)

    return network_interface
