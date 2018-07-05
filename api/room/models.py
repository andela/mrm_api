from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields
from api.floor.models import Floor  # noqa: F401
from api.location.models import Location   # noqa: F401


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    image_url = Column(String)
    calendar_id = Column(String)
    location = Column(String, ForeignKey('locations.name'))
    floor_id = Column(Integer, ForeignKey('floors.id'))
    floor = relationship('Floor')
    locations = relationship('Location')
    resources = relationship('Resource')

    def __init__(self, **kwargs):
        # validating empty fields
        validate_empty_fields(**kwargs)

        self.name = kwargs['name']
        self.room_type = kwargs['room_type']
        self.capacity = kwargs['capacity']
        self.image_url = kwargs['image_url']
        self.calendar_id = kwargs['calendar_id']
        self.location = kwargs['location']
        self.floor_id = kwargs['floor_id']
