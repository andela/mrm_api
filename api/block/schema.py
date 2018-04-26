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
    get_rooms_in_a_block = graphene.List(
        lambda:Block,
        id = graphene.Int()
    )

    def resolve_get_rooms_in_a_block(self,info,id):
        query = Block.get_query(info)
        result = query.filter(BlockModel.id == id)
        return result