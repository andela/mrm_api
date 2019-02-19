import graphene
from graphql import GraphQLError
from helpers.calendar.analytics import RoomAnalytics  # noqa: E501
from helpers.calendar.ratios_and_utilization import RoomAnalyticsRatios
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from api.room.schema import (PaginatedRooms, Calendar, Room)
from helpers.calendar.events import RoomSchedules
from helpers.calendar.analytics import RoomStatistics  # noqa: E501
from api.room.models import Room as RoomModel
from api.room.schema import (RatioOfCheckinsAndCancellations,
                             BookingsAnalyticsCount)
from helpers.pagination.paginate import ListPaginate
from helpers.calendar.analytics_helper import CommonAnalytics
from helpers.calendar.credentials import get_google_api_calendar_list


def resolve_booked_rooms_analytics(*args):
    instance, info, start_date, end_date, criteria, limit = args
    query = Room.get_query(info)
    location_id = admin_roles.user_location_for_analytics_view()
    active_rooms = query.filter(
        RoomModel.state == "active",
        RoomModel.location_id == location_id)
    booked_rooms = get_most_and_least_booked_rooms(
        instance, active_rooms, start_date, end_date, limit, criteria)
    rooms_booked_per_week = Analytics(
        analytics=booked_rooms
    )
    return rooms_booked_per_week


def get_most_and_least_booked_rooms(*args):
    instance, active_rooms, start_date, end_date, criteria, limit = args
    if limit and criteria == "least_booked":
        limit = (-limit)
        return RoomAnalytics.get_booked_rooms(instance, active_rooms,
                                              start_date, end_date
                                              )[limit:]
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


class RemoteRoom(graphene.ObjectType):
    calendar_id = graphene.String()
    name = graphene.String()


class AllRemoteRooms(graphene.ObjectType):
    rooms = graphene.List(RemoteRoom)


class CalendarEvent(graphene.ObjectType):
    no_of_participants = graphene.Int()
    event_summary = graphene.String()
    start_time = graphene.String()
    end_time = graphene.String()
    room_name = graphene.String()
    event_id = graphene.String()


class DailyEvents(graphene.ObjectType):
    day = graphene.String()
    events = graphene.List(CalendarEvent)


class Query(graphene.ObjectType):
    all_rooms = graphene.Field(
        PaginatedRooms,
        page=graphene.Int(),
        per_page=graphene.Int(),
        capacity=graphene.Int(),
        resources=graphene.String(),
        location=graphene.String(),
        office=graphene.String(),
        devices=graphene.String()
    )
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int()
    )

    all_remote_rooms = graphene.Field(AllRemoteRooms)

    get_room_by_name = graphene.List(
        Room,
        name=graphene.String()
    )

    room_schedule = graphene.Field(
        Calendar,
        calendar_id=graphene.String(),
        days=graphene.Int(),
    )
    room_occupants = graphene.Field(
        Calendar,
        calendar_id=graphene.String(),
        days=graphene.Int(),
    )

    analytics_for_daily_room_events = graphene.Field(
        graphene.List(DailyEvents),
        start_date=graphene.String(required=True),
        end_date=graphene.String(required=True)

    )

    analytics_for_meetings_durations = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        page=graphene.Int(),
        per_page=graphene.Int(),
    )

    analytics_for_least_used_rooms = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
    )
    analytics_for_most_used_rooms = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
    )

    analytics_for_booked_rooms = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        limit=graphene.Int(),
        criteria=graphene.String(),
    )

    analytics_for_meetings_per_room = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
    )

    analytics_ratios = graphene.Field(
        RatioOfCheckinsAndCancellations,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
    )

    analytics_ratios_per_room = graphene.Field(
        RatiosPerRoom,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
    )

    bookings_analytics_count = graphene.List(
        BookingsAnalyticsCount,
        start_date=graphene.String(required=True),
        end_date=graphene.String(required=True),
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
    def resolve_all_remote_rooms(self, info):
        page_token = None
        remote_rooms = []
        while True:
            calendar_list = get_google_api_calendar_list(pageToken=page_token)
            for room_object in calendar_list['items']:
                if 'andela.com' in room_object['id'] and room_object['id'].endswith('resource.calendar.google.com'):  # noqa
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

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_for_least_used_rooms(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_least_used_rooms_analytics(
            self, query, start_date, end_date
        )
        return Analytics(
            analytics=room_analytics
        )

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_for_most_used_rooms(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_most_used_rooms_analytics(
            self, query, start_date, end_date
        )
        room_most_used_per_week = Analytics(
            analytics=room_analytics
        )
        return room_most_used_per_week

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_for_meetings_per_room(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        meeting_summary = RoomAnalytics.get_meetings_per_room_analytics(
            self, query, start_date, end_date
        )
        return Analytics(
            analytics=meeting_summary
        )

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_for_meetings_durations(self, info, start_date, end_date=None, per_page=None, page=None):  # noqa: E501
        query = Room.get_query(info)
        results = RoomAnalytics.get_meetings_duration_analytics(self, query, start_date, end_date)  # noqa: E501
        if page and per_page:
            paginated_results = ListPaginate(iterable=results, per_page=per_page, page=page)  # noqa: E501
            current_page = paginated_results.current_page
            has_previous = paginated_results.has_previous
            has_next = paginated_results.has_next
            pages = paginated_results.pages
            return Analytics(MeetingsDurationaAnalytics=current_page, has_previous=has_previous, has_next=has_next, pages=pages)  # noqa: E501
        return Analytics(MeetingsDurationaAnalytics=results)

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_ratios(
            self, info, start_date, end_date=None):
        query = Room.get_query(info)
        ratio = RoomAnalyticsRatios.get_analytics_ratios(
            self, query, start_date, end_date)
        return ratio

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_ratios_per_room(
            self, info, start_date, end_date=None):
        query = Room.get_query(info)
        ratio = RoomAnalyticsRatios.get_analytics_ratios_per_room(
            self, query, start_date, end_date)
        return RatiosPerRoom(ratio)

    @Auth.user_roles('Admin', 'Default User')
    def resolve_bookings_analytics_count(
            self, info, start_date, end_date):
        query = Room.get_query(info)
        analytics = RoomAnalyticsRatios.get_bookings_analytics_count(
            self, query, start_date, end_date)
        return analytics

    def resolve_analytics_for_daily_room_events(self, info,
                                                start_date, end_date
                                                ):
        start_date, end_date = CommonAnalytics().convert_dates(
            start_date, end_date
        )
        query = Room.get_query(info)
        all_events, all_dates = RoomSchedules().get_all_room_schedules(
            query, start_date, end_date
        )
        all_days_events = []
        for date in set(all_dates):
            daily_events = []
            for event in all_events:
                if date == event["date_of_event"]:
                    current_event = CalendarEvent(
                        no_of_participants=event["no_of_participants"],
                        event_summary=event["event_summary"],
                        start_time=event["start_time"],
                        end_time=event["end_time"],
                        room_name=event["room_name"],
                        event_id=event["event_id"]
                    )
                    daily_events.append(current_event)
            all_days_events.append(
                DailyEvents(
                    day=date,
                    events=daily_events
                )
            )

        return all_days_events

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_for_booked_rooms(self, info, **kwargs):
        start_date, criteria, end_date, limit = (
            kwargs.get('start_date', ''),
            kwargs.get('criteria', None),
            kwargs.get('end_date', None),
            kwargs.get('limit', None)
        )
        return resolve_booked_rooms_analytics(
            self, info, start_date, end_date, limit, criteria)
