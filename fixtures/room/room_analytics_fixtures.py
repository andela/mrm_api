get_least_used_room_per_week_query = '''
    {
        analyticsForRoomLeastUsedPerWeek(
            locationId: 1,
            weekStart: "Sep 8 2018"
            weekEnd: "Sep 15 2018"
        )
        {
            events
        }
    }
'''

get_least_used_room_per_week_response = {
    "data": {
        "analyticsForRoomLeastUsedPerWeek": {
            "events":
            "[{'RoomName': 'Nairobi - 2nd Floor Block A Khartoum (1)', 'count': 5, 'Events in minutes': {'30.0': 1, '25.0': 4}}]"}  # noqa: E501
    }
}

get_least_used_room_without_event_query = '''
    {
        analyticsForRoomLeastUsedPerWeek(
            locationId: 1,
            weekStart: "Aug 8 2018"
            weekEnd: "Aug 12 2018"
        )
        {
            events
        }
    }
'''

get_least_used_room_without_event_response = {
    "data": {
        "analyticsForRoomLeastUsedPerWeek": {
            'events': "[{'RoomName': 'Entebbe', 'has_no_events': True}]"}}
}

most_used_room_per_day_query = '''
{
    mostUsedRoomPerDay(locationId:1, date: "Sep 18 2018") {
        analytics
   }
}
'''

most_used_room_per_day_response = {
    'data': {
        'mostUsedRoomPerDay': {
            'analytics':
            ["{'RoomName': 'Nairobi - 2nd Floor Block A Khartoum (1)', 'count': 2, 'Events in minutes': {'120.0': 1, '25.0': 1}}"]  # noqa: E501
        }
    }
}
