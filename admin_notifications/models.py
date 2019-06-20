from sqlalchemy import (Column, String, Enum, Integer, ForeignKey)
from helpers.database import Base
from utilities.utility import Utility, StatusType


class AdminNotification(Base, Utility):
    __tablename__ = 'admin_notifications'

    id = Column(Integer, primary_key=True) # noqa
    title = Column(String, nullable=True)
    message = Column(String, nullable=True)
    date_received = Column(String, nullable=True)
    date_read = Column(String, nullable=True)
    status = Column(Enum(StatusType), default="unread")
    location_id = Column(
        Integer,
        ForeignKey('locations.id', ondelete="CASCADE"),
        nullable=True
    )
