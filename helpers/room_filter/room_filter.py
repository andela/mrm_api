from api.room.models import Room as RoomModel
from api.room_resource.models import Resource
from api.location.models import Location
from api.room.models import Room
from sqlalchemy import String, func, cast


def resource_join_location(query):
    """
    Join resources model upto location model via foreign keys
    :param
        queryset
    :return
        queryset
    """
    query_room = query.join(Resource.room)
    query_location = query_room.join(Location)
    return query_location


def room_join_location(query):
    """
    Join room model upto location model via foreign keys
    :param
        queryset
    :return
        queryset
    """
    query_location = query.join(Location.rooms)
    return query_location


def location_join_room():
    location_query = Location.query.join(Room)
    return location_query


def location_join_resources():
    location_query = Location.query.join(Room).join(Resource)
    return location_query


def room_filter(query, filter_data):  # noqa: ignore=C901
    """
    Filters for rooms by given specifics and
    returns all rooms if no specific is passed
    :param
        query
        **kwargs
    :return
        List of rooms
    """
    location = filter_data.pop("location", None)
    capacity = filter_data.pop("capacity", None)
    resources = filter_data.pop("resources", None)
    room_labels = filter_data.get("room_labels")

    if location and not (resources or capacity):
        query = room_join_location(query)
        return query.filter(Location.name.ilike('%' + location + '%'))
    elif capacity and not (resources or location):
        return query.filter(RoomModel.capacity == capacity)
    elif resources and not (capacity or location):
        query = query.join(Resource.room)
        return query.filter(Resource.name.ilike('%' + resources + '%'))
    elif (resources and capacity) and not location:
        query = query.join(Resource.room)
        query = query.filter(RoomModel.capacity == capacity)
        return query.filter(Resource.name.ilike('%' + resources + '%'))
    elif (capacity and location) and not resources:
        query = room_join_location(query)
        query = query.filter(RoomModel.capacity == capacity)
        return query.filter(Location.name.ilike('%' + location + '%'))
    elif (location and resources) and not capacity:
        query = resource_join_location(query)
        query = query.filter(Resource.name.ilike('%' + resources + '%'))
        return query.filter(Location.name.ilike('%' + location + '%'))
    elif (location and capacity and resources):
        query = resource_join_location(query)
        query = query.filter(RoomModel.capacity == capacity)
        query = query.filter(Resource.name.ilike('%' + resources + '%'))
        return query.filter(Location.name.ilike('%' + location + '%'))
    elif room_labels:
        room_labels = room_labels.split(",")
        for room_label in room_labels:
            query = query.filter(func.lower(
                cast(RoomModel.room_labels, String)).contains(
                    room_label.lower().strip()))
        return query
    else:
        return query
