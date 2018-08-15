query_nonexistant_location_id = '''{
getRoomsInALocation(locationId:4){
    name
    capacity
    roomType
    imageUrl
    }
}
'''

expected_query_with_nonexistant_id = {
    "data": {
        "getRoomsInALocation": []
    }
}
