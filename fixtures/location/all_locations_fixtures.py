
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