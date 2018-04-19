from sqlalchemy import (
    Column, String, Integer, ForeignKey, func, 
    DateTime, create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ScalarListType

from mrm_api.database import Base, db_session


class Utility(object):
    
    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()


class Location(Base, Utility):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)
    block = relationship('Block')


class Block(Base, Utility):
    __tablename__ = 'blocks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location_id = Column(Integer, ForeignKey('locations.id'))
    floor = relationship('Floor')


class Floor(Base, Utility):
    __tablename__ = 'floors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    block_id = Column(Integer, ForeignKey('blocks.id'))
    room = relationship('Room')


class Room(Base, Utility):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_of_room = Column(String)
    capacity = Column(Integer)
    floor_id = Column(Integer, ForeignKey('floors.id'))
    equipment = relationship('Equipment')


class Equipment(Base, Utility):
    __tablename__ = 'equipments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    room_id = Column(Integer, ForeignKey('rooms.id'))