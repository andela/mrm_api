import graphene
from math import ceil

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


class PaginatedUsers(graphene.ObjectType):
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()
    users = graphene.List(User)

    def __init__(self, **kwargs):
        self.page = kwargs.pop('page', None)
        self.per_page = kwargs.pop('per_page', None)
        self.query_total
        self.pages

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

    def resolve_pages(self, pages):
        if self.per_page:
            self.pages = ceil(self.query_total / self.per_page)
        pages = self.pages
        return pages

    def resolve_has_next(self, has_next):
        if self.page:
            page = self.page
            pages = self.pages
            pages = self.resolve_pages(pages)
            if page < pages:
                has_next = True
            else:
                has_next = False
        return has_next

    def resolve_has_previous(self, has_previous):
        if self.page:
            page = self.page
            pages = self.resolve_pages(self.pages)
            if (page > 1) and (pages > 1) and (page <= pages):
                has_previous = True
            else:
                has_previous = False

        return has_previous


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
