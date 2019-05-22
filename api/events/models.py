from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey, Enum)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType


class Events(Base, Utility):
    __tablename__ = 'events'
    id = Column(Integer, Sequence('events_id_seq', start=1, increment=1), primary_key=True) # noqa
    event_id = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id', ondelete="CASCADE"))
    event_title = Column(String, nullable=True)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    checked_in = Column(Boolean, nullable=True)
    cancelled = Column(Boolean, nullable=True)
    state = Column(Enum(StateType), default="active")
    room = relationship('Room')
    recurring_event_id = Column(String, nullable=True)
    number_of_participants = Column(Integer, nullable=False)
    check_in_time = Column(String, nullable=True)
    meeting_end_time = Column(String, nullable=True)
    auto_cancelled = Column(Boolean, nullable=True, default=False)
    app_booking = Column(Boolean, nullable=True, default=False)
