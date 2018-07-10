null = None

room_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, floorId: 1,
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",
            location:"Uganda") {  # noqa: E501
            room {
                name
                roomType
                capacity
                floorId
                imageUrl
                location
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
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg" ,
                "location": "Uganda" # noqa: E501
            }
        }
    }
}


rooms_query = '''
    {
    allRooms(location:"Uganda"){
                name
                capacity
                roomType
                imageUrl
                location
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
                location
                }
    }
    '''

db_rooms_query_response = {
    "data": {
        "rooms": [{
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",  
                "location": "Uganda" # noqa: E501
            }]
    }
}

query_rooms_response = {
    "data": {
        "allRooms": [{
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg" ,
                "location": "Uganda" # noqa: E501
            }]
    }
}

room_query_by_id = '''
{
    getRoomById(roomId: 1){
        capacity
        name
        roomType
    }
}
'''

room_query_by_id_response = {
    "data": {
        "getRoomById": {
            "capacity": 6,
            "name": "Entebbe",
            "roomType": "meeting"
        }
    }
}

room_with_non_existant_id = '''{
    getRoomById(roomId: 100) {
        id
        name
    }
}
'''

room_query_with_non_existant_id_response = {
    "errors": [
        {
            "message": "Room not found",
            "locations": [
                {
                    "line": 2,
                    "column": 5
                }
            ]
        }
    ],
    "data": {
        "getRoomById": null
    }
}

room_occupants_query = '''
                        {
                        roomOccupants(
                            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
                            days:7){
                        occupants
                        }
                        }
                        '''
room_schedule_query = '''
                        {
                        roomSchedule(
                            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
                            days:7){
                        events
                        }
                        }
                        '''

room_schedule_query_with_non_existant_calendar_id = '''
                        {
                        roomSchedule(
                            calendarId:"andela.com_38363230343935@resource.calendar.google.com",
                            days:7){
                        events
                        }
                        }
                        '''
room_occupants_query_with_non_existant_calendar_id = '''
                        {
                        roomOccupants(
                            calendarId:"andela.com_38363230343935@resource.calendar.google.com",
                            days:7){
                        occupants
                        }
                        }
                        '''

room_occupants_of_non_existant_calendar_id_response = {
    "errors": [
        {
            "message": "Invalid CalendarId",
            "locations": [
                {
                    "line": 1,
                    "column": 2
                }
            ]
        }
    ],
    "data": {
        "roomSchedule": null
    }
}
room_schedule_of_non_existant_calendar_id_response = {
    "errors": [
        {
            "message": "Invalid CalendarId",
            "locations": [
                {
                    "line": 1,
                    "column": 2
                }
            ]
        }
    ],
    "data": {
        "roomSchedule": null
    }
}
