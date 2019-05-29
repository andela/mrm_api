import graphene
from graphql import GraphQLError
from api.response.schema import Response
from api.room.schema import Room
from api.room.models import Room as RoomModel
from helpers.auth.authentication import Auth
from helpers.pagination.paginate import ListPaginate
from helpers.response.query_response import (
    filter_response_by_date, check_limits_are_provided,
    filter_rooms_by_responses,
    validate_responses_by_room,
    check_response_and_room,
    filter_responses,
    filter_by_dates_and_limits
)


class ResponseDetails(graphene.ObjectType):
    response_id = graphene.Int()
    suggestion = graphene.String()
    missing_items = graphene.List(graphene.String)
    created_date = graphene.DateTime()
    rating = graphene.Int()
    resolved = graphene.Boolean()


class RoomResponse(graphene.ObjectType):
    room_id = graphene.Int()
    room_name = graphene.String()
    total_responses = graphene.Int()
    response = graphene.List(ResponseDetails)


class PaginatedResponses(graphene.ObjectType):
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    responses = graphene.List(RoomResponse)


class Query(graphene.ObjectType):
    room_response = graphene.Field(
        RoomResponse, room_id=graphene.Int(),
        description="Returns a list of paginated room responses. Accepts the arguments\
            \n- room_id: Unique identifier of a room")
    all_room_responses = graphene.Field(
        PaginatedResponses,
        page=graphene.Int(),
        per_page=graphene.Int(),
        upper_limit_count=graphene.Int(),
        lower_limit_count=graphene.Int(),
        end_date=graphene.String(),
        start_date=graphene.String(),
        room=graphene.String(),
        description="Returns a list of room responses. Accepts the arguments\
            \n- page: Page number of responses\
            \n- per_page: Number of room responses per page\
            \n- upper_limit_count: Highest number of room responses\
            \n- lower_limit_count: Lowest number of room responses\
             \n- end_date: Latest date range given\
            \n- start_date: Earliest date range given\
            \n- room: Room name where the response is sent to"
    )

    def get_room_response(self, room_response, room_id):
        response = []
        missing_resource = []
        for responses in room_response:
            response_id = responses.id
            suggestion = responses.text_area
            created_date = responses.created_date
            rating = responses.rate
            resolved = responses.resolved
            if len(responses.missing_resources) > 0:
                for resources in responses.missing_resources:
                    resource_name = resources.name
                    missing_resource.append(resource_name)
                response_in_room = ResponseDetails(
                    response_id=response_id,
                    suggestion=suggestion,
                    created_date=created_date,
                    rating=rating,
                    missing_items=missing_resource,
                    resolved=resolved)
                missing_resource = []
                response.append(response_in_room)
            else:
                missing_items = responses.missing_resources
                response_in_room = ResponseDetails(
                    response_id=response_id,
                    suggestion=suggestion,
                    created_date=created_date,
                    rating=rating,
                    missing_items=missing_items,
                    resolved=resolved)
                response.append(response_in_room)
        return (response)

    @Auth.user_roles('Admin')
    def resolve_room_response(self, info, room_id):
        query = Room.get_query(info)
        query_response = Response.get_query(info)
        room = query.filter_by(id=room_id).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        room_response = query_response.filter_by(room_id=room_id)
        responses = Query.get_room_response(
            self, room_response, room_id)
        total_response = room_response.count()
        room_name = room.name
        return RoomResponse(
            room_name=room_name,
            total_responses=total_response,
            response=responses)

    def search_response_by_room(self, info, **kwargs):
        search_result = []
        filtered_search = []
        if isinstance(kwargs.get('upper_limit'), int):
            filtered_count_search = validate_responses_by_room(
                int, filter_rooms_by_responses, **kwargs, Query=Query,
                info=info,
                filtered_search=filtered_search
            )
            if filtered_count_search:
                return filtered_count_search
        filtered_date_search = validate_responses_by_room(
            str, filter_response_by_date, **kwargs, Query=Query,
            info=info,
            filtered_search=filtered_search
        )
        if filtered_date_search:
            return filtered_date_search
        exact_room = RoomModel.query.filter(
            RoomModel.name.ilike('%' + kwargs.get('room') + '%')).first()
        if not exact_room:
            raise GraphQLError(
                "No response for this room, enter a valid room name")
        room_response_query = Response.get_query(info).filter_by(
            room_id=exact_room.id)
        room_response = room_response_query.all()
        if not room_response:
            raise GraphQLError("No response for this room at the moment")
        total_response = room_response_query.count()
        all_responses = Query.get_room_response(
            self, room_response, exact_room.id)
        responses = RoomResponse(
            room_name=exact_room.name,
            total_responses=total_response,
            response=all_responses
        )
        search_result.append(responses)
        return search_result

    def get_all_responses(self, info):
        response = []
        rooms = RoomModel.query.filter(RoomModel.state == "active").all()
        for room in rooms:
            room_name = room.name
            room_response = Response.get_query(info).filter_by(
                room_id=room.id)
            response_count = room_response.count()
            if response_count:
                all_responses = Query.get_room_response(
                    self, room_response, room.id)
                responses = RoomResponse(
                    room_id=room.id,
                    room_name=room_name,
                    total_responses=response_count,
                    response=all_responses)
                response.append(responses)
        return response

    @Auth.user_roles('Admin')
    def resolve_all_room_responses(self, info, **kwargs):
        responses = Query.get_all_responses(self, info)
        check_limits_are_provided(
            kwargs.get('lower_limit_count'),
            kwargs.get('upper_limit_count'), int
        )
        responses = filter_responses(
            int, filter_rooms_by_responses, kwargs.get('upper_limit_count'),
            kwargs.get('lower_limit_count'),  Query, info, responses
        )
        responses = check_response_and_room(
            int, info, kwargs.get('room'), kwargs.get('upper_limit_count'),
            kwargs.get('lower_limit_count'), responses, Query
        )
        if 'upper_limit_count' and 'lower_limit_count' not in kwargs and kwargs.get('room'): # noqa
            upper_limit, lower_limit = (kwargs.get('upper_limit'),
                                        kwargs.get('lower_limit'))
            responses = Query().search_response_by_room(info,
                                                        lower_limit=lower_limit,
                                                        upper_limit=upper_limit,
                                                        **kwargs)
        if kwargs.get('page') and kwargs.get('per_page'):
            paginated_response = ListPaginate(
                iterable=responses, per_page=kwargs.get('per_page'),
                page=kwargs.get('page'))
            current_page = paginated_response.current_page
            has_previous = paginated_response.has_previous
            has_next = paginated_response.has_next
            pages = paginated_response.pages
            query_total = paginated_response.query_total
            return PaginatedResponses(responses=current_page,
                                      has_previous=has_previous,
                                      has_next=has_next,
                                      query_total=query_total,
                                      pages=pages)

        responses = filter_responses(
            str, filter_response_by_date, kwargs.get('end_date'),
            kwargs.get('start_date'),  Query, info, responses
        )
        responses = check_response_and_room(
            str, info, kwargs.get('room'), kwargs.get('end_date'),
            kwargs.get('start_date'), responses, Query
        )
        if kwargs.get('end_date') and kwargs.get('start_date') and kwargs.get(
                'upper_limit_count') and kwargs.get('lower_limit_count'):
            filtered_responses = check_response_and_room(
                str, info, kwargs.get('room'), kwargs.get('end_date'),
                kwargs.get('start_date'), responses, Query
            )
            responses = filter_by_dates_and_limits(
                filtered_responses, kwargs.get('upper_limit_count'),
                kwargs.get('lower_limit_count'))
        return PaginatedResponses(responses=responses)
