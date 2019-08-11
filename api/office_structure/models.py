from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_mptt.mixins import BaseNestedSets
from utilities.utility import Utility, StateType
from helpers.database import Base


class OfficeStructure(Base, Utility, BaseNestedSets):
    __tablename__ = "structures"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(100), nullable=False)
    tag = Column(String(100), nullable=False)
    location_id = Column(Integer, nullable=False)
    state = Column(Enum(StateType), default="active")
