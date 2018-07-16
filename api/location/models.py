from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.orm import relationship

from helpers.database import Base


from utilities.utility import Utility
import enum


class CountryType(enum.Enum):
    Uganda = "Uganda"
    Kenya = "Kenya"
    Nigeria = "Nigeria"


class TimeZoneType(enum.Enum):
    EAST_AFRICA_TIME = "UTC+3"
    WEST_AFRICA_TIME = "UTC+1"


class Location(Base, Utility):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False)
    country = Column(Enum(CountryType))
    time_zone = Column(Enum(TimeZoneType))
    image_url = Column(String)
    offices = relationship('Office')
