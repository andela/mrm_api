from sqlalchemy import (Column, String, Integer, ForeignKey, Enum, Index)
from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType, cascade_soft_delete
from api.floor.models import Floor  # noqa: F401


class Wing(Base, Utility):
    __tablename__ = 'wings'
    id = Column(Integer, Sequence('wings_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    floor_id = Column(
        Integer, ForeignKey('floors.id',  ondelete="CASCADE")
    )
    floor = relationship('Floor')
    rooms = relationship('Room')
    state = Column(Enum(StateType), default="active")

    __table_args__ = (
            Index(
                'ix_unique_wing_content',
                'name',
                unique=True,
                postgresql_where=(state == 'active')),
        )

    @validates('name')
    def convert_upper(self, key, value):
        return value.title()


cascade_soft_delete(
    Wing, 'room', 'wing_id'
)
