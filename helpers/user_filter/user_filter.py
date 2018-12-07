from graphql import GraphQLError

from api.user_role.models import UsersRole
from api.location.models import Location as LocationModel


def user_filter(query, filter_data):
    """
    Filters for users by given specifics and
    returns all users if no specific is passed
    :param
        query
        filter_data
    :return
        List of users
    """
    location = filter_data.get('location_id', None)
    role = filter_data.get('role_id', None)

    if location and not role:
        return filter_by_location(query, location)
    elif role and not location:
        return filter_by_role(query, role)
    elif all([location, role]):
        query = filter_by_location(query, location)
        return filter_by_role(query, role)
    else:
        return query


def filter_by_location(query, location):
    get_location = LocationModel.query.filter_by(id=location).first()
    if not get_location:
        raise GraphQLError("No users found")
    return query.filter_by(location=get_location.name)


def filter_by_role(query, role):
    query = query.join(UsersRole)
    return query.filter_by(role_id=role)
