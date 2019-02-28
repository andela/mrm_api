from api.office.models import Office
from api.floor.models import Floor
from api.wing.models import Wing
from api.location.models import Location


def verify_ids(office_id, kwargs):
    get_office = Office.query.filter_by(id=office_id).first()
    if not get_office:
        raise AttributeError("Office Id does not exist")

    location_id = kwargs.get('location_id')
    if location_id and not Location.query.filter_by(id=location_id).first():
        raise AttributeError("Location Id does not exist")

    get_floor = Floor.query.filter_by(id=kwargs.get('floor_id')).first()
    if not get_floor:
        raise AttributeError("Floor Id does not exist")

    wing_id = kwargs.get('wing_id')
    if wing_id and not Wing.query.filter_by(id=wing_id).first():
        raise AttributeError("Wing Id does not exist")
