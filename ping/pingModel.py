import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session


class Base(DeclarativeBase): pass


class PingTable(Base):
    __tablename__ = "ping"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ping = Column(String)

    def update_pingTable(self, ping):
        self.ping = ping


engine = create_engine("postgresql://postgres:root@localhost/niva1")
Base.metadata.create_all(bind=engine)
DBsession = sqlalchemy.orm.sessionmaker(bind=engine)
session = DBsession()

# def work_pingTable():
#     with Session(autoflush=False, bind=engine) as db:
#         pingRow = PingTable(ping="127.0.0.1")
#         db.add(pingRow)
#         db.commit()
#         print(pingRow.id)

#
