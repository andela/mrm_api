import graphene
from sqlalchemy import exc
from helpers.auth.authentication import Auth
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.response.models import Response as ResponseModel
from utilities.validations import validate_empty_fields
from graphql import GraphQLError
from api.room.schema import Room
from api.question.models import Question as QuestionModel
from helpers.response.create_response import create_response


class Response(SQLAlchemyObjectType):
    class Meta:
        model = ResponseModel


class ResponseInputs(graphene.InputObjectType):
    question_id = graphene.Int(required=True)
    rate = graphene.Int()
    text_area = graphene.String()
    missing_items = graphene.List(graphene.Int)


class CreateResponse(graphene.Mutation):
    class Arguments:
        responses = graphene.List(
            ResponseInputs, required=True
        )
        room_id = graphene.Int(required=True)

    response = graphene.List(Response)

    def mutate(self, info, **kwargs):
        try:
            validate_empty_fields(**kwargs)
            query = Room.get_query(info)
            responses = []
            errors = []
            room = query.filter_by(id=kwargs['room_id']).first()
            if not room:
                raise GraphQLError("Non-existent room id")
            for each_response in kwargs['responses']:
                question = QuestionModel.query.filter_by(
                    id=each_response.question_id).first()
                if not question:
                    errors.append(
                        "Response to question {} was not saved because it does not exist".format(each_response.question_id)) # noqa
                    continue
                question_type = question.question_type
                each_response['room_id'] = kwargs['room_id']
                responses, errors = create_response(question_type,
                                                    errors,
                                                    responses,
                                                    **each_response)
            if errors:
                raise GraphQLError(
                    ('The following errors occured: {}').format(
                        str(errors).strip('[]'))
                    )
            return CreateResponse(response=responses)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Query(graphene.ObjectType):
    get_room_response = graphene.List(Response, room_id=graphene.Int())

    @Auth.user_roles('Admin')
    def resolve_get_room_response(self, info, **kwargs):
        try:
            query = Response.get_query(info)
            room_feedback = query.filter_by(room_id=kwargs['room_id'])
            if room_feedback.count() < 1:
                raise GraphQLError("No Feedback Found")
            return room_feedback
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Mutation(graphene.ObjectType):
    create_response = CreateResponse.Field()
