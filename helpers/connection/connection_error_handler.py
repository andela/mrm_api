from graphql import GraphQLError
from flask_json import JsonError


def handle_http_error(*args):
    """
    Handle exceptionn raised when there is http error.
    """
    message, status, expected_args = args
    if 'REST' in expected_args:
        raise JsonError(message=message, status=status)
    raise GraphQLError(message)
