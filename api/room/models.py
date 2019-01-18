from sqlalchemy import (Column, String, Integer, ForeignKey, event)
from sqlalchemy.orm import relationship
from graphql import GraphQLError
from sqlalchemy.schema import Sequence

from helpers.database import Base, db_session
from utilities.utility import Utility
from api.floor.models import Floor  # noqa: F401
from api.wing.models import Wing  # noqa: F401
from api.events.models import Events  # noqa: F401
from api.response.models import Response  # noqa: F401
from helpers.auth.validator import verify_calendar_id


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, Sequence('rooms_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    room_type = Column(String)
    capacity = Column(Integer, nullable=False)
    image_url = Column(String)
    calendar_id = Column(String)
    floor_id = Column(Integer, ForeignKey('floors.id'))
    wing_id = Column(Integer, ForeignKey('wings.id'))
    cancellation_duration = Column(Integer, default=10)
    floor = relationship('Floor')
    resources = relationship(
        'Resource', cascade="all, delete-orphan",
        order_by="func.lower(Resource.name)")
    events = relationship('Events', cascade="all, delete-orphan")
    response = relationship('Response', cascade="all, delete-orphan")


@event.listens_for(Room, 'before_insert')
def receive_before_insert(mapper, connection, target):
    @event.listens_for(db_session, "after_flush", once=True)
    def receive_after_flush(session, context):
        if not verify_calendar_id(target.calendar_id):
            raise GraphQLError("Room calendar Id is invalid")
        pass
