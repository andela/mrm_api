import graphene
from math import ceil


class Paginate(graphene.ObjectType):
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()

    def __init__(self, **kwargs):
        self.page = kwargs.pop('page', None)
        self.per_page = kwargs.pop('per_page', None)
        self.unique = kwargs.pop('unique', None)
        self.query_total
        self.pages
        self.filter_data = {}
        self.filter_data.update(**kwargs)

    def resolve_pages(self, pages):
        if self.per_page:
            self.pages = ceil(self.query_total / self.per_page)
        pages = self.pages
        return pages

    def resolve_has_next(self, has_next):
        if self.page:
            page = self.page
            pages = self.pages
            pages = self.resolve_pages(pages)
            if page < pages:
                has_next = True
            else:
                has_next = False
        return has_next

    def resolve_has_previous(self, has_previous):
        if self.page:
            page = self.page
            pages = self.resolve_pages(self.pages)
            if (page > 1) and (pages > 1) and (page <= pages):
                has_previous = True
            else:
                has_previous = False

        return has_previous
