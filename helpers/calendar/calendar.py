from api.room.models import Room


def check_calendar_id(info, calender_id):
    """ Check calendar id. This method is responsible
    for checking if a calendar exists
    :params
    - calendar_id
    - info
    """
    query = Room.get_query(info)
    result = query.filter(
        Room.calendar_id == calendar_id  # noqa: F821
    ).first()
    return result
