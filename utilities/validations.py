import datetime
import validators

from api.location.models import CountryType, TimeZoneType


def validate_url(**kwargs):
    """
    Function to validate url when
    saving an object
    :params kwargs
    """
    if not validators.url(kwargs.get('image_url')):
        raise AttributeError("Please enter a valid image url")


def validate_empty_fields(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        value = kwargs.get(field)
        if not type(value) is bool and not value:
            raise AttributeError(field + " is required field")


def validate_rating_field(**kwargs):
    """
    Function to validate rating fields when
    saving an object
    :params kwargs
    """
    rating = [1, 2, 3, 4, 5]
    if kwargs['rate'] not in rating:
        raise AttributeError("Please rate between 1 and 5")


def validate_date_time_range(**kwargs):
    """
    Function to validate the dates entered
    for questions for feedback
    :params kwargs
    """
    if ('start_date' and 'end_date' in kwargs) and\
            kwargs['start_date'] < datetime.datetime.now():
        raise ValueError('startDate should be today or after')
    elif ('start_date' and 'end_date' in kwargs) and\
            kwargs['end_date'] - kwargs['start_date'] < datetime.timedelta(
                days=1
            ):
        raise ValueError(
            'endDate should be at least a day after startDate'
        )


def validate_missing_items_field(**kwargs):
    """
    Function to validate the missing item field
    when saving a check question response
    :params kwargs
    """
    if 'missing_items' not in kwargs:
        raise AttributeError("Provide the missing items")


def validate_country_field(**kwargs):
    """
    Function to validate country fields when
    saving an object
    :params kwargs
    """
    valid_countries = [country.value for country in CountryType]
    country_name = kwargs['country']
    if country_name not in valid_countries:
        raise AttributeError("Not a valid country")


def validate_timezone_field(**kwargs):
    """
    Function to validate timezone fields when
    saving an object
    :params kwargs
    """
    timezones = [timezone.name for timezone in TimeZoneType]
    time_zone = kwargs['time_zone']
    if time_zone not in timezones:
        raise AttributeError("Not a valid time zone")
