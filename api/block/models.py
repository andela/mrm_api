from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility
from api.office.models import Office  # noqa: F401


class Block(Base, Utility):
    __tablename__ = 'blocks'
    id = Column(Integer, Sequence('blocks_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    office_id = Column(Integer, ForeignKey('offices.id'))
    offices = relationship('Office')
    floors = relationship('Floor', cascade="all, delete-orphan")

    @validates('name')
    def convert_upper(self, key, value):
        return value.title()
