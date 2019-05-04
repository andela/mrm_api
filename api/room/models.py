from sqlalchemy import (
    Column, String, Integer, ForeignKey, event, Table, Enum, Index
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from graphql import GraphQLError
from sqlalchemy.schema import Sequence

from helpers.database import Base, db_session
from utilities.utility import Utility, StateType, cascade_soft_delete
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


class RoomResource(Base, Utility):
    __tablename__ = 'room_resources'
    room_id = Column(Integer, ForeignKey('rooms.id'), primary_key=True)
    resource_id = Column(Integer, ForeignKey('resources.id'), primary_key=True)
    quantity = Column(Integer)
    name = Column(String)
    resource = relationship("Resource", back_populates="room")
    room = relationship("Room", back_populates="resources")


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, Sequence('rooms_id_seq',
                                  start=1, increment=1), primary_key=True)
    name = Column(String, nullable=False)
    room_type = Column(String)
    capacity = Column(Integer, nullable=False)
    room_labels = Column(postgresql.ARRAY(String), default=[])
    image_url = Column(String)
    calendar_id = Column(String)
    location_id = Column(
        Integer,
        ForeignKey('locations.id', ondelete="CASCADE"),
        nullable=True
    )
    firebase_token = Column(String, nullable=True)
    cancellation_duration = Column(Integer, default=10)
    state = Column(Enum(StateType), default="active")
    next_sync_token = Column(String, nullable=True)
    events = relationship('Events', cascade="all, delete-orphan")
    response = relationship('Response', cascade="all, delete-orphan")
    structure_id = Column(String, default="place-holder-id")
    room_tags = relationship(
        'Tag',
        secondary="room_tags",
        backref=('tags'),
        lazy="joined")
    devices = relationship(
        'Devices', cascade="all, delete-orphan",
        order_by="func.lower(Devices.name)")
    resources = relationship("RoomResource", back_populates='room')

    __table_args__ = (
            Index(
                'ix_unique_room_in_location_content',
                'name',
                'location_id',
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
    Room, 'events', 'room_id'
)
