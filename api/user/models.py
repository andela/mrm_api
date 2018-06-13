from sqlalchemy import (Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields
from api.user_role.models import UsersRole


class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)
    roles = relationship('Role', secondary='users_role')
        
    def __init__(self, **kwargs):

        validate_empty_fields(**kwargs)

        self.email = kwargs['email']
        self.location = kwargs['location']
