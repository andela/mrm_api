import os
from fabric.api import local
from fabfile import (user_exists, check_dir,
                     set_up, run_migrations)
from tests.base import BaseTestCase
sys.path.append(os.getcwd())


class AutomationTestCase(BaseTestCase):

    def test_user(self):
        current_user = local("users")
        user = user_exists(current_user)
        self.assertTrue(user)

    def test_check_dir(self):
        count = check_dir()
        self.assertIs(int, type(count))

    def test_set_up(self):
        non_sys_user = "xxx"
        n_run_set = set_up(non_sys_user)
        self.assertEqual(n_run_set, "System user doesnt exist")

    def test_migration(self):
        self.assertTrue(run_migrations())
    
    def test_database_creation_and_existence(self):
        current_user = local('whoami',capture=True)
        test_db = create_database(owner=current_user,name='mrm_db_test')
        db = database_exists("mrm_db_test")
        self.assertTrue(db)
        local('dropdb mrm_db_test')

