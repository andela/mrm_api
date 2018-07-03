from helpers.database import db_session


def validate_empty_fields(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        if not kwargs.get(field):
            raise AttributeError(field + " is required field")


def validate_country_field(**kwargs):
    """
    Function to validate country fields when
    saving an object
    :params kwargs
    """
    my_args = []
    countries = ['Kenya', 'Uganda', 'Nigeria']
    for value in kwargs:
        country_args = kwargs.get(value)
        my_args.append(country_args)
    if my_args[2] not in countries:
        raise AttributeError("Not a valid country")


def validate_timezone_field(**kwargs):
    """
    Function to validate country fields when
    saving an object
    :params kwargs
    """
    my_args = []
    timezones = ['GMT+3', 'GMT+1']
    for value in kwargs:
        time_zone_args = kwargs.get(value)
        my_args.append(time_zone_args)
    if my_args[3] not in timezones:
        raise AttributeError("Not a valid time zone")


def update_entity_fields(entity, **kwargs):
    """
    Function to update an entities fields
    :param kwargs
    :param entity
    """
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity


class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()
