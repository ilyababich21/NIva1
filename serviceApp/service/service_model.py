from datetime import datetime

from connection_to_db import session, engine, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Manufacture(Base):
    __tablename__ = "manufacture"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    discription = Column(String)
    setting_networks = relationship("SettingNetwork", back_populates="manufacture")
    network_interface = relationship("NetworkInterface", back_populates="manufacture")
    users = relationship("Users", back_populates="manufacture")
    creps = relationship("Crep_ifc", back_populates="manufacture")




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

from ifcApp.crep.crep_model import Crep_ifc

# class Crep_ifc(Base):
#     __tablename__ = "creps"
#     id = Column(Integer,primary_key=True, index=True)
#     num = Column(Integer)
#     sensors=relationship("Sensors_ifc", back_populates="crep")
#     manufacture_id=Column(Integer,ForeignKey(Manufacture.id))
#     manufacture=relationship("Manufacture", back_populates="creps")
#
#
#
# class Sensors_ifc(Base):
#     __tablename__ = "sensors"
#     id =Column(Integer,primary_key=True, index=True)
#     id_dat = Column(Integer)
#     value = Column(String)
#     create_date = Column(DateTime,default=datetime.now())
#     crep_id = Column(Integer,ForeignKey("creps.id"))
#     crep = relationship("Creps", back_populates="sensors")


Base.metadata.create_all(bind=engine)


