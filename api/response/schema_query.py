import graphene
from graphql import GraphQLError
from api.response.schema import Response
from api.response.models import Response as ResponseModel
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
    total_responses = graphene.Int()
    room_name = graphene.String()
    response = graphene.List(ResponseDetails)


class AllResponses(graphene.ObjectType):
    room_name = graphene.String()
    responses = graphene.List(RoomResponse)


class Query(graphene.ObjectType):
    room_response = graphene.Field(
        RoomResponse, room_id=graphene.Int())
    all_room_responses = graphene.Field(AllResponses)

    def get_room_response(self, test_response):
        response = []
        missing_resource = []
        for responses in test_response:
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
        return response

    @Auth.user_roles('Admin')
    def resolve_room_response(self, info, room_id):
        query = Room.get_query(info)
        query_response = Response.get_query(info)
        room = query.filter_by(id=room_id).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        room_response = query_response.filter_by(room_id=room_id)
        responses = Query.get_room_response(self, room_response)
        total_response = room_response.count()
        room_name = room.name
        return RoomResponse(
                room_name=room_name,
                total_responses=total_response,
                response=responses)

    @Auth.user_roles('Admin')
    def resolve_all_room_responses(self, info):
        response = []
        rooms = RoomModel.query.all()
        for room in rooms:
            room_name = room.name
            total_response = ResponseModel.query.filter_by(
                room_id=room.id).count()
            room_response = Response.get_query(info).filter_by(room_id=room.id)
            all_responses = Query.get_room_response(self, room_response)
            responses = RoomResponse(
                room_name=room_name,
                total_responses=total_response,
                response=all_responses)
            response.append(responses)
        return AllResponses(responses=response, room_name=room_name)
