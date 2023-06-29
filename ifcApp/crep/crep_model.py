# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.orm import relationship
# from serviceApp.service.service_model import engine
#
# class Base(DeclarativeBase): pass
import datetime

import sqlalchemy

from serviceApp.service.service_model import Manufacture, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, DeclarativeBase

engine = create_engine("postgresql://postgres:root@localhost/niva1")
db_session = sqlalchemy.orm.sessionmaker(bind=engine)
session = db_session()




class Creps(Base):
    __tablename__ = "creps"
    id = Column(Integer,primary_key=True, index=True)
    num = Column(Integer)
    sensors=relationship("Sensors_ifc", back_populates="crep")
    manufacture_id=Column(Integer,ForeignKey("manufacture.id"))
    manufacture=relationship(Manufacture, back_populates="creps")



class Sensors_ifc(Base):
    __tablename__ = "sensors"
    id =Column(Integer,primary_key=True, index=True)
    id_dat = Column(Integer)
    value = Column(String)
    # created_date = Column(String)
    create_date = Column(DateTime,default=datetime.datetime.now())
    crep_id = Column(Integer,ForeignKey("creps.id"))
    crep = relationship("Creps", back_populates="sensors")





Base.metadata.create_all(bind=engine)
# if not session.query(Creps).count():
#     for elem in range(1, 301):
#         microsoft = Creps(num=elem, manufacture_id=1)
#
#         session.add(microsoft)
#         session.commit()

# with Session(autoflush=False, bind=engine) as db:
#     # создаем компании
#     # manuf = Manufacture(name="Pizda", discription="Da poshlo ono vse v pizdu")
#     # db.add(manuf)
#     # db.commit()
#     for elem in range(1,301):
#
#         microsoft = Crep_ifc(num = elem,manufacture_id=1)
#
#         db.add(microsoft)
#         db.commit()