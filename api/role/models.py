from sqlalchemy import (Column, String, Integer)
from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields


class Role(Base, Utility):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    role = Column(String, nullable=False, unique=True)

    def __init__(self, **kwargs):

        validate_empty_fields(**kwargs)

        self.role = kwargs['role']
