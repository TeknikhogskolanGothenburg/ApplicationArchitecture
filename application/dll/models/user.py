from sqlalchemy import Column, Integer, String

from application.dll.db import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, {self.email}'

    def to_dict(self):
        obj_dict = self.__dict__
        del obj_dict['_sa_instance_state']
        return obj_dict
