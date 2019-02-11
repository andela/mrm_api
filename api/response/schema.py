import graphene
from helpers.auth.authentication import Auth
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.response.models import Response as ResponseModel
from utilities.validations import validate_empty_fields
from graphql import GraphQLError
from api.room.schema import Room
from api.question.models import Question
from helpers.response.create_response import create_response


class Response(SQLAlchemyObjectType):
    class Meta:
        model = ResponseModel

    question_response_count_in_room = graphene.Int()


class CreateResponse(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        room_id = graphene.Int(required=True)
        rate = graphene.Int()
        text_area = graphene.String()
        missing_items = graphene.List(graphene.Int)

    response = graphene.Field(Response)

    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        query = Room.get_query(info)
        room = query.filter_by(id=kwargs['room_id']).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        get_question = Question.query.filter_by(id=kwargs['question_id']).first() # noqa
        if not get_question:
            raise GraphQLError("Question does not exist")
        question_type = get_question.question_type
        resource = create_response(question_type, **kwargs)
        return CreateResponse(response=resource)


class Query(graphene.ObjectType):
    get_room_response = graphene.List(Response, room_id=graphene.Int())

    @Auth.user_roles('Admin')
    def resolve_get_room_response(self, info, **kwargs):
        query = Response.get_query(info)
        room_feedback = query.filter_by(room_id=kwargs['room_id'])
        if room_feedback.count() < 1:
            raise GraphQLError("No Feedback Found")
        return room_feedback


class Mutation(graphene.ObjectType):
    create_response = CreateResponse.Field()
