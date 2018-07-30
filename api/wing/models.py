from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from api.floor.models import Floor  # noqa: F401


class Wing(Base, Utility):
    __tablename__ = 'wings'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    floor_id = Column(Integer, ForeignKey('floors.id'))
    floor = relationship('Floor')
    rooms = relationship('Room')
