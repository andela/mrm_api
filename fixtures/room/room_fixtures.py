null = None

room_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, floorId: 1,
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
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


rooms_query = '''
    {
    allRooms{
                name
                capacity
                roomType
                imageUrl
                }
    }
    '''
query_rooms_response = {
    "data": {
        "allRooms": [{
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
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


room_query_by_nonexistant_id = '''{
    getRoomById(roomId: 100) {
        id
        name
    }
}
'''

room_query_by_nonexistant_id_response = {
    "errors": [{
        "message": "Room not found",
        "locations": [{
                "line": 2,
                "column": 5
            }
        ]
    }],
    "data": {
        "getRoomById": null
    }
}

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

room_schedule_of_non_existant_calendar_id_response = {
                                        "errors": [
                                            {
                                                "message": "CalendarId given not assigned to any room on converge",  # noqa: E501
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
