import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from connection_to_db import engine, Base
from serviceApp.service.service_model import Manufacture


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


Base.metadata.create_all(bind=engine)
