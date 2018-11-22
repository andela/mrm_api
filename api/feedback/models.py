from datetime import datetime
from sqlalchemy import (Column, String, Integer, ForeignKey)
from helpers.database import Base
from utilities.utility import Utility


class Feedback(Base, Utility):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    comments = Column(String, nullable=True)
    creation_time = Column(String, nullable=False, default=datetime.now().isoformat()[:-7] + 'Z')  # noqa
    overall_rating = Column(String, nullable=True)
    cleanliness_rating = Column(String, nullable=True)
