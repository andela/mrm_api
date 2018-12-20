import graphene
from helpers.auth.authentication import Auth
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.response.models import Response as ResponseModel
from utilities.utility import validate_empty_fields, validate_rating_field
from graphql import GraphQLError
from api.room.schema import Room
from api.question.models import Question


class Response(SQLAlchemyObjectType):
    class Meta:
        model = ResponseModel


class CreateResponse(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        room_id = graphene.Int(required=True)
        rate = graphene.Int()
        check = graphene.Boolean()
        text_area = graphene.String()

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
        if question_type.lower() == 'rate':
            if 'rate' not in kwargs:
                raise GraphQLError("Provide a rating response")
            else:
                validate_rating_field(**kwargs)
                rating = ResponseModel(rate=kwargs['rate'],
                                       room_id=kwargs['room_id'],
                                       question_id=kwargs['question_id'])
                rating.save()
                return CreateResponse(response=rating)
        if question_type.lower() == 'check':
            if 'check' not in kwargs:
                raise GraphQLError("Provide a check response")
            checking = ResponseModel(
                check=kwargs['check'],
                room_id=kwargs['room_id'],
                question_id=kwargs['question_id'])
            checking.save()
            return CreateResponse(response=checking)
        if question_type.lower() == 'input':
            if 'text_area' not in kwargs:
                raise GraphQLError("Provide a text response")
            suggestion = ResponseModel(
                text_area=kwargs['text_area'],
                room_id=kwargs['room_id'],
                question_id=kwargs['question_id'])
            suggestion.save()
            return CreateResponse(response=suggestion)


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
