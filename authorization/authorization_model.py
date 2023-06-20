from sqlalchemy.orm import relationship

from serviceApp.service.service_model import engine, Base, Manufacture
from serviceApp.service.service_model import session
from sqlalchemy import Column, Integer, String, ForeignKey


class Users(Base):
    __tablename__ = "credential"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    login = Column(String)
    password = Column(String)
    manufacture_id = Column(Integer, ForeignKey(Manufacture.id))
    manufacture=relationship("Manufacture", back_populates="users")
    role_id = Column(Integer, ForeignKey("role.id"))
    role = relationship("Role_ifc", back_populates="users")


class Role_ifc(Base):
    __tablename__ = "role"
    id =Column(Integer,primary_key=True, index=True)
    role = Column(String)
    description = Column(String)

    users = relationship("Users", back_populates="role")

Base.metadata.create_all(bind=engine)
