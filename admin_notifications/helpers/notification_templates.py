def event_auto_cancelled_notification(event_name, room_name):
    return {
        "title": "Event Auto cancelled.",
        "message": f"An event {event_name} in {room_name} \
has been auto cancelled."
    }
