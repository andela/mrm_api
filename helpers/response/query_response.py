from datetime import datetime, timedelta
from graphql import GraphQLError
from utilities.validations import validate_date_range


def filter_rooms_by_responses(
    Query, info, upper_limit_count, lower_limit_count
):
    all_responses = Query().get_all_responses(info)
    filtered_responses = []
    for response in all_responses:
        response_count = response.total_responses
        if lower_limit_count <= response_count <= upper_limit_count:
            filtered_responses.append(response)
    return filtered_responses


def filter_by_dates_and_limits(
    filtered_responses, upper_limit_count, lower_limit_count
):
    responses = []
    for response in filtered_responses:
        response_count = response.total_responses
        if lower_limit_count <= response_count <= upper_limit_count:
            responses.append(response)
    return responses


def filter_response_by_date(Query, info, end_date, start_date):
    all_responses = Query().get_all_responses(info)
    end_date = datetime.strptime(end_date, '%b %d %Y')
    start_date = datetime.strptime(start_date, '%b %d %Y')
    validate_date_range(
        end_date=end_date, start_date=start_date
    )
    end_date = end_date + timedelta(days=1)
    filtered_responses = []
    for responses in all_responses:
        for response in responses.response:
            if (response.created_date >= start_date and
                    response.created_date <= end_date):
                filtered_responses.append(response)
            setattr(responses, 'response', filtered_responses)
        filtered_responses = []
    return all_responses


def check_limits_are_provided(lower_limit, upper_limit, data_type):
    if (
        (isinstance(lower_limit, data_type)
         and not isinstance(upper_limit, data_type))
        or (isinstance(upper_limit, data_type)
            and not isinstance(lower_limit, data_type))):
        raise GraphQLError(
            "Provide upper and lower limits to filter")


def validate_responses_by_room(data_type, function, **kwargs):
    if ((isinstance(kwargs['upper_limit'], data_type)) and kwargs['upper_limit']
            and kwargs['lower_limit']):
        filtered_response = function(
            kwargs['Query'], kwargs['info'], kwargs['upper_limit'],
            kwargs['lower_limit'])
        for room_response in filtered_response:
            if (room_response.room_name.lower() == kwargs['room'].lower()
                    and room_response.response):
                kwargs['filtered_search'].append(room_response)
        if kwargs['filtered_search']:
            return kwargs['filtered_search']
        else:
            raise GraphQLError(
                "No response for this room at this range")


def check_response_and_room(*args):
    data_type, info, room, upper_limit, lower_limit, responses, Query = args
    if (isinstance(upper_limit, data_type)
            and isinstance(lower_limit, data_type) and room):
        responses = Query().search_response_by_room(
            info, upper_limit=upper_limit, lower_limit=lower_limit, room=room
        )
    return responses


def filter_responses(data_type, function, *args,):
    upper_limit, lower_limit, Query, info, responses = args
    if (isinstance(upper_limit, data_type)
            and isinstance(lower_limit, data_type)):
        responses = function(
            Query, info, upper_limit,
            lower_limit
        )
    return responses
