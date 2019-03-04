import os
from sqlalchemy import exc
from graphql import GraphQLError
from utilities.validator import ErrorHandler


class SaveContextManager():
    '''Manage sqlalchemy exceptions.'''

    def __init__(self, model_obj, entity_name, entity, **kwargs):
        self.model_obj = model_obj
        self.entity_name = entity_name
        self.entity = entity
        self.kwargs = kwargs

    def __enter__(self):
        try:
            self.model_obj.save()
        except exc.ProgrammingError as error:
            if (os.getenv('APP_SETTINGS') in ("testing", "development")):
                long_error_message = str(error.orig)
                index = long_error_message.find("\n")
                Specific_error = long_error_message[:index]
                raise GraphQLError(Specific_error)
            else:  # pragma: no cover
                raise GraphQLError(
                    "There seems to be a database connection error \
                        contact your admin for assistance")
        except exc.IntegrityError as err:
            res = 'Database integrity error'
            if "duplicate key value violates unique constraint" in str(err):
                res = ErrorHandler.check_conflict(
                    self, self.entity['value'], self.entity_name)
            elif "violates foreign key constraint" in str(err):
                res = ErrorHandler.foreign_key_conflict(
                    self, self.entity_name, self.entity)
            return res
        except exc.DBAPIError:
            return ErrorHandler.db_connection(self)

    def __exit__(self, type, value, traceback):
        return False
