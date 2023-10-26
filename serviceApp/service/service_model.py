from PyQt6.QtCore import QObject
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from connection_to_db import session, engine, Base


class ServiceModel(QObject):

    def __init__(self):
        super().__init__()

    @staticmethod
    def load_information_from_db(model_object):
        object_database = session.get(model_object, 1)
        if object_database is None:
            session.add(model_object(manufacture_id=1))
            session.commit()
            object_database = session.get(model_object, 1)
        return object_database


Base.metadata.create_all(bind=engine)
