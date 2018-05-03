import graphene

import api.room.schema
import api.user.schema
import api.room_resource.schema
import api.room_resource.schema



class Query(
    api.room.schema.Query,
    api.user.schema.Query,
    api.room_resource.schema.Query
):
    pass


class Mutation(
    api.room.schema.Mutation,
    api.user.schema.Mutation,
    api.room_resource.schema.Mutation
):
    pass

admin_schema = graphene.Schema(query=Query, mutation=Mutation)
