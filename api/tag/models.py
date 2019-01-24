from sqlalchemy import (Column, String, Table, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility
from utilities.validations import validate_empty_fields

room_tags = Table(
    'room_tags',
    Base.metadata,
    Column('room_id', Integer, ForeignKey('rooms.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
    )


class Tag(Base, Utility):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    color = Column(String, nullable=False)
    description = Column(String, nullable=False)
    room_tag = relationship(
        'Room',
        secondary=room_tags,
        backref=('rooms'),
        lazy="joined")

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.color = kwargs.get('color')
        self.description = kwargs.get('description')
        self.name = kwargs.get('name')
