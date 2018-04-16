from sqlalchemy import (
    Column, String, Integer, ForeignKey, func, 
    DateTime, create_engine)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility


class Location(Base, Utility):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False)
    block = relationship('Block')