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


def filter_response_by_date(Query, info, end_date, start_date):
    all_responses = Query().get_all_reponses(info)
    filtered_responses = []
    for responses in all_responses:
        for response in responses.response:
            validate_response_dates(
                response,
                end_date, start_date, filtered_responses
            )
        setattr(responses, 'response', filtered_responses)
        filtered_responses = []
    return all_responses


def validate_response_dates(
    response, end_date, start_date, filtered_responses
):
    end_date = datetime.strptime(end_date, '%Y %b %d')
    start_date = datetime.strptime(start_date, '%Y %b %d')
    validate_date_range(
        end_date=end_date, start_date=start_date
    )
    if (response.created_date < end_date and
            response.created_date > start_date):
        filtered_responses.append(response)
    return filtered_responses


def check_limits_are_provided(lower_limit, upper_limit, typ):
    if (
      (isinstance(lower_limit, typ)
          and not isinstance(upper_limit, typ))
      or (isinstance(upper_limit, typ)
            and not isinstance(lower_limit, typ))):
        raise GraphQLError(
            "Provide upper and lower limits to filter")


def validate_responses_by_room(obj, function, **kwargs):
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


def filter_responses(typ, function, *args,):
    upper_limit, lower_limit, Query, info, responses = args
    if (isinstance(upper_limit, typ)
            and isinstance(lower_limit, typ)):
        responses = function(
            Query, info, upper_limit,
            lower_limit
        )
    return responses
