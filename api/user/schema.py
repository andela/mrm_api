import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from api.user.models import User as UserModel
from helpers.auth.user_details import get_user_id_from_db
from api.user_role.models import UsersRole
from api.role.models import Role
from helpers.auth.authentication import Auth


class User(SQLAlchemyObjectType):

    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):

    class Arguments:
        email = graphene.String(required=True)
        location = graphene.String(required=True)
    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        user = UserModel(**kwargs)
        user.save()

        return CreateUser(user=user)


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(lambda: User, email=graphene.String())

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()

    def resolve_user(self, info, email):
        query = User.get_query(info)
        return query.filter(UserModel.email == email).first()


class DeleteUser(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
    user = graphene.Field(User)

    @Auth.user_roles('Admin')
    def mutate(self, info, user_id, **kwargs):
        query_user = User.get_query(info)
        exact_query_user = query_user.filter(
            UserModel.id == user_id).first()
        user_role = UsersRole.query.filter_by(user_id=user_id).first()
        user_id_from_db = get_user_id_from_db()
        if not exact_query_user:
            raise GraphQLError("User not found")
        if user_id_from_db == user_id:
            raise GraphQLError("You cannot delete yourself")
        role_name = Role.query.filter_by(id=user_role.role_id).first().role
        if role_name == "Admin":
            raise GraphQLError("You are not authorized to delete an Admin")
        exact_query_user.delete()
        return DeleteUser(user=exact_query_user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
