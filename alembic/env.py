from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None

import os
import sys


database_url = ''
if os.getenv('APP_SETTINGS') == 'testing':
    database_url = os.getenv('TEST_DATABASE_URL')
elif os.getenv('APP_SETTINGS') == 'development':
    database_url = os.getenv('DEV_DATABASE_URL')
elif os.getenv('APP_SETTINGS') == 'production':
    database_url = os.getenv('DATABASE_URL')

sys.path.append(os.getcwd())
config.set_main_option('sqlalchemy.url', database_url)

from helpers.database import Base
from api.location.models import Location
from api.room.models import Room
from api.room_resource.models import Resource
from api.user.models import User
from api.notification.models import Notification
from api.role.models import Role
from api.devices.models import Devices
from api.events.models import Events
from api.question.models import Question
from api.response.models import Response
from api.tag.models import Tag
from api.structure.models import Structure


target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
