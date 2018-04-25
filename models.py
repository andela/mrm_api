from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

#local imports.

Base = declarative_base()
# test class to run migration. It is expected to change.
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)



