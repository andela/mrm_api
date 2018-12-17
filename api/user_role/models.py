from sqlalchemy import (Column, Integer, ForeignKey)
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, validate_empty_fields


class UsersRole(Base, Utility):
    __tablename__ = 'users_roles'
    id = Column(Integer, Sequence('users_roles_id_seq', start=1, increment=1), primary_key=True) # noqa
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'))

    def __init__(self, **kwargs):

        validate_empty_fields(**kwargs)

        self.user_id = kwargs['user_id']
        self.role_id = kwargs['role_id']
