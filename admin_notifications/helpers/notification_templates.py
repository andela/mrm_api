
def device_offline_notification(room_name, room_id):
    """Notification message when device has been offline for a while"""
    return {
        "title": "Device is offline",
        "message": f"A device in {room_name} roomid:{room_id} is offline."
    }
