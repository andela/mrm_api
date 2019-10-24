from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey, Enum)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence
from graphql import GraphQLError

from helpers.database import Base
from utilities.utility import Utility, StateType
from helpers.events_filter.events_filter import (
   validate_date_input,
   format_range_dates,
)


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


def filter_events_by_date_range(query, start_date, end_date):
    """
    Returns events that fall within the date range supplied
    """
    validate_date_input(start_date, end_date)
    if not start_date and not end_date:
        events = query.filter(
                Events.state == 'active'
            ).all()
        if not events:
            raise GraphQLError('Events do not exist')
        return events

    start_date, end_date = format_range_dates(start_date, end_date)

    events = query.filter(
            Events.state == 'active',
            Events.start_time >= start_date,
            Events.end_time <= end_date
        ).all()
    if not events:
        raise GraphQLError('Events do not exist for the date range')
    return events


def filter_event_by_room(room_id, start_date, end_date):
    """
    Returns all events in a room using the calendar id as the filter field.
    If the start and end dates are provided, it considers them as well.
    """
    validate_date_input(start_date, end_date)
    if not start_date and not end_date:
        events = Events.query.filter_by(
                room_id = room_id,
                state = 'active'
            ).all()
        if not events:
            raise GraphQLError('Events do not exist')
        return events

    start_date, end_date = format_range_dates(start_date, end_date)

    events = Events.query.filter(
        Events.room_id == room_id,
        Events.state == 'active',
        Events.start_time >= start_date,
        Events.end_time <= end_date
        ).all()
    if not events:
        raise GraphQLError('Events do not exist for the date range')
    return events
