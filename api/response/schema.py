import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.response.models import Response as ResponseModel
from utilities.utility import validate_empty_fields, validate_rating_field
from helpers.auth.user_details import get_user_from_db
from graphql import GraphQLError
from api.room.schema import Room
from api.question.models import Question
from helpers.auth.authentication import Auth


class Response(SQLAlchemyObjectType):
    class Meta:
        model = ResponseModel


class CreateRate(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        room_id = graphene.Int(required=True)
        rate = graphene.Int(required=True)
    rating = graphene.Field(Response)

    @Auth.user_roles('Default User')
    def mutate(self, info, **kwargs):
        query = Room.get_query(info)
        room = query.filter_by(id=kwargs['room_id']).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        get_question = Question.query.filter_by(id=kwargs['question_id']).first() # noqa
        if not get_question:
            raise GraphQLError("Question does not exist")
        question_type = get_question.question_type
        if question_type.lower() == 'rate':
            validate_rating_field(**kwargs)
        else:
            raise GraphQLError("Select a rating question")
        user = get_user_from_db()
        rating = ResponseModel(**kwargs, user_id=user.id)
        rating.save()
        return CreateRate(rating=rating)


class CreateCheck(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        room_id = graphene.Int(required=True)
        check = graphene.Boolean(required=True)
    checking = graphene.Field(Response)

    @Auth.user_roles('Default User')
    def mutate(self, info, **kwargs):
        query = Room.get_query(info)
        room = query.filter_by(id=kwargs['room_id']).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        get_question = Question.query.filter_by(id=kwargs['question_id']).first() # noqa
        if not get_question:
            raise GraphQLError("Question does not exist")
        question_type = get_question.question_type
        if question_type.lower() == 'check':
            user = get_user_from_db()
            checking = ResponseModel(**kwargs, user_id=user.id)
            checking.save()
        else:
            raise GraphQLError("Select a check question")
        return CreateCheck(checking=checking)


class CreateSuggestion(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        room_id = graphene.Int(required=True)
        text_area = graphene.String(required=True)
    suggestion = graphene.Field(Response)

    @Auth.user_roles('Default User')
    def mutate(self, info, **kwargs):
        query = Room.get_query(info)
        room = query.filter_by(id=kwargs['room_id']).first()
        if not room:
            raise GraphQLError("Non-existent room id")
        get_question = Question.query.filter_by(id=kwargs['question_id']).first() # noqa
        if not get_question:
            raise GraphQLError("Question does not exist")
        question_type = get_question.question_type
        if question_type.lower() == 'input':
            validate_empty_fields(**kwargs)
            user = get_user_from_db()
            suggestion = ResponseModel(**kwargs, user_id=user.id)
            suggestion.save()
        else:
            raise GraphQLError("Select the correct question")
        return CreateSuggestion(suggestion=suggestion)


class Mutation(graphene.ObjectType):
    create_rate = CreateRate.Field()
    create_check = CreateCheck.Field()
    create_suggestion = CreateSuggestion.Field()
