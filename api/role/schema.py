import graphene
from sqlalchemy import exc, func
from graphql import GraphQLError

from utilities.validator import ErrorHandler
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
        try:
            role = RoleModel(**kwargs)
            payload = {
                'model': RoleModel, 'field': 'role', 'value':  kwargs['role']
                }
            query = Role.get_query(info)
            role_name = query.filter(
                func.lower(RoleModel.role) ==
                func.lower(kwargs['role'])).count()
            if role_name > 0:
                ErrorHandler.check_conflict(self, kwargs['role'], 'Role')
            with SaveContextManager(role,  'Role', payload):
                return CreateRole(role=role)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Query(graphene.ObjectType):
    roles = graphene.List(Role)
    role = graphene.Field(Role, role=graphene.String())

    def resolve_roles(self, info):
        try:
            query = Role.get_query(info)
            return query.all()
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")

    def resolve_role(self, info, role):
        try:
            query = Role.get_query(info)
            return query.filter(RoleModel.role == role).first()
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Mutation(graphene.ObjectType):
    create_role = CreateRole.Field()
