# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import relationship
# from serviceApp.service.service_model import engine
#
# class Base(DeclarativeBase): pass

from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from serviceApp.service.service_model import engine


class Base(DeclarativeBase): pass



class Crep_ifc(Base):
    __tablename__ = "creps"
    id = Column(Integer,primary_key=True, index=True)
    num = Column(Integer)
    sensors=relationship("Sensors_ifc", back_populates="crep")




class Sensors_ifc(Base):
    __tablename__ = "sensors"
    id =Column(Integer,primary_key=True, index=True)
    id_dat = Column(Integer)
    value = Column(String)
    crep_id = Column(Integer,ForeignKey("creps.id"))
    crep = relationship("Crep_ifc", back_populates="sensors")




Base.metadata.create_all(bind=engine)
