import graphene
from helpers.auth.admin_roles import admin_roles
from helpers.calendar.all_analytics_helper import (
    AllAnalyticsHelper, Event, BookingsCount
)
from helpers.calendar.analytics_helper import CommonAnalytics
from helpers.auth.authentication import Auth
from api.room.schema import Room


class ConsolidatedAnalytics(graphene.ObjectType):
    room_name = graphene.String()
    number_of_meetings = graphene.Int()
    bookings_count = graphene.List(BookingsCount)
    cancellations = graphene.Int()
    cancellations_percentage = graphene.Float()
    checkins_percentage = graphene.Float()
    checkins = graphene.Int()
    app_bookings = graphene.Int()
    app_bookings_percentage = graphene.Float()
    percentage_share = graphene.Float()
    period = graphene.Int()
    events = graphene.List(
        Event,
        description='Returns all the events in that room'
    )
    auto_cancellations = graphene.Int()


class AllAnalytics(graphene.ObjectType):
    analytics = graphene.List(ConsolidatedAnalytics)
    bookings = graphene.Int()


class Query(graphene.ObjectType):
    all_analytics = graphene.Field(
        AllAnalytics,
        start_date=graphene.String(),
        end_date=graphene.String(),
        description="Query that returns a list of all analytics")

    @Auth.user_roles('Admin', 'Default User')
    def resolve_all_analytics(self, info, **kwargs):
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        unconverted_dates = {
            'start': start_date,
            'end': end_date
        }
        location_id = admin_roles.user_location_for_analytics_view()
        start_date, end_date = CommonAnalytics.all_analytics_date_validation(
            self, start_date, end_date
        )
        query = Room.get_query(info)
        room_analytics, bookings = AllAnalyticsHelper.get_all_analytics(
            self, query, start_date, end_date, location_id, unconverted_dates)
        analytics = []
        for analytic in room_analytics:
            current_analytic = ConsolidatedAnalytics(
                room_name=analytic['room_name'],
                number_of_meetings=analytic['number_of_meetings'],
                checkins_percentage=analytic['checkins_percentage'],
                bookings_count=analytic['bookings_count'],
                cancellations=analytic['cancellations'],
                checkins=analytic['checkins'],
                cancellations_percentage=analytic['cancellations_percentage'],
                app_bookings=analytic['app_bookings'],
                app_bookings_percentage=analytic['app_bookings_percentage'],
                percentage_share=analytic['percentage_share'],
                events=analytic['room_events'],
                auto_cancellations=analytic['auto_cancellations']
            )
            analytics.append(current_analytic)
        return AllAnalytics(bookings=bookings, analytics=analytics)
