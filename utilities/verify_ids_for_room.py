from api.room.models import Room as RoomModel


def get_room_name(room_id):
    exact_room = RoomModel.query.filter_by(id=room_id).first()
    if exact_room:
        room_name = exact_room.name
    else:
        room_name = None
    return room_name
