import csv
import os
import shutil
import time
import pandas as pd
from PyQt6.QtCore import QObject
from connection_to_db import session
from ifcApp.ifc.mainMenu.globalparam_model import GlobalParamTable
from serviceApp.service.service_model import engine
from multiprocessing import Process

CSV_History = 'CSV_History'


def traversing_directories():
    for folder in range(1, len(os.listdir(CSV_History)) + 1):
        crep_dir = CSV_History + "\\" + str(folder)
        for chunk in pd.read_csv(crep_dir + "\\" + str(len(os.listdir(crep_dir))) + ".csv", chunksize=5000):
            chunk.to_sql("sensors", engine, if_exists="append", index=False)


def DBWriterIter():
    try:
        try:
            traversing_directories()

        except:
            print("shit")

        print("prokatilo")
        for dir in range(1, len(os.listdir(CSV_History)) + 1):
            crep_dir = CSV_History + "\\" + str(dir)
            with open(crep_dir + "\\" + str(len(os.listdir(crep_dir)) + 1) + ".csv", "w", newline="") as file:
                writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                        extrasaction='ignore')
                writer.writeheader()
    except:
        print('rig')


def DBwrite():
    while True:
        print("hel")
        try:

            time.sleep(120)
        except:
            print("ebanutsa")
        DBWriterIter()


class IfcModel(QObject):
    def __init__(self):
        super().__init__()
        for files in os.listdir("CSV_History"):
            path = os.path.join("CSV_History", files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

        for count in range(1, 201):
            folder_addr = "CSV_History\\" + str(count)
            if not os.path.exists(folder_addr):
                os.makedirs(folder_addr)
                with open("CSV_History\\" + str(count) + "\\" + "1.csv", "w",
                          newline="") as file:
                    writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                            extrasaction='ignore')
                    writer.writeheader()
        proc = Process(target=DBwrite, daemon=True)
        proc.start()

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
