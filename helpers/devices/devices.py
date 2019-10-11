from graphql import GraphQLError
from api.devices.models import Devices as DeviceModel
from api.devices.schema import Devices as DeviceSchema


def update_device_last_activity(info, room_id, activity_time, activity):
    device_query = DeviceSchema.get_query(info)
    device = device_query.filter(
                DeviceModel.room_id == room_id
            ).first()
    if not device:
        raise GraphQLError("Room device not found")
    device.last_seen = activity_time
    device.last_activity = activity
    device.save()
