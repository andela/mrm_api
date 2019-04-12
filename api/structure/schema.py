import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.structure.models import Structure as StructureModel
from helpers.auth.authentication import Auth
from helpers.structure.create_structure import create_structure
from graphql import GraphQLError
from sqlalchemy import func


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
        office_structure = []
        for each_structure in kwargs['data']:
            node = create_structure(**each_structure)
            office_structure.append(node)
        return CreateOfficeStructure(structure=office_structure)


class Mutation(graphene.ObjectType):
    create_office_structure = CreateOfficeStructure.Field()


class Query(graphene.ObjectType):
    """
      Query for office structures
    """
    all_structures = graphene.List(
      Structure, description="Returns a list containing all office structures")
    structure_by_structure_id = graphene.Field(
      Structure, structure_id=graphene.String(), description="Returns the office \
        structure corresponding to the provided structureId")

    @Auth.user_roles('Admin')
    def resolve_all_structures(self, info):
        query = Structure.get_query(info)
        return query.order_by(func.lower(StructureModel.name)).all()

    @Auth.user_roles('Admin')
    def resolve_structure_by_structure_id(self, info, structure_id):
        if not structure_id.strip():
            raise GraphQLError("Please input a valid structureId")
        query = Structure.get_query(info)
        structure = query.filter(
          StructureModel.structure_id == structure_id).first()
        if not structure:
            raise GraphQLError("Structure not found")
        return structure
