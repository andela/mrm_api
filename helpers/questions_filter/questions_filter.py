from dateutil import parser
from dateutil.relativedelta import relativedelta
from graphql import GraphQLError


def filter_questions_by_date_range(questions, start_date, end_date):
    """
    Return questions that  fall in the date range
    """
    if not (start_date and end_date):
        return questions
    start_date, end_date = format_range_dates(start_date, end_date)
    filtered_questions = []
    for question in questions:
        question_start_date = parser.parse(question.start_date)
        question_end_date = parser.parse(question.end_date)
        if question_start_date >= start_date and question_end_date <= end_date:
            filtered_questions.append(question)
    return filtered_questions


def format_range_dates(start_date, end_date):
    """
    Convert dates to date objects and add one day to end_date
    Data from front-end doesn't include time
    """
    start_date = parser.parse(start_date).strftime('%Y-%m-%d')
    end_date = parser.parse(end_date).strftime('%Y-%m-%d')
    if start_date > end_date:
        raise GraphQLError("Start date must be lower than end date")
    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date) + relativedelta(days=1)
    return(start_date, end_date)
