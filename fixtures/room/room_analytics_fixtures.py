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
