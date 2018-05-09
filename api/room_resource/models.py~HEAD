from sqlalchemy import (
    Column, String, Integer, ForeignKey)
from helpers.database import Base
from utilities.utility import Utility
from api.room.models import Room  # noqa: F401


class Resource(Base, Utility):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
