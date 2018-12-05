from sqlalchemy import (Column, String, Integer)
from helpers.database import Base
from utilities.utility import Utility


class Question(Base, Utility):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_type = Column(String, nullable=False)
    question = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    total_responses = Column(String, nullable=True)
