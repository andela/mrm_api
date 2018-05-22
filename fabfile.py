from __future__ import with_statement
from fabric.api import *
import fabtools
import fnmatch


def user_exists(name):
    """
    Check if a user exists.
    """
    with settings(hide('running', 'stdout','stderr', 'warnings'), warn_only=True):
        res = local('groups %(name)s' % locals()).succeeded
        return res
    
def create_database(owner, name='mrm_db', template='template0', encoding='UTF8',
                    locale='en_US.UTF-8'):
    with settings(hide('running', 'stdout','stderr', 'warnings'), warn_only=True):
        local('''createdb --owner %(owner)s --template %(template)s \
                    --encoding=%(encoding)s --lc-ctype=%(locale)s \
                    --lc-collate=%(locale)s %(name)s''' % locals())

def database_exists(name):
    """
    Check if a PostgreSQL database exists.
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        db = local('''psql -d %(name)s -c ""''' % locals()).succeeded
        return db


def run_migrations():
    """
    To run migrations
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        res = local('ls -l ../mrm_api/alembic/versions/| egrep -c "^-"' ,capture=True)
        if int(res) == 2:
           local("alembic stamp head")
           local("alembic upgrade head")
        if int(res)==0:
            local("alembic revision -- autogenerate")
            local("alembic upgrade head")
        if  int(res)>2:
            local("alembic stamp head")
            local("alembic upgrade head")
            local("alembic revision -- autogenerate")
            local("alembic upgrade head")

            
def run_app():
    """
    To start the app
    """
    # local("source .env")
    # local("sudo pip install -r requirements.txt")
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
    


    