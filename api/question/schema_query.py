import graphene
from api.response.models import Response as ResponseModel
from api.room.models import Room
from api.question.schema import Question
from helpers.auth.authentication import Auth
from helpers.pagination.paginate import ListPaginate


class ResponsePerRoom(graphene.ObjectType):
    room_name = graphene.String()
    response_count = graphene.Int()
    cleanliness_rating = graphene.Int()


class Responses(graphene.ObjectType):
    total_responses = graphene.Int()
    has_previous = graphene.Boolean()
    has_next = graphene.Boolean()
    pages = graphene.Int()
    responses = graphene.List(ResponsePerRoom)


class Query(graphene.ObjectType):
    all_questions = graphene.List(Question)
    feedback_question = graphene.Field(Responses,
                                       page=graphene.Int(),
                                       per_page=graphene.Int())

    def get_room_response(self, unique_responses, question_id, question_type):
        response = []

        for room in unique_responses:
            room_name = Room.query.filter_by(id=room.room_id).first().name   # noqa: E501
            responses_in_room = ResponseModel.query.filter_by(room_id=room.room_id, question_id=question_id)  # noqa: E501
            response_count = ResponseModel.query.filter_by(room_id=room.room_id).count()  # noqa: E501
            if question_type == "rate":
                average_rating = sum([response.rate for response in responses_in_room]) / responses_in_room.count()  # noqa: E501
                room_response = ResponsePerRoom(room_name=room_name, response_count=response_count, cleanliness_rating=average_rating)  # noqa: E501

            response.append(room_response)
        return response

    @Auth.user_roles('Admin')
    def resolve_feedback_question(self, info, per_page=None, page=None):
        query = Question.get_query(info)
        rate_question = query.filter_by(question_type="rate").all()

        unique_responses = ResponseModel.query.filter_by(question_id=rate_question[0].id).distinct(ResponseModel.room_id).all()  # noqa: E501
        responses = Query.get_room_response(self, unique_responses, rate_question[0].id, rate_question[0].question_type)  # noqa: E501
        total_responses = len(ResponseModel.query.all())  # noqa: E501

        if page and per_page:
            paginated_response = ListPaginate(iterable=responses, per_page=per_page, page=page)  # noqa: E501
            current_page = paginated_response.current_page
            has_previous = paginated_response.has_previous
            has_next = paginated_response.has_next
            pages = paginated_response.pages
            return Responses(responses=current_page,
                             has_previous=has_previous,
                             has_next=has_next,
                             pages=pages,
                             total_responses=total_responses)
        return Responses(responses=responses, total_responses=total_responses)  # noqa: E501

    def resolve_all_questions(self, info):
        query = Question.get_query(info)
        return query.all()
