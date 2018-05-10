import graphene

from graphene import Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from api.room_resource.models import Resource as ResourceModel


class Resource(SQLAlchemyObjectType):
    
    class Meta:
        model = ResourceModel

    def resolve_Resource(self,info):
        query = Resource.get_query(info)
        return query.all()
