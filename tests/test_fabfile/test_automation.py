import os
from tests.base import BaseTestCase
from fabric.api import *
from fabfile import (user_exists, check_dir,
                     database_exists, create_database,
                     set_up, run_migrations,run_app)
from tests.base import BaseTestCase


class AutomationTestCase(BaseTestCase):

    def test_user(self):
        current_user = local("users")
        user = user_exists(current_user)
        self.assertTrue(user)
    
    def test_check_dir(self):
        count = check_dir()
        self.assertIs(int,type(count))

    def test_set_up(self):
        non_sys_user = "xxx"
        n_run_set = set_up(non_sys_user)
        self.assertEqual(n_run_set,"System user doesnt exist")

    def test_migration(self):
        self.assertTrue(run_migrations())



    
    

