import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.room_resource.models import Resource as ResourceModel


class Resource(SQLAlchemyObjectType):
    
    class Meta:
        model = ResourceModel