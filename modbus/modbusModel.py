from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


def connection_database():
    engine = create_engine("postgresql://postgres:root@localhost/niva1", echo=True)

    return engine


class Base(DeclarativeBase): pass


class modbusTable(Base):
    __tablename__ = "modbus"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    RTU = Column(Boolean)
    TCP = Column(Boolean)
    devive = Column(String)
    speed = Column(BigInteger)
    stop_bit = Column(Integer)
    parity = Column(Integer)
    ip_address = Column(String)
    port = Column(String)
    address_device = Column(Integer)
    start_number = Column(Integer)
    number = Column(Integer)





Base.metadata.create_all(bind=connection_database())
