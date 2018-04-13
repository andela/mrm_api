import graphene

from graphene import relay, Schema
from graphene_sqlalchemy import (SQLAlchemyObjectType, 
                                 SQLAlchemyConnectionField)

from equipment.models import Equipment as EquipmentModel


class Equipment(SQLAlchemyObjectType):
    
    class Meta:
        model = EquipmentModel
        interfaces = (relay.Node, )