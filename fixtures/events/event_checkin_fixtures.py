event_checkin_mutation = '''mutation {
    eventCheckin(
        calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_id5", eventTitle:"Onboarding", numberOfParticipants: 4,
        startTime:"2018-07-10T09:00:00Z",
        endTime:"2018-07-10T09:45:00Z",
        checkInTime:"2018-07-10T09:00:00Z"){
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

event_checkin_response = {
    "data": {
        "eventCheckin": {
            "event": {
                "eventId": "test_id5",
                "roomId": 1,
                "checkedIn": True,
                "cancelled": False,
                "room": {
                    "id": "1",
                    "name": "Entebbe",
                    "calendarId": "andela.com_3630363835303531343031@resource.calendar.google.com"  # noqa
                }
            }
        }
    }
}

event_2_checkin_mutation = '''mutation {
    eventCheckin(
        calendarId:"andela.com_3730313534393638323232@resource.calendar.google.com",
        eventId:"test_id6", eventTitle:"Onboarding 2", numberOfParticipants: 4,
        startTime:"2019-07-10T09:00:00Z",
        endTime:"2018-07-10T09:45:00Z",
        checkInTime:"2018-07-10T09:00:00Z"){
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

wrong_calendar_id_checkin_mutation = '''mutation {
    eventCheckin(
        calendarId:"fake_calendar_id",
        eventId:"test_id5", eventTitle:"Onboarding", numberOfParticipants: 4,
        startTime:"2018-07-10T09:00:00Z",
        endTime:"2018-07-10T09:45:00Z"){
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

cancel_event_mutation = '''
    mutation {
        cancelEvent(
        calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_id5", eventTitle:"Onboarding", numberOfParticipants: 4,
        startTime:"2018-07-10T09:00:00Z",
        endTime:"2018-07-10T09:45:00Z")
        {
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

cancel_event_respone = "Event cancelled but email not sent"

cancel_event_invalid_start_time = '''
    mutation {
        cancelEvent(
        calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_id5", eventTitle:"Onboarding", numberOfParticipants: 4,
        startTime:"invalid",
        endTime:"2018-07-10T09:45:00Z")
        {
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

checkin_mutation_for_event_existing_in_db = '''mutation {
    eventCheckin(
        calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
        eventId:"test_id5", eventTitle:"Onboarding", numberOfParticipants: 4,
        startTime:"2018-07-11T09:00:00Z",
        endTime:"2018-07-11T09:45:00Z"){
            event{
                eventId
                roomId
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

response_for_event_existing_in_db_checkin = {
    "data": {
        "eventCheckin": {
            "event": {
                "eventId": "test_id5",
                "roomId": 1,
                "checkedIn": True,
                "cancelled": False,
                "room": {
                    "id": "1",
                    "name": "Entebbe",
                    "calendarId": "andela.com_3630363835303531343031@resource.calendar.google.com"  # noqa
                }
            }
        }
    }
}
