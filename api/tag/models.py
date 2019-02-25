
from sqlalchemy import (Column, String, Integer, Enum, Index)

from helpers.database import Base
from utilities.utility import Utility, StateType
from utilities.validations import validate_empty_fields


class Tag(Base, Utility):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    state = Column(Enum(StateType), default="active")
    description = Column(String, nullable=False)

    __table_args__ = (
            Index(
                'ix_unique_tag_content',
                'name',
                unique=True,
                postgresql_where=(state == 'active')),
        )

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)
        self.color = kwargs.get('color')
        self.description = kwargs.get('description')
        self.name = kwargs.get('name')
