from __future__ import with_statement
from fabric.api import *
import fabtools
import fnmatch
import os


def user_exists(name):
    """
    Check if a user exists.
    """
    with settings(hide('running', 'stdout','stderr', 'warnings'), warn_only=True):
        res = local('users %(name)s' % locals()).succeeded
        return res
    
def create_database(owner, name, template='template0', encoding='UTF8',
                    locale='en_US.UTF-8'):
    """
    To create database
    """
    with settings(hide('running', 'stdout','stderr', 'warnings'), warn_only=True):
        local('''createdb --owner %(owner)s --template %(template)s \
                    --encoding=%(encoding)s --lc-ctype=%(locale)s \
                    --lc-collate=%(locale)s %(name)s''' % locals())

def database_exists(name):
    """
    Check if a PostgreSQL database exists.
    """
    with settings(hide('running','stdout', 'stderr', 'warnings'),
                  warn_only=True):
        db = local('''psql -d %(name)s -c ""''' % locals()).succeeded
        print(db)
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
        if res > 0 and res <2:
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
    with settings(hide('stdout', 'stderr', 'warnings'),
                  warn_only=True):
        local(" pip install -r requirements.txt")
        local("python manage.py runserver")

def set_up(user):
    """
    To automate the set process
    """
    u = user_exists(user)
    if u:
        db_exists = database_exists("mrm_db")
        if db_exists:
            run_migrations()
            run_app()
        else:
             create_database(user,"mrm_db")
             run_migrations()
             run_app()
    else:
        print("System user doesnt exist")
    


    
