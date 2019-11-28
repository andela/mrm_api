daily_room_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
        DailyRoomEvents {
            day
            events{
                eventSummary
                startTime
                endTime
                roomName
                noOfParticipants
            }
        }
    }
}
'''
daily_room_events_wrong_date_format_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"10 jan 2019", endDate:"jan 10 2019"){
        DailyRoomEvents {
            day
            events {
                noOfParticipants,
                eventSummary,
                startTime,
                endTime,
                roomName,
                eventId
            }
        }
    }
}
'''

paginated_daily_room_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"Jul 11 2018",page:1, perPage:1,
     endDate:"Jul 11 2018"){
        DailyRoomEvents {
            day
            events{
                eventSummary
                startTime
                endTime
                roomName
                noOfParticipants
            }
        }
        pages
        hasNext
        hasPrevious
    }
}'''

invalid_page_for_analytics_for_daily_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"Jul 11 2018",page:1500, perPage:1000,
     endDate:"Jul 11 2018"){
        DailyRoomEvents {
            day
            events{
                eventSummary
                startTime
                endTime
                roomName
                noOfParticipants
            }
        }
        pages
        hasNext
        hasPrevious
    }
}'''  # fetch for invalid page number(non-existing)
