null = None

room_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, floorId: 2, officeId: 1,
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            roomTags: [1], locationId: 1,
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                id
                name
                roomType
                capacity
                floorId
                locationId
                imageUrl
                roomTags {
                  name
                  description
                }
            }
        }
    }
'''

room_invalid_location_id_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 4,
            officeId: 1,
            locationId: 9,
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                name
                roomType
                capacity
                floorId
                imageUrl
            }
        }
    }
'''

update_fields_mutation = '''mutation{
    updateRoom(roomId: 1, name: "Jinja", capacity: 8,
    roomType: "board room", roomTags: [2]){
        room{
            name
            capacity
            roomType
            roomTags {
                name
                color
            }
        }
    }
}
'''

update_fields_response = {
    "data": {
        "updateRoom": {
            "room": {
                "name": "Jinja",
                "capacity": 8,
                "roomType": "board room",
                "roomTags": [
                    {
                        "name": "Block-C",
                        "color": "blue"
                    }
                ]
            }
        }
    }
}

non_existing_tag_room_update = '''mutation{
    updateRoom(roomId: 1, name: "Jinja", capacity: 8,
    roomType: "board room", roomTags: [8]){
        room{
            name
            capacity
            roomType
        }
    }
}
'''

rooms_query = '''
query {
  allRooms{
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomTags {
          name
          color
      }
        }
    }
}
'''

query_rooms_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "roomTags": [
                        {
                            "name": "Block-B",
                            "color": "green"
                        }
                    ],
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

room_query_by_id = '''
{
    getRoomById(roomId: 1){
        capacity
        name
        roomType
        roomTags {
            name
            color
        }
    }
}
'''

room_query_by_id_response = {
    "data": {
        "getRoomById": {
            "capacity": 6,
            "name": "Entebbe",
            "roomType": "meeting",
            "roomTags": [
                {
                    "name": "Block-B",
                    "color": "green"
                }
            ],
        }
    }
}
