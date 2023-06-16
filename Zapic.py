from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from ifcApp.crep.crep_model import Crep_ifc

engine = create_engine("postgresql://postgres:root@localhost/niva1")


with Session(autoflush=False, bind=engine) as db:
    # создаем компании
    # manuf = Manufacture(name="Pizda", discription="Da poshlo ono vse v pizdu")
    # db.add(manuf)
    # db.commit()
    for elem in range(1,301):

        microsoft = Crep_ifc(num = elem,manufacture_id=1)

        db.add(microsoft)
        db.commit()