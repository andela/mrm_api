import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)

from api.room.models import Room as RoomModel


class Room(SQLAlchemyObjectType):
    class Meta:
        model = RoomModel


class Query(graphene.ObjectType):
    rooms = graphene.List(Room)

    def resolve_rooms(self, info):
        query = Room.get_query(info)
        res = query.all()
        return res


healthcheck_schema = graphene.Schema(query=Query)
