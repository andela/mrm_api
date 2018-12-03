import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from utilities.utility import validate_empty_fields, update_entity_fields
from helpers.auth.validator import ErrorHandler
from api.block.models import Block
from api.floor.models import Floor as FloorModel
from api.room.models import Room as RoomModel
from api.room.schema import Room


class Floor(SQLAlchemyObjectType):
    class Meta:
        model = FloorModel


class CreateFloor(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        block_id = graphene.Int(required=True)
    floor = graphene.Field(Floor)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        get_block = Block.query.filter_by(id=kwargs['block_id']).first()
        if not get_block:
            raise GraphQLError("Block not found")
        query = Floor.get_query(info)
        query_block = query.join(Block.floors)

        admin_roles.create_floor(kwargs['block_id'])
        result = query_block.filter(
            Block.id == kwargs['block_id'],
            FloorModel.name == kwargs.get('name').capitalize()
        )
        if result.count() > 0:
            ErrorHandler.check_conflict(self, kwargs['name'], 'Floor')

        floor = FloorModel(**kwargs)
        floor.save()
        return CreateFloor(floor=floor)


class UpdateFloor(graphene.Mutation):

    class Arguments:
        floor_id = graphene.Int(required=True)
        name = graphene.String(required=True)
    floor = graphene.Field(Floor)

    @Auth.user_roles('Admin')
    def mutate(self, info, floor_id, **kwargs):
        validate_empty_fields(**kwargs)
        query_floor = Floor.get_query(info)
        exact_floor = query_floor.filter(FloorModel.id == floor_id).first()
        if not exact_floor:
            raise GraphQLError("Floor not found")

        admin_roles.update_delete_floor(floor_id)
        result = query_floor.filter(
            FloorModel.block_id == exact_floor.block_id,
            FloorModel.name == kwargs.get('name').capitalize()
        )
        if result.count() > 0:
            ErrorHandler.check_conflict(self, kwargs['name'], 'Floor')

        update_entity_fields(exact_floor, **kwargs)
        exact_floor.save()
        return UpdateFloor(floor=exact_floor)


class DeleteFloor(graphene.Mutation):

    class Arguments:
        floor_id = graphene.Int(required=True)
    floor = graphene.Field(Floor)

    @Auth.user_roles('Admin')
    def mutate(self, info, floor_id, **kwargs):
        query_floor = Floor.get_query(info)
        exact_floor = query_floor.filter(
            FloorModel.id == floor_id).first()
        if not exact_floor:
            raise GraphQLError("Floor not found")

        admin_roles.update_delete_floor(floor_id)
        exact_floor.delete()
        return DeleteFloor(floor=exact_floor)


class Query(graphene.ObjectType):
    all_floors = graphene.List(Floor)
    get_rooms_in_a_floor = graphene.List(
        lambda: Room,
        floor_id=graphene.Int()
    )

    def resolve_all_floors(self, info):
        query = Floor.get_query(info)
        return query.all()

    def resolve_get_rooms_in_a_floor(self, info, floor_id):
        query = Room.get_query(info)
        rooms = query.filter(RoomModel.floor_id == floor_id)
        return rooms


class Mutation(graphene.ObjectType):
    create_floor = CreateFloor.Field()
    update_floor = UpdateFloor.Field()
    delete_floor = DeleteFloor.Field()
