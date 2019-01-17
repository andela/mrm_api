import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.location.models import Location as LocationModel

from api.devices.models import Devices as DevicesModel  # noqa: F401
from api.room_resource.models import Resource as ResourceModel  # noqa: F401
from api.room.schema import Room
from utilities.utility import validate_country_field, validate_timezone_field, update_entity_fields, validate_empty_fields, validate_url  # noqa: E501
from helpers.room_filter.room_filter import room_join_location


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
    location = graphene.Field(Location)

    def mutate(self, info, **kwargs):
        # Validate if the country given is a valid country
        validate_country_field(**kwargs)
        validate_timezone_field(**kwargs)
        validate_url(**kwargs)
        location = LocationModel(**kwargs)
        location.save()
        return CreateLocation(location=location)


class UpdateLocation(graphene.Mutation):
    class Arguments:
        location_id = graphene.Int()
        name = graphene.String()
        abbreviation = graphene.String()
        country = graphene.String()
        image_url = graphene.String()
        time_zone = graphene.String()
    location = graphene.Field(Location)

    def mutate(self, info, location_id, **kwargs):
        location = Location.get_query(info)
        location_object = location.filter(
            LocationModel.id == location_id).first()
        if not location_object:
            raise GraphQLError("Location not found")
        if "time_zone" in kwargs:
            validate_timezone_field(**kwargs)
        if "country" in kwargs:
            validate_country_field(**kwargs)
        if "image_url" in kwargs:
            validate_url(**kwargs)
        if "abbreviation" in kwargs:  # noqa
            validate_empty_fields(**kwargs)
        result = location.filter(LocationModel.name == kwargs.get('name'))
        if result.count() > 0:
            pass
        else:
            raise AttributeError("Not a valid location")
        update_entity_fields(location_object, **kwargs)
        location_object.save()
        return UpdateLocation(location=location_object)


class Query(graphene.ObjectType):
    all_locations = graphene.List(Location)
    get_rooms_in_a_location = graphene.List(
        lambda: Room,
        location_id=graphene.Int()
    )

    def resolve_all_locations(self, info):
        query = Location.get_query(info)
        return query.all()

    def resolve_get_rooms_in_a_location(self, info, location_id):
        query = Room.get_query(info)
        exact_query = room_join_location(query)
        result = exact_query.filter(LocationModel.id == location_id)
        return result.all()


class Mutation(graphene.ObjectType):
    create_location = CreateLocation.Field()
    update_location = UpdateLocation.Field()
