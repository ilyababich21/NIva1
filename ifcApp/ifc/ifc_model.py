import datetime

from PyQt6 import QtGui
from PyQt6.QtCore import QObject, QUrl, Qt, pyqtProperty
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, relationship
from connection_to_db import engine, session
from ifcApp.ifc.mainMenu.globalparam_model import GlobalParamTable
from serviceApp.service.service_model import engine, SettingNetwork


class IfcModel(QObject):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_global_param():
        return session.query(GlobalParamTable).all()

        # self.list_icon = ["conveyor_distance.png", "conveyor_clearance.png",
        #                   "prop_pressure_1.png", "prop_pressure_2.png",
        #                   "articulated_cantilever_pos.png", "articulated_cantilever_pos.png",
        #                   "articulated_cantilever_switch.png", "articulated_cantilever_way.png",
        #                   "articulated_cantilever_pressure.png", "articulated_cantilever3.png",
        #                   "cantilever.png", "articulated_cantilever_way.png", "slidebar_pos.png",
        #                   "cantilever_state.png", "shield_height_1.png"]
        # self.icon_paths = [f"resources/image/img tools/{i}" for i in self.list_icon]
        #
        # self.list_name_for_groupbox = ["ЦП", "Зазор цлиндра передвижки", "Давление в стойке левая",
        #                           "Давление в стойке правая", "Щит УГЗ", "Щит Угз Угол",
        #                           "Щит УГЗ ход", "Щит угз давление",
        #                           "9", "10", "11", "12", "13", "14", "15"]

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
