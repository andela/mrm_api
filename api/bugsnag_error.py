import bugsnag
import os
from graphql import GraphQLError


class Errors:

    def report_errors_bugsnag_and_graphQL(error_message):
        if os.getenv("APP_SETTINGS") != "testing":
            bugsnag.notify(Exception(error_message), severity="error")
        raise GraphQLError(error_message)


return_error = Errors
