import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, relationship


engine = create_engine("postgresql://postgres:root@localhost/niva1")
db_session = sqlalchemy.orm.sessionmaker(bind=engine)
session = db_session()


class Base(DeclarativeBase): pass


class SettingNetwork(Base):
    __tablename__ = "setting_network"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    host_name = Column(String)
    domain_name = Column(String)
    primary_name_server = Column(String)
    secondary_name_server = Column(String)
    default_gateway = Column(String)
    manufacture_id = Column(Integer, ForeignKey("manufacture.id"))
    manufacture = relationship("Manufacture", back_populates="setting_network")

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

