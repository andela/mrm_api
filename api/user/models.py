from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields
from api.user_role.models import UsersRole  # noqa: F401
from api.notification.models import Notification  # noqa: F401
from api.feedback.models import Feedback  # noqa: F401
from api.response.models import Response  # noqa: F401


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=True)
    name = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    roles = relationship('Role', secondary='users_roles')
    notification_settings = relationship(
        'Notification', cascade="all, delete-orphan")
    feedback = relationship('Feedback', cascade="all, delete-orphan")
    response = relationship('Response', cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        validate_empty_fields(**kwargs)

        self.email = kwargs['email']
        self.name = kwargs['name']
        self.picture = kwargs['picture']
