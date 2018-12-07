from sqlalchemy import (Column, String, ForeignKey, Integer, Boolean)
from sqlalchemy.orm import relationship
from helpers.database import Base
from utilities.utility import Utility
from api.question.models import Question  # noqa: F401


class Response(Base, Utility):
    __tablename__ = 'responses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    rate = Column(Integer, nullable=True)
    check = Column(Boolean, nullable=True)
    text_area = Column(String, nullable=True)
    question = relationship('Question')
    room = relationship('Room')
