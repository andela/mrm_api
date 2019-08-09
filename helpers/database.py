from sqlalchemy import create_engine, DateTime, Column, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from config import config

import os
import sys
sys.path.append(os.getcwd())

config_name = os.getenv('APP_SETTINGS')
database_uri = config.get(config_name).SQLALCHEMY_DATABASE_URI
engine = create_engine(database_uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

DeclarativeBase = declarative_base()
DeclarativeBase.query = db_session.query_property()


class Base(DeclarativeBase):
    """
    Extends the base class to the specific models and by default places the
    date_created and date_updated fields on all the tables in the database.
    """
    __abstract__ = True  # directive for class should not be mapped to a table
    date_created = Column(DateTime, server_default=func.now())
    date_updated = Column(DateTime, server_default=func.now(),
                          onupdate=func.now())
