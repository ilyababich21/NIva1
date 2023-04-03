from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from sqlalchemy.orm import DeclarativeBase

from serviceApp.service.service_model import engine


class Base(DeclarativeBase): pass


class modbusTable(Base):
    __tablename__ = "modbus"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    RTU = Column(Boolean)
    TCP = Column(Boolean)
    device = Column(String)
    speed = Column(BigInteger)
    stop_bit = Column(Integer)
    parity = Column(Integer)
    ip_address = Column(String)
    port = Column(String)
    address_device = Column(Integer)
    start_number = Column(Integer)
    number = Column(Integer)

    def update_modbusTable(self, RTU, TCP, device, speed, stop_bit,
                           parity, ip_address, port, address_device,
                           start_number, number):
        self.RTU = RTU
        self.TCP = TCP
        self.device = device
        self.parity = parity
        self.ip_address = ip_address
        self.port = port
        self.address_device = address_device
        self.speed = speed
        self.stop_bit = stop_bit
        self.start_number = start_number
        self.number = number


Base.metadata.create_all(bind=engine)
