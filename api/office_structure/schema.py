import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.office_structure.models import OfficeStructure as StructureModel
from helpers.auth.authentication import Auth
from utilities.validations import (
    validate_empty_fields,
    validate_structure_nodes
)
from helpers.auth.admin_roles import admin_roles
from helpers.database import db_session


class Node(SQLAlchemyObjectType):
    class Meta:
        model = StructureModel


class InputNode(graphene.InputObjectType):
    id = graphene.UUID(required=True)
    parent_id = graphene.UUID()
    name = graphene.String(required=True)
    tag = graphene.String(required=True)


class CreateStructure(graphene.Mutation):
    """ Returns payload on structure creation"""
    class Arguments:
        node_list = graphene.List(
            InputNode,
            required=True,
            description="Creates a new structure with the arguments\
            \n- id: The id of the node[required]\
            \n- parent_id: The parent id of the node. Null for root node\
            \n- name: The name of the node[required]\
            \n- tag: The tag to be associated with the node[required]"
        )

    structure = graphene.List(Node)

    @Auth.user_roles('Admin', 'Super Admin')
    def mutate(self, info, node_list):
        validate_structure_nodes(node_list)
        admin_location_id = admin_roles.user_location_for_analytics_view()
        nodes = []
        for node in node_list:
            validate_empty_fields(**node)
            node['name'] = node.name.strip()
            node['tag'] = node.tag.strip()
            nodes.append(StructureModel(
              **node, location_id=admin_location_id))
        db_session.add_all(nodes)
        db_session.commit()
        return CreateStructure(structure=nodes)


class Mutation(graphene.ObjectType):
    create_structure = CreateStructure.Field()
