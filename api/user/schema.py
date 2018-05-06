import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from api.user.models import User as UserModel

class User(SQLAlchemyObjectType):
    
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class CreateUser(graphene.Mutation):
    
    class Arguments:
        email = graphene.String(required=True)
        name = graphene.String(required=True)
    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        user  = UserModel(**kwargs)
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


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
