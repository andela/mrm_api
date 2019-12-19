import graphene
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

from helpers.response.create_response import (
    map_response_type,
    ResponseDetail
)
from api.bugsnag_error import return_error


class RoomResponse(graphene.ObjectType):
    room_id = graphene.Int()
    room_name = graphene.String()
    total_responses = graphene.Int()
    response = graphene.List(ResponseDetail)


class PaginatedResponses(graphene.ObjectType):
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    responses = graphene.List(RoomResponse)


class Query(graphene.ObjectType):
    room_response = graphene.Field(
        RoomResponse,
        room_id=graphene.Int(),
        resolved=graphene.Boolean(),
        description="Returns a list of paginated room responses. Accepts the arguments\
            \n- room_id: Unique identifier of a room\
            \n- resolved: Boolean field to fetch only resolved responses\
                        if true")
    all_room_responses = graphene.Field(
        PaginatedResponses,
        page=graphene.Int(),
        per_page=graphene.Int(),
        upper_limit_count=graphene.Int(),
        lower_limit_count=graphene.Int(),
        end_date=graphene.String(),
        start_date=graphene.String(),
        room=graphene.String(),
        resolved=graphene.Boolean(),
        archived=graphene.Boolean(),
        description="Returns a list of room responses. Accepts the arguments\
            \n- page: Page number of responses\
            \n- per_page: Number of room responses per page\
            \n- upper_limit_count: Highest number of room responses\
            \n- lower_limit_count: Lowest number of room responses\
            \n- end_date: Latest date range given\
            \n- start_date: Earliest date range given\
            \n- room: Room name where the response is sent to\
            \n- resolved: Boolean field to fetch only resolved responses\
                        if true"
    )

    def get_room_response(self, room_response, room_id):
        response_list = []
        for responses in room_response:
            response_id = responses.id
            created_date = responses.created_date
            question_type = responses.question_type
            response = map_response_type(
                question_type.value
            )(responses.response)
            resolved = responses.resolved
            state = responses.state.value
            response_in_room = ResponseDetail(
                id=response_id,
                response=response,
                created_date=created_date,
                question_type=question_type,
                resolved=resolved,
                state=state
            )
            response_list.append(response_in_room)
        return (response_list)

    @Auth.user_roles('Admin', 'Super Admin')
    def resolve_room_response(self, info, room_id, resolved=False):
        query = Room.get_query(info)
        query_response = Response.get_query(info)
        room = query.filter_by(id=room_id).first()
        if not room:
            return_error.report_errors_bugsnag_and_graphQL(
                "Non-existent room id")
        room_response = query_response.filter_by(room_id=room_id)
        if resolved:
            room_response = room_response.filter_by(resolved=True)
        responses = Query.get_room_response(
            self, room_response, room_id)
        total_response = room_response.count()
        room_name = room.name
        return RoomResponse(
            room_id=room_id,
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
            RoomModel.name.ilike('%' + kwargs.get('room') + '%'),
            RoomModel.state == "active").first()
        if not exact_room:
            return_error.report_errors_bugsnag_and_graphQL(
                "No response for this room, enter a valid room name")
        room_response = Response.get_query(info).filter_by(
            room_id=exact_room.id)
        if kwargs.get('resolved'):
            room_response = room_response.filter_by(resolved=True)
        if not room_response:
            return_error.report_errors_bugsnag_and_graphQL(
                "No response for this room at the moment")
        total_response = room_response.count()
        all_responses = Query.get_room_response(
            self, room_response, exact_room.id)
        responses = RoomResponse(
            room_name=exact_room.name,
            total_responses=total_response,
            response=all_responses
        )
        search_result.append(responses)
        return search_result

    def get_all_responses(self, info, resolved=False):
        response = []
        rooms = RoomModel.query.filter(RoomModel.state == "active").all()
        for room in rooms:
            room_name = room.name
            room_response = Response.get_query(
                info
            ).filter_by(room_id=room.id)
            if resolved:
                room_response = room_response.filter_by(resolved=True)
            response_count = room_response.count()
            active_responses = []
            for res in room_response:
                if res.state.value == "active":
                    active_responses.append(res)
            response_count = len(active_responses)
            if response_count:
                all_responses = Query.get_room_response(
                    self, active_responses, room.id)
                responses = RoomResponse(
                    room_id=room.id,
                    room_name=room_name,
                    total_responses=response_count,
                    response=all_responses)
                response.append(responses)
        return response

    def get_all_archived_responses(self, info):
        response = []
        rooms = RoomModel.query.filter(RoomModel.state == "active").all()
        for room in rooms:
            room_name = room.name
            room_response = Response.get_query(
                info
            ).filter_by(room_id=room.id).all()
            archived_responses = []
            for res in room_response:
                if res.state.value == "archived":
                    archived_responses.append(res)
            response_count = len(archived_responses)
            if response_count:
                all_responses = Query.get_room_response(
                    self, archived_responses, room.id)
                responses = RoomResponse(
                    room_id=room.id,
                    room_name=room_name,
                    total_responses=response_count,
                    response=all_responses)
                response.append(responses)
        return response

    @Auth.user_roles('Admin', 'Super Admin')
    def resolve_all_room_responses(self, info, **kwargs):
        responses = Query.get_all_responses(self, info, kwargs.get('resolved'))
        check_limits_are_provided(
            kwargs.get('lower_limit_count'),
            kwargs.get('upper_limit_count'), int
        )
        if 'upper_limit_count' and 'lower_limit_count' not in kwargs and kwargs.get('room'):  # noqa
            upper_limit, lower_limit = (kwargs.get('upper_limit'),
                                        kwargs.get('lower_limit'))
            responses = Query().search_response_by_room(info,
                                                        lower_limit=lower_limit,
                                                        upper_limit=upper_limit,
                                                        **kwargs)
        if kwargs.get('end_date') and kwargs.get('start_date'):
            responses = filter_responses(
                str, filter_response_by_date, kwargs.get('end_date'),
                kwargs.get('start_date'),  Query, info, responses
            )
        if kwargs.get('upper_limit_count') and kwargs.get('lower_limit_count'):
            responses = filter_by_dates_and_limits(
                responses, kwargs.get('upper_limit_count'),
                kwargs.get('lower_limit_count'))
        responses = check_response_and_room(
            str, info, kwargs.get('room'), kwargs.get('end_date'),
            kwargs.get('start_date'), responses, Query
        )
        responses = check_response_and_room(
            int, info, kwargs.get('room'), kwargs.get('upper_limit_count'),
            kwargs.get('lower_limit_count'), responses, Query
        )
        if kwargs.get('archived'):
            responses = Query.get_all_archived_responses(self, info)
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
        return PaginatedResponses(responses=responses)
