from datetime import datetime
from api.devices.models import Devices as DevicesModel
from utilities.utility import update_entity_fields
from admin_notifications.helpers.create_notification import create_notification
from admin_notifications.helpers.notification_templates import device_offline_notification  # noqa 501
import celery


@celery.task(name='check-device-last-seen')
def notify_when_device_is_offline():
    """Asynchronous method that checks whether a device's last seen is greater\
        than 24hours, turns them to offline and subsequently notify's
    """
    query = DevicesModel.query
    online_devices = query.filter(DevicesModel.activity == "online").all()
    for device in online_devices:
        device_last_seen = device.last_seen
        current_time = datetime.now()
        duration_offline = current_time - device_last_seen

        if duration_offline.days > 1:
            update_entity_fields(device, activity="offline")
            device.save()

            room_name = device.room.name
            room_id = device.room.id
            notification_payload = device_offline_notification(
                room_name, room_id)
            create_notification(title=notification_payload['title'],
                                message=notification_payload['message'],
                                location_id=device.room.location_id)

    return online_devices
