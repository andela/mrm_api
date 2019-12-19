from datetime import datetime, timedelta
from graphql import GraphQLError
import pytz
import inspect
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


def empty_string_checker(string_to_check):
    """Raises a GraphQL error when an empty string is passed

    Args:
        string_to_check: Any string that should not be empty
    """
    frame = inspect.currentframe()
    info_data = inspect.getouterframes(frame, context=1)
    context = info_data[1].code_context[0].strip()
    error_title = context[context.index("(") + 1:context.rindex(")")]
    if not string_to_check:
        raise GraphQLError('{} can not be empty'.format(error_title))


def date_time_format_validator(date_text, time_text):
    """This function validates the date and time format

    Args:
        start_date: Date string of the day of the event:'YY-MM-DD'
        start_time: Time sting of the time of the event: 'HH:MM'
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("start date should be in this format: 'YY-MM-DD'")
    try:
        datetime.strptime(time_text, '%H:%M')
    except ValueError:
        raise ValueError("start time should be in this format: 'HH:MM'")


def calendar_dates_format(start_date, start_time, duration):
    """Converts user date, time and duration input into start_date
        and end_date format that is acceptable by the Google Calendar API

    Args:
        start_date: Date string of the day of the event
        start_time: Time sting of the time of the event
        duration: A float of the duration of the event

    Returns:
        start_date and end_date in this format "%Y-%m-%dT%H:%M:%S".
    """
    empty_string_checker(start_date)
    empty_string_checker(start_time)
    date_time_format_validator(start_date, start_time)
    start_date = start_date + " " + start_time
    start_date = parser.parse(start_date)
    current_date = datetime.now()

    if current_date > start_date:
        raise GraphQLError("Sorry time travel hasn't been invented yet")

    end_date = start_date + timedelta(minutes=duration)

    start_date = start_date.strftime('%Y-%m-%dT%H:%M:%S')
    end_date = end_date.strftime('%Y-%m-%dT%H:%M:%S')

    return (start_date, end_date)


def format_range_time(start_time, end_time):
    """
    Raises a GraphQL error when
    start_time is bigger than end_time
    """
    start_time = datetime.strptime(start_time, '%H:%M:%S')
    end_time = datetime.strptime(end_time, '%H:%M:%S')

    if start_time > end_time:
        raise GraphQLError("Start time must be lower than end time")
    return start_time, end_time


def convert_date(provided_date, provided_time, time_zone):
    date = provided_date + ' ' + provided_time
    new_date = parser.parse(date)
    new_date_format = str(pytz.timezone(time_zone).localize(new_date))
    return new_date_format.replace(new_date_format[10], 'T')


def convert_date_into_user_time(time, requester_time_zone):
    events_time_in_utc = str(datetime.strptime(
        time[:19], "%Y-%m-%dT%H:%M:%S"
    ) + timedelta(hours=int(
        time[-6:20] + time[-4:22]))
    )

    time_zone = pytz.timezone(requester_time_zone)
    user_time = str(datetime.strptime(
        events_time_in_utc, '%Y-%m-%d %H:%M:%S'
    ).replace(tzinfo=pytz.utc).astimezone(time_zone))
    return user_time.replace(" ", "T")
