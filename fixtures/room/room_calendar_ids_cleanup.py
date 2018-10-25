null = None

room_calendar_ids_cleanup_query = '''
query {
    validateRoomsCalendarIds{
        response
        rooms
    }
}
'''
room_calendar_ids_cleanup_response_when_all_ids_are_valid = {
    "data": {
        "validateRoomsCalendarIds": {
            "response": "All rooms have valid calendar IDs",
            "rooms": []
        }
    }
}
