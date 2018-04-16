from sqlalchemy import (
    Column, String, Integer, ForeignKey, func, 
    DateTime, create_engine)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from api.block.models import Block


class Floor(Base, Utility):
    __tablename__ = 'floors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    block_id = Column(Integer, ForeignKey('blocks.id'))
    room = relationship('Room')
