import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)

from api.user_role.models import UsersRole as UserRoleModel


class UsersRole(SQLAlchemyObjectType):

    class Meta:
        model = UserRoleModel


class CreateUserRole(graphene.Mutation):

    class Arguments:
        user_id = graphene.Int(required=True)
        role_id = graphene.Int(required=True)
    user_role = graphene.Field(UsersRole)

    def mutate(self, info, **kwargs):
        user_role = UserRoleModel(**kwargs)
        user_role.save()

        return CreateUserRole(user_role=user_role)


class Mutation(graphene.ObjectType):
    create_users_role = CreateUserRole.Field()
