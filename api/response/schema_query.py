import graphene
from graphql import GraphQLError
from api.response.schema import Response
from api.room_resource.models import Resource
from api.room.schema import Room
from api.room.models import Room as RoomModel
from helpers.auth.authentication import Auth


class ResponseDetails(graphene.ObjectType):
    response_id = graphene.Int()
    suggestion = graphene.String()
    missing_items = graphene.List(graphene.String)
    created_date = graphene.DateTime()
    rating = graphene.Int()


class RoomResponse(graphene.ObjectType):
    room_name = graphene.String()
    total_responses = graphene.Int()
    total_room_resources = graphene.Int()
    response = graphene.List(ResponseDetails)


class AllResponses(graphene.ObjectType):
    responses = graphene.List(RoomResponse)


class Query(graphene.ObjectType):
    room_response = graphene.Field(
        RoomResponse, room_id=graphene.Int())
    all_room_responses = graphene.Field(
        AllResponses,
        filter_by=graphene.String(),
        upper_limit=graphene.Int(),
        lower_limit=graphene.Int()
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
                room_name=room_name,
                total_responses=total_response,
                total_room_resources=total_room_resources,
                response=all_responses)
            response.append(responses)
        return response

    def filter_rooms_by_responses(self, info, upper_limit, lower_limit):
        all_responses = Query.get_all_reponses(self, info)
        filtered_responses = []
        for response in all_responses:
            reponse_count = response.total_responses
            if lower_limit <= reponse_count <= upper_limit:
                filtered_responses.append(response)
        return filtered_responses

    @Auth.user_roles('Admin')
    def resolve_all_room_responses(
            self, info, filter_by=None,
            lower_limit=None, upper_limit=None):
        responses = Query.get_all_reponses(self, info)
        if filter_by == 'Responses':
            if isinstance(lower_limit, int) and isinstance(upper_limit, int):
                responses = Query.filter_rooms_by_responses(
                    self, info, upper_limit, lower_limit
                )
            else:
                raise GraphQLError("lower_limit and upper_limit are \
                required to filter by responses")

        return AllResponses(responses=responses)
