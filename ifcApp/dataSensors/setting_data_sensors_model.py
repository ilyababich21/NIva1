from sqlalchemy import Column, Integer, String

from connection_to_db import Base
from serviceApp.service.service_model import engine




class SettingsSensorsTable(Base):
    __tablename__ = "settings_sensors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    color_button_one = Column(String)
    color_button_two = Column(String)
    color_button_three = Column(String)
    color_button_four = Column(String)
    min_value = Column(Integer)
    max_value = Column(Integer)
    coefficient_value = Column(Integer)

    def update_settingsSensorsTable(self, color_button_one,
                                    color_button_two,
                                    color_button_three,
                                    color_button_four,
                                    min_value, max_value,
                                    coefficient_value, ):
        self.color_button_one = color_button_one
        self.color_button_two = color_button_two
        self.color_button_three = color_button_three
        self.color_button_four = color_button_four
        self.min_value = min_value
        self.max_value = max_value
        self.coefficient_value = coefficient_value


Base.metadata.create_all(bind=engine)
