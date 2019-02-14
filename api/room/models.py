from sqlalchemy import (
    Column, String, Integer, ForeignKey, event, Table, Enum, Index
)
from sqlalchemy.orm import relationship
from graphql import GraphQLError
from sqlalchemy.schema import Sequence

from helpers.database import Base, db_session
from utilities.utility import Utility, StateType, cascade_soft_delete
from api.floor.models import Floor  # noqa: F401
from api.wing.models import Wing  # noqa: F401
from api.events.models import Events  # noqa: F401
from api.response.models import Response  # noqa: F401
from api.tag.models import Tag  # noqa: F401
from utilities.validator import verify_calendar_id
from api.devices.models import Devices # noqa F4


tags = Table(
    'room_tags',
    Base.metadata,
    Column('tag_id', Integer, ForeignKey('tags.id')),
    Column('room_id', Integer, ForeignKey('rooms.id'))
    )


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, Sequence('rooms_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    room_type = Column(String)
    capacity = Column(Integer, nullable=False)
    image_url = Column(String)
    calendar_id = Column(String)
    location_id = Column(
        Integer,
        ForeignKey('locations.id', ondelete="CASCADE"),
        nullable=True
    )
    firebase_token = Column(String, nullable=True)
    floor_id = Column(Integer, ForeignKey('floors.id', ondelete="CASCADE"))
    wing_id = Column(Integer, ForeignKey('wings.id', ondelete="CASCADE"))
    cancellation_duration = Column(Integer, default=10)
    floor = relationship('Floor')
    state = Column(Enum(StateType), default="active")
    resources = relationship(
        'Resource', cascade="all, delete-orphan",
        order_by="func.lower(Resource.name)")
    events = relationship('Events', cascade="all, delete-orphan")
    response = relationship('Response', cascade="all, delete-orphan")
    room_tags = relationship(
        'Tag',
        secondary="room_tags",
        backref=('tags'),
        lazy="joined")
    devices = relationship(
        'Devices', cascade="all, delete-orphan",
        order_by="func.lower(Devices.name)")

    __table_args__ = (
            Index(
                'ix_unique_room_content',
                'name',
                unique=True,
                postgresql_where=(state == 'active')),
        )


@event.listens_for(Room, 'before_insert')
def receive_before_insert(mapper, connection, target):
    @event.listens_for(db_session, "after_flush", once=True)
    def receive_after_flush(session, context):
        if not verify_calendar_id(target.calendar_id):
            raise GraphQLError("Room calendar Id is invalid")
        pass


cascade_soft_delete(
    Room, 'room_resource', 'room_id'
)
cascade_soft_delete(
    Room, 'events', 'room_id'
)
