from sqlalchemy import (
    Table, Column, String, ForeignKey, Integer, DateTime, Enum, Boolean
)
from sqlalchemy.orm import relationship
from helpers.database import Base
from utilities.utility import Utility, QuestionType
import api.question.models
from api.room_resource.models import Resource  # noqa: F401

# not importing it directly prevents a circular-import error
Question = api.question.models.Question  # noqa: F401

missing_items = Table(
    'missing_items', Base.metadata,
    Column('item_id', Integer, ForeignKey('resources.id')),
    Column('response_id', Integer, ForeignKey('responses.id')))


class Response(Base, Utility):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id', ondelete="CASCADE"))
    question_id = Column(Integer, ForeignKey(
        'questions.id', ondelete="CASCADE"))
    question_type = Column(Enum(QuestionType), default="rate")
    response = Column(String)
    created_date = Column(DateTime, nullable=False)
    resolved = Column(Boolean, default=False)
    question = relationship('Question')
    room = relationship('Room')
    missing_resources = relationship(
        'Resource',
        secondary="missing_items",
        backref=('resources'),
        lazy="joined")
