import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from api.user.models import User as UserModel
from api.equipment.schema import Equipment

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
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(User)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
