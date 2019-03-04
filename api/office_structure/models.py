from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy_mptt.mixins import BaseNestedSets

from helpers.database import Base
from utilities.utility import Utility
from helpers.database import db_session


class OfficeStructure(Base, Utility, BaseNestedSets):
    __tablename__ = "structure"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, unique=True)
    tag_id = Column(
        Integer,
        ForeignKey('tags.id', ondelete="CASCADE"),
        nullable=True
    )

    def __repr__(self):
        return "<OfficeStructure {}>".format(self.name)

    def add_node(self, name, parent_id=None):
        """Function for adding nodes"""
        if parent_id is None:
            db_session.add(OfficeStructure(name=name))
        else:
            db_session.add(OfficeStructure(name=name, parent_id=parent_id))

        db_session.commit()

    def add_branch(self, nodes):
        """
        Function to add a single branch
        :params list of nodes
        """
        db_session.add_all(nodes)

        db_session.commit()
