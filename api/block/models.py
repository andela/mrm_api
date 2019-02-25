from sqlalchemy import (Column, String, Integer, ForeignKey, Enum, Index)
from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import Sequence

from helpers.database import Base
from utilities.utility import Utility, StateType, cascade_soft_delete
from api.office.models import Office  # noqa: F401


class Block(Base, Utility):
    __tablename__ = 'blocks'
    id = Column(Integer, Sequence('blocks_id_seq', start=1, increment=1), primary_key=True) # noqa
    name = Column(String, nullable=False)
    office_id = Column(Integer, ForeignKey('offices.id', ondelete="CASCADE"))
    offices = relationship('Office')
    state = Column(Enum(StateType), default="active")
    floors = relationship(
        'Floor', cascade="all, delete-orphan",
        order_by="func.lower(Floor.name)")

    __table_args__ = (
            Index(
                'ix_unique_block_content',
                'name',
                unique=True,
                postgresql_where=(state == 'active')),
        )

    @validates('name')
    def convert_upper(self, key, value):
        return value.title()


cascade_soft_delete(
    Block, 'floor', 'block_id'
)
