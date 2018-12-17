from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility


class Events(Base, Utility):
    __tablename__ = 'events'
    id = Column(Integer, Sequence('events_id_seq', start=1, increment=1), primary_key=True) # noqa
    event_id = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    event_title = Column(String, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    checked_in = Column(Boolean, nullable=True)
    cancelled = Column(Boolean, nullable=True)
    room = relationship('Room')
