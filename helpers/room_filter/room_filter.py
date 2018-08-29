from api.room.models import Room as RoomModel
from api.room_resource.models import Resource
from api.floor.models import Floor
from api.block.models import Block
from api.office.models import Office
from api.location.models import Location
from api.wing.models import Wing


def resource_join_location(query):
    """
    Join resources model upto location model via foreign keys
    :param
        queryset
    :return
        queryset
    """
    query_room = query.join(Resource.room)
    query_floor = query_room.join(Floor)
    query_block = query_floor.join(Block)
    query_office = query_block.join(Office)
    query_location = query_office.join(Location)
    return query_location


def room_join_location(query):
    """
    Join room model upto location model via foreign keys
    :param
        queryset
    :return
        queryset
    """
    query_floor = query.join(Floor.rooms)
    query_block = query_floor.join(Block)
    query_office = query_block.join(Office)
    query_location = query_office.join(Location)
    return query_location


def office_join_location(query):
    query_floor = query.join(Floor.rooms)
    query_block = query_floor.join(Block)
    query_office = query_block.join(Office)
    query_location = query_office.join(Location)
    return query_location


def lagos_office_join_location(query):
    query_block = query.join(Block)
    query_floor = query_block.join(Floor)
    query_wing = query_floor.join(Wing)
    return query_wing


def room_filter(query, filter_data):
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
    elif location and capacity and resources:
        query = resource_join_location(query)
        query = query.filter(RoomModel.capacity == capacity)
        query = query.filter(Resource.name.ilike('%' + resources + '%'))
        return query.filter(Location.name.ilike('%' + location + '%'))
    else:
        return query
