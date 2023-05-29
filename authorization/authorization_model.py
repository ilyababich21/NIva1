from serviceApp.service.service_model import engine, Base
from serviceApp.service.service_model import session
from sqlalchemy import Column, Integer, String


class Users(Base):
    __tablename__ = "credential"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String)
    password = Column(String)
    role = Column(String)


Base.metadata.create_all(bind=engine)
