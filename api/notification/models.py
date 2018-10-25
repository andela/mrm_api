from sqlalchemy import (Column, Integer, ForeignKey, Boolean)

from helpers.database import Base
from utilities.utility import Utility


class Notification(Base, Utility):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    device_health_notification = Column(Boolean, default=True)
    meeting_update_notification = Column(Boolean, default=True)
