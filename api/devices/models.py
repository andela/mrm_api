from sqlalchemy import (Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.schema import Sequence
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.validations import validate_empty_fields
from utilities.utility import Utility


class Devices(Base, Utility):
    __tablename__ = 'devices'
    id = Column(Integer, Sequence('devices_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
    date_added = Column(DateTime, nullable=False)
    last_seen = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id', ondelete="CASCADE"))
    room = relationship('Room')

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.name = kwargs['name']
        self.device_type = kwargs['device_type']
        self.date_added = kwargs['date_added']
        self.last_seen = kwargs['last_seen']
        self.location = kwargs['location']
        self.room_id = kwargs.get('room_id')
