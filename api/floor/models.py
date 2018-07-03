from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from api.office.models import Office   # noqa: F401


class Floor(Base, Utility):
    __tablename__ = 'floors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    office_id = Column(Integer, ForeignKey('offices.id'))
    office = relationship('Office')
    rooms = relationship('Room')
