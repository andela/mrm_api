from sqlalchemy import (Column, String, Integer, Enum, Index)
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship
from helpers.database import Base
from utilities.utility import Utility, StateType
from utilities.validations import validate_empty_fields


class Resource(Base, Utility):
    __tablename__ = 'resources'
    id = Column(Integer, Sequence('resources_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    state = Column(Enum(StateType), default="active")
    room = relationship("RoomResource", back_populates="resource")

    __table_args__ = (
            Index(
                'ix_unique_resource_content',
                'name',
                unique=True,
                postgresql_where=(state == 'active')),
        )

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.name = kwargs.get('name')
        self.quantity = kwargs.get('quantity')
