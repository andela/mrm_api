from sqlalchemy import (
    Column, String, Integer, ForeignKey, func, 
    DateTime, create_engine)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from location.models import Location


class Block(Base, Utility):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'))
    floor = relationship('Floor')
