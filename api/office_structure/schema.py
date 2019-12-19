import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from enum import Enum
from sqlalchemy import asc, desc
from api.office_structure.models import OfficeStructure as StructureModel
from helpers.auth.authentication import Auth
from utilities.validations import (
    validate_empty_fields,
    validate_structure_nodes
)
from helpers.auth.admin_roles import admin_roles
from helpers.database import db_session
from utilities.utility import update_entity_fields
from api.bugsnag_error import return_error


class StructureNode(SQLAlchemyObjectType):
    class Meta:
        model = StructureModel


class InputNode(graphene.InputObjectType):
    id = graphene.UUID(required=True)
    parent_id = graphene.UUID()
    name = graphene.String(required=True)
    tag = graphene.String(required=True)


class UpdateNode(graphene.Mutation):
    """
        Returns a node payload after updating a node
    """
    class Arguments:
        node_id = graphene.UUID(required=True)
        name = graphene.String()
        tag = graphene.String()
    node = graphene.Field(StructureNode)

    @Auth.user_roles('Admin', 'Super Admin')
    def mutate(self, info, **kwargs):
        query = StructureNode.get_query(info)
        node = query.filter(
            StructureModel.id == kwargs['node_id']).first()

        if not node:
            return_error.report_errors_bugsnag_and_graphQL("node not found")

        validate_empty_fields(**kwargs)

        if kwargs.get('name'):
            kwargs['name'] = kwargs['name'].strip()
        else:
            kwargs['name'] = node.name

        if kwargs.get('tag'):
            kwargs['tag'] = kwargs['tag'].strip()
        else:
            kwargs['tag'] = node.tag

        update_entity_fields(node, **kwargs)
        node.save()

        return UpdateNode(node=node)


class DeleteNode(graphene.Mutation):
    """
    Returns node payload after deleting a node
    """

    class Arguments:
        node_id = graphene.UUID(required=True)

    node = graphene.Field(StructureNode)

    @Auth.user_roles('Admin', 'Super Admin')
    def mutate(self, info, node_id):
        exact_node = db_session.query(StructureModel).filter(
            StructureModel.id == node_id).first()
        if not exact_node:
            return_error.report_errors_bugsnag_and_graphQL(
                "The specified node does not exist"
            )
        db_session.delete(exact_node)
        db_session.commit()
        return DeleteNode(node=exact_node)


class CreateStructure(graphene.Mutation):
    """ Returns a list of nodes on structure creation"""
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

    structure = graphene.List(StructureNode)

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
    delete_node = DeleteNode.Field(
        description="Mutation to delete a node\
            \n- node_id: Unique key identifier of a node"
    )
    update_node = UpdateNode.Field(
        description="Mutation to update a node\
            \n - node_id: Unique key identifier of a node (required)\
            \n - name: name of the node to be updated (optional)\
            \n - tag: tag of the node to be updated (optional)\
            \n If only node_id is passed, no update is made and\
            \n the current node is returned")


class Order(Enum):
    ASC = 'asc'
    DESC = 'desc'


class Query(graphene.ObjectType):
    """
      Query for node path
    """
    node_path_by_name = graphene.List(
        StructureNode,
        node_name=graphene.String(required=True),
        order=graphene.Argument(graphene.Enum.from_enum(Order)),
        description="Returns the path from root to the node within structure"
    )

    @Auth.user_roles('Admin', 'Default User', 'Super Admin')
    def resolve_node_path_by_name(self, info, **kwargs):
        node_name = kwargs['node_name']
        order = kwargs.get('order')
        query = StructureNode.get_query(info)
        order = asc if order == 'asc' else desc
        node = query.filter(
            StructureModel.name.ilike(node_name.strip())).first()
        if not node:
            return_error.report_errors_bugsnag_and_graphQL('node not found')
        return node.path_to_root(order=order)
