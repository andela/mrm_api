from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility


class Events(Base, Utility):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event_id = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    checked_in = Column(Boolean, nullable=True)
    cancelled = Column(Boolean, nullable=True)
    room = relationship('Room')
