from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session



def connection_database():
    engine = create_engine("postgresql://postgres:root@localhost/niva1", echo=True)

    return engine


class Base(DeclarativeBase): pass


class PingTabel(Base):
    __tablename__ = "ping"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ping = Column(String)


def work_pingTable():
    with Session(autoflush=False, bind=connection_database()) as db:
        pingRow = PingTabel(ping="127.0.0.1")
        db.add(pingRow)
        db.commit()
        print(pingRow.id)

#
Base.metadata.create_all(bind=connection_database())


