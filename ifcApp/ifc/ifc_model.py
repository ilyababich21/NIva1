import csv
import os
import shutil
import threading
import time
import pandas as pd

from address import resource_path
from database import NivaStorage
from multiprocessing import Process

CSV_History = 'CSV_History'


def traversing_directories():
    niva_storage = NivaStorage()
    database_engine = niva_storage.engine
    addr_csv = resource_path(CSV_History)
    for folder in range(1, len(os.listdir(addr_csv)) + 1):
        crep_dir = addr_csv + "\\" + str(folder)
        print(crep_dir)
        for chunk in pd.read_csv(crep_dir + "\\" + str(len(os.listdir(crep_dir))) + ".csv", chunksize=10000):
            chunk.to_sql("sensors", database_engine, if_exists="append", index=False)


def DBWriterIter():
    try:
        try:
            traversing_directories()

        except:
            print("shit")

        print("prokatilo")
        for dir in range(1, len(os.listdir(resource_path('CSV_History'))) + 1):
            crep_dir = resource_path('CSV_History' + "\\" + str(dir))
            with open(crep_dir + "\\" + str(len(os.listdir(crep_dir)) + 1) + ".csv", "w", newline="") as file:
                writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                        extrasaction='ignore')
                writer.writeheader()
    except:
        print('rig')

class IfcModel(threading.Thread):
    def __init__(self):
        super().__init__()
        for files in os.listdir(resource_path("CSV_History")):
            path = os.path.join(resource_path("CSV_History"), files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

        for count in range(1, 201):
            folder_addr = resource_path("CSV_History\\" + str(count))
            if not os.path.exists(folder_addr):
                os.makedirs(folder_addr)
                with open(resource_path("CSV_History\\" + str(count) + "\\" + "1.csv"), "w",
                          newline="") as file:
                    writer = csv.DictWriter(file, ["id_dat", "value", "crep_id", "create_date"], restval='Unknown',
                                            extrasaction='ignore')
                    writer.writeheader()
        self.running=False
        self.play = True


    def run(self):
        self.running =True
        threads = threading.enumerate()
        print("Active threads:", threads)
        pTime=time.time()
        while self.running:
            if time.time()-pTime>60:
                print('IDI ')
                proc = Process(target=DBWriterIter, daemon=True)
                proc.start()
                threads = threading.enumerate()
                print("Active threads:", threads)
                pTime=time.time()
            else:
                time.sleep(3)
        print("Goodbye")
        threads = threading.enumerate()
        print("Active threads:", threads)





