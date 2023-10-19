import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, relationship
import datetime

engine = create_engine("postgresql://postgres:root@localhost/niva1")
db_session = sqlalchemy.orm.sessionmaker(bind=engine)
session = db_session()


class Base(DeclarativeBase): pass


class Manufacture(Base):
    __tablename__ = "manufacture"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    discription = Column(String)
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


class Crep_ifc(Base):
    __tablename__ = "creps"
    id = Column(Integer, primary_key=True, index=True)
    num = Column(Integer)
    sensors = relationship("Sensors_ifc", back_populates="crep")
    manufacture_id = Column(Integer, ForeignKey(Manufacture.id))
    manufacture = relationship("Manufacture", back_populates="creps")


class Sensors_ifc(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    id_dat = Column(Integer)
    value = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.now())
    crep_id = Column(Integer, ForeignKey("creps.id"))
    crep = relationship("Crep_ifc", back_populates="sensors")


class Users(Base):
    __tablename__ = "credential"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String)
    password = Column(String)
    manufacture_id = Column(Integer, ForeignKey(Manufacture.id))
    manufacture = relationship("Manufacture", back_populates="users")
    role_id = Column(Integer, ForeignKey("role.id"))
    role = relationship("Role_ifc", back_populates="users")


class Role_ifc(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    description = Column(String)

    users = relationship("Users", back_populates="role")


Base.metadata.create_all(bind=engine)

if not session.query(Manufacture).count():
    session.add(Manufacture(name='niva', discription='null'))
    session.commit()

if not session.query(SettingNetwork).count():
    session.add(SettingNetwork(host_name="124", domain_name="453", manufacture_id=1))
    session.commit()
if not session.query(Crep_ifc).count():
    for elem in range(1, 301):
        microsoft = Crep_ifc(num=elem, manufacture_id=1)

        session.add(microsoft)
        session.commit()
