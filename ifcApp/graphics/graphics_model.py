from sqlalchemy import Column, Integer, String

from connection_to_db import Base
from serviceApp.service.service_model import engine


class Graphics(Base):
    __tablename__ = "graphics"

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(String)
    sensors = Column(Integer)


Base.metadata.create_all(bind=engine)
