import graphene
from graphql import GraphQLError
from helpers.calendar.analytics import RoomAnalytics  # noqa: E501
from helpers.auth.authentication import Auth
from api.room.schema import (PaginatedRooms, Analytics, Calendar, Room)
from helpers.calendar.events import RoomSchedules
from api.room.models import Room as RoomModel


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
    daily_durations_of_meetings = graphene.Field(
        Analytics,
        day_start=graphene.String(),
    )

    monthly_durations_of_meetings = graphene.Field(
        Analytics,
        month=graphene.String(),
        year=graphene.Int(),
    )

    weekly_durations_of_meetings = graphene.Field(
        Analytics,
        week_start=graphene.String(),
        week_end=graphene.String(),
    )

    analytics_for_room_least_used_per_week = graphene.Field(
        Analytics,
        week_start=graphene.String(),
        week_end=graphene.String(),
    )
    analytics_for_room_most_used_per_week = graphene.Field(
        Analytics,
        week_start=graphene.String(),
        week_end=graphene.String(),
    )

    most_used_room_per_month_analytics = graphene.Field(
        Analytics,
        month=graphene.String(),
        year=graphene.Int(),
    )

    analytics_for_meetings_per_room = graphene.Field(
        Analytics,
        day_start=graphene.String(),
        day_end=graphene.String(),
    )

    analytics_for_least_used_room_per_month = graphene.Field(
        Analytics,
        month=graphene.String(),
        year=graphene.Int(),
    )

    analytics_for_least_used_room_per_day = graphene.Field(
        Analytics,
        day=graphene.String(),
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
    def resolve_analytics_for_room_least_used_per_week(self, info, week_start, week_end):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_least_used_room_week(
            self, query, week_start, week_end
        )
        return Analytics(
            analytics=room_analytics
        )

    @Auth.user_roles('Admin')
    def resolve_most_used_room_per_month_analytics(self, info, month, year):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_most_used_room_per_month(
            self, query, month, year)
        return Analytics(
            analytics=room_analytics
        )

    @Auth.user_roles('Admin')
    def resolve_analytics_for_room_most_used_per_week(self, info, week_start, week_end):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_most_used_room_week(
            self, query, week_start, week_end
        )
        room_most_used_per_week = Analytics(
            analytics=room_analytics
        )
        return room_most_used_per_week

    @Auth.user_roles('Admin')
    def resolve_analytics_for_meetings_per_room(self, info, day_start, day_end):  # noqa: E501
        query = Room.get_query(info)
        meeting_summary = RoomAnalytics.get_meetings_per_room(
            self, query, day_start, day_end
        )
        return Analytics(
            analytics=meeting_summary
        )

    @Auth.user_roles('Admin')
    def resolve_daily_durations_of_meetings(self, info, day_start):  # noqa: E501
        query = Room.get_query(info)
        results = RoomAnalytics.get_daily_meetings_details(self, query, day_start)  # noqa: E501
        return Analytics(MeetingsDurationaAnalytics=results)

    @Auth.user_roles('Admin')
    def resolve_monthly_durations_of_meetings(self, info, month, year):  # noqa: E501
        query = Room.get_query(info)
        results = RoomAnalytics.get_meeting_duration_of_room_per_month(self, query, month, year)  # noqa
        return Analytics(MeetingsDurationaAnalytics=results)

    @Auth.user_roles('Admin')
    def resolve_weekly_durations_of_meetings(self, info, week_start, week_end):  # noqa: E501
        query = Room.get_query(info)
        results = RoomAnalytics.get_weekly_meetings_details(self, query, week_start, week_end)  # noqa: E501
        return Analytics(MeetingsDurationaAnalytics=results)

    @Auth.user_roles('Admin')
    def resolve_analytics_for_least_used_room_per_month(self, info, month, year):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_least_used_room_per_month(
            self, query, month, year)
        return Analytics(
            analytics=room_analytics
        )

    @Auth.user_roles('Admin')
    def resolve_analytics_for_least_used_room_per_day(self, info, day):  # noqa: E501
        query = Room.get_query(info)
        room_analytics = RoomAnalytics.get_least_used_room_day(
            self, query, day
        )
        return Analytics(
            analytics=room_analytics
        )
