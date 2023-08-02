from PyQt6.QtCore import QObject, pyqtSignal
from sqlalchemy.orm import relationship

from connection_to_db import session, engine, Base
from serviceApp.service.service_model import Manufacture
from sqlalchemy import Column, Integer, String, ForeignKey


class AuthorizationModel(QObject):
    login_successful = pyqtSignal(str)
    login_failed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.query_from_database_users = session.query(Users).all()
        self.qury_role = session.query(Role).all()

        if self.qury_role == []:
            session.add_all([Role(role="admin", description="Администратор"),
                             Role(role="miner", description="Шахтёр"),
                             Role(role="service", description="Сервис")])
            session.commit()

        if self.query_from_database_users == []:
            session.add_all([Users(login="service", password="1111", manufacture_id=1,
                                   role_id=session.query(Role).filter(Role.role == "service").first().id),
                             Users(login="IFC", password="ifc", manufacture_id=1,
                                   role_id=session.query(Role).filter(Role.role == "admin").first().id)])

            session.commit()

        # self.login_from_database()

    def login_from_database(self):
        query_login = session.query(Users.login).all()
        return query_login

    def login(self, username, password):
        user = session.query(Users).filter_by(login=username, password=password).first()

        if user:
            self.login_successful.emit(user.role.role)
        else:
            self.login_failed.emit()


class Users(Base):
    __tablename__ = "credential"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String)
    password = Column(String)
    manufacture_id = Column(Integer, ForeignKey(Manufacture.id))
    manufacture = relationship("Manufacture", back_populates="users")
    role_id = Column(Integer, ForeignKey("role.id"))
    role = relationship("Role", back_populates="users")


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    description = Column(String)

    users = relationship("Users", back_populates="role")


Base.metadata.create_all(bind=engine)
