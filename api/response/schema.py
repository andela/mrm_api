import graphene
from helpers.auth.authentication import Auth
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.response.models import Response as ResponseModel
from utilities.validations import validate_empty_fields
from graphql import GraphQLError
from api.room.schema import Room
from api.question.models import Question as QuestionModel
from api.question.schema import Question
from helpers.response.create_response import create_response


class Response(SQLAlchemyObjectType):
    class Meta:
        model = ResponseModel


class CreateResponse(graphene.Mutation):
    class Arguments:
        question_id = graphene.List(graphene.Int, required=True)
        room_id = graphene.Int(required=True)
        rate = graphene.Int()
        text_area = graphene.String()
        missing_items = graphene.List(graphene.Int)

    response = graphene.List(Response)

    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        query = Room.get_query(info)
        room = query.filter_by(id=kwargs['room_id']).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        question_ids = kwargs.pop('question_id')
        responses = []
        questions = Question.get_query(info).filter(
            QuestionModel.id.in_(question_ids)).all()
        valid_question_ids = set()
        for question in questions:
            valid_question_ids.add(question.id)
            question_type = question.question_type
            response = create_response(
                question_type, question_id=question.id, **kwargs)
            responses.append(response)
        invalid_question_ids = set(question_ids).difference(
            valid_question_ids)
        if invalid_question_ids:
            raise GraphQLError(
                ('Responses for question ids {} were not saved because '
                    'the questions do not exist').format(
                    str(invalid_question_ids).strip('{}'))
                )
        return CreateResponse(response=responses)


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
