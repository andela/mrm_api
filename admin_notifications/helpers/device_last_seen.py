from datetime import datetime
from api.devices.models import Devices as DevicesModel
from utilities.utility import update_entity_fields
import celery


@celery.task(name='check-device-last-seen')
def notify_when_device_is_offline(**kwargs):
    query = DevicesModel.query
    active_devices = query.filter(DevicesModel.activity == "online").all()
    for device in active_devices:
        device_last_seen = device.last_seen
        current_time = datetime.now()
        duration_offline = current_time - device_last_seen

        if duration_offline.days > 1:
            update_entity_fields(device, activity="offline")
            device.save()
    return active_devices
