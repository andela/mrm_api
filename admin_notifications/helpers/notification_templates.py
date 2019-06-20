def event_auto_cancelled_notification(event_name, room_name):
    return {
        "title": "Event Auto cancelled.",
        "message": f"An event {event_name} in {room_name} \
has been auto cancelled."
    }


def room_overbooked_notification(room_name, event_name):
    return {
        "title": f"Room {room_name} is overbooked.",
        "message": f"An event {event_name} in {room_name} \
was booked with more participants than the room can take."
    }
