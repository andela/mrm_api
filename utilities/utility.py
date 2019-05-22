import enum
import api
from helpers.database import db_session
from sqlalchemy import event


def update_entity_fields(entity, **kwargs):
    """
    Function to update an entities fields
    :param kwargs
    :param entity
    """
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity


def cascade_soft_delete(parent_model, child, parent_id):
    @event.listens_for(parent_model, 'after_update')
    def receive_after_update(mapper, connection, target):
        listen_for_after_flush_event(target, child, parent_id)


def listen_for_after_flush_event(target, child, parent_id):
    @event.listens_for(db_session, "after_flush", once=True)
    def receive_after_flush(session, context):
        """
        Function to update related child data after a delete
        mutation has been run.
        The check statement on line 42 caters for the difference
        in naming of room_resource folder and Resource class
            :param session:
            :param context:
        """
        if target.state == 'archived':
            child_model = getattr(api, child)
            child_object = getattr(
                child_model.models,
                'Resource' if child.capitalize() == 'Room_resource'
                else child.capitalize()
            )
            id_of_parent = getattr(child_object, parent_id)
            session.query(
                child_object
            ).filter(
                id_of_parent == target.id
            ).update(
                {child_object.state: target.state}
            )
        pass


def percentage_formater(portion, total):
    """ Calculates the percentage of the entered portion to the total and returns it
        :params
        - portion, total
    """
    try:
        percentage = (portion/total) * 100
        return percentage
    except ZeroDivisionError:
        return 0


class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()


class StateType(enum.Enum):
    active = "active"
    archived = "archived"
    deleted = "deleted"
