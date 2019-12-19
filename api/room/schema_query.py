import graphene
import os
import re
from helpers.calendar.analytics import RoomAnalytics  # noqa: E501
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from api.room.schema import (PaginatedRooms, Calendar, Room)
from helpers.calendar.events import RoomSchedules
from helpers.calendar.analytics import RoomStatistics  # noqa: E501
from api.room.models import Room as RoomModel
from api.room.models import tags
from api.tag.models import Tag
from helpers.auth.user_details import get_user_from_db
from helpers.remote_rooms.remote_rooms_location import (
    map_remote_room_location_to_filter
)
from helpers.calendar.credentials import (get_google_api_calendar_list,
                                          credentials
                                          )
from helpers.events_filter.events_filter import (convert_date,
                                                 validate_date_input,
                                                 format_range_dates,
                                                 format_range_time,
                                                 empty_string_checker
                                                 )
from api.room.schema import (RatioOfCheckinsAndCancellations,
                             BookingsAnalyticsCount)
from api.bugsnag_error import return_error


def resolve_booked_rooms_analytics(*args):
    instance, info, start_date, end_date, criteria, limit = args
    query = Room.get_query(info)
    location_id = admin_roles.user_location_for_analytics_view()
    active_rooms = query.filter(
        RoomModel.state == "active",
        RoomModel.location_id == location_id)
    booked_rooms = get_most_and_least_booked_rooms(
        instance, active_rooms, start_date, end_date, limit, criteria)
    booked_rooms_statistics = Analytics(
        analytics=booked_rooms
    )
    return booked_rooms_statistics


def get_most_and_least_booked_rooms(*args):
    instance, active_rooms, start_date, end_date, criteria, limit = args
    if limit and criteria == "least_booked":
        reversed_order = RoomAnalytics.get_booked_rooms(instance, active_rooms,
                                                        start_date, end_date
                                                        )[::-1]
        return reversed_order[:limit]
    elif limit and criteria == "most_booked":
        return RoomAnalytics.get_booked_rooms(instance, active_rooms,
                                              start_date, end_date
                                              )[:limit]
    else:
        return RoomAnalytics.get_booked_rooms(instance, active_rooms,
                                              start_date, end_date)


class Analytics(graphene.ObjectType):
    analytics = graphene.List(RoomStatistics)
    MeetingsDurationaAnalytics = graphene.List(RoomStatistics)
    has_previous = graphene.Boolean()
    has_next = graphene.Boolean()
    pages = graphene.Int()


class RatiosPerRoom(graphene.ObjectType):
    ratios = graphene.List(RatioOfCheckinsAndCancellations)
    ratio = graphene.Field(RatioOfCheckinsAndCancellations)


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


class CalendarEvent(graphene.ObjectType):
    no_of_participants = graphene.Int()
    event_summary = graphene.String()
    start_time = graphene.String()
    end_time = graphene.String()
    room_name = graphene.String()
    event_id = graphene.String()
    cancelled = graphene.Boolean()
    state = graphene.String()
    checked_in = graphene.Boolean()
    check_in_time = graphene.String()
    meeting_end_time = graphene.String()


class DailyEvents(graphene.ObjectType):
    day = graphene.String()
    events = graphene.List(CalendarEvent)


class PaginatedEvents(graphene.ObjectType):
    """
        Paginated result for daily room events
        analytics
    """
    DailyRoomEvents = graphene.List(DailyEvents)
    has_previous = graphene.Boolean()
    has_next = graphene.Boolean()
    pages = graphene.Int()


