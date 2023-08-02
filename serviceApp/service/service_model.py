from datetime import datetime
from PyQt6.QtCore import QObject
from connection_to_db import session, engine, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class ServiceModel(QObject):
    def __init__(self):
        super().__init__()

    def check_first_load(self, model_object):
        object_database = session.get(model_object, 1)
        if object_database is None:
            session.add(model_object(manufacture_id=1))
            session.commit()
            object_database = session.get(model_object, 1)
        return object_database


class Manufacture(Base):
    __tablename__ = "manufacture"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    discription = Column(String)
    count_shield = Column(Integer)
    setting_networks = relationship("SettingNetwork", back_populates="manufacture")
    network_interface = relationship("NetworkInterface", back_populates="manufacture")
    users = relationship("Users", back_populates="manufacture")
    creps = relationship("Crep_ifc", back_populates="manufacture")

    def update_manufacture(self, count_shield):
        self.count_shield = count_shield
        session.commit()



class SettingNetwork(Base):
    __tablename__ = "setting_network"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    host_name = Column(String)
    domain_name = Column(String)
    primary_name_server = Column(String)
    secondary_name_server = Column(String)
    default_gateway = Column(String)
    manufacture_id = Column(Integer, ForeignKey("manufacture.id"))
    manufacture = relationship("Manufacture", back_populates="setting_networks")

    def update_setting_network(self, host_name, domain_name, primary_name_server, secondary_name_server,
                               default_gateway):
        self.host_name = host_name
        self.domain_name = domain_name
        self.primary_name_server = primary_name_server
        self.secondary_name_server = secondary_name_server
        self.default_gateway = default_gateway
        session.commit()


class NetworkInterface(Base):
    __tablename__ = "network_interface"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    device = Column(String)
    addressing = Column(String)
    ip_address = Column(String)
    subnet_mask = Column(String)
    manufacture_id = Column(Integer, ForeignKey("manufacture.id"))
    manufacture = relationship("Manufacture", back_populates="network_interface")

    def update_network_interface(self, device, addressing, ip_address, subnet_mask):
        self.device = device
        self.addressing = addressing
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
        session.commit()


Base.metadata.create_all(bind=engine)
