from sqlalchemy import (Column, String, Integer, ForeignKey, Enum, Index)
from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType, cascade_soft_delete
from api.block.models import Block   # noqa: F401


class Floor(Base, Utility):
    __tablename__ = 'floors'
    type(id)
    id = Column(Integer, Sequence('floors_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    block_id = Column(Integer, ForeignKey('blocks.id', ondelete="CASCADE"))
    block = relationship('Block')
    state = Column(Enum(StateType), default="active")
    rooms = relationship(
        'Room', cascade="all, delete-orphan",
        order_by="func.lower(Room.name)")
    wings = relationship(
        'Wing', cascade="all, delete-orphan",
        order_by="func.lower(Wing.name)")

    __table_args__ = (
            Index(
                'ix_unique_floor_content',
                'name',
                unique=True,
                postgresql_where=(state == 'active')),
        )

    @validates('name')
    def convert_capitalize(self, key, value):
        return value.capitalize()


cascade_soft_delete(
    Floor, 'room', 'floor_id'
)
cascade_soft_delete(
    Floor, 'wing', 'floor_id'
)
