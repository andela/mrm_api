import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from api.equipment.models import Equipment as EquipmentModel


class Equipment(SQLAlchemyObjectType):
    
    class Meta:
        model = EquipmentModel
        interfaces = (relay.Node, )