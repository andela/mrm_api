import os
from tests.base import BaseTestCase
from fabric.api import *
from fabfile import (user_exists, check_dir,
                     database_exists, create_database,
                     set_up)
from tests.base import BaseTestCase


class AutomationTestCase(BaseTestCase):

    def test_user(self):
        current_user = local("users")
        user = user_exists(current_user)
        self.assertTrue(user)
    
    def test_check_dir(self):
        count = check_dir()
        self.assertIs(int,type(count))

    
    

