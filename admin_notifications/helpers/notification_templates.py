def event_auto_cancelled_notification(event_name, room_name):
    return {
        "title": "Event Auto cancelled.",
        "message": f"An event {event_name} in {room_name} \
has been auto cancelled."
    }


def underbooked_room_notification(room_name, event_name):
    return {
        "title": f"Room {room_name} is underbooked.",
        "message": f"An event {event_name} in {room_name} \
was booked with less participants than the sufficient room capacity."
    }
