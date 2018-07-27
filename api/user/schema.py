import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from api.user.models import User as UserModel
from api.user_role.models import UsersRole
from helpers.auth.user_details import get_user_email_from_db
from helpers.auth.authentication import Auth
from helpers.auth.validator import verify_email


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
        email = graphene.String(required=True)
    user = graphene.Field(User)

    @Auth.user_roles('Admin')
    def mutate(self, info, email, **kwargs):
        query_user = User.get_query(info)
        exact_query_user = query_user.filter(
            UserModel.email == email).first()
        user_email_from_db = get_user_email_from_db()
        if not verify_email(email):
            raise GraphQLError("Invalid email format")
        if not exact_query_user:
            raise GraphQLError("User not found")
        if user_email_from_db == email:
            raise GraphQLError("You cannot delete yourself")
        exact_query_user.delete()
        return DeleteUser(user=exact_query_user)


class ChangeUserRole(graphene.Mutation):
    class Arguments:

        email = graphene.String(required=True)
        role_id = graphene.Int()
    user = graphene.Field(User)

    @Auth.user_roles('Admin')
    def mutate(self, info, email, **kwargs):
        query_user = User.get_query(info)
        exact_user = query_user.filter(
            UserModel.email == email).first()
        if not exact_user:
            raise GraphQLError("User not found")
        user_role = UsersRole.query.filter_by(user_id=exact_user.id).first()
        new_role = kwargs.pop('role_id')
        user_role.role_id = new_role
        user_role.save()
        return ChangeUserRole(user=exact_user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    change_user_role = ChangeUserRole.Field()
