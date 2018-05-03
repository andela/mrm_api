from helpers.database import db_session

def validate_empty_fields(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        if not kwargs.get(field):
            raise AttributeError("Room {field} is required field")


class Utility(object):
    
    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()
