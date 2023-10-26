import csv
import os
import shutil
import time
import pandas as pd
from PyQt6.QtCore import QObject
from serviceApp.service.service_model import engine
from multiprocessing import Process

CSV_History = 'CSV_History'


def traversing_directories():
    for folder in range(1, len(os.listdir(CSV_History)) + 1):
        crep_dir = CSV_History + "\\" + str(folder)
        print(crep_dir)
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
        self.proc = Process(target=DBwrite, daemon=True)
        self.proc.start()




