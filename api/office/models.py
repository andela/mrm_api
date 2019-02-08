from sqlalchemy import (Column, String, Integer, ForeignKey, event, Enum)
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType
from api.location.models import Location  # noqa: F401
from api.block import models
from helpers.database import db_session
from utilities.validator import check_office_name


class Office(Base, Utility):
    __tablename__ = 'offices'
    id = Column(Integer, Sequence('offices_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=True, unique=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship('Location')
    state = Column(Enum(StateType), default="active")
    blocks = relationship(
        'Block', cascade="all, delete-orphan",
        order_by="func.lower(Block.name)")


@event.listens_for(Office, 'after_insert')
def receive_after_insert(mapper, connection, target):
    @event.listens_for(db_session, "after_flush", once=True)
    def receive_after_flush(session, context):
        if check_office_name(target.name):
            session.add(models.Block(name=target.name, office_id=target.id))
        pass
