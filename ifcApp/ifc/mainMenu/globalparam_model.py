from sqlalchemy import Column, Integer, String

from serviceApp.service.service_model import engine, Base
from serviceApp.service.service_model import session


class GlobalParamTable(Base):
    __tablename__ = "global_param"

    id = Column(Integer, primary_key=True, index=True)
    min_value = Column(Integer)
    max_value = Column(Integer)
    from_normal_value = Column(Integer)
    to_normal_value = Column(Integer)
    units = Column(String)

    def update_globalParamTable(self, ListParam):
        self.min_value,self.max_value,self.from_normal_value,self.to_normal_value,self.units =ListParam
        session.commit()


Base.metadata.create_all(bind=engine)
