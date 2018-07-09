from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.orm import relationship

from helpers.database import Base


from utilities.utility import Utility
import enum


class Country_type(enum.Enum):
    Uganda = "Uganda"
    Kenya = "Kenya"
    Nigeria = "Nigeria"


class TimeZone_type(enum.Enum):
    EAST_AFRICA_TIME = "UTC+3"
    WEST_AFRICA_TIME = "UTC+1"


class Location(Base, Utility):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False)
    country = Column(Enum(Country_type))
    time_zone = Column(Enum(TimeZone_type))
    image_url = Column(String)
    blocks = relationship('Block')
