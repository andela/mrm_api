end_event_mutation = '''mutation {
    endEvent(calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
            eventId:"test_id5",
            startTime:"2018-07-10T09:00:00Z",
            endTime:"2018-07-10T09:45:00Z",
            meetingEndTime: "2018-07-10T09:45:00Z"){
            event{
                eventId
                  eventTitle
                checkedIn
                cancelled
                meetingEndTime
                room{
                    id
                    name
                    calendarId
                }
            }
        }
    }
'''

end_unchecked_in_event_mutation = '''mutation {
    endEvent(calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
            eventId:"test_id5",
            startTime:"2018-07-11T09:00:00Z",
            endTime:"2018-07-11T09:45:00Z",
            meetingEndTime: "2018-07-11T09:45:00Z"){
            event{
                eventId
                  eventTitle
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
              meetingEndTime
            }
        }
    }
'''

wrong_calendar_id_end_event_mutation = '''mutation {
    endEvent(calendarId:"invalid_calendar_id",
            eventId:"test_id5",
            startTime:"2018-08-11T09:00:00Z",
            endTime:"2018-08-11T09:45:00Z",
            meetingEndTime: "2018-08-11T09:45:00Z"){
            event{
                eventId
                  eventTitle
                checkedIn
                cancelled
                room{
                    id
                    name
                    calendarId
                }
              meetingEndTime
            }
        }
    }
'''
