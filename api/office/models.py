from sqlalchemy import (
    Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields
from api.location.models import Location  # noqa: F401


class Office(Base, Utility):
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    building_name = Column(String, nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    location = relationship('Location')
    blocks = relationship('Block')

    def __init__(self, **kwargs):

        validate_empty_fields(**kwargs)

        self.building_name = kwargs['building_name']
        self.location_id = kwargs['location_id']
