
import graphene
from graphql import GraphQLError
from helpers.auth.authentication import Auth
from api.room.schema import (PaginatedRooms, Calendar, Room)
from helpers.calendar.events import RoomSchedules
from api.room.models import Room as RoomModel
from helpers.auth.user_details import get_user_from_db
from helpers.remote_rooms.remote_rooms_location import (
    map_remote_room_location_to_filter
)
from helpers.calendar.credentials import get_google_api_calendar_list


class RemoteRoom(graphene.ObjectType):
    """
        Get remote room
    """
    calendar_id = graphene.String()
    name = graphene.String()


class AllRemoteRooms(graphene.ObjectType):
    """
        Get all remote rooms
    """
    rooms = graphene.List(RemoteRoom)


class Query(graphene.ObjectType):
    """
        Returns paginated rooms
    """
    all_rooms = graphene.Field(
        PaginatedRooms,
        page=graphene.Int(),
        per_page=graphene.Int(),
        capacity=graphene.Int(),
        resources=graphene.String(),
        location=graphene.String(),
        office=graphene.String(),
        devices=graphene.String(),
        description="Returns a list of paginated rooms. Accepts the arguments\
            \n- page: particular room page that is returned\
            \n- per_page: Lower limit responses per page\
            \n- capacity: number of users that a room can hold\
            \n- resources: Resuources found in the room\
            \n- location: Location of the room\
            \n- office: Office where the room is found\
            \n- devices: Devices that are in a room"
    )
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int(),
        description="Returns a specific room using its id and accepts the argument\
            \n- room_id: A unique identifier of the room"
    )

    all_remote_rooms = graphene.Field(
        AllRemoteRooms,
        description="Returns a list of all remote rooms",
        return_all=graphene.Boolean()
    )

    get_room_by_name = graphene.List(
        Room,
        name=graphene.String(),
        description="Returns a specific room by its name and takes the argument\
            \n- name: Name of the room"
    )

    room_schedule = graphene.Field(
        Calendar,
        calendar_id=graphene.String(),
        days=graphene.Int(),
        description="Returns the schedule of a room and accepts the arguments\
            \n- calender_id: Unique identifier of the calendar\
            \n- days: Number of days that the room has a schedule"
    )
    room_occupants = graphene.Field(
        Calendar,
        calendar_id=graphene.String(),
        days=graphene.Int(),
        description="Returns the room's occupants in an event and accepts the arguments\
            \n- calender_id: Unique identifier of the calendar\
            \n- days: Number of days that the room has a schedule"
    )

    def check_valid_calendar_id(self, query, calendar_id):
        check_calendar_id = query.filter(
            RoomModel.calendar_id == calendar_id
        ).first()
        if not check_calendar_id:
            raise GraphQLError("CalendarId given not assigned to any room on converge")  # noqa: E501

    def room_occupants_room_schedule(self, info, calender_id, days):
        query = Room.get_query(info)
        Query.check_valid_calendar_id(self, query, calender_id)
        resource = RoomSchedules.get_room_schedules(
            self,
            calender_id,
            days)
        return resource

    def resolve_all_rooms(self, info, **kwargs):
        response = PaginatedRooms(**kwargs)
        return response

    @Auth.user_roles('Admin')
    def resolve_all_remote_rooms(self, info, return_all=None):
        page_token = None
        filter = map_remote_room_location_to_filter()
        location = 'all' if return_all else get_user_from_db().location
        remote_rooms = []
        while True:
            calendar_list = get_google_api_calendar_list(pageToken=page_token)
            for room_object in calendar_list['items']:
                if 'andela.com' in room_object['id'] and room_object['id'].endswith(  # noqa
                    'resource.calendar.google.com') and filter.get(location)(
                        room_object[
                            'summary'
                        ]):
                    calendar_id = room_object['id']
                    room_name = room_object['summary']
                    remote_room = RemoteRoom(
                        calendar_id=calendar_id,
                        name=room_name)
                    remote_rooms.append(remote_room)
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
        return AllRemoteRooms(rooms=remote_rooms)

    def resolve_get_room_by_id(self, info, room_id):
        query = Room.get_query(info)
        check_room = query.filter(RoomModel.id == room_id).first()
        if not check_room:
            raise GraphQLError("Room not found")
        return check_room

    def resolve_get_room_by_name(self, info, name):
        query = Room.get_query(info)
        if name == "":
            raise GraphQLError("Please input Room Name")
        check_room_name = list(query.filter(RoomModel.name.ilike("%" + name + "%")).all())   # noqa: E501
        if not check_room_name:
            raise GraphQLError("Room not found")
        return check_room_name

    def resolve_room_occupants(self, info, calendar_id, days):
        resource = Query.room_occupants_room_schedule(self, info, calendar_id, days)  # noqa: E501
        return Calendar(
            occupants=resource[0]
        )

    def resolve_room_schedule(self, info, calendar_id, days):
        resource = Query.room_occupants_room_schedule(self, info, calendar_id, days)  # noqa: E501
        return Calendar(
            events=resource[1]
        )
