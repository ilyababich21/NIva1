import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("postgresql://postgres:root@localhost/niva1")
db_session = sqlalchemy.orm.sessionmaker(bind=engine)
session = db_session()


class Base(DeclarativeBase): pass
