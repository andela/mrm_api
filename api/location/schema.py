import graphene
from sqlalchemy import func, exc
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.location.models import Location as LocationModel
from utilities.validator import ErrorHandler

from api.devices.models import Devices as DevicesModel  # noqa: F401
from api.room.models import Room as RoomModel
from api.room_resource.models import Resource as ResourceModel  # noqa: F401
from api.room.schema import Room
from utilities.validations import (
    validate_empty_fields,
    validate_url,
    validate_country_field,
    validate_timezone_field)
from utilities.utility import update_entity_fields
from helpers.room_filter.room_filter import room_join_location
from helpers.auth.authentication import Auth
from helpers.auth.error_handler import SaveContextManager
from helpers.auth.admin_roles import admin_roles


class Location(SQLAlchemyObjectType):
    class Meta:
        model = LocationModel


class CreateLocation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        abbreviation = graphene.String(required=True)
        country = graphene.String(required=True)
        image_url = graphene.String()
        time_zone = graphene.String(required=True)
        state = graphene.String()
    location = graphene.Field(Location)

    @Auth.user_roles('Admin')
    def mutate(self, info, **kwargs):
        # Validate if the country given is a valid country
        try:
            validate_country_field(**kwargs)
            validate_timezone_field(**kwargs)
            location = LocationModel(**kwargs)
            payload = {
                'model': LocationModel, 'field': 'name',
                'value':  kwargs['name']
                }
            query = Location.get_query(info)
            result = query.filter(LocationModel.state == "active")
            location_name = result.filter(
                func.lower(LocationModel.name) ==
                func.lower(kwargs['name'])).count()
            if location_name > 0:
                ErrorHandler.check_conflict(self, kwargs['name'], 'Location')
            with SaveContextManager(location, 'Location', payload):
                return CreateLocation(location=location)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class UpdateLocation(graphene.Mutation):
    class Arguments:
        location_id = graphene.Int()
        name = graphene.String()
        abbreviation = graphene.String()
        country = graphene.String()
        image_url = graphene.String()
        time_zone = graphene.String()
    location = graphene.Field(Location)

    @Auth.user_roles('Admin')
    def mutate(self, info, location_id, **kwargs):
        try:
            location = Location.get_query(info)
            result = location.filter(LocationModel.state == "active")
            location_object = result.filter(
                LocationModel.id == location_id).first()
            if not location_object:
                raise GraphQLError("Location not found")
            admin_roles.verify_admin_location(location_id)
            if "time_zone" in kwargs:
                validate_timezone_field(**kwargs)
            if "country" in kwargs:
                validate_country_field(**kwargs)
            if "image_url" in kwargs:
                validate_url(**kwargs)
            if "abbreviation" in kwargs:  # noqa
                validate_empty_fields(**kwargs)
            active_locations = result.filter(
                LocationModel.name == kwargs.get('name'))
            if active_locations:
                pass
            else:
                raise AttributeError("Not a valid location")
            update_entity_fields(location_object, **kwargs)
            location_object.save()
            return UpdateLocation(location=location_object)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class DeleteLocation(graphene.Mutation):
    class Arguments:
        location_id = graphene.Int(required=True)
        state = graphene.String()

    location = graphene.Field(Location)

    @Auth.user_roles('Admin')
    def mutate(self, info, location_id, **kwargs):
        try:
            query = Location.get_query(info)
            result = query.filter(LocationModel.state == "active")
            location = result.filter(
                LocationModel.id == location_id).first()  # noqa: E501
            if not location:
                raise GraphQLError("location not found")
            admin_roles.verify_admin_location(location_id)
            update_entity_fields(location, state="archived", **kwargs)
            location.save()
            return DeleteLocation(location=location)
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Query(graphene.ObjectType):
    all_locations = graphene.List(Location)
    get_rooms_in_a_location = graphene.List(
        lambda: Room,
        location_id=graphene.Int()
    )

    def resolve_all_locations(self, info):
        try:
            query = Location.get_query(info)
            result = query.filter(LocationModel.state == "active")
            return result.order_by(func.lower(LocationModel.name)).all()
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")

    def resolve_get_rooms_in_a_location(self, info, location_id):
        try:
            query = Room.get_query(info)
            active_rooms = query.filter(RoomModel.state == "active")
            exact_query = room_join_location(active_rooms)
            result = exact_query.filter(LocationModel.id == location_id)
            return result.all()
        except exc.ProgrammingError:
            raise GraphQLError("There seems to be a database connection error, \
                contact your administrator for assistance")


class Mutation(graphene.ObjectType):
    create_location = CreateLocation.Field()
    update_location = UpdateLocation.Field()
    delete_location = DeleteLocation.Field()
