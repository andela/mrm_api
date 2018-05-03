from sqlalchemy import (
    Column, String, Integer, ForeignKey, func, 
    DateTime, create_engine)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from api.room.models import Room


class Resource(Base, Utility):
    __tablename__ = 'resource'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))

    def __init__(self, **kwargs):
        for field in kwargs:
            if not kwargs.get(field):
                raise AttributeError(f"Room {field} is required field")
            else:
                self.name = kwargs.get('name') 
                self.room_id = kwargs.get('room_id') 
