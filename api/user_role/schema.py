import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

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
        user_role  = UserRoleModel(**kwargs)
        user_role.save()

        return CreateUserRole(user_role=user_role)

class Query(graphene.ObjectType):
    users_role = graphene.List(UsersRole)
    user_role = graphene.Field(lambda: UsersRole, user_id=graphene.Int())

    def resolve_users_role(self, info):
        query = UsersRole.get_query(info)
        return query.all()

    def resolve_user_role(self, info, user_id):
       query = UsersRole.get_query(info)
       return query.filter(UserRoleModel.user_id == user_id).first()


class Mutation(graphene.ObjectType):
    create_users_role = CreateUserRole.Field()
