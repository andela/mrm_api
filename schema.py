import graphene
import api.room.schema
import api.room_resource.schema


class Query(
    api.room.schema.Query,
    api.room_resource.schema.Query
):
    pass


class Mutation(
    api.room.schema.Mutation,
    api.room_resource.schema.Mutation
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
