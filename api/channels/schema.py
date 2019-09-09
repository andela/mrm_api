import graphene
from api.room.models import Room as RoomModel
from api.room.schema import Room


class Channel(graphene.ObjectType):
    """
        Generates return type of Channel
    """
    calendar_id = graphene.String()
    firebase_token = graphene.String()


class Channels(graphene.ObjectType):
    """
        Generates return type of Channels
        a list of all channels
    """
    channels = graphene.List(Channel)


class Query(graphene.ObjectType):
    """
        Queries all notification channels
    """
    all_channels = graphene.Field(
        Channels,
        description="Returns a list of all notification channels"
    )

    def resolve_all_channels(self, info):
        all_rooms = Room.get_query(info).filter(RoomModel.state == "active")

        all_channels = []

        for room in all_rooms:
            channel = Channel(
                calendar_id=room.calendar_id,
                firebase_token=room.firebase_token
            )

            all_channels.append(channel)

        return Channels(channels=all_channels)
