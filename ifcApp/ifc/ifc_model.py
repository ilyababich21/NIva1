import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship
from serviceApp.service.service_model import engine, SettingNetwork


# class Base(DeclarativeBase): pass
# # class Manufacture(Base):
# #     __tablename__ = "manufacture"
# #     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
# #     name = Column(String)
# #     discription = Column(String)
# #     creps=relationship("Crep_ifc", back_populates="manufacture")
# #     setting_networks=relationship("SettingNetwork", back_populates="manufacture")
# #     network_interface=relationship("NetworkInterface", back_populates="manufacture")
# #
#
#
#
#
#
#
# Base.metadata.create_all(bind=engine)

