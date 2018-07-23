from api.office.models import Office
from api.floor.models import Floor
from api.wing.models import Wing


def verify_ids(kwargs, office_id):
    get_office = Office.query.filter_by(id=office_id).first()
    if not get_office:
        raise AttributeError("Office Id does not exist")

    get_floor = Floor.query.filter_by(id=kwargs.get('floor_id')).first()
    if not get_floor:
        raise AttributeError("Floor Id does not exist")

    wing_id = kwargs.get('wing_id')
    if wing_id and not Wing.query.filter_by(id=wing_id).first():
        raise AttributeError("Wing Id does not exist")
