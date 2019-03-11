all_locations_query = '''
{
    allLocations{
        name
        abbreviation
        structureInfo{
            name
            nodes{
                name
                level
            }
        }
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
                "structureInfo": {
                    "name": "location",
                    "nodes": [
                        {
                            "name": "location",
                            "level": 1,
                        },
                        {
                            "name": "wings",
                            "level": 2
                        }
                    ]
                },
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
                    }
                ]
            },
            {
                "name": "Lagos",
                "abbreviation": "LOS",
                "structureInfo": {
                    "name": "location",

                    "nodes": [
                        {
                            "name": "location",
                            "level": 1,
                        },
                        {
                            "name": "wings",
                            "level": 2
                        }
                    ]
                },
                "rooms": []
            },
            {
                "name": "Nairobi",
                "abbreviation": "NBO",
                "structureInfo": {
                    "name": "location",
                    "nodes": [
                        {
                            "name": "location",
                            "level": 1,
                        },
                        {
                            "name": "wings",
                            "level": 2
                        }
                    ],
                },
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
        {'rooms': [{'name': 'Entebbe',
                    'roomType': 'meeting',
                    'capacity': 6}
                   ]},
        {'rooms': []},
        {'rooms': []}
    ]
    }
}
