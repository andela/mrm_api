from datetime import datetime, timedelta
from graphql import GraphQLError
import pytz

from api.events.models import Events as EventsModel
from api.location.models import Location as LocationModel
from api.role.models import Role as RoleModel
from api.room.models import Room as RoomModel

utc = pytz.utc


def filter_events_by_date_range_in_location(query, start_date, end_date, user):
    """
    Return events that  fall in the date range
    and matches the current_user's location with the events in that
    location and filters to return the events for that location
    but returns all locations for a user with super admin role
    """
    if start_date and not end_date:
        raise GraphQLError("endDate argument missing")
    if end_date and not start_date:
        raise GraphQLError("startDate argument missing")

    if not start_date and not end_date:

        events = query.filter(
                EventsModel.state == 'active'
            ).all()
        return events

    start_date, end_date = format_range_dates(start_date, end_date)

    admin_role = RoleModel.query.filter_by(
            id=user.roles[0].id).first()
    if admin_role.role == 'Super Admin':
        events = query.filter(
            EventsModel.state == 'active',
            EventsModel.start_time >= start_date,
            EventsModel.end_time <= end_date
        ).all()
        return events

    location = LocationModel.query.filter_by(
            name=user.location
            ).first()
    events = query.join(RoomModel).filter(
            EventsModel.state == 'active',
            EventsModel.start_time >= start_date,
            EventsModel.end_time <= end_date,
            RoomModel.location_id == location.id
        ).all()
    return events


def format_range_dates(start_date, end_date):
    """
    Convert dates to date objects and add one day to end_date
    Data from front-end doesn't include time
    """

    start_date = datetime.strptime(start_date, '%b %d %Y')
    end_date = datetime.strptime(end_date, '%b %d %Y')

    if start_date > end_date:
        raise GraphQLError("Start date must be lower than end date")

    start_date = start_date
    end_date = end_date + timedelta(days=1)

    start_date = start_date.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')
    end_date = end_date.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')

    return (start_date, end_date)


def validate_page_and_per_page(page, per_page):
    if page is not None and page < 1:
        raise GraphQLError("page must be at least 1")
    if per_page is not None and per_page < 1:
        raise GraphQLError("perPage must be at least 1")
    if page and not per_page:
        raise GraphQLError("perPage argument missing")
    if per_page and not page:
        raise GraphQLError("page argument missing")
    else:
        return (page, per_page)
