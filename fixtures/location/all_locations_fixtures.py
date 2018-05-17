
all_locations_query = '''
                                    {
                            allLocations{
                                    name
                                    abbreviation
                                    block{
                                        name
                                        floor{
                                                name
                                                room{
                                                    capacity
                                                    name
                                                    roomType
                                                    }
                                             }
                                         }
                                        }
                                    }
                                    '''


expected_query_all_locations = {
                                "data": {
                                    "allLocations": [{
                                            "name": "Uganda",
                                            "abbreviation": "KLA",
                                            "block": [{
                                                    "name": "EC",
                                                    "floor": [{
                                                            "name": "3rd",
                                                            "room": [{
                                                                "capacity": 6,
                                                                "name": "Entebbe",
                                                                "roomType": "meeting"
                                                                    }]
                                                             }]
                                                     }]
                                 }]
                                }
                            }

pass_an_arg_all_locations = '''
                    {
                    allLocations(locationId:1){
                        name
                        id
                        abbreviation
                        block{
                        name
                        id
                        floor{
                            name
                            id
                            room{
                            id
                            name
                            roomType
                            capacity
                            }
                        }
                        }
                    }
                    }'''

expected_response_pass_an_arg = {
                    "errors": [
                        {
                        "message": "Unknown argument \"locationId\" on field \"allLocations\" of type \"Query\".",
                        "locations": [
                            {
                            "line": 3,
                            "column": 34
                            }
                        ]
                        }
                    ]
                    }

all_location_no_hierachy = '''{
                    allLocations{
                            room{
                            id
                            name
                            roomType
                            capacity
                            }
                    }
                    }'''
expected_all_location_no_hierachy = {
                        "errors": [
                            {
                            "message": "Cannot query field \"room\" on type \"Location\".",
                            "locations": [
                                {
                                "line": 3,
                                "column": 29
                                }
                            ]
                            }
                        ]
                        }