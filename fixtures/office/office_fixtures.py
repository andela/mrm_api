get_all_offices_query = '''{
    allOffices {
        id
        name
        locationId
    }
}
'''

get_offices_query_response = {
    "data": {
        "allOffices": [
            {
                "id": "1",
                "name": "EC",
                "locationId": 1
            }
        ]
    }
}

rooms_in_office_query = '''
    {
        getRoomsInAnOffice(officeId:1){
            name
            floors{
                name
                rooms{
                    name
                    capacity
                    roomType
                }
            }
        }
    }
'''


rooms_in_office_query_response = {
    "data": {
        "getRoomsInAnOffice": [
            {
                "name": "EC",
                "floors": [
                    {
                        "name": "3rd",
                        "rooms": [
                            {
                                "name": "Entebbe",
                                "capacity": 6,
                                "roomType": "meeting"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
