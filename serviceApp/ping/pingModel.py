from sqlalchemy import Column, Integer, String

from connection_to_db import Base
from serviceApp.service.service_model import engine


class PingTable(Base):
    __tablename__ = "ping"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ping = Column(String)

    def update_pingTable(self, ping):
        self.ping = ping


Base.metadata.create_all(bind=engine)
