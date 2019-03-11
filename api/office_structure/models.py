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

    def add_node(self, **kwargs):
        """Function for adding nodes"""
        db_session.add(OfficeStructure(
                name=kwargs['name'],
                parent_id=kwargs.get('parent_id', None),
                tag_id=kwargs.get('tag_id', None)))

        db_session.commit()

    def add_branch(self, nodes):
        """
        Function to add a single branch
        :params list of nodes
        """
        db_session.add_all(nodes)

        db_session.commit()

    @property
    def nodes(self):
        """
        Function to return all the nodes
        """
        nodes = OfficeStructure.query.filter_by(tree_id=self.tree_id).all()
        return nodes
