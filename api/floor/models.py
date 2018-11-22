from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship, validates

from helpers.database import Base
from utilities.utility import Utility
from api.block.models import Block   # noqa: F401


class Floor(Base, Utility):
    __tablename__ = 'floors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    block_id = Column(Integer, ForeignKey('blocks.id'))
    block = relationship('Block')
    rooms = relationship('Room', cascade="all, delete-orphan")
    wings = relationship('Wing', cascade="all, delete-orphan")

    @validates('name')
    def convert_capitalize(self, key, value):
        return value.capitalize()
