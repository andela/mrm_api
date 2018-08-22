null = None

room_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, floorId: 1,
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

room_mutation_response = {
    "data": {
        "createRoom": {
            "room": {
                "name": "Mbarara",
                "roomType": "Meeting",
                "capacity": 4,
                "floorId": 1,
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }
        }
    }
}

room_name_empty_mutation = '''
    mutation {
        createRoom(
            name: "", roomType: "Meeting", capacity: 4, floorId: 1,
            officeId: 1
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

room_invalid_officeId_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 1,
            officeId: 10
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

room_invalid_floorId_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 10,
            officeId: 1
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

room_invalid_wingId_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 1,
            wingId: 3
            officeId: 1
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


room_invalid_officeId_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 1,
            officeId: 10
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

room_invalid_floorId_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 10,
            officeId: 1
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

room_invalid_wingId_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 1,
            wingId: 3
            officeId: 1
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


rooms_query = '''
query {
  allRooms{
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
db_rooms_query = '''
    {
    rooms{
                name
                capacity
                roomType
                imageUrl
                }
    }
    '''

db_rooms_query_response = {
    "data": {
        "rooms": [{
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }]
    }
}

query_rooms_response = {
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
