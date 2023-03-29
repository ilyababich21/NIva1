from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

from serviceApp.service.service_model import engine


class Base(DeclarativeBase): pass


class PingTable(Base):
    __tablename__ = "ping"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ping = Column(String)

    def update_pingTable(self, ping):
        self.ping = ping


Base.metadata.create_all(bind=engine)
