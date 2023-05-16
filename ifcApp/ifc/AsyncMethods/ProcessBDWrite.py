import csv
import sys
import time

import pandas as pd
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer

from serviceApp.service.service_model import engine

def flush_then_wait():
    sys.stdout.flush()
    time.sleep(0.5)

sys.stdout.write("Script stdout 1\n")
print("pognali")
flush_then_wait()
time.sleep(10)
columns = ["id_dat", "value", "crep_id"]

while True:
    time.sleep(10)
    sys.stdout.write("Script stdout 1\n")
    print("pognali")
    flush_then_wait()
    # time.sleep(10)
    # try:
    #     for chunk in pd.read_csv('D:\\PythonProjects\\NIva1\\data1.csv', chunksize=10000):
    #         chunk.to_sql("sensors", engine, if_exists="append", index=False)
    #     with open('D:\\PythonProjects\\NIva1\\data1.csv', "w", newline="") as file:
    #         writer = csv.DictWriter(file, columns, restval='Unknown', extrasaction='ignore')
    #         writer.writeheader()
    # except:
    #     print('rig')
    # time.sleep(10)
