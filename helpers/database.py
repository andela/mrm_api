from sqlalchemy import create_engine
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

Base = declarative_base()
Base.query = db_session.query_property()
