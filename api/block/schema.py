import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func
from api.block.models import Block as BlockModel
from api.room.schema import Room
from api.office.models import Office
from helpers.room_filter.room_filter import room_join_location
from helpers.auth.admin_roles import admin_roles
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth


class Block(SQLAlchemyObjectType):
    class Meta:
        model = BlockModel


class CreateBlock(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        office_id = graphene.Int(required=True)
    block = graphene.Field(Block)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        block_name = BlockModel.query.filter_by(name=kwargs['name'].title()).all()  # noqa
        if block_name:
            raise GraphQLError("Block aleady exists")
        get_office = Office.query.filter_by(id=kwargs['office_id']).first()
        if not get_office:
            raise GraphQLError("Office not found")
        location = get_office.location.name
        if location.lower() == 'nairobi':
            block = BlockModel(**kwargs)
            block.save()
        else:
            raise GraphQLError("You can only create block in Nairobi")
        return CreateBlock(block=block)


class UpdateBlock(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        block_id = graphene.Int(required=True)

    block = graphene.Field(Block)

    @Auth.user_roles("Admin")
    def mutate(self, info, block_id, **kwargs):
        validate_empty_fields(**kwargs)
        query = Block.get_query(info)
        exact_block = query.filter(BlockModel.id == block_id).first()
        if not exact_block:
            raise GraphQLError("Block not found")

        admin_roles.create_floor_update_delete_block(block_id)

        update_entity_fields(exact_block, **kwargs)
        exact_block.save()
        return UpdateBlock(block=exact_block)


class DeleteBlock(graphene.Mutation):
    class Arguments:
        block_id = graphene.Int(required=True)

    block = graphene.Field(Block)

    @Auth.user_roles("Admin")
    def mutate(self, info, block_id, **kwargs):
        query = Block.get_query(info)
        exact_block = query.filter(BlockModel.id == block_id).first()
        if not exact_block:
            raise GraphQLError("Block not found")

        admin_roles.create_floor_update_delete_block(block_id)
        exact_block.delete()
        return DeleteBlock(block=exact_block)


class Query(graphene.ObjectType):
    all_blocks = graphene.List(Block)
    get_rooms_in_a_block = graphene.List(
        lambda: Room,
        block_id=graphene.Int()
    )

    def resolve_all_blocks(self, info):
        query = Block.get_query(info)
        return query.order_by(func.lower(BlockModel.name)).all()

    def resolve_get_rooms_in_a_block(self, info, block_id):
        query = Room.get_query(info)
        new_query = room_join_location(query)
        result = new_query.filter(BlockModel.id == block_id)
        return result


class Mutation(graphene.ObjectType):
    create_block = CreateBlock.Field()
    update_block = UpdateBlock.Field()
    Delete_block = DeleteBlock.Field()
