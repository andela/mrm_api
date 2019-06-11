from graphql import GraphQLError
from api.devices.models import Devices as DeviceModel
from api.devices.schema import Devices as DeviceSchema


def update_device_last_seen(info, room_id, check_in_time):
    device_query = DeviceSchema.get_query(info)
    device = device_query.filter(
                DeviceModel.room_id == room_id
            ).first()
    if not device:
        raise GraphQLError("Room device not found")
    device.last_seen = check_in_time
    device.save()
