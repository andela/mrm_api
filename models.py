from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base

#local imports.
from app import db

# test class to run migration. It is expected to change.
class User(db.Model):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)



