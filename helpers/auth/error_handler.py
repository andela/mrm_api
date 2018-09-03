from sqlalchemy import exc
from helpers.auth.validator import ErrorHandler


class SaveContextManager():
    '''Manage sqlalchemy exceptions.'''

    def __init__(self, model_obj, entity_name, entity):
        self.model_obj = model_obj
        self.entity_name = entity_name
        self.entity = entity

    def __enter__(self):
        try:
            self.model_obj.save()
        except exc.IntegrityError:
            return ErrorHandler.check_conflict(
                self, self.entity_name, self.entity)
        except exc.DBAPIError:
            return ErrorHandler.db_connection(self)

    def __exit__(self, type, value, traceback):
        return False
