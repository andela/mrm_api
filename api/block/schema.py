import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func, exc
from api.block.models import Block as BlockModel
from api.room.schema import Room
from api.office.models import Office
from api.room.models import Room as RoomModel
from helpers.room_filter.room_filter import room_join_location
from helpers.auth.admin_roles import admin_roles
from utilities.validations import validate_empty_fields
from utilities.validator import ErrorHandler
from utilities.utility import update_entity_fields
from helpers.auth.authentication import Auth
from helpers.auth.error_handler import SaveContextManager


class Block(SQLAlchemyObjectType):
    class Meta:
        model = BlockModel


class CreateBlock(graphene.Mutation):
    class Arguments:
        state = graphene.String()
        name = graphene.String(required=True)
        office_id = graphene.Int(required=True)
    block = graphene.Field(Block)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        try:
            validate_empty_fields(**kwargs)
            get_office = Office.query.filter_by(id=kwargs['office_id']).first()
            if not get_office:
                raise GraphQLError("Office not found")
            location = get_office.location.name
            if location.lower() == 'nairobi':
                block = BlockModel(**kwargs)
                payload = {
                    'model': BlockModel, 'field': 'name',
                    'value':  kwargs['name']
                }
                query = Block.get_query(info)
                result = query.filter(BlockModel.state == "active")
                block_name = result.filter(
                    func.lower(BlockModel.name) ==
                    func.lower(kwargs['name'])).count()
                if block_name > 0:
                    ErrorHandler.check_conflict(self, kwargs['name'], 'Block')
                with SaveContextManager(
                    block, 'Block', payload
                ):
                    return CreateBlock(block=block)
            else:
                raise GraphQLError("You can only create block in Nairobi")
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class UpdateBlock(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        block_id = graphene.Int(required=True)

    block = graphene.Field(Block)

    @Auth.user_roles("Admin")
    def mutate(self, info, block_id, **kwargs):
        try:
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
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class DeleteBlock(graphene.Mutation):
    class Arguments:
        block_id = graphene.Int(required=True)
        state = graphene.String()

    block = graphene.Field(Block)

    @Auth.user_roles("Admin")
    def mutate(self, info, block_id, **kwargs):
        try:
            query = Block.get_query(info)
            result = query.filter(BlockModel.state == "active")
            exact_block = result.filter(BlockModel.id == block_id).first()
            if not exact_block:
                raise GraphQLError("Block not found")

            admin_roles.create_floor_update_delete_block(block_id)
            update_entity_fields(exact_block, state="archived", **kwargs)
            exact_block.save()
            return DeleteBlock(block=exact_block)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Query(graphene.ObjectType):
    all_blocks = graphene.List(Block)
    get_rooms_in_a_block = graphene.List(
        lambda: Room,
        block_id=graphene.Int()
    )

    def resolve_all_blocks(self, info):
        try:
            query = Block.get_query(info)
            result = query.filter(BlockModel.state == "active")
            return result.order_by(func.lower(BlockModel.name)).all()
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")

    def resolve_get_rooms_in_a_block(self, info, block_id):
        try:
            query = Room.get_query(info)
            active_rooms = query.filter(RoomModel.state == "active")
            new_query = room_join_location(active_rooms)
            result = new_query.filter(BlockModel.id == block_id)
            return result
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Mutation(graphene.ObjectType):
    create_block = CreateBlock.Field()
    update_block = UpdateBlock.Field()
    Delete_block = DeleteBlock.Field()
