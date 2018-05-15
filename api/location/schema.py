import graphene
from graphene import Schema
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.location.models import Location as LocationModel

from api.floor.models import Floor as FloorModel 
from api.room.models import Room as RoomModel

from api.room_resource.models import Resource as ResourceModel 

class Location(SQLAlchemyObjectType):
    class Meta:
        model = LocationModel

class Query(graphene.ObjectType):
    all_locations = graphene.List(Location)
    get_rooms_in_a_location =graphene.List(
        lambda:Location,
        location_id = graphene.Int()
    )


    def resolve_all_locations(self,info):
        query = Location.get_query(info)
        return query.all()

    def resolve_get_rooms_in_a_location(self,info,location_id):
        query =Location.get_query(info)
        result = query.filter(LocationModel.id == location_id)
        return result




