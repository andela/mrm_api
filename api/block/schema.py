import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func
from api.block.models import Block as BlockModel
from api.room.schema import Room
from api.office.models import Office
from api.room.models import Room as RoomModel
from helpers.room_filter.room_filter import room_join_location
from helpers.auth.admin_roles import admin_roles
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.error_handler import SaveContextManager


class Block(SQLAlchemyObjectType):
    """
        Returns the payload with the fields
        (id, name, officeId, state, offices, floors)
    """
    class Meta:
        model = BlockModel


class CreateBlock(graphene.Mutation):
    '''
        Returns payload after creating a block
    '''
    class Arguments:
        state = graphene.String()
        name = graphene.String(required=True)
        office_id = graphene.Int(required=True)
    block = graphene.Field(Block)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        get_office = Office.query.filter_by(id=kwargs['office_id']).first()
        if not get_office:
            raise GraphQLError("Office not found")
        location = get_office.location.name
        if location.lower() == 'nairobi':
            block = BlockModel(**kwargs)
            payload = {
                'model': BlockModel, 'field': 'name', 'value':  kwargs['name']
            }
            with SaveContextManager(
                block, 'Block', payload
            ):
                return CreateBlock(block=block)
        else:
            raise GraphQLError("You can only create block in Nairobi")


class UpdateBlock(graphene.Mutation):
    """
       Returns payload on updating a block
    """
    class Arguments:
        name = graphene.String(required=True)
        block_id = graphene.Int(required=True)

    block = graphene.Field(Block)

    @Auth.user_roles("Admin")
    def mutate(self, info, block_id, **kwargs):
        validate_empty_fields(**kwargs)
        query = Block.get_query(info)
        result = query.filter(BlockModel.state == "active")
        exact_block = result.filter(BlockModel.id == block_id).first()
        if not exact_block:
            raise GraphQLError("Block not found")

        admin_roles.create_floor_update_delete_block(block_id)

        update_entity_fields(exact_block, **kwargs)
        exact_block.save()
        return UpdateBlock(block=exact_block)


class DeleteBlock(graphene.Mutation):
    """
        Returns payload on deleting a block
    """
    class Arguments:
        block_id = graphene.Int(required=True)
        state = graphene.String()

    block = graphene.Field(Block)

    @Auth.user_roles("Admin")
    def mutate(self, info, block_id, **kwargs):
        query = Block.get_query(info)
        result = query.filter(BlockModel.state == "active")
        exact_block = result.filter(BlockModel.id == block_id).first()
        if not exact_block:
            raise GraphQLError("Block not found")

        admin_roles.create_floor_update_delete_block(block_id)
        update_entity_fields(exact_block, state="archived", **kwargs)
        exact_block.save()
        return DeleteBlock(block=exact_block)


class Query(graphene.ObjectType):
    all_blocks = graphene.List(
        Block, description="Query That returns a list of all blocks")
    get_rooms_in_a_block = graphene.List(
        lambda: Room,
        block_id=graphene.Int(),
        description="Query that returns a list of rooms in a block and accepts the argument\
            \n- block_id: Unique identifier of a block"
    )

    def resolve_all_blocks(self, info):
        """
            Returns list of all blocks
        """
        query = Block.get_query(info)
        result = query.filter(BlockModel.state == "active")
        return result.order_by(func.lower(BlockModel.name)).all()

    def resolve_get_rooms_in_a_block(self, info, block_id):
        """
            Returns all rooms in a specific block
        """
        query = Room.get_query(info)
        active_rooms = query.filter(RoomModel.state == "active")
        new_query = room_join_location(active_rooms)
        result = new_query.filter(BlockModel.id == block_id)
        return result


class Mutation(graphene.ObjectType):
    create_block = CreateBlock.Field(
        description="Creates a new block given the arguments\
            \n- state: Check if the block is created\
            \n- name: The name field of the block[required]\
            \n- office_id: The unique identifier of the office where the \
            block is found[required]")
    update_block = UpdateBlock.Field(
        description="Updates a block given the arguments\
            \n- name: The name field of the block[required]\
            \n- block_id: The unique identifier of the block[required]")
    Delete_block = DeleteBlock.Field(
        description="Deletes a given block given the arguments\
            \n- block_id: The unique identifier of the block[required]\
            \n- state: Check if the block is active, archived or deleted")
