import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from api.role.models import Role as RoleModel
from helpers.auth.error_handler import SaveContextManager


class Role(SQLAlchemyObjectType):

    class Meta:
        model = RoleModel


class CreateRole(graphene.Mutation):

    class Arguments:
        role = graphene.String(required=True)
    role = graphene.Field(Role)

    def mutate(self, info, **kwargs):
        role = RoleModel(**kwargs)
        with SaveContextManager(role, kwargs.get('role'), 'Role'):
            return CreateRole(role=role)


class Query(graphene.ObjectType):
    roles = graphene.List(Role)
    role = graphene.Field(Role, role=graphene.String())

    def resolve_roles(self, info):
        query = Role.get_query(info)
        return query.all()

    def resolve_role(self, info, role):
        query = Role.get_query(info)
        return query.filter(RoleModel.role == role).first()


class Mutation(graphene.ObjectType):
    create_role = CreateRole.Field()
