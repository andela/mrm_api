from sqlalchemy import (Column, Integer, ForeignKey)

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields


class UsersRole(Base, Utility):
    __tablename__ = 'users_roles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'))

    def __init__(self, **kwargs):

        validate_empty_fields(**kwargs)

        self.user_id = kwargs['user_id']
        self.role_id = kwargs['role_id']
