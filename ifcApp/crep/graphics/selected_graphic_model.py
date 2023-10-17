from PyQt6.QtCore import QObject
import pandas as pd
from connection_to_db import session
from ifcApp.crep.crep_model import Sensors_ifc


class SelectedGraphicModel(QObject):
    def __init__(self, num_crep, num_sensors):
        self.num_crep = num_crep
        self.num_sensors = num_sensors
        super().__init__()

    def get_data(self, from_datetime, before_datetime):
        query_sql = session.query(Sensors_ifc).filter(Sensors_ifc.id_dat == self.num_sensors,
                                                      Sensors_ifc.crep_id == self.num_crep).all()
        df = pd.DataFrame([(one.create_date, one.value) for one in query_sql])
        df.columns = ['create_date', 'value']
        df.sort_values(by=['create_date'], inplace=True)
        df['value'] = df['value'].astype("int64")
        df = df.groupby(["create_date"])['value'].mean().astype(int).reset_index()
        df = pd.DataFrame(df).set_index(['create_date'])
        print(df)
        df = df.loc[f"{from_datetime}": f"{before_datetime}"]
        return df
