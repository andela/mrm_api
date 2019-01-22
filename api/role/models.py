from sqlalchemy import (Column, String, Integer)
from sqlalchemy.schema import Sequence
from helpers.database import Base
from utilities.utility import Utility
from utilities.validations import validate_empty_fields


class Role(Base, Utility):
    __tablename__ = 'roles'
    id = Column(Integer, Sequence('roles_id_seq', start=1, increment=1), primary_key=True) # noqa
    role = Column(String, nullable=False, unique=True)

    def __init__(self, **kwargs):

        validate_empty_fields(**kwargs)

        self.role = kwargs['role']
