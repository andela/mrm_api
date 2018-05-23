from __future__ import with_statement
from fabric.api import *
import fabtools
import fnmatch
import os

def Run_App():
    local("python app.py")

def database_exists(name):
    """
    Check if a PostgreSQL database exists.
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        db = local('''psql -d %(name)s -c ""''' % locals()).succeeded
        return db


def check_dir():
    """
    To check for migrations
    """
    files = os.listdir(path='../mrm_api/alembic/versions/')
    number_migrations = len(fnmatch.filter(files, '*.py'))
    return number_migrations
    


def run_migrations():
    
    """
    To run migrations
    """

    with settings(hide('stdout', 'stderr', 'warnings'),
                  warn_only=True):
        res = check_dir()
        if res == 2:
            local("alembic stamp head")
            local("alembic upgrade head")
        if res==0:
            local("alembic revision --autogenerate")
            local("alembic upgrade head")
        if  res > 2:
            local("alembic stamp head")
            local("alembic upgrade head")
            local("alembic revision --autogenerate")
            local("alembic upgrade head")

            
def run_app():
    """
    To start the app
    """
    with settings(hide('running','stdout', 'warnings'),
                  warn_only=True):
        local("source .env")
        local(" pip install -r requirements.txt")
        local("python manage.py runserver")


def set_up(user):
    u = user_exists(user)
    if u:
        db_exists = database_exists("mrm_db")
        if db_exists:
            run_migrations()
            run_app()
        else:
             create_database(user)
             run_migrations()
             run_app()
    else:
        print("System user doesnt exist")
    


    
