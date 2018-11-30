import graphene
from graphql import GraphQLError
from helpers.calendar.analytics import RoomAnalytics  # noqa: E501
from helpers.calendar.ratios_and_utilization import RoomAnalyticsRatios
from helpers.auth.authentication import Auth
from api.room.schema import (PaginatedRooms, Calendar, Room)
from helpers.calendar.events import RoomSchedules
from helpers.calendar.analytics import RoomStatistics  # noqa: E501
from api.room.models import Room as RoomModel
from api.room.schema import RatioOfCheckinsAndCancellations
from helpers.pagination.paginate import ListPaginate


class Analytics(graphene.ObjectType):
    analytics = graphene.List(RoomStatistics)
    MeetingsDurationaAnalytics = graphene.List(RoomStatistics)
    has_previous = graphene.Boolean()
    has_next = graphene.Boolean()
    pages = graphene.Int()


class RatiosPerRoom(graphene.ObjectType):
    ratios = graphene.List(RatioOfCheckinsAndCancellations)


class Query(graphene.ObjectType):
    all_rooms = graphene.Field(
        PaginatedRooms,
        page=graphene.Int(),
        per_page=graphene.Int(),
        capacity=graphene.Int(),
        resources=graphene.String(),
        location=graphene.String(),
        office=graphene.String()
    )
    get_room_by_id = graphene.Field(
        Room,
        room_id=graphene.Int()
    )

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

    def check_valid_calendar_id(self, query, calendar_id):
        check_calendar_id = query.filter(
            RoomModel.calendar_id == calendar_id
        ).first()
        if not check_calendar_id:
            raise GraphQLError("CalendarId given not assigned to any room on converge")  # noqa: E501

    def resolve_all_rooms(self, info, **kwargs):
        response = PaginatedRooms(**kwargs)
        return response

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
        query = Room.get_query(info)
        Query.check_valid_calendar_id(self, query, calendar_id)
        room_occupants = RoomSchedules.get_room_schedules(
            self,
            calendar_id,
            days)
        return Calendar(
            occupants=room_occupants[0]
        )

    def resolve_room_schedule(self, info, calendar_id, days):
        query = Room.get_query(info)
        Query.check_valid_calendar_id(self, query, calendar_id)
        room_schedule = RoomSchedules.get_room_schedules(
            self,
            calendar_id,
            days)
        return Calendar(
            events=room_schedule[1]
        )

    @Auth.user_roles('Admin')
    def resolve_analytics_for_least_used_rooms(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_least_used_rooms_analytics(
            self, query, start_date, end_date
        )
        return Analytics(
            analytics=room_analytics
        )

    @Auth.user_roles('Admin')
    def resolve_analytics_for_most_used_rooms(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_most_used_rooms_analytics(
            self, query, start_date, end_date
        )
        room_most_used_per_week = Analytics(
            analytics=room_analytics
        )
        return room_most_used_per_week

    @Auth.user_roles('Admin')
    def resolve_analytics_for_meetings_per_room(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        meeting_summary = RoomAnalytics.get_meetings_per_room_analytics(
            self, query, start_date, end_date
        )
        return Analytics(
            analytics=meeting_summary
        )

    @Auth.user_roles('Admin')
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

    @Auth.user_roles('Admin')
    def resolve_analytics_ratios(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        ratio = RoomAnalyticsRatios.get_analytics_ratios(
            self, query, start_date, end_date)
        return ratio

    @Auth.user_roles('Admin')
    def resolve_analytics_ratios_per_room(self, info, start_date, end_date=None):  # noqa: E501
        query = Room.get_query(info)
        ratio = RoomAnalyticsRatios.get_analytics_ratios_per_room(
            self, query, start_date, end_date)
        return RatiosPerRoom(ratio)
