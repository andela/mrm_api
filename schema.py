import graphene

import room.schema


class Query(
    room.schema.Query
):
    pass


class Mutation(
    room.schema.Mutation
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
