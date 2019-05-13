from sqlalchemy import Column, String, Integer, Enum

from utilities.utility import Utility, StateType
from helpers.database import Base


class Structure(Base, Utility):
    __tablename__ = "office_structures"

    id = Column(Integer, primary_key=True)
    # structure_id is the id from the client side
    structure_id = Column(String, nullable=False, unique=True)
    level = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    parent_id = Column(String, nullable=True)
    parent_title = Column(String, nullable=True)
    tag = Column(String(50), nullable=False)
    location_id = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
    state = Column(Enum(StateType), default="active")
