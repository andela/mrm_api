import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from api.block.models import Block as BlockModel
from api.room.schema import Room
from helpers.room_filter.room_filter import room_join_location


class Block(SQLAlchemyObjectType):
    class Meta:
        model = BlockModel


class Query(graphene.ObjectType):
    all_blocks = graphene.List(Block)
    get_rooms_in_a_block = graphene.List(
        lambda: Room,
        block_id=graphene.Int()
    )

    def resolve_all_blocks(self, info):
        query = Block.get_query(info)
        return query.all()

    def resolve_get_rooms_in_a_block(self, info, block_id):
        query = Room.get_query(info)
        new_query = room_join_location(query)
        result = new_query.filter(BlockModel.id == block_id)
        return result
