from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String

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
