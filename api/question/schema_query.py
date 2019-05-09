import graphene
from api.question.models import Question as QuestionModel
from api.question.schema import Question


class ResponsePerRoom(graphene.ObjectType):
    room_name = graphene.String(description="Name field of the room")
    response_count = graphene.Int(
        description="Number of responses field for the room")
    cleanliness_rating = graphene.Int(
        description="Rating on cleanliness field of the room")


class Responses(graphene.ObjectType):
    total_responses = graphene.Int(
        description="Field having the total number of responses")
    has_previous = graphene.Boolean(
        description="Boolean field for previous page responses")
    has_next = graphene.Boolean(
        description="Boolean field next page responses")
    pages = graphene.Int(description="The pages field of the responses")
    responses = graphene.List(
        ResponsePerRoom,
        description="Foreign field of the responses")


class Query(graphene.ObjectType):
    """
        Query to return questions
    """
    all_questions = graphene.List(
        Question,
        description="Returns a list of all questions")
    feedback_question = graphene.Field(
        Responses,
        page=graphene.Int(),
        per_page=graphene.Int(),
        description="Returns a list of responses and accepts the arguments\
            \n- page: Page number of responses\
            \n- per_page: Number of feedback questions per page")

    def resolve_all_questions(self, info):
        """
            Resolve all questions
        """
        query = Question.get_query(info)
        active_questions = query.filter(QuestionModel.state == "active")
        return active_questions.all()
