from sqlalchemy import (
    Column, String, Integer, ForeignKey, func, 
    DateTime, create_engine, CheckConstraint)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from api.floor.models import Floor


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    floor_id = Column(Integer, ForeignKey('floors.id'))
    equipment = relationship('Equipment')

    def __init__(self, **kwargs):
        for field in kwargs:
            if not kwargs.get(field):
                raise AttributeError(f"Room {field} is required field")
        
        self.name = kwargs['name']
        self.room_type = kwargs['room_type']
        self.capacity = kwargs['capacity']
        self.floor_id = kwargs['floor_id']