class AvailableRooms(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()


class AllAvailableRooms(graphene.ObjectType):
    availableRoom = graphene.List(AvailableRooms)


class Query(graphene.ObjectType):
    """
        Returns paginated rooms
    """
    all_rooms = graphene.Field(
        PaginatedRooms,
        room_labels=graphene.String(),
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
            \n- devices: Devices that are in a room\
            \n- room_labels: Labels to filter the rooms with"
    )
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int(),
        description="Returns a specific room using its id and accepts the argument\
            \n- room_id: A unique identifier of the room"
    )

    filter_rooms_by_tag = graphene.List(
        Room,
        tagId=graphene.Int(),
        description="Returns a list of rooms with a specific tag. Accepts the argument\
           \n- tagId: Unique identifier of a tag")

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

    analytics_for_daily_room_events = graphene.Field(
        PaginatedEvents,
        start_date=graphene.String(required=True),
        end_date=graphene.String(required=True),
        page=graphene.Int(),
        per_page=graphene.Int(),
        description="Returns the analytics of daily room events and accepts the arguments\
            \n- start_date: Start date when you want to get analytics from\
            [required]\n- end_date: The end date to take the analytics upto\
                [required]"

    )

    analytics_for_meetings_durations = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        page=graphene.Int(),
        per_page=graphene.Int(),
        description="Returns the anylytics for meetings durations and accepts the arguments\
            \n- start_date: Start date when you want to get analytics from\
            [required]\n- end_date: The end date to take the analytics upto\
            \n- page: particular room page that is returned\
            \n- per_page: Lower limit responses per page"
    )

    analytics_for_booked_rooms = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        limit=graphene.Int(),
        criteria=graphene.String(),
        description="Returns the analytics for booked rooms and accepts the arguments\
            \n- start_date: Start date when you want to get analytics from\
            [required]\n- end_date: The end date to take the analytics upto"
    )

    analytics_for_meetings_per_room = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        description="Returns the analytics of the number of meetings per room \
            and accepts the arguments\n- start_date: When the scheduled event \
            begins[required]\n- end_date: The end date to take the analytics\
                 upto"
    )

    analytics_ratios = graphene.Field(
        RatioOfCheckinsAndCancellations,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        room_id=graphene.Int(),
        description="Returns the ratios of meetings checkins to cancellations \
            and accepts the arguments\n- start_date: When the scheduled event \
            begins[required]\n- end_date: The end date to take the analytics \
                upto"
    )

    analytics_ratios_per_room = graphene.Field(
        RatiosPerRoom,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        room_id=graphene.Int(),
        description="Returns the ratios per room and accepts the arguments\
            \n- start_date: Start date when you want to get analytics from\
            [required]\n- end_date: The end date to take the analytics upto\
            room_id: Room id which you want to get analytics for"
    )

    bookings_analytics_count = graphene.List(
        BookingsAnalyticsCount,
        start_date=graphene.String(required=True),
        end_date=graphene.String(required=True),
        room_id=graphene.Int(),
        description="Returns the total number of room bookings and accepts the arguments\
            \n- start_date: Start date when you want to get analytics from\
            [required]\n- end_date: The end date to take the analytics upto\
                [required]"
    )

    def check_valid_calendar_id(self, query, calendar_id):
        check_calendar_id = query.filter(
            RoomModel.calendar_id == calendar_id
        ).first()
        if not check_calendar_id:
            return_error.report_errors_bugsnag_and_graphQL("CalendarId given not assigned to any room on converge")  # noqa: E501

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

    @Auth.user_roles('Admin', 'Super Admin')
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
        match = r'\bTest|\bDummy|\btest|\bdummy'
        if os.getenv("APP_SETTINGS") != "production":
            test_rooms = [room for room in remote_rooms
                          if re.search(match, room.name)]
            return AllRemoteRooms(rooms=test_rooms)
        actual_rooms = [room for room in remote_rooms
                        if not re.search(match, room.name)]
        return AllRemoteRooms(rooms=actual_rooms)

    all_available_rooms = graphene.Field(
        AllAvailableRooms,
        start_date=graphene.String(required=True),
        start_time=graphene.String(required=True),
        end_date=graphene.String(required=True),
        end_time=graphene.String(required=True),
        time_zone=graphene.String(required=True),
        description="Returns available rooms in a given period \
            \n- start_time: Start time and date when you want to book room from\
            [required]\n- end_time: time and date you want to book room upto\
                [required]\n time_zone: The time zone of the location\
                    [required]\n location: The location of the office's \
                        room you want to book"
    )

    @Auth.user_roles('Admin', 'Super Admin')
    def resolve_all_available_rooms(self, info, **kwargs):

        time_zone = kwargs['time_zone']
        empty_string_checker(time_zone)
        validate_date_input(kwargs['start_date'], kwargs['end_date'])
        validate_date_input(kwargs['start_time'], kwargs['end_time'])
        format_range_dates(kwargs['start_date'], kwargs['end_date'])
        format_range_time(kwargs['start_time'], kwargs['end_time'])

        start_time = convert_date(kwargs['start_date'],
                                  kwargs['start_time'],
                                  time_zone
                                  )
        end_time = convert_date(kwargs['end_date'],
                                kwargs['end_time'],
                                time_zone
                                )

        # list of all remote rooms in a user's location
        locational_remote_rooms = Query.resolve_all_remote_rooms(
            self, info, return_all=False)
        all_rooms = []
        for room in locational_remote_rooms.rooms:
            all_rooms.append({
                "id": room.calendar_id,
                "name": room.name
            })

        # list of all remote rooms and
        # for each room shows whether it is free or busy in a given period.
        service = credentials.set_api_credentials()
        all_calendars = get_google_api_calendar_list()['items']
        all_remote_rooms = []
        for room in all_calendars:
            free_busy_rooms_request_object = {
                "timeMin": start_time,
                "timeMax": end_time,
                "timeZone": time_zone,
                "items": [
                    {
                        "id": room['id']
                    }
                ]
            }
            res = service.freebusy().query(
                body=free_busy_rooms_request_object
            ).execute()
            all_remote_rooms.append(res[u'calendars'])

        # all busy remote rooms in a given period
        busy_rooms = [key for element in all_remote_rooms for key,
                      value in element.items() if len(value["busy"]) != 0]

        # all available rooms in a user's location in a given period
        available_rooms = [room for room in all_rooms if room[
            'id'
        ] not in busy_rooms]
        all_available_rooms = [AvailableRooms(room['id'],
                                              room['name']
                                              ) for room in available_rooms]

        def raise_no_available_rooms():
            return_error.report_errors_bugsnag_and_graphQL(
                "No available rooms at the moment")

        return AllAvailableRooms(
            availableRoom=all_available_rooms
        ) if available_rooms else raise_no_available_rooms()

    @Auth.user_roles('Admin', 'Super Admin')
    def resolve_filter_rooms_by_tag(self, info, tagId):
        rooms = Room.get_query(info).join(tags).join(
            Tag).filter(tags.c.tag_id == tagId).all()
        if not rooms:
            return_error.report_errors_bugsnag_and_graphQL(
                'No rooms found with this tag')

        return rooms

    def resolve_get_room_by_id(self, info, room_id):
        query = Room.get_query(info)
        check_room = query.filter(
            RoomModel.id == room_id,
            RoomModel.state == "active").first()
        if not check_room:
            return_error.report_errors_bugsnag_and_graphQL("Room not found")
        return check_room

    def resolve_get_room_by_name(self, info, name):
        query = Room.get_query(info)
        if name == "":
            return_error.report_errors_bugsnag_and_graphQL(
                "Please input Room Name")
        check_room_name = list(query.filter(
            RoomModel.name.ilike("%" + name + "%"),  RoomModel.state == "active").all())  # noqa: E501
        if not check_room_name:
            return_error.report_errors_bugsnag_and_graphQL("Room not found")
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
