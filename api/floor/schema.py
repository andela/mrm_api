import graphene

from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from helpers.auth.authentication import Auth
from helpers.auth.admin_roles import admin_roles
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from utilities.validator import ErrorHandler
from helpers.pagination.paginate import Paginate, validate_page
from api.block.models import Block
from api.floor.models import Floor as FloorModel
from api.room.models import Room as RoomModel
from api.room.schema import Room


class Floor(SQLAlchemyObjectType):
    class Meta:
        model = FloorModel


class CreateFloor(graphene.Mutation):

    class Arguments:
        state = graphene.String()
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

        admin_roles.create_floor_update_delete_block(kwargs['block_id'])
        result = query_block.filter(
            Block.id == kwargs['block_id'],
            FloorModel.name == kwargs.get('name').capitalize(),
            FloorModel.state == 'active'
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
        active_rooms = query_floor.filter(FloorModel.state == "active")
        exact_floor = active_rooms.filter(FloorModel.id == floor_id).first()
        if not exact_floor:
            raise GraphQLError("Floor not found")

        admin_roles.update_delete_floor(floor_id)
        result = query_floor.filter(
            FloorModel.block_id == exact_floor.block_id,
            FloorModel.name == kwargs.get('name').capitalize(),
            FloorModel.state == 'active'
        )
        if result.count() > 0:
            ErrorHandler.check_conflict(self, kwargs['name'], 'Floor')

        update_entity_fields(exact_floor, **kwargs)
        exact_floor.save()
        return UpdateFloor(floor=exact_floor)


class DeleteFloor(graphene.Mutation):

    class Arguments:
        state = graphene.String()
        floor_id = graphene.Int(required=True)
    floor = graphene.Field(Floor)

    @Auth.user_roles('Admin')
    def mutate(self, info, floor_id, **kwargs):
        query_floor = Floor.get_query(info)
        active_rooms = query_floor.filter(FloorModel.state == "active")
        exact_floor = active_rooms.filter(
            FloorModel.id == floor_id).first()
        if not exact_floor:
            raise GraphQLError("Floor not found")

        admin_roles.update_delete_floor(floor_id)
        update_entity_fields(exact_floor, state="archived", **kwargs)
        exact_floor.save()
        return DeleteFloor(floor=exact_floor)


class PaginatedFloors(Paginate):
    floors = graphene.List(Floor)

    def resolve_floors(self, info, **kwargs):
        ''' This function paginates the returned response
        if page parameter is passed,
        otherwise it returns all floors
        '''
        page = self.page
        per_page = self.per_page
        query = Floor.get_query(info)
        active_rooms = query.filter(FloorModel.state == "active")
        if not page:
            return active_rooms.order_by(FloorModel.name).all()
        page = validate_page(page)
        self.query_total = active_rooms.count()
        result = active_rooms.order_by(
            FloorModel.name).limit(per_page).offset(page*per_page)
        if result.count() == 0:
            return GraphQLError("No more resources")
        return result


class Query(graphene.ObjectType):
    all_floors = graphene.Field(
        PaginatedFloors,
        page=graphene.Int(),
        per_page=graphene.Int(),
        name=graphene.String()
    )
    get_rooms_in_a_floor = graphene.List(
        lambda: Room,
        floor_id=graphene.Int()
    )
    filter_by_block = graphene.List(Floor, blockId=graphene.Int())

    def resolve_all_floors(self, info, **kwargs):
        response = PaginatedFloors(**kwargs)
        return response

    def resolve_get_rooms_in_a_floor(self, info, floor_id):
        query = Room.get_query(info)
        active_rooms = query.filter(RoomModel.state == "active")
        rooms = active_rooms.filter(RoomModel.floor_id == floor_id)
        return rooms

    @Auth.user_roles('Admin')
    def resolve_filter_by_block(self, info, blockId):
        query = Floor.get_query(info)
        floors = query.filter_by(block_id=blockId)
        if floors.count() < 1:
            raise GraphQLError('Floors not found in this block')
        return floors


class Mutation(graphene.ObjectType):
    create_floor = CreateFloor.Field()
    update_floor = UpdateFloor.Field()
    delete_floor = DeleteFloor.Field()
