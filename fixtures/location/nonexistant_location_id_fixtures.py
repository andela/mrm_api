

query_nonexistant_location_id = '''{
                                getRoomsInALocation(id:4){
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
                                    '''

expected_query_with_nonexistant_id = {
                            "data": {
                                "getRoomsInALocation": []
                            }
                            }