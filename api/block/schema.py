import graphene
from graphene import relay,Schema
from graphene_sqlalchemy import (
    SQLAlchemyObjectType, 
    SQLAlchemyConnectionField
)
from api.block.models import Block as BlockModel

class Block(SQLAlchemyObjectType):
    class Meta:
        model = BlockModel
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    floor = SQLAlchemyConnectionField(Block)