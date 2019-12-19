import graphene
from helpers.auth.admin_roles import admin_roles
from helpers.calendar.all_analytics_helper import (
    AllAnalyticsHelper, Event, BookingsCount, DeviceAnalytics
)
from api.role.schema import Role
from helpers.calendar.analytics_helper import CommonAnalytics
from helpers.auth.authentication import Auth
from api.room.schema import Room
from api.devices.schema import Devices
from utilities.utility import percentage_formater
from helpers.auth.user_details import get_user_from_db
from utilities.validator import verify_location_id


class ConsolidatedAnalytics(graphene.ObjectType):
    room_name = graphene.String()
    number_of_bookings = graphene.Int()
    bookings_percentage_share = graphene.Float()
    events = graphene.List(
        Event,
        description='Returns all the events in that room'
    )
    cancellations = graphene.Int()
    cancellations_percentage = graphene.Float()
    checkins_percentage = graphene.Float()
    checkins = graphene.Int()
    app_bookings = graphene.Int()
    app_bookings_percentage = graphene.Float()
    auto_cancellations = graphene.Int()


class AllAnalytics(graphene.ObjectType):
    analytics = graphene.List(ConsolidatedAnalytics)
    bookings = graphene.Int()
    checkins_percentage = graphene.Float()
    auto_cancellations_percentage = graphene.Float()
    cancellations_percentage = graphene.Float()
    app_bookings_percentage = graphene.Float()
    bookings_count = graphene.List(BookingsCount)
    device_analytics = graphene.List(DeviceAnalytics)


class Query(graphene.ObjectType):
    all_analytics = graphene.Field(
        AllAnalytics,
        start_date=graphene.String(),
        end_date=graphene.String(),
        location_id=graphene.Int(),
        description="Query that returns a list of all analytics")

    @Auth.user_roles('Admin', 'Default User', 'Super Admin')
    def resolve_all_analytics(self, info, **kwargs):
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        location_id = admin_roles.user_location_for_analytics_view()

        admin_details = get_user_from_db()
        query = Role.get_query(info)
        admin_role = query.filter_by(id=admin_details.roles[0].id).first()

        # check that id is valid
        verify_location_id(kwargs)
        if admin_role.role == 'Super Admin' and kwargs.get('location_id', None):
            location_id = kwargs.get('location_id')

        unconverted_dates = {
            'start': start_date,
            'end': end_date,
        }
        start_date, end_date = CommonAnalytics.all_analytics_date_validation(
            self, start_date, end_date
        )
        device_query = Devices.get_query(info)
        device_analytics = AllAnalyticsHelper.get_devices_analytics(
            self,
            device_query
        )
        query = Room.get_query(info)
        room_analytics, bookings, percentages_dict, bookings_count =  \
            AllAnalyticsHelper.get_all_analytics(
                self,
                query,
                start_date=start_date,
                end_date=end_date,
                location_id=location_id,
                unconverted_dates=unconverted_dates
                )
        analytics = []
        for analytic in room_analytics:
            current_analytic = ConsolidatedAnalytics(
                room_name=analytic['room_name'],
                cancellations=analytic['cancellations'],
                cancellations_percentage=analytic['cancellations_percentage'],
                auto_cancellations=analytic['auto_cancellations'],
                number_of_bookings=analytic['number_of_meetings'],
                checkins=analytic['checkins'],
                checkins_percentage=analytic['checkins_percentage'],
                bookings_percentage_share=percentage_formater(
                    analytic['num_of_events'],
                    bookings
                ),
                app_bookings=analytic['app_bookings'],
                app_bookings_percentage=analytic['app_bookings_percentage'],
                events=analytic['room_events'],
            )
            analytics.append(current_analytic)
        device_analytics_list = []
        for device_object in device_analytics:
            device_analytic = DeviceAnalytics(
                device_name=device_object['device_name'],
                device_id=device_object['device_id'],
                down_time=device_object['down_time']
            )
            device_analytics_list.append(device_analytic)
        return AllAnalytics(
            bookings=bookings,
            checkins_percentage=percentage_formater(
                percentages_dict['total_checkins'],
                bookings
            ),
            auto_cancellations_percentage=percentage_formater(
                percentages_dict['total_auto_cancellations'],
                bookings
            ),
            cancellations_percentage=percentage_formater(
                percentages_dict['total_cancellations'],
                bookings
            ),
            app_bookings_percentage=percentage_formater(
                percentages_dict['total_app_bookings'],
                bookings
            ),
            bookings_count=bookings_count,
            analytics=analytics,
            device_analytics=device_analytics_list)
