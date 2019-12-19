import graphene
import pytz
from datetime import datetime, timedelta
import dateutil.parser
from dateutil.relativedelta import relativedelta
from sqlalchemy.sql import text
from helpers.database import db_session
from helpers.calendar.events_sql import room_events_query
from api.room.models import Room as RoomModel
from api.location.models import Location as LocationModel
from helpers.room_filter.room_filter import room_join_location
from helpers.auth.admin_roles import admin_roles
from flask import request
from flask_json import JsonError
from api.events.models import Events as EventsModel
from api.bugsnag_error import return_error


class EventsDuration(graphene.ObjectType):
    duration_in_minutes = graphene.Int()
    number_of_meetings = graphene.Int()


class RoomStatistics(graphene.ObjectType):
    room_name = graphene.String()
    count = graphene.Int()
    meetings = graphene.Int()
    events = graphene.List(EventsDuration)
    has_events = graphene.Boolean()
    total_duration = graphene.Int()
    percentage = graphene.Int()


class CommonAnalytics:

    def get_user_time_zone():
        user_location = admin_roles.user_location_for_analytics_view(
            location_name=True)
        if user_location.lower() in ['lagos', 'nairobi', 'kigali', 'kampala']:
            return 'Africa/' + user_location
        return 'Etc/UTC'

    def convert_dates(self, start_date, end_date):
        """
        Convert date format to UTC and add one day to end_date
        Google calendar is exclusive of end_date
        """
        if end_date is None:
            end_date = start_date
        start_date = datetime.strptime(start_date, '%b %d %Y').astimezone(
            pytz.utc)
        end_date = (datetime.strptime(
            end_date, "%b %d %Y") + relativedelta(days=1)).astimezone(pytz.utc)
        return(start_date, end_date)

    def all_analytics_date_validation(self, start_date, end_date):
        """
        Checks that the start date is not greater than end date
        """
        start_date, end_date = CommonAnalytics.convert_dates(
            self, start_date, end_date
        )
        if start_date > end_date:
            return_error.report_errors_bugsnag_and_graphQL(
                'Earlier date should be lower than later date')
        return (start_date, end_date)

    def validate_current_date(self, start_date, end_date):
        """
        Checks for today's date
        """
        start_date, end_date = CommonAnalytics.convert_dates(
            self, start_date, end_date)

        now = datetime.utcnow().strftime('%b %d %Y')
        date_now = (datetime.strptime(now, "%b %d %Y") + relativedelta(
            days=1)).isoformat() + 'Z'
        user_start_date = dateutil.parser.parse(start_date)
        user_end_date = dateutil.parser.parse(end_date)
        today = dateutil.parser.parse(date_now)
        if user_start_date > today or user_end_date > today:
            return_error.report_errors_bugsnag_and_graphQL(
                "Invalid date. You can not retrieve data beyond today")
        return(start_date, end_date)

    def format_date(date):
        '''
        Convert ISO 8601 date to simple DD/MM/YYYY
        :params
            - date (in ISO format)
        '''
        try:
            result = datetime.strptime(str(date), "%Y-%m-%dT%H:%M:%SZ")
            return result.strftime('%d/%m/%Y')
        except Exception:
            return date

    def get_time_duration_for_event(self, start_time, end_time):
        """ Calculate duration range of an event
         :params
            - start_time
            - end_time
        """
        start_time = dateutil.parser.parse(start_time)
        end_time = dateutil.parser.parse(end_time)
        event_duration = end_time - start_time
        return event_duration.seconds / 60

    def get_room_details(self, query):
        """ Get all room(name, calendar_id, room_id) in a location
         :params
        """
        location_id = admin_roles.user_location_for_analytics_view()
        exact_query = room_join_location(query)
        rooms_in_locations = exact_query.filter(
            LocationModel.id == location_id)
        if not rooms_in_locations.all():
            if 'analytics' in request.url:
                raise JsonError(Message='No rooms in this location')
            else:
                return_error.report_errors_bugsnag_and_graphQL(
                    "No rooms in this location")
        result = [{
            'name': room.name,
            'room_id': room.id,
            'calendar_id': room.calendar_id
        }for room in rooms_in_locations.all()]
        return result

    def get_all_events_in_a_room(self,
                                 room_id,
                                 event_start_time,
                                 event_end_time):
        """ Get all events in a room
         :params
            - room_id - for specific room
            - event_start_time, event_end_time(Time range)
        """
        user_time_zone = CommonAnalytics.get_user_time_zone()
        hour_offset = str(event_start_time.astimezone(pytz.timezone(
            user_time_zone)).utcoffset().total_seconds()/60/60) + 'h'

        events = db_session.query(EventsModel).from_statement(
            text(room_events_query)).params(
            state="active",
            room_id=room_id,
            event_end_time=event_end_time.isoformat(),
            event_start_time=event_start_time.isoformat(),
            hour_offset=hour_offset
        ).all()
        return events

    def get_event_details(self, query, event, room_id):
        """ Filter details of an event
         :params
            - event
        """
        event_details = {}
        rooms_available = CommonAnalytics.get_room_details(
            self, query)
        for room in rooms_available:
            event_details["minutes"] = CommonAnalytics.get_time_duration_for_event(self, event.start_time, event.end_time)  # noqa: E501
            event_details["roomName"] = room['name']
            event_details["summary"] = event.event_title
        return event_details

    @staticmethod
    def get_total_bookings(instance, query, start_date, end_date, room_id=None):
        bookings = 0
        rooms = CommonAnalytics.get_room_details(instance, query)
        active_rooms = RoomModel.query.filter(RoomModel.state == "active")
        for room in rooms:
            if room_id:
                exact_room = active_rooms.filter(
                    RoomModel.id == room_id).first()
                if not exact_room:
                    return_error.report_errors_bugsnag_and_graphQL(
                        "Room Id does not exist")

            bookings = CommonAnalytics.get_bookings_count(instance, room,
                                                          start_date,
                                                          end_date,
                                                          bookings)
        return bookings

    @staticmethod
    def get_bookings_count(*args):
        instance, room, start_date, end_date, bookings_count = args
        all_events = CommonAnalytics.get_all_events_in_a_room(
            instance, room["room_id"], start_date, end_date)
        bookings_count += len(all_events)
        return bookings_count

    @staticmethod
    def get_last_day_of_month(date_obj):
        next_month = date_obj.replace(day=28) + timedelta(days=4)
        end_of_month = next_month - timedelta(days=next_month.day)
        return end_of_month.strftime("%b %d %Y")

    @staticmethod
    def get_list_of_dates(start, number_of_days):
        dates = []
        for num in range(0, number_of_days):
            starting_date = (datetime.strptime(start, "%b %d %Y") + relativedelta(days=num)).isoformat() + 'Z'  # noqa E501
            ending_date = (datetime.strptime(start, "%b %d %Y") + relativedelta(days=num+1)).isoformat() + 'Z'  # noqa E501
            dates.append([starting_date, ending_date])
        return dates

    @staticmethod
    def get_list_of_month_dates(start_date, start_dt, end_date, end_dt):
        dates = []
        diff = relativedelta(end_dt, start_dt)
        number_of_months = 12 * diff.years + diff.months
        month_one_end = CommonAnalytics.get_last_day_of_month(start_dt)
        month_one_end_date = datetime.strptime(month_one_end, '%b %d %Y').isoformat() + 'Z'  # noqa E501
        if diff.days >= 1:
            number_of_months += 1
        dates.append([start_date, month_one_end_date])

        for num in range(1, number_of_months):
            month_start = start_dt.replace(day=1).strftime("%b %d %Y")
            month_start_date = (datetime.strptime(month_start, "%b %d %Y") + relativedelta(months=num)).isoformat() + 'Z'  # noqa E501
            month_end = CommonAnalytics.get_last_day_of_month(dateutil.parser.parse(month_start_date))  # noqa E501
            month_end_date = datetime.strptime(month_end, '%b %d %Y').isoformat() + 'Z'  # noqa E501
            dates.append([month_start_date, month_end_date])

        last_month_start = (end_dt.replace(day=1)).strftime("%b %d %Y")
        last_month_start_date = datetime.strptime(last_month_start, '%b %d %Y').isoformat() + 'Z'  # noqa E501
        booked_dates = [n for n in dates if last_month_start_date in n]
        for last_month in booked_dates:
            dates.remove(last_month)
        dates.append([last_month_start_date, end_date])
        return dates
