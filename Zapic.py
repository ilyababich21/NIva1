import datetime

from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import Session, DeclarativeBase, relationship


from serviceApp.service.service_model import Manufacture


class Base(DeclarativeBase): pass




engine = create_engine("postgresql://postgres:root@localhost/niva1")

class Crep_ifc(Base):
    __tablename__ = "creps"
    id = Column(Integer,primary_key=True, index=True)
    num = Column(Integer)
    sensors=relationship("Sensors_ifc", back_populates="crep")
    manufacture_id=Column(Integer,ForeignKey(Manufacture.id))
    manufacture=relationship(Manufacture, back_populates="creps")


class Sensors_ifc(Base):
    __tablename__ = "sensors"
    id =Column(Integer,primary_key=True, index=True)
    id_dat = Column(Integer)
    value = Column(String)
    # created_date = Column(String)
    create_date = Column(DateTime,default=datetime.datetime.now())
    crep_id = Column(Integer,ForeignKey("creps.id"))
    crep = relationship("Crep_ifc", back_populates="sensors")

Base.metadata.create_all(bind=engine)
with Session(autoflush=False, bind=engine) as db:
    # создаем компании
    # manuf = Manufacture(name="Pizda", discription="Da poshlo ono vse v pizdu")
    # db.add(manuf)
    # db.commit()
    for elem in range(1,301):

        microsoft = Crep_ifc(num = elem,manufacture_id=1)

        db.add(microsoft)
        db.commit()