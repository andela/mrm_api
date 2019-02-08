from sqlalchemy import (Column, String, Integer, ForeignKey, Enum)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType
from utilities.validations import validate_empty_fields


class Resource(Base, Utility):
    __tablename__ = 'resources'
    id = Column(Integer, Sequence('resources_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    state = Column(Enum(StateType), default="active")
    room = relationship('Room')

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.name = kwargs.get('name')
        self.quantity = kwargs.get('quantity')
        self.room_id = kwargs.get('room_id')
