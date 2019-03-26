from sqlalchemy import Column, String, Integer

from utilities.utility import Utility
from helpers.database import Base


class Structure(Base, Utility):
    __tablename__ = "office_structures"

    id = Column(Integer, primary_key=True)
    # web_id is the id from the client side
    web_id = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    parent_id = Column(Integer, nullable=False)
    tag = Column(String(50), nullable=False)
    location_id = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
