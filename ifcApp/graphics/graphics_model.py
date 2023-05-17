from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from serviceApp.service.service_model import engine


class Base(DeclarativeBase): pass


class Graphics(Base):
    __tablename__ = "graphics"

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(String)
    sensors = Column(Integer)


Base.metadata.create_all(bind=engine)