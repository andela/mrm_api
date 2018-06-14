"""This module deals with testing Calendar Integration with focus on
    googleapi credentials
"""
from helpers.calendar.credentials import Credentials
from tests.base import BaseTestCase

import sys
import os
sys.path.append(os.getcwd())


class TestCredentials(BaseTestCase):
    """ This class tests for the google api credentials
    func :
        - test_response_credentails
    """

    def test_response_credentails(self):
        """ This function tests for type of response
        of the response to see if its a googleapi object
        """
        response = Credentials.set_api_credentials(self)
        self.assertEquals(str(type(response)), "<class 'googleapiclient.discovery.Resource'>")  # noqa: E501
