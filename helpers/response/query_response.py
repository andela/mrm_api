from datetime import datetime
from graphql import GraphQLError
from utilities.validations import validate_date_range


def filter_rooms_by_responses(
    Query, info, upper_limit_count, lower_limit_count
):
    all_responses = Query().get_all_reponses(info)
    filtered_responses = []
    for response in all_responses:
        reponse_count = response.total_responses
        if lower_limit_count <= reponse_count <= upper_limit_count:
            filtered_responses.append(response)
    return filtered_responses


def filter_response_by_date(Query, info, upper_date_limit, lower_date_limit):
    all_responses = Query().get_all_reponses(info)
    filtered_responses = []
    for responses in all_responses:
        for response in responses.response:
            validate_response_dates(
                response,
                upper_date_limit, lower_date_limit, filtered_responses
            )
        setattr(responses, 'response', filtered_responses)
        filtered_responses = []
    return all_responses


def validate_response_dates(
    response, upper_date_limit, lower_date_limit, filtered_responses
):
    upper_date_limit = datetime.strptime(upper_date_limit, '%Y %b %d')
    lower_date_limit = datetime.strptime(lower_date_limit, '%Y %b %d')
    validate_date_range(
        upper_date_limit=upper_date_limit, lower_date_limit=lower_date_limit
    )
    if (response.created_date < upper_date_limit and
            response.created_date > lower_date_limit):
        filtered_responses.append(response)
    return filtered_responses


def check_limits(lower_limit, upper_limit, typ):
    if (
      (isinstance(lower_limit, typ)
          and not isinstance(upper_limit, typ))
      or (isinstance(upper_limit, typ)
            and not isinstance(lower_limit, typ))):
        raise GraphQLError(
            "Provide upper and lower limits to filter")


def check_room_instance(obj, function, **kwargs):
    if ((isinstance(kwargs['upper_limit'], obj)) and kwargs['upper_limit']
            and kwargs['lower_limit']):
        filtered_response = function(
            kwargs['Query'], kwargs['info'], kwargs['upper_limit'],
            kwargs['lower_limit'])
        for room_response in filtered_response:
            if room_response.room_name.lower() == kwargs['room'].lower():
                kwargs['filtered_search'].append(room_response)
        if kwargs['filtered_search']:
            return kwargs['filtered_search']
        else:
            raise GraphQLError(
                "No response for this room at this range")


def check_response_and_room(*args):
    typ, info, room, upper_limit, lower_limit, responses, Query = args
    if (isinstance(upper_limit, typ)
            and isinstance(lower_limit, typ) and room):
        responses = Query().search_response_by_room(
            info, upper_limit, lower_limit, room
        )
    return responses
