from __future__ import with_statement
from fabric.api import local, settings, hide
import fnmatch
import os

def Run_Migration():
    local("alembic upgrade head ")
    local("alembic revision --autogenerate ")

def user_exists(name):
    """
    Check if a user exists.
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        res = local('groups %(name)s' % locals()).succeeded
        return res

def prepare_to_host(user):
    InstallDB(user)
    Run_Migration()
    Run_App()
