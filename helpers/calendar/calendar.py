from api.room.models import Room as RoomModel


def check_calendar_id(self, info, calender_id):
    """ Check calendar id. This method is responsible
    for checking if a calendar exists
    :params
    - calendar_id
    - info
    """
    query = RoomModel.get_query(info)  # noqa: F821
    result = query.filter(
        RoomModel.calendar_id == calendar_id  # noqa: F821
    ).first()
    return result
