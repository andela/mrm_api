filter_rooms_by_capacity = '''query {
  allRooms(capacity:6){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}
filter_rooms_by_location = '''query {
  allRooms(location:"Kampala"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_location_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

filter_rooms_by_resources = '''query {
  allRooms(resources:"Markers"){
   rooms{
      name
        }
    }
}
    '''
filter_rooms_by_resources_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe"
                }
            ]
        }
    }
}
filter_rooms_by_resources_location_capacity = '''query {
  allRooms(location:"Kampala",capacity:6,resources:"Markers"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_resources_location_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}
filter_rooms_by_non_existant_data = '''query {
  allRooms(location:"kireka",capacity:7,resources:"Mghyt"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_non_existant_data_response = {
    "data": {
        "allRooms": {
            "rooms": []
        }
    }
}
filter_rooms_by_location_capacity = '''query {
  allRooms(location:"Kampala",capacity:6){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_location_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}
filter_rooms_by_resources_capacity_location = '''query {
  allRooms(location:"Kampala",capacity:6,resources:"Markers"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_resources_capacity_location_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}
filter_rooms_by_resources_location = '''query {
  allRooms(location:"Kampala",resources:"Markers"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_resources_location_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

filter_rooms_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

filter_rooms_by_resources_capacity = '''query {
  allRooms(capacity:6,resources:"Markers"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''

filter_rooms_by_resources_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

filter_rooms_by_tag = '''query {
    filterRoomsByTag(tagId: 1){
        id
        name
        }
    }'''

filter_rooms_by_tag_response = {
    "data": {
        "filterRoomsByTag": [
            {
                "id": "1",
                "name": "Entebbe"
            }
        ]
    }
}

filter_rooms_by_invalid_tag = '''query {
    filterRoomsByTag(tagId: 100){
        id
        name
        }
    }'''

filter_rooms_by_invalid_tag_error_response = {
    "errors": [
        {
            "message": "No rooms found with this tag",
            "locations": [
                {
                    "line": 2,
                    "column": 5
                }
            ],
            "path": [
                "filterRoomsByTag"
            ]
        }
    ],
    "data": {
        "filterRoomsByTag": None
    }
}
