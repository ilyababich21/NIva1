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

    def update_globalParamTable(self, min_value, max_value, from_normal_value, to_normal_value, units):
        self.min_value = min_value
        self.max_value = max_value
        self.from_normal_value = from_normal_value
        self.to_normal_value = to_normal_value
        self.units = units

        session.commit()


Base.metadata.create_all(bind=engine)
