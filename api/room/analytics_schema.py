import graphene
from graphql import GraphQLError
from helpers.calendar.analytics import RoomAnalytics  # noqa: E501
from helpers.calendar.ratios_and_utilization import RoomAnalyticsRatios
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from api.room.schema import (Room)
from helpers.calendar.analytics import RoomStatistics  # noqa: E501
from api.room.models import Room as RoomModel
from api.room.schema import (RatioOfCheckinsAndCancellations,
                             BookingsAnalyticsCount)
from helpers.pagination.paginate import ListPaginate
from api.room.events_schema import PaginatedEvents


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


class RatiosPerRoom(graphene.ObjectType):
    ratio = graphene.Field(RatioOfCheckinsAndCancellations)
    ratios = graphene.List(RatioOfCheckinsAndCancellations)


class Analytics(graphene.ObjectType):
    analytics = graphene.List(RoomStatistics)
    MeetingsDurationaAnalytics = graphene.List(RoomStatistics)
    has_previous = graphene.Boolean()
    has_next = graphene.Boolean()
    pages = graphene.Int()


class Query(graphene.ObjectType):

    analytics_for_daily_room_events = graphene.Field(
        PaginatedEvents,
        start_date=graphene.String(required=True),
        end_date=graphene.String(required=True),
        page=graphene.Int(),
        per_page=graphene.Int(),
        description="Returns the analytics of daily room events and accepts the arguments\
            \n- start_date: Start date when you want to get analytics from\
            [required]\n- end_date: The end date to take the analytics upto\
            [required]\n- page: Particular page that is returned\
            \n- per_page: The number of analytics per page",
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

    analytics_for_least_used_rooms = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        description="Returns the analytics for the least used rooms and accepts the arguments\
                \n- start_date: Start date when you want to get analytics from\
                [required]\n- end_date: The end date to take the analytics upto"
    )
    analytics_for_most_used_rooms = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        description="Returns the analytics for the most used rooms and accepts the arguments\
                \n- start_date: Start date when you want to get analytics from\
                [required]\n- end_date: The end date to take the analytics upto"
    )

    analytics_for_booked_rooms = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        limit=graphene.Int(),
        criteria=graphene.String(),
        description="Returns the analytics for booked rooms and accepts the arguments\
                \n- start_date: Start date when you want to get analytics from\
                [required]\n- end_date: The end date to take the analytics upto\
                \n- limit: Set limit to get analytics\n- criteria: Set criteria\
                to get analytics"
    )

    analytics_for_meetings_per_room = graphene.Field(
        Analytics,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        description="Returns the analytics of the number of meetings per room \
                and accepts the arguments\n- start_date: When the scheduled  \
                event begins[required]\n- end_date: The end date to take the \
                    analytics upto"
    )

    analytics_ratios = graphene.Field(
        RatioOfCheckinsAndCancellations,
        start_date=graphene.String(required=True),
        end_date=graphene.String(),
        description="Returns the ratios of meetings checkins to cancellations \
                and accepts the arguments\n- start_date: When the scheduled  \
                event begins[required]\n- end_date: The end date to take the  \
                    analytics upto"
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
    def resolve_analytics_for_meetings_durations(
            self,
            info,
            start_date,
            end_date=None,
            per_page=None,
            page=None):
        query = Room.get_query(info)
        results = RoomAnalytics.get_meetings_duration_analytics(
            self,
            query,
            start_date,
            end_date)  # noqa: E501
        if page and per_page:
            paginated_results = ListPaginate(iterable=results, per_page=per_page, page=page)  # noqa: E501
            current_page = paginated_results.current_page
            has_previous = paginated_results.has_previous
            has_next = paginated_results.has_next
            pages = paginated_results.pages
            return Analytics(
                MeetingsDurationaAnalytics=current_page,
                has_previous=has_previous,
                has_next=has_next,
                pages=pages)
        return Analytics(MeetingsDurationaAnalytics=results)

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_ratios(
            self, info, start_date, end_date=None):
        query = Room.get_query(info)
        ratio = RoomAnalyticsRatios.get_analytics_ratios(
            self, query, start_date, end_date)
        return ratio

    @Auth.user_roles('Admin', 'Default User')
    def resolve_analytics_ratios_per_room(self, info, **kwargs):
        room_id = kwargs.get('room_id')
        query = Room.get_query(info)
        ratio = RoomAnalyticsRatios.get_analytics_ratios_per_room(
            self, query, **kwargs)
        if room_id:
            exact_room = query.filter(RoomModel.id == room_id).first()
            if not exact_room:
                raise GraphQLError("Room not found")
            return RatiosPerRoom(ratios=[], ratio=ratio)
        return RatiosPerRoom(ratios=ratio, ratio={})

    @Auth.user_roles('Admin', 'Default User')
    def resolve_bookings_analytics_count(
            self, info, start_date, end_date, room_id=None):
        # Getting booking analytics count
        query = Room.get_query(info)
        analytics = RoomAnalyticsRatios.get_bookings_analytics_count(
            self, query, start_date, end_date, room_id=room_id)
        return analytics

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
