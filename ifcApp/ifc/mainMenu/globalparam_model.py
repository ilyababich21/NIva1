from sqlalchemy import Column, Integer

from serviceApp.service.service_model import engine, Base
from serviceApp.service.service_model import session



class GlobalParamTable(Base):
    __tablename__ = "global_param"

    id = Column(Integer, primary_key=True, index=True)
    min_value = Column(Integer)
    max_value = Column(Integer)
    normal_value = Column(Integer)

    def update_globalParamTable(self, min_value, max_value, normal_value):
        self.min_value = min_value
        self.max_value = max_value
        self.normal_value = normal_value
        session.commit()


Base.metadata.create_all(bind=engine)
