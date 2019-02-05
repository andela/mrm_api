all_locations_query = '''
{
    allLocations{
        name
        abbreviation
        offices{
            name
            blocks {
                name
                floors {
                    name
                    rooms {
                        capacity
                        name
                        roomType
                    }
                }
            }
        }
    }
}
'''


expected_query_all_locations = {
    "data": {
        "allLocations": [{
            "name": "Kampala",
            "abbreviation": "KLA",
            "offices": [
                {
                    "name": "St. catherines",
                    "blocks": [{
                        "name": "Ec",
                        "floors": [{
                            "name": "3rd",
                            "rooms": [{
                                "capacity": 6,
                                "name": "Entebbe",  # noqa: E501
                                "roomType": "meeting"  # noqa: E501
                            }]
                        }]
                    }]
                }
            ]
        },
        {
            "name": "Lagos",
            "abbreviation": "LOS",
            "offices": [
                {
                    "name": "Epic tower",
                    "blocks": [{
                        "name": "Epic Tower",
                        "floors": [{
                            "name": "2nd",
                            "rooms": []
                        }]
                    }]
                }
            ]
        },
        {
            "name": "Nairobi",
            "abbreviation": "NBO",
            "offices": [
                {
                    "name": "Dojo",
                    "blocks": []
                }
                 ]
        },
        ]
    }
}

pass_an_arg_all_locations = '''
    {
        allLocations(locationId: 1){
            name
            id
            abbreviation
            offices {
                blocks {
                    name
                    id
                    floors {
                        name
                        id
                        rooms {
                            id
                            name
                            roomType
                            capacity
                        }
                    }
                }
            }
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
