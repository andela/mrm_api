from sqlalchemy import (Column, Integer, ForeignKey, Boolean)
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility


class Notification(Base, Utility):
    __tablename__ = 'notifications'
    id = Column(Integer, Sequence('notifications_id_seq', start=1, increment=1), primary_key=True) # noqa
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    device_health_notification = Column(Boolean, default=True)
    meeting_update_notification = Column(Boolean, default=True)
