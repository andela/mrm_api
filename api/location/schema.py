import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from api.location.models import Location as LocationModel

from api.devices.models import Devices as DevicesModel  # noqa: F401
from graphql import GraphQLError
from api.room_resource.models import Resource as ResourceModel  # noqa: F401
from utilities.utility import validate_country_field, validate_timezone_field


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
        location = LocationModel(**kwargs)
        location.save()
        return CreateLocation(location=location)


class Query(graphene.ObjectType):
    all_locations = graphene.List(Location)
    get_rooms_in_a_location = graphene.List(
        lambda: Location,
        location_id=graphene.Int()
    )

    def resolve_all_locations(self, info):
        query = Location.get_query(info)
        return query.all()

    def resolve_get_rooms_in_a_location(self, info, location_id):
        query = Location.get_query(info)
        result = query.filter(LocationModel.id == location_id)
        return result


class Mutation(graphene.ObjectType):
    create_location = CreateLocation.Field()
