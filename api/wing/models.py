from sqlalchemy import (Column, String, Integer, ForeignKey, Enum)
from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType
from api.floor.models import Floor  # noqa: F401


class Wing(Base, Utility):
    __tablename__ = 'wings'
    id = Column(Integer, Sequence('wings_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False, unique=True)
    floor_id = Column(Integer, ForeignKey('floors.id'))
    floor = relationship('Floor')
    rooms = relationship('Room')
    state = Column(Enum(StateType), default="active")

    @validates('name')
    def convert_upper(self, key, value):
        return value.title()
