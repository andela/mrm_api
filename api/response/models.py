from sqlalchemy import (
    Table, Column, String,
    ForeignKey, Integer, DateTime, Boolean)
from sqlalchemy.orm import relationship
from helpers.database import Base
from utilities.utility import Utility
from api.question.models import Question  # noqa: F401


missing_items = Table(
    'missing_items',
    Base.metadata,
    Column('item_id', Integer, ForeignKey('resources.id')),
    Column('response_id', Integer, ForeignKey('responses.id'))
    )


class Response(Base, Utility):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    rate = Column(Integer, nullable=True)
    check = Column(Boolean, nullable=True)
    text_area = Column(String, nullable=True)
    created_date = Column(DateTime, nullable=False)
    question = relationship('Question')
    room = relationship('Room')
    missing_resources = relationship(
        'Resource',
        secondary="missing_items",
        backref=('resources'),
        lazy="dynamic")
