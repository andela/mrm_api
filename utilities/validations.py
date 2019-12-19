import datetime
import validators
import re

from api.location.models import CountryType, TimeZoneType
from api.structure.models import Structure as StructureModel
from api.office_structure.models import OfficeStructure as OfficeStructureModel
from api.bugsnag_error import return_error


def validate_url(**kwargs):
    """
    Function to validate url when
    saving an object
    :params kwargs
    """
    if not validators.url(kwargs.get('image_url')):
        raise AttributeError("Please enter a valid image url")


def validate_empty_fields(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        value = kwargs.get(field)
        if isinstance(value, str):
            value = value.strip()
        if not type(value) is bool and not value:
            raise AttributeError(field + " is required field")


def validate_date_time_range(**kwargs):
    """
    Function to validate the dates entered
    for questions for feedback
    :params kwargs
    """
    if ('start_date' and 'end_date' in kwargs) and\
            kwargs['start_date'] < datetime.datetime.now():
        raise ValueError('startDate should be today or after')
    elif ('start_date' and 'end_date' in kwargs) and\
            kwargs['end_date'] - kwargs['start_date'] < datetime.timedelta(
                days=1
    ):
        raise ValueError(
            'endDate should be at least a day after startDate'
        )


def validate_country_field(**kwargs):
    """
    Function to validate country fields when
    saving an object
    :params kwargs
    """
    valid_countries = [country.value for country in CountryType]
    country_name = kwargs['country']
    if country_name not in valid_countries:
        raise AttributeError("Not a valid country")


def validate_timezone_field(**kwargs):
    """
    Function to validate timezone fields when
    saving an object
    :params kwargs
    """
    timezones = [timezone.name for timezone in TimeZoneType]
    time_zone = kwargs['time_zone']
    if time_zone not in timezones:
        raise AttributeError("Not a valid time zone")


def validate_question_type(**kwargs):
    """
    Function to validate the question types,
    should allow only check, input and rate
    :params kwargs
    """
    question_types = ['check', 'input', 'rate', 'missing_items']
    if 'question_type' in kwargs:
        type = kwargs['question_type']
        if type.lower() not in question_types:
            raise AttributeError("Not a valid question type")


def validate_date_range(**kwargs):
    """
    Function to validate the date range
    :params kwargs
    """
    if (('end_date' and 'start_date' in kwargs) and
        kwargs['end_date'] > datetime.datetime.now() or
            kwargs['start_date'] > datetime.datetime.now()):
        raise ValueError('Dates should be before today')
    elif (('end_date' and 'start_date' in kwargs) and
            kwargs['end_date'] < kwargs['start_date']):
        raise ValueError('Earlier date should be lower than later date')


def validate_room_labels(**kwargs):
    """
    Function to validate the room label string type
    :params **kwargs
    """
    room_labels = kwargs.get('room_labels')
    label = re.search("[{}:]", str(room_labels))
    if label:
        raise AttributeError("Room label is not a valid string type")
    for label in room_labels:
        structure = StructureModel.query.filter_by(name=label).first()
        if structure is None:
            return_error.report_errors_bugsnag_and_graphQL(
                "Structure does not exist")
        break


def validate_structure_id(**kwargs):
    """
    Function to validate that a structure id exists
    :param structure_id
    """
    structure_id = kwargs.get('structure_id')
    structure = StructureModel.query.filter_by(
        structure_id=structure_id).first()
    if not structure:
        error_message = 'The structure {} does not exist'.format(structure_id)
        return_error.report_errors_bugsnag_and_graphQL(error_message)


def validate_unique_structure_id(**kwargs):
    """
    Function to validate that structure ids are unique
    """
    structure_id_list = \
        [structure['structure_id'] for structure in kwargs['data']]
    for structure_id in structure_id_list:
        if structure_id_list.count(structure_id) > 1:
            return_error.report_errors_bugsnag_and_graphQL(
                'The office stuctures does not contain unique ids')

        structure_in_db = StructureModel.query.filter_by(
            structure_id=structure_id).first()
        if structure_in_db:
            return_error.report_errors_bugsnag_and_graphQL(
                '{} already exists'.format(structure_in_db.name))


def ensure_unique_id(node_list):
    node_id_list = [node.id for node in node_list]
    if len(node_list) != len(set(node_id_list)):
        return_error.report_errors_bugsnag_and_graphQL(
            'nodes must have unique id')
    node_with_id = OfficeStructureModel.query.filter(
        OfficeStructureModel.id.in_(node_id_list)).first()
    if node_with_id:
        return_error.report_errors_bugsnag_and_graphQL(
            'node id "{}" in use'.format(node_with_id.id))


def ensure_single_root_node(node_list):
    total_root_nodes = len(
        [node.parent_id for node in node_list if node.parent_id is None])
    if total_root_nodes != 1:
        return_error.report_errors_bugsnag_and_graphQL(
            'there must be exactly 1 root node. {} were supplied'.format(
                total_root_nodes))


def ensure_valid_parent_id(node_list):
    """
    Function to validate that parent nodes do not appear before their children
    """
    available_parents = set()
    for node in node_list:
        if node.parent_id and node.parent_id not in available_parents:
            return_error.report_errors_bugsnag_and_graphQL(
                'node "{}" appears before its parent'.format(
                    node.name))
        available_parents.add(node.id)


def validate_structure_nodes(node_list):
    """
    This function ensures the structure nodes are well formatted to form
    a valid structure
    """
    if not len(node_list):
        return_error.report_errors_bugsnag_and_graphQL(
            'node_list cannot be empty')
    ensure_unique_id(node_list)
    ensure_single_root_node(node_list)
    ensure_valid_parent_id(node_list)
