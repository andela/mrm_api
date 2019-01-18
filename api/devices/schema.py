import graphene
from graphql import GraphQLError
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func

from api.devices.models import Devices as DevicesModel
from utilities.validations import validate_empty_fields, update_entity_fields


class Devices(SQLAlchemyObjectType):
    class Meta:
        model = DevicesModel


class CreateDevice(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        device_type = graphene.String(required=True)
        location = graphene.String()
        resource_id = graphene.Int(required=True)
    device = graphene.Field(Devices)

    def mutate(self, info, **kwargs):
        device = DevicesModel(
            **kwargs,
            date_added=datetime.now(),
            last_seen=datetime.now()
        )
        device.save()

        return CreateDevice(device=device)


class UpdateDevice(graphene.Mutation):
    class Arguments:
        device_id = graphene.Int()
        name = graphene.String()
        device_type = graphene.String()
        location = graphene.String()
        resource_id = graphene.Int()
    device = graphene.Field(Devices)

    def mutate(self, info, device_id, **kwargs):
        validate_empty_fields(**kwargs)

        query_device = Devices.get_query(info)
        exact_device = query_device.filter(
            DevicesModel.id == device_id
            ).first()
        if not exact_device:
            raise GraphQLError("DeviceId not found")
        exact_device.date_added = datetime.now()
        exact_device.last_seen = datetime.now()
        update_entity_fields(exact_device, **kwargs)

        exact_device.save()
        return UpdateDevice(device=exact_device)


class Query(graphene.ObjectType):
    all_devices = graphene.List(Devices)

    def resolve_all_devices(self, info):
        query = Devices.get_query(info)
        return query.order_by(func.lower(DevicesModel.name)).all()


class Mutation(graphene.ObjectType):
    create_device = CreateDevice.Field()
    update_device = UpdateDevice.Field()
