from tests.base import BaseTestCase

from fixtures.location.all_locations_fixtures import (
    all_locations_query,
    expected_query_all_locations,
    pass_an_arg_all_locations,
    expected_response_pass_an_arg,
    all_location_no_hierachy,
    expected_all_location_no_hierachy
)
from fixtures.location.rooms_in_location_fixtures import (
    query_get_rooms_in_location,
    expected_query_get_rooms_in_location
)

from fixtures.location.nonexistant_location_id_fixtures import (
    query_nonexistant_location_id,
    expected_query_with_nonexistant_id
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryLocation(BaseTestCase):
    def test_query_all_locations(self):
        # test if all_location executes in a hierachy
        all_locations = self.client.execute(all_locations_query)
        self.assertEquals(all_locations, expected_query_all_locations)

        # test all_locations query if passed an argument
        query = self.client.execute(pass_an_arg_all_locations)
        self.assertEquals(query, expected_response_pass_an_arg)

        # test all_locations without query being hierachical
        query = self.client.execute(all_location_no_hierachy)
        self.assertEquals(query, expected_all_location_no_hierachy)

    def test_query_rooms_in_a_location(self):
        # test query for rooms in a location in a hierachy
        get_room_in_a_location = self.client.execute(query_get_rooms_in_location)  # noqa: E501
        self.assertEquals(get_room_in_a_location, expected_query_get_rooms_in_location)  # noqa: E501

        # test query rooms in a location with a non existant_id
        query_with_wrong_id = self.client.execute(query_nonexistant_location_id)
        self.assertEquals(query_with_wrong_id, expected_query_with_nonexistant_id)  # noqa: E501
