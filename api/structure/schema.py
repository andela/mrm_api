import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.structure.models import Structure as StructureModel
from helpers.auth.authentication import Auth
from helpers.structure.create_structure import create_structure
from graphql import GraphQLError
from helpers.auth.admin_roles import admin_roles
from api.room.schema import Room
from api.room.models import Room as RoomModel
from utilities.validations import (
    validate_empty_fields,
    validate_structure_id
)
from utilities.utility import update_entity_fields


class Structure(SQLAlchemyObjectType):
    class Meta:
        model = StructureModel


class StructureInputs(graphene.InputObjectType):
    structure_id = graphene.String(required=True)
    level = graphene.Int(required=True)
    name = graphene.String(required=True)
    parent_id = graphene.String()
    parent_title = graphene.String()
    tag = graphene.String(required=True)
    location_id = graphene.Int(required=True)
    position = graphene.Int(required=True)


class CreateOfficeStructure(graphene.Mutation):
    """ Returns payload on office structure creation"""
    class Arguments:
        data = graphene.List(
            StructureInputs,
            required=True,
            description="Creates a new office structure with the arguments\
            \n- structure_id: The structure id for office structure[required]\
            \n- level: The level of the office structure[required]\
            \n- name: The name of the office structure[required]\
            \n- parent_id: The parent id of the office structure\
            \n- parent_title: The parent title of the structure\
            \n- tag: Tags for the office structure[required]\
            \n- location_id: The location id of the office structure[required]\
            \n- position: The position of the office structure[required]"
        )

    structure = graphene.List(Structure)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_structure_id(**kwargs)
        office_structure = []
        for each_structure in kwargs['data']:
            node = create_structure(**each_structure)
            office_structure.append(node)
        return CreateOfficeStructure(structure=office_structure)


class DeleteOfficeStructure(graphene.Mutation):
    """
        Delete an office_structure
    """

    class Arguments:
        structure_ids = graphene.List(graphene.String, required=True)
    structure = graphene.List(Structure)

    @Auth.user_roles('Admin')
    def mutate(self, info, structure_ids):
        office_structure_query = Structure.get_query(info)
        room_query = Room.get_query(info)
        active_structures = office_structure_query.filter(
            StructureModel.state == "active")
        active_rooms = room_query.filter(
            RoomModel.state == "active")
        structures = []
        for structure_id in structure_ids:
            office_structure = active_structures.filter(
                StructureModel.structure_id == structure_id).first()
            if not office_structure:
                message = 'The structure {} does not exist'.format(structure_id)
                raise GraphQLError(message)
            rooms = active_rooms.filter(
                RoomModel.structure_id == structure_id).all()
            if len(rooms) > 0:
                for room in rooms:
                    update_entity_fields(room, state="archived")
                    room.save()
            update_entity_fields(office_structure, state="archived")
            office_structure.save()
            structures.append(office_structure)
        return DeleteOfficeStructure(structure=structures)


class UpdateOfficeStructure(graphene.Mutation):
    """
    Updates an office structure
    """
    class Arguments:
        structure_id = graphene.String()
        level = graphene.Int()
        name = graphene.String()
        parent_id = graphene.String()
        parent_title = graphene.String()
        tag = graphene.String()
        location_id = graphene.Int()
        position = graphene.Int()
    structure = graphene.Field(Structure)

    @Auth.user_roles('Admin')
    def mutate(self, info, structure_id, **kwargs):
        validate_empty_fields(**kwargs)
        query = Structure.get_query(info)
        active_structure = query.filter(
            StructureModel.structure_id == structure_id,
            StructureModel.state == "active").first()
        if not active_structure:
            raise GraphQLError('Structure not found')
        update_entity_fields(active_structure, **kwargs)
        active_structure.save()
        return UpdateOfficeStructure(structure=active_structure)


class Mutation(graphene.ObjectType):
    create_office_structure = CreateOfficeStructure.Field()
    delete_office_structure = DeleteOfficeStructure.Field(
        description="Deletes office structures and the rooms associated\
        \n- structure_ids: The structure_id of the structure(s)"
    )
    update_office_structure = UpdateOfficeStructure.Field(
        description="Updates an office structure and takes the arguments\
            \n- structure_id: The structure id for the office structure\
            \n- level: The level of the office structure\
            \n- name: The name of the office structure\
            \n- parent_id: The parent id of the office structure\
            \n- parent_title: The parent title of the structure\
            \n- tag: Tags for the office structure\
            \n- location_id: The location id of the office structure\
            \n- position: The position of the office structure"
    )


class Query(graphene.ObjectType):
    """
      Query for office structures
    """
    all_structures = graphene.List(
        Structure,
        description="Returns a list containing all office structures")
    structure_by_structure_id = graphene.Field(
        Structure, structure_id=graphene.String(), description="Returns the office \
        structure corresponding to the provided structureId")

    @Auth.user_roles('Admin')
    def resolve_all_structures(self, info):
        query = Structure.get_query(info)
        location_id = admin_roles.user_location_for_analytics_view()
        all_structures = query.filter(
            StructureModel.state == "active",
            StructureModel.location_id == location_id).all()
        return all_structures

    @Auth.user_roles('Admin')
    def resolve_structure_by_structure_id(self, info, structure_id):
        if not structure_id.strip():
            raise GraphQLError("Please input a valid structureId")
        query = Structure.get_query(info)
        location_id = admin_roles.user_location_for_analytics_view()
        structure = query.filter(
            StructureModel.structure_id == structure_id).first()
        if not structure or location_id != structure.location_id:
            raise GraphQLError("Structure not found")
        return structure
