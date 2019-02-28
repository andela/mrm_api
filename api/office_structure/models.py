from sqlalchemy import Column, Integer, String
from helpers.database import Base
from utilities.utility import Utility

from sqlalchemy_mptt.mixins import BaseNestedSets


class OfficeStructure(Base, Utility, BaseNestedSets):
    __tablename__ = "structure"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), Index=True, unique=True)

    def __repr__(self):
        return "<{}>".format(self.name)
