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
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_locations = SQLAlchemyConnectionField(Location)
    get_rooms_in_a_location =graphene.List(
        lambda:Location,
        id = graphene.Int()
    )

    def resolve_get_rooms_in_a_location(self,info,id):
        query =Location.get_query(info)
        result = query.filter(LocationModel.id ==id)
        return result




