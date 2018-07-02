from sqlalchemy import (Column, String, Integer, DateTime, ForeignKey)

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields
from api.room_resource.models import Resource  # noqa: F401


class Devices(Base, Utility):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
    date_added = Column(DateTime, nullable=False)
    last_seen = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    resource_id = Column(Integer, ForeignKey('resources.id'))

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.name = kwargs['name']
        self.device_type = kwargs['device_type']
        self.date_added = kwargs['date_added']
        self.last_seen = kwargs['last_seen']
        self.location = kwargs['location']
        self.resource_id = kwargs['resource_id']
