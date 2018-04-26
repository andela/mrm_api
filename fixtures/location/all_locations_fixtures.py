
all_locations_query = '''
                                    {
                            allLocations{
                                edges{
                                node{
                                    name
                                    abbreviation
                                    block{
                                    edges{
                                        node{
                                        name
                                        floor{
                                            edges{
                                            node{
                                                name
                                                room{
                                                edges{
                                                    node{
                                                    capacity
                                                    name
                                                    roomType
                                                    }
                                                }
                                                }
                                            }
                                            }
                                        }
                                        }
                                    }
                                    }
                                }
                                }
                            }
                            }
                                    '''


expected_query_all_locations = {
                                "data": {
                                    "allLocations": {
                                    "edges": [
                                        {
                                        "node": {
                                            "name": "Uganda",
                                            "abbreviation": "KLA",
                                            "block": {
                                            "edges": [
                                                {
                                                "node": {
                                                    "name": "EC",
                                                    "floor": {
                                                    "edges": [
                                                        {
                                                        "node": {
                                                            "name": "3rd",
                                                            "room": {
                                                            "edges": [
                                                                {
                                                            "node": {
                                                                "capacity": 6,
                                                                "name": "Entebbe",
                                                                "roomType": "meeting"
                                                            }
                                                            }
                                                            ]
                                                            }
                                                        }
                                                        }
                                                    ]
                                                    }
                                                }
                                                }
                                            ]
                                            }
                                        }
                                    }
                                    ]
                                 }
                                }
                            }