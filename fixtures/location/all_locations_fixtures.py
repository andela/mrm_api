all_locations_query = '''
{
    allLocations{
        name
        abbreviation
        rooms {
            name
            roomType
            capacity
            roomTags {
                name
                color
                description
            }
        }
    }
}
'''

expected_query_all_locations = {
    "data": {
        "allLocations": [
            {
                "name": "Kampala",
                "abbreviation": "KLA",
                "rooms": [
                    {
                        "name": "Entebbe",
                        "roomType": "meeting",
                        "capacity": 6,
                        "roomTags": [
                            {
                                "name": "Block-B",
                                "color": "green",
                                "description": "The description"
                            }
                        ]
                    },
                    {
                        "name": "Tana",
                        "roomType": "meeting",
                        "capacity": 14,
                        "roomTags": [
                            {
                                "name": "Block-B",
                                "color": "green",
                                "description": "The description"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Lagos",
                "abbreviation": "LOS",
                "rooms": []
            },
            {
                "name": "Nairobi",
                "abbreviation": "NBO",
                "rooms": []
            }
        ]
    }
}

pass_an_arg_all_locations = '''
    {
        allLocations(locationId: 1){
            name
            id
            abbreviation
        }
    }'''

expected_response_pass_an_arg = {
                                    "errors": [
                                        {
                                        "message": "Unknown argument \"locationId\" on field \"allLocations\" of type \"Query\".",  # noqa: E501
                                        "locations": [
                                            {
                                                "line": 3,
                                                "column": 22
                                                        }
                                                        ]
                                                        }
                                                        ]
                                                        }

all_location_no_hierachy = '''{
    allLocations{
        rooms {
            name
            roomType
            capacity
        }
    }
}'''

expected_all_location_no_hierachy = {
    'data': {'allLocations': [
        {'rooms': [
                {
                    'name': 'Entebbe',
                    'roomType': 'meeting',
                    'capacity': 6
                },
                {
                    'name': 'Tana',
                    'roomType': 'meeting',
                    'capacity': 14
                },
            ]},
        {'rooms': []},
        {'rooms': []}
    ]
    }
}
