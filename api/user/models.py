from sqlalchemy import (
    Column, String, Integer)
from helpers.database import Base
from utilities.utility import Utility


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
