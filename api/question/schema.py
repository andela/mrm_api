import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.question.models import Question as QuestionModel
from utilities.utility import validate_empty_fields
from helpers.auth.authentication import Auth


class Question(SQLAlchemyObjectType):
    class Meta:
        model = QuestionModel


class CreateQuestion(graphene.Mutation):
    class Arguments:
        question_type = graphene.String(required=True)
        question = graphene.String(required=True)
        start_date = graphene.String(required=True)
        end_date = graphene.String(required=True)
    question = graphene.Field(Question)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        question = QuestionModel(**kwargs)
        question.save()
        return CreateQuestion(question=question)


class Mutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()
