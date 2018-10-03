from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from api.floor.models import Floor  # noqa: F401
from api.wing.models import Wing  # noqa: F401


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    room_type = Column(String)
    capacity = Column(Integer, nullable=False)
    image_url = Column(String)
    calendar_id = Column(String)
    floor_id = Column(Integer, ForeignKey('floors.id'))
    wing_id = Column(Integer, ForeignKey('wings.id'))
    floor = relationship('Floor')
    resources = relationship('Resource', cascade="all, delete-orphan")
