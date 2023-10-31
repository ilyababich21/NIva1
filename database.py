import datetime

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship


class NivaStorage:
    class Base(DeclarativeBase):
        pass

    # ОПИСАНИЕ БАЗЫ ДАННЫХ
    class Role(Base):
        __tablename__ = "role"
        id = Column(Integer, primary_key=True, index=True)
        role = Column(String)
        description = Column(String)

        users = relationship("Users", back_populates="role")

    class Manufacture(Base):
        __tablename__ = "manufacture"
        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        name = Column(String)
        discription = Column(String)
        ip_address = Column(String)
        port = Column(Integer)
        count_shield = Column(Integer)
        count_dat = Column(Integer)
        users = relationship("Users", back_populates="manufacture")
        creps = relationship("Crep_ifc", back_populates="manufacture")

    class Users(Base):
        __tablename__ = "credential"
        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        login = Column(String)
        password = Column(String)
        manufacture_id = Column(Integer, ForeignKey("manufacture.id"))
        manufacture = relationship("Manufacture", back_populates="users")
        role_id = Column(Integer, ForeignKey("role.id"))
        role = relationship("Role", back_populates="users")
        settings = relationship("SettingsSensorsTable", back_populates="users")

    class Modbus(Base):
        __tablename__ = "modbus"
        id = Column(Integer, primary_key=True, autoincrement=True)
        ip_address = Column(String)
        port = Column(Integer)
        slave_id = Column(Integer)
        start_register = Column(Integer)
        count_register = Column(Integer)

    class Crep_ifc(Base):
        __tablename__ = "creps"
        id = Column(Integer, primary_key=True, index=True)
        num = Column(Integer)
        sensors = relationship("Sensors_ifc", back_populates="crep")
        manufacture_id = Column(Integer, ForeignKey("manufacture.id"))
        manufacture = relationship("Manufacture", back_populates="creps")

    class Sensors_ifc(Base):
        __tablename__ = "sensors"
        id = Column(Integer, primary_key=True, index=True)
        id_dat = Column(Integer, ForeignKey("global_param.id"))
        dat = relationship("GlobalParamTable", back_populates="sensors")
        value = Column(String)
        create_date = Column(DateTime, default=datetime.datetime.now())
        crep_id = Column(Integer, ForeignKey("creps.id"))
        crep = relationship("Crep_ifc", back_populates="sensors")

    class GlobalParamTable(Base):
        __tablename__ = "global_param"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String)
        min_value = Column(Integer)
        max_value = Column(Integer)
        from_normal_value = Column(Integer)
        to_normal_value = Column(Integer)
        units = Column(String)
        sensors = relationship("Sensors_ifc", back_populates="dat")
        settings = relationship("SettingsSensorsTable", back_populates="sensor")

    class SettingsSensorsTable(Base):
        __tablename__ = "settings_sensors"

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        user_id = Column(Integer, ForeignKey("credential.id"))
        sensor_id = Column(Integer, ForeignKey("global_param.id"))
        color_button_one = Column(String)
        color_button_two = Column(String)
        color_button_three = Column(String)
        color_button_four = Column(String)
        min_value = Column(Integer)
        max_value = Column(Integer)

        users = relationship("Users", back_populates="settings")
        sensor = relationship("GlobalParamTable", back_populates="settings")

    def __init__(self):
        # Создаём движок базы данных
        self.engine = create_engine("postgresql://postgres:root@localhost/niva1")
        self.Base.metadata.create_all(bind=self.engine)

        db_session = sqlalchemy.orm.sessionmaker(bind=self.engine)
        self.session = db_session()
        # ЗАПОЛНЯЕМ БАЗУ В СЛУЧАЕ ОТСУТСТВИЯ ПОЛЕЙ
        if not self.session.query(self.Manufacture).count():
            self.session.add(self.Manufacture(name='niva',ip_address="127.0.0.1",port=502,count_dat = 15, discription='null', count_shield=20))
            # self.session.commit()

        if not self.session.query(self.Modbus).count():
            self.session.add(
                self.Modbus(ip_address="127.0.0.1", port=502, slave_id=1, start_register=1, count_register=15))
            # self.session.commit()

        if not self.session.query(self.Crep_ifc).count():
            for elem in range(1, 301):  # я бы переписал конечно
                number = self.Crep_ifc(num=elem, manufacture_id=1)

                self.session.add(number)

        if not self.session.query(self.GlobalParamTable).count():
            self.session.add_all(
                [self.GlobalParamTable(id=id, name="NULL", min_value=0, max_value=600, from_normal_value=300,
                                       to_normal_value=400, units="bar") for id in range(1, 16)])

        if not self.session.query(self.Role).count():
            self.session.add_all([self.Role(role="admin", description="Администратор"),
                                  self.Role(role="miner", description="Шахтёр"),
                                  self.Role(role="service", description="Сервис")])

        if not self.session.query(self.Users).count():
            self.session.add_all([self.Users(login="service", password="1111", manufacture_id=1,
                                             role_id=self.session.query(self.Role).filter(
                                                 self.Role.role == "service").first().id),
                                  self.Users(login="IFC", password="ifc", manufacture_id=1,
                                             role_id=self.session.query(self.Role).filter(
                                                 self.Role.role == "admin").first().id)])

        if not self.session.query(self.SettingsSensorsTable).count():
            self.session.add_all([self.SettingsSensorsTable(user_id=1, sensor_id=id,
                                                            color_normal_pushButton="#24a319",
                                                            color_reduced_pushButton="#ff6b00",
                                                            color_increased_pushButton="#ff0000", min_value=1,
                                                            max_value=2) for id in range(1, 16)])
        self.session.commit()

    # РАБОТА С USERS
    def users_list(self):
        """Метод возвращающий список известных пользователей"""
        query = self.session.query(self.Users).all()
        return query

    def check_user(self, username, password):
        query = self.session.query(self.Users).filter_by(login=username, password=password).first()
        if query:
            return query.role.role, query.id
        else:
            return None

    def add_user(self, username, password, role_id):
        self.session.add_all(
            [self.Users(login=username, password=password, manufacture_id=1,
                        role_id=role_id)])
        self.session.commit()

    def add_settings_sensors_of_user(self, user_id):
        self.session.add_all([self.SettingsSensorsTable(user_id=user_id, sensor_id=id,
                                                        color_normal_pushButton="#24a319",
                                                        color_reduced_pushButton="#ff6b00",
                                                        color_increased_pushButton="#ff0000", min_value=1,
                                                        max_value=2) for id in range(1, 16)])
        # self.session.commit()

    def remove_user(self, username):
        """Метод удаляющий пользователя из базы."""
        delete_query = self.session.query(self.Users).filter(self.Users.login == username).first()
        self.session.delete(delete_query)
        self.session.commit()

    # USERS IN IFC
    def users_in_ifc(self):
        users = self.session.query(self.Users).filter(self.Users.role_id <= 2).all()
        return users

    def roles_in_ifc(self):
        roles = self.session.query(self.Role).filter(self.Role.id <= 2).all()
        return roles

    def get_global_params(self):
        query = self.session.query(self.GlobalParamTable).all()
        return query

    def update_global_params(self, params, list_param):
        params.name, params.min_value, params.max_value, params.from_normal_value, params.to_normal_value, params.units = list_param
        self.session.commit()

    # MANUFACTURE
    def get_count_shield(self):
        count = self.session.query(self.Manufacture).first()
        return count.count_shield

    def update_count_shield(self, count):
        manufacture = self.session.query(self.Manufacture).first()
        manufacture.count_shield = count
        self.session.commit()

    # SENSORS
    def query_sensors(self, id_dat, crep_id):
        query = self.session.query(self.Sensors_ifc).filter(self.Sensors_ifc.id_dat == id_dat,
                                                            self.Sensors_ifc.crep_id == crep_id).all()
        return query

    def query_modbus(self):
        query = self.session.get(self.Modbus, 1)
        return query

    def get_setting_sensors(self, user):
        query = self.session.query(self.SettingsSensorsTable).filter(self.SettingsSensorsTable.user_id == user).all()
        return query

    def update_settings_sensors(self, sensor_id,user_id, color_normal_pushButton, color_reduced_pushButton,
                                color_increased_pushButton):
        update = self.session.query(self.SettingsSensorsTable).filter_by(user_id = user_id,sensor_id = sensor_id).first()
        update.color_normal_pushButton = color_normal_pushButton
        update.color_reduced_pushButton = color_reduced_pushButton
        update.color_increased_pushButton = color_increased_pushButton
        self.session.commit()

    def update_modbus_table(self, params, list_param):
        params.ip_address, params.port, params.slave_id, params.start_register, params.count_register = list_param
        self.session.commit()

    def query_manufacture(self):
        query = self.session.get(self.Manufacture, 1)
        return query

    def update_manufacture_table(self, params, list_param):
        params.ip_address,params.port,params.count_shield,params.count_dat, = list_param
        self.session.commit()



if __name__ == "__main__":
    test_db = NivaStorage()
