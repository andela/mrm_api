import graphene
from graphql import GraphQLError
from api.response.schema import Response
from api.room_resource.models import Resource
from api.room.schema import Room
from api.room.models import Room as RoomModel
from helpers.auth.authentication import Auth
from helpers.pagination.paginate import ListPaginate
from helpers.response.query_response import (
    filter_response_by_date, check_limits,
    filter_rooms_by_responses,
    check_room_instance,
    check_response_and_room
)


class ResponseDetails(graphene.ObjectType):
    response_id = graphene.Int()
    suggestion = graphene.String()
    missing_items = graphene.List(graphene.String)
    created_date = graphene.DateTime()
    rating = graphene.Int()


class RoomResponse(graphene.ObjectType):
    room_id = graphene.Int()
    room_name = graphene.String()
    total_responses = graphene.Int()
    total_room_resources = graphene.Int()
    response = graphene.List(ResponseDetails)


class PaginatedResponses(graphene.ObjectType):
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    responses = graphene.List(RoomResponse)


class Query(graphene.ObjectType):
    room_response = graphene.Field(
        RoomResponse, room_id=graphene.Int())
    all_room_responses = graphene.Field(
        PaginatedResponses,
        page=graphene.Int(),
        per_page=graphene.Int(),
        upper_limit_count=graphene.Int(),
        lower_limit_count=graphene.Int(),
        upper_date_limit=graphene.String(),
        lower_date_limit=graphene.String(),
        room=graphene.String()
    )

    def get_room_response(self, room_response, room_id):
        response = []
        missing_resource = []
        total_room_resources = Resource.query.filter_by(room_id=room_id).count()
        for responses in room_response:
            response_id = responses.id
            suggestion = responses.text_area
            created_date = responses.created_date
            rating = responses.rate
            if len(responses.missing_resources) > 0:
                for resources in responses.missing_resources:
                    resource_name = resources.name
                    missing_resource.append(resource_name)
                response_in_room = ResponseDetails(
                    response_id=response_id,
                    suggestion=suggestion,
                    created_date=created_date,
                    rating=rating,
                    missing_items=missing_resource)
                missing_resource = []
                response.append(response_in_room)
            else:
                missing_items = responses.missing_resources
                response_in_room = ResponseDetails(
                    response_id=response_id,
                    suggestion=suggestion,
                    created_date=created_date,
                    rating=rating,
                    missing_items=missing_items)
                response.append(response_in_room)
        return (response, total_room_resources)

    @Auth.user_roles('Admin')
    def resolve_room_response(self, info, room_id):
        query = Room.get_query(info)
        query_response = Response.get_query(info)
        room = query.filter_by(id=room_id).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        room_response = query_response.filter_by(room_id=room_id)
        responses, total_room_resources = Query.get_room_response(
            self, room_response, room_id)
        total_response = room_response.count()
        room_name = room.name
        return RoomResponse(
            room_name=room_name,
            total_responses=total_response,
            total_room_resources=total_room_resources,
            response=responses)

    def search_response_by_room(self, info, upper_limit, lower_limit, room):
        search_result = []
        filtered_search = []
        if isinstance(upper_limit, int):
            filtered_count_search = check_room_instance(
                    int, filter_rooms_by_responses, upper_limit=upper_limit,
                    lower_limit=lower_limit, room=room, Query=Query, info=info,
                    filtered_search=filtered_search
                )
            if filtered_count_search:
                return filtered_count_search
        filtered_date_search = check_room_instance(
            str, filter_response_by_date, upper_limit=upper_limit,
            lower_limit=lower_limit, room=room, Query=Query, info=info,
            filtered_search=filtered_search
        )
        if filtered_date_search:
            return filtered_date_search
        exact_room = RoomModel.query.filter(
            RoomModel.name.ilike('%' + room + '%')).first()
        if not exact_room:
            raise GraphQLError(
                "No response for this room, enter a valid room name")
        room_response_query = Response.get_query(info).filter_by(
            room_id=exact_room.id)
        room_response = room_response_query.all()
        if not room_response:
            raise GraphQLError("No response for this room at the moment")
        total_response = room_response_query.count()
        all_responses, total_room_resources = Query.get_room_response(
            self, room_response, exact_room.id)
        responses = RoomResponse(
            room_name=exact_room.name,
            total_responses=total_response,
            total_room_resources=total_room_resources,
            response=all_responses
        )
        search_result.append(responses)
        return search_result

    def get_all_reponses(self, info):
        response = []
        rooms = RoomModel.query.all()
        for room in rooms:
            room_name = room.name
            room_response = Response.get_query(info).filter_by(room_id=room.id)
            total_response = room_response.count()
            all_responses, total_room_resources = Query.get_room_response(
                self, room_response, room.id)
            responses = RoomResponse(
                room_id=room.id,
                room_name=room_name,
                total_responses=total_response,
                total_room_resources=total_room_resources,
                response=all_responses)
            response.append(responses)
        return response

    @Auth.user_roles('Admin')
    def resolve_all_room_responses(
        self, info, page=None, per_page=None, lower_limit_count=None,
        upper_limit_count=None, room=None, upper_date_limit=None,
        lower_date_limit=None, **kwargs
    ):
        responses = Query.get_all_reponses(self, info)
        check_limits(lower_limit_count, upper_limit_count, int)
        if (isinstance(upper_limit_count, int)
                and isinstance(lower_limit_count, int)):
            responses = filter_rooms_by_responses(
                Query, info, upper_limit_count, lower_limit_count
            )
        responses = check_response_and_room(
            int, info, room, upper_limit_count,
            lower_limit_count, responses, Query
        )
        if not upper_limit_count and not lower_limit_count and room:
            upper_limit = None
            lower_limit = None
            responses = Query.search_response_by_room(
                self, info, upper_limit, lower_limit, room)
        if page and per_page:
            paginated_response = ListPaginate(
                iterable=responses, per_page=per_page, page=page)
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
        check_limits(lower_date_limit, upper_date_limit, str)
        if (isinstance(upper_date_limit, str)
                and isinstance(lower_date_limit, str)):
            responses = filter_response_by_date(
                Query, info, upper_date_limit, lower_date_limit
            )
        responses = check_response_and_room(
            str, info, room, upper_date_limit,
            lower_date_limit, responses, Query
        )
        return PaginatedResponses(responses=responses)
