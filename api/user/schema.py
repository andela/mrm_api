import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from api.user.models import User as UserModel
from helpers.auth.user_details import get_user_email_from_db
from helpers.auth.authentication import Auth
from helpers.auth.validator import verify_email
from helpers.pagination.paginate import Paginate


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


class PaginatedUsers(Paginate):
    users = graphene.List(User)

    def resolve_users(self, info):
        page = self.page
        per_page = self.per_page
        query = User.get_query(info)
        if not page:
            return query.all()

        if page:
            if page < 1:
                return GraphQLError("No page requested")

            page = page - 1
            self.query_total = query.count()
            result = query.limit(per_page).offset(page*per_page)
            if result.count() == 0:
                return GraphQLError("No more resources")
            return result


class Query(graphene.ObjectType):
    users = graphene.Field(PaginatedUsers, page=graphene.Int(),
                           per_page=graphene.Int())
    user = graphene.Field(lambda: User, email=graphene.String())

    def resolve_users(self, info, **kwargs):
        response = PaginatedUsers(**kwargs)
        return response

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


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
