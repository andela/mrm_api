from helpers.database import db_session
import enum


class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()


class StateType(enum.Enum):
    active = "active"
    archived = "archived"
    deleted = "deleted"
