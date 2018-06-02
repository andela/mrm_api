import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.block.models import Block as BlockModel


class Block(SQLAlchemyObjectType):
    class Meta:
        model = BlockModel


class Query(graphene.ObjectType):
    all_blocks = graphene.List(Block)
    get_rooms_in_a_block = graphene.List(
        lambda: Block,
        block_id=graphene.Int()
    )

    def resolve_all_blocks(self, info):
        query = Block.get_query(info)
        return query.all()

    def resolve_get_rooms_in_a_block(self, info, block_id):
        query = Block.get_query(info)
        result = query.filter(BlockModel.id == block_id)
        return result
