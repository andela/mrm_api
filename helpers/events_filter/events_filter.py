from datetime import datetime, timedelta
from graphql import GraphQLError
import pytz
from dateutil import parser


utc = pytz.utc


def validate_date_input(start_date, end_date):
    """
    Ensures either both or none of start_date and end_date is supplied
    """
    if start_date and not end_date:
        raise GraphQLError("endDate argument missing")
    if end_date and not start_date:
        raise GraphQLError("startDate argument missing")


def validate_calendar_id_input(calendar_id):
    """
    Ensures that the calendar id is supplied
    """
    if not calendar_id:
        raise GraphQLError("Calendar Id missing")


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


def sort_events_by_date(events):
    events.sort(
        key=lambda x: parser.parse(x.start_time).astimezone(utc),
        reverse=True)
