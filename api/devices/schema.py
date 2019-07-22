import graphene
from graphql import GraphQLError
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func, String, cast

from api.devices.models import Devices as DevicesModel
from helpers.auth.authentication import Auth
from api.room.models import Room as RoomModel
from api.location.schema import Location as LocationSchema
from api.location.models import Location as LocationModel
from utilities.validations import validate_empty_fields
from utilities.utility import update_entity_fields
from helpers.room_filter.room_filter import location_join_room
from helpers.auth.user_details import get_user_from_db
from helpers.auth.admin_roles import admin_roles


class Devices(SQLAlchemyObjectType):
    """
        Returns the device payload with the fields
        [id: ID!, name: String!, deviceType: String!,
         dateAdded: DateTime!, lastSeen: DateTime!
    """
    class Meta:
        model = DevicesModel


class CreateDevice(graphene.Mutation):
    """
        Returns the device payload after creating
    """
    class Arguments:
        name = graphene.String(required=True)
        room_id = graphene.Int(required=True)
        device_type = graphene.String(required=True)
    device = graphene.Field(Devices)

    @Auth.user_roles('Admin', 'Super_Admin')
    def mutate(self, info, **kwargs):
        room_location = location_join_room().filter(
            RoomModel.id == kwargs['room_id'],
            RoomModel.state == 'active'
        ).first()
        if not room_location:
            raise GraphQLError("Room not found")
        user = get_user_from_db()
        device = DevicesModel(
            **kwargs,
            date_added=datetime.now(),
            last_seen=datetime.now(),
            location=user.location
        )
        device.save()

        return CreateDevice(device=device)


class UpdateDevice(graphene.Mutation):
    """
         Returns the device payload after updating
    """
    class Arguments:
        device_id = graphene.Int()
        name = graphene.String()
        device_type = graphene.String()
        location = graphene.String()
        room_id = graphene.Int(required=True)
    device = graphene.Field(Devices)

    @Auth.user_roles('Admin', 'Super_Admin')
    def mutate(self, info, device_id, **kwargs):
        validate_empty_fields(**kwargs)

        query_device = Devices.get_query(info)
        exact_device = query_device.filter(
            DevicesModel.id == device_id
        ).first()
        if not exact_device:
            raise GraphQLError("Device ID not found")
        update_entity_fields(exact_device, **kwargs)

        exact_device.save()
        return UpdateDevice(device=exact_device)


class DeleteDevice(graphene.Mutation):
    """
         Returns device payload on deleting a device
    """
    class Arguments:
        device_id = graphene.Int(required=True)
        state = graphene.String()

    device = graphene.Field(Devices)

    @Auth.user_roles('Admin')
    def mutate(self, info, device_id, **kwargs):
        query_device = Devices.get_query(info)
        result = query_device.filter(DevicesModel.state == "active")
        exact_device = result.filter(
            DevicesModel.id == device_id
        ).first()
        if not exact_device:
            raise GraphQLError("Device not found")
        update_entity_fields(exact_device, state="archived", **kwargs)
        exact_device.save()
        return DeleteDevice(device=exact_device)


class Query(graphene.ObjectType):
    """
        Query to get list of all devices
    """
    all_devices = graphene.List(
        Devices,
        device_labels=graphene.String(),
        description="Query that returns a list of all devices,\
        if device_labels is passed, it filters devices with the device labels\
        \n- device_labels: A string of labels to filter with")

    specific_device = graphene.Field(
        Devices,
        device_id=graphene.Int(),
        description="Returns device details and accepts the argument\
            \n- device_id: A unique identifier of the device"
    )

    device_by_name = graphene.List(
        Devices,
        device_name=graphene.String(),
        description="Returns device details and accepts the argument\
            \n- device_name: The name of the device"
    )

    def resolve_all_devices(self, info, **kwargs):
        device_labels = kwargs.get('device_labels')
        query = Devices.get_query(info)
        location_id = admin_roles.user_location_for_analytics_view()
        location_query = LocationSchema.get_query(info)
        exact_location = location_query.filter(
            LocationModel.state == "active",
            LocationModel.id == location_id).first()
        location_name = exact_location.name.lower()
        all_devices = query.filter(
            func.lower(DevicesModel.location) == location_name,
            DevicesModel.state == "active")

        if device_labels:
            all_devices = all_devices.join(RoomModel)
            for device_label in device_labels.split(','):
                all_devices = all_devices.filter(
                    cast(RoomModel.room_labels, String)
                    .ilike(f'%{device_label.strip()}%'))
        return all_devices

    @Auth.user_roles('Admin', 'Super_Admin')
    def resolve_specific_device(self, info, device_id):
        query = Devices.get_query(info)
        device = query.filter(DevicesModel.id == device_id).first()

        if not device:
            raise GraphQLError("Device not found")

        return device

    @Auth.user_roles('Admin', 'Super_Admin')
    def resolve_device_by_name(self, info, device_name):
        devices = Devices.get_query(info)
        device_name = ''.join(device_name.split()).lower()
        if not device_name:
            raise GraphQLError("Please provide the device name")
        found_devices = []
        for device in devices:
            exact_name = ''.join(device.name.split()).lower()
            if device_name in exact_name:
                found_devices.append(device)
        return found_devices


class Mutation(graphene.ObjectType):
    create_device = CreateDevice.Field(
        description="Creates a new device with the arguments\
            \n- device_name: The name field of the device[required]\
            \n- room_id: Unique identifier of a room where the device is found\
            [required]\n- device_type: The type field of the device[required]")
    update_device = UpdateDevice.Field(
        description="Updates a given device details given the arguments\
            \n- device_id: Unique identifier of the tag\
            \n- name: The name field of the device\
            \n- device_type: The type field of the device\
            \n- location: The location of the device\
            \n- room_id: Unique identifier of a room where the device is found\
            [required]")
    delete_device = DeleteDevice.Field(
        description="Deletes a given device given the arguments to delete\
            \n- device_id: Unique identifier of the tag\
            [required]"
    )
