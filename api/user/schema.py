import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)

from api.user.models import User as UserModel


class User(SQLAlchemyObjectType):

    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):

    class Arguments:
        email = graphene.String(required=True)
    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        user = UserModel(**kwargs)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
