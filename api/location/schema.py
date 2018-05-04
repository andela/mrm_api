import graphene
from graphene import relay,Schema
from graphene_sqlalchemy import (
    SQLAlchemyObjectType, 
    SQLAlchemyConnectionField
)

from api.location.models import Location as LocationModel

from api.floor.models import Floor as FloorModel 
from api.room.models import Room as RoomModel

from api.equipment.models import Equipment 

class Location(SQLAlchemyObjectType):
    class Meta:
        model = LocationModel

class Query(graphene.ObjectType):
    node = relay.Node.Field()
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




