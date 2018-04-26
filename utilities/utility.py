from helpers.database import db_session


class Utility(object):
    
    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()
