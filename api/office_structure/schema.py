import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.office_structure.models import OfficeStructure as OfficeStructureModel
from helpers.auth.error_handler import SaveContextManager
from helpers.auth.authentication import Auth
from utilities.validations import (
    validate_empty_fields,
    validate_parent_node_id,
    )


class OfficeStructure(SQLAlchemyObjectType):
    """Autogenerated Return type for OfficeStructure"""

    class Meta:
        model = OfficeStructureModel


class CreateNode(graphene.Mutation):
    """ Returns payload on node creation"""

    class Arguments:
        name = graphene.String(required=True)
        parent_id = graphene.Int(required=False)
    node = graphene.Field(OfficeStructure)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        if 'parent_id' in kwargs:
            validate_parent_node_id(parent_id=kwargs['parent_id'])
        node = OfficeStructureModel(**kwargs)
        payload = {
            'model': OfficeStructureModel,
            'field': 'name',
            'value':  kwargs['name']
            }
        with SaveContextManager(
          node, 'node level', payload
        ):
            return CreateNode(node=node)


class DeleteNode(graphene.Mutation):
    """ Returns payload when a level/node is deleted """

    class Arguments:
        id = graphene.Int(required=True)
    node = graphene.Field(OfficeStructure)

    @Auth.user_roles('Admin')
    def mutate(self, info, id):
        query_node = OfficeStructure.get_query(info)
        node = query_node.filter(
            OfficeStructureModel.id == id).first()
        if not node:
            raise GraphQLError("Level not found")
        node.delete()
        return DeleteNode(node=node)


class Mutation(graphene.ObjectType):
    create_node = CreateNode.Field(
        description="Creates a level or node when given the arguments\
            \n- name: The name field of a specific node/level, and\
            parent_id: This is provided when creating a child node"
    )
    delete_level = DeleteNode.Field(
        description="Deletes a level or node when given the arguments\
            \n- id: The id field of a specific node/level"
    )
