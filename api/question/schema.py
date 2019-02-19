import graphene
from sqlalchemy import exc
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.question.models import Question as QuestionModel
from utilities.validations import (
    validate_empty_fields,
    validate_date_time_range
    )
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.error_handler import SaveContextManager
from helpers.pagination.paginate import Paginate, validate_page


class Question(SQLAlchemyObjectType):
    class Meta:
        model = QuestionModel

    question_response_count = graphene.Int()

    def resolve_question_response_count(self, info):
        return self.question_response_count


class CreateQuestion(graphene.Mutation):
    class Arguments:
        question_title = graphene.String(required=True)
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
        payload = {
            'model': QuestionModel, 'field': 'question',
            'value':  kwargs['question']
            }
        with SaveContextManager(question, 'Question', payload):
            return CreateQuestion(question=question)


class PaginatedQuestions(Paginate):
    questions = graphene.List(Question)

    def resolve_questions(self, info):
        try:
            page = self.page
            per_page = self.per_page
            query = Question.get_query(info)
            active_questions = query.filter(QuestionModel.state == "active")
            if not page:
                return active_questions.all()
            page = validate_page(page)
            self.query_total = active_questions.count()
            result = active_questions.limit(per_page).offset(page * per_page)
            if result.count() == 0:
                return GraphQLError("No questions found")
            return result
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class UpdateQuestion(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        question_title = graphene.String()
        question_type = graphene.String()
        question = graphene.String()
        start_date = graphene.DateTime()
        end_date = graphene.DateTime()
        is_active = graphene.Boolean()

    question = graphene.Field(Question)

    @Auth.user_roles('Admin')
    def mutate(self, info, question_id, **kwargs):
        try:
            validate_empty_fields(**kwargs)
            query_question = Question.get_query(info)
            active_questions = query_question.filter(
                QuestionModel.state == "active")
            exact_question = active_questions.filter(
                QuestionModel.id == question_id).first()
            if not exact_question:
                raise GraphQLError("Question not found")
            validate_date_time_range(**kwargs)
            update_entity_fields(exact_question, **kwargs)
            exact_question.save()
            return UpdateQuestion(question=exact_question)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class DeleteQuestion(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int(required=True)
        state = graphene.String()

    question = graphene.Field(Question)

    @Auth.user_roles('Admin')
    def mutate(self, info, question_id):
        try:
            query_question = Question.get_query(info)
            active_questions = query_question.filter(
                QuestionModel.state == "active")
            exact_question = active_questions.filter(
                QuestionModel.id == question_id).first()
            if not exact_question:
                raise GraphQLError("Question not found")
            update_entity_fields(exact_question, state="archived")
            exact_question.save()
            return DeleteQuestion(question=exact_question)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class UpdateQuestionViews(graphene.Mutation):
    class Arguments:
        increment_total_views = graphene.Boolean(required=True)

    questions = graphene.List(Question)

    def mutate(self, info, **kwargs):
        query = Question.get_query(info)
        questions = query.all()
        new_total_views = 0
        for question in questions:
            if kwargs['increment_total_views'] and not question.total_views:
                new_total_views = 1
            if kwargs['increment_total_views'] and question.total_views:
                new_total_views = question.total_views + 1
            update_entity_fields(question, total_views=new_total_views)
            question.save()
        return UpdateQuestionViews(questions=questions)


class Query(graphene.ObjectType):
    questions = graphene.Field(
        PaginatedQuestions,
        page=graphene.Int(),
        per_page=graphene.Int(),
    )
    question = graphene.Field(lambda: Question, id=graphene.Int())
    all_questions = graphene.List(Question)

    def resolve_all_questions(self, info):
        query = Question.get_query(info)
        return query.all()

    def resolve_questions(self, info, **kwargs):
        response = PaginatedQuestions(**kwargs)
        return response

    def resolve_question(self, info, id):
        query = Question.get_query(info)
        active_questions = query.filter(QuestionModel.state == "active")
        response = active_questions.filter(QuestionModel.id == id).first()
        if not response:
            raise GraphQLError('Question does not exist')
        return response


class Mutation(graphene.ObjectType):
    create_question = CreateQuestion.Field()
    delete_question = DeleteQuestion.Field()
    update_question = UpdateQuestion.Field()
    update_question_views = UpdateQuestionViews.Field()
