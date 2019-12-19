from flask_json import JsonError
from api.bugsnag_error import return_error


def handle_http_error(*args):
    """
    Handle exceptionn raised when there is http error.
    """
    message, status, expected_args = args
    if 'REST' in expected_args:
        raise JsonError(message=message, status=status)
    return_error.report_errors_bugsnag_and_graphQL(message)
