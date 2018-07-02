from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields
from api.room.models import Room  # noqa: F401


class Resource(Base, Utility):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship('Room')
    devices = relationship('Devices')

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.name = kwargs.get('name')
        self.quantity = kwargs.get('quantity')
        self.room_id = kwargs.get('room_id')
