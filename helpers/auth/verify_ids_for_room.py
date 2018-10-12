from api.office.models import Office
from api.floor.models import Floor
from api.wing.models import Wing
from api.block.models import Block


def verify_ids(office_id, kwargs):
    get_office = Office.query.filter_by(id=office_id).first()
    if not get_office:
        raise AttributeError("Office Id does not exist")

    get_floor = Floor.query.filter_by(id=kwargs.get('floor_id')).first()
    if not get_floor:
        raise AttributeError("Floor Id does not exist")

    wing_id = kwargs.get('wing_id')
    if wing_id and not Wing.query.filter_by(id=wing_id).first():
        raise AttributeError("Wing Id does not exist")


def validate_block(office_id, kwargs):
    block_id = kwargs.get("block_id")
    get_floor = Floor.query.filter_by(id=kwargs.get('floor_id')).first()
    if block_id:
        exact_block = Block.query.filter_by(id=block_id, office_id=office_id).first()  # noqa: E501
        if not exact_block:
            raise AttributeError("Block with such id does not exist")
        # checks if the floor exists in the given block
        if get_floor.block_id != block_id:
            raise AttributeError("Floor does not exist in this Block")
