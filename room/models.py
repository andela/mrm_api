from sqlalchemy import (
    Column, String, Integer, ForeignKey, func, 
    DateTime, create_engine)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from floor.models import Floor


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    floor_id = Column(Integer, ForeignKey('floors.id'))
    equipment = relationship('Equipment')
