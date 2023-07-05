from sqlalchemy.orm import Session

from connection_to_db import engine
from ifcApp.crep.crep_model import Crep_ifc

with Session(autoflush=False, bind=engine) as db:
    # создаем компании
    # manuf = Manufacture(name="Pizda", discription="Da poshlo ono vse v pizdu")
    # db.add(manuf)
    # db.commit()
    for elem in range(1, 301):
        microsoft = Crep_ifc(num=elem, manufacture_id=1)

        db.add(microsoft)
        db.commit()
