from api.structure.models import Structure as StructureModel


def create_structure(**kwargs):
    """ Creates a single node in the office structure model"""
    structure = StructureModel(
        structure_id=kwargs.get('structure_id'),
        name=kwargs.get('name'),
        level=kwargs.get('level'),
        parent_id=kwargs.get('parent_id'),
        parent_title=kwargs.get('parent_title'),
        tag=kwargs.get('tag'),
        location_id=kwargs.get('location_id'),
        position=kwargs.get('position')
    )
    structure.save()
    return structure
