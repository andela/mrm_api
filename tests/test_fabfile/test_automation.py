import os
from tests.base import BaseTestCase
from fabric.api import *
from fabfile import *


class AutomationTestCase(BaseTestCase):

    def test_user(self):
        current_user = local("users")
        user = user_exists(current_user)
        self.assertTrue(user)

    def test_database_existence(self):
        db = database_exists("mrm_test_db")
        self.assertTrue(db)
    
    def test_check_dir(self):
        count = check_dir()
        self.assertIs(int,count)
    

