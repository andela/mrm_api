from sqlalchemy import (Column, String, Integer)

from helpers.database import Base
from utilities.utility import Utility
from utilities.validations import validate_empty_fields


class Tag(Base, Utility):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    description = Column(String, nullable=False)

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.color = kwargs.get('color')
        self.description = kwargs.get('description')
        self.name = kwargs.get('name')
