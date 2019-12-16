from sqlalchemy import (Column, String, Integer, Boolean, ForeignKey, Enum)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType
from helpers.events_filter.events_filter import (
    validate_date_input,
    format_range_dates,
)
from api.bugsnag_error import return_error


class Events(Base, Utility):
    __tablename__ = 'events'
    id = Column(Integer, Sequence('events_id_seq', start=1, increment=1), primary_key=True)  # noqa
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


def filter_event(start_date, end_date, room_id=None):
    """
    Returns events filtered by room id,
    start date and end date if provided,
    or returns all events otherwise.
    """
    def error_message(error):
        return_error.report_errors_bugsnag_and_graphQL(error)

    validate_date_input(start_date, end_date)

    if room_id and start_date:
        start_date, end_date = format_range_dates(start_date, end_date)
        return Events.query.filter(
            Events.room_id == room_id,
            Events.state == 'active',
            Events.start_time >= start_date,
            Events.end_time <= end_date
        ).all() or error_message('Events do not exist for the date range')

    if room_id:
        return Events.query.filter_by(
            room_id=room_id,
            state='active'
        ).all() or error_message('Events do not exist')

    if start_date:
        start_date, end_date = format_range_dates(start_date, end_date)
        return Events.query.filter(
            Events.state == 'active',
            Events.start_time >= start_date,
            Events.end_time <= end_date
        ).all() or error_message('Events do not exist for the date range')

    return Events.query.filter(
        Events.state == 'active'
    ).all() or error_message('Events do not exist')
