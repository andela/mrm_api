from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.orm import relationship

from helpers.database import Base

from utilities.utility import Utility


class Location(Base, Utility):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False)
    country = Column(Enum('Uganda', 'Kenya', 'Nigeria', name='al_country'))
    time_zone = Column(Enum('GTM+3', 'GMT+1', name='all_timezones'))
    image_url = Column(String)
    blocks = relationship('Block')
