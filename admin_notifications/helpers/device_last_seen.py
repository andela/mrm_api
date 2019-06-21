from datetime import datetime
from api.devices.models import Devices as DevicesModel
from utilities.utility import update_entity_fields
import celery


@celery.task(name='check-device-last-seen')
def notify_when_device_is_offline(**kwargs):
    query = DevicesModel.query
    online_devices = query.filter(DevicesModel.activity == "online").all()
    for device in online_devices:
        device_last_seen = device.last_seen
        current_time = datetime.now()
        duration_offline = current_time - device_last_seen

        if duration_offline.days > 1:
            update_entity_fields(device, activity="offline")
            device.save()
    return online_devices


def notify(**kwargs):
    query = DevicesModel.query
    offline_device = query.filter(DevicesModel.activity == "offline").first()
    if offline_device:
        pass