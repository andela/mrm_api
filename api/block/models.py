from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from api.office.models import Office  # noqa: F401


class Block(Base, Utility):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    office_id = Column(Integer, ForeignKey('offices.id'))
    offices = relationship('Office')
    floors = relationship('Floor', cascade="all, delete-orphan")
