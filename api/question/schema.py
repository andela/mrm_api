import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.question.models import Question as QuestionModel
from utilities.utility import (
    validate_empty_fields,
    update_entity_fields,
    validate_date_time_range
    )
from helpers.auth.authentication import Auth


class Question(SQLAlchemyObjectType):
    class Meta:
        model = QuestionModel


class CreateQuestion(graphene.Mutation):
    class Arguments:
        question_type = graphene.String(required=True)
        question = graphene.String(required=True)
        start_date = graphene.DateTime(required=True)
        end_date = graphene.DateTime(required=True)
    question = graphene.Field(Question)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        validate_date_time_range(**kwargs)
        question = QuestionModel(**kwargs)
        question.save()
        return CreateQuestion(question=question)


class DeleteQuestion(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
    question = graphene.Field(Question)

    @Auth.user_roles('Admin')
    def mutate(self, info, question_id, **kwargs):
        query_question = Question.get_query(info)
        exact_question = query_question.filter(
            QuestionModel.id == question_id
        ).first()
        if not exact_question:
            raise GraphQLError("Question not found")
        exact_question.delete()
        return DeleteQuestion(question=exact_question)


class UpdateQuestion(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        question_type = graphene.String()
        question = graphene.String()
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()
        is_active = graphene.Boolean()

    question = graphene.Field(Question)

    @Auth.user_roles('Admin')
    def mutate(self, info, question_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_question = Question.get_query(info)
        exact_question = query_question.filter(
            QuestionModel.id == question_id).first()
        if not exact_question:
            raise GraphQLError("Question not found")
        validate_date_time_range(**kwargs)
        update_entity_fields(exact_question, **kwargs)
        exact_question.save()
        return UpdateQuestion(question=exact_question)


class Mutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()
    delete_question = DeleteQuestion.Field()
    update_question = UpdateQuestion.Field()
