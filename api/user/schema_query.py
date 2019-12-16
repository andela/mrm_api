import graphene
from sqlalchemy import func
from api.user.schema import User
from api.user.models import User as UserModel
from helpers.auth.authentication import Auth
from helpers.user_filter.user_filter import user_filter
from helpers.pagination.paginate import Paginate, validate_page
from api.bugsnag_error import return_error


class PaginatedUsers(Paginate):
    """
        Paginated users data
    """
    users = graphene.List(User)

    def resolve_users(self, info):
        page = self.page
        per_page = self.per_page
        query = User.get_query(info)
        active_user = query.filter(UserModel.state == "active")
        exact_query = user_filter(active_user, self.filter_data)
        if not page:
            return exact_query.order_by(func.lower(UserModel.email)).all()
        page = validate_page(page)
        self.query_total = exact_query.count()
        users = exact_query.order_by(
            func.lower(UserModel.name)).limit(per_page).offset(page * per_page)
        if users.count() == 0:
            return_error.report_errors_bugsnag_and_graphQL("No users found")
        return users


class Query(graphene.ObjectType):
    """
        Returns PaginatedUsers
    """
    users = graphene.Field(
        PaginatedUsers,
        per_page=graphene.Int(),
        role_id=graphene.Int(),
        location_id=graphene.Int(),
        page=graphene.Int(),
        description="Returns a list of paginated users and accepts arguments\
            \n- page: Field with the users page\
            \n- per_page: Field indicating users per page\
            \n- location_id: Field with the unique key of user's location\
            \n- role_id: Field with the unique key of the user role"
    )
    user = graphene.Field(
        lambda: User,
        email=graphene.String(),
        description="Query to get a specific user using the user's email\
            accepts the argument\n- email: Email of a user")

    user_by_name = graphene.List(
        User,
        user_name=graphene.String(),
        description="Returns user details and accepts the argument\
            \n- user_name: The name of the user"
    )

    def resolve_users(self, info, **kwargs):
        # Returns all users
        response = PaginatedUsers(**kwargs)
        return response

    @Auth.user_roles('Admin', 'Default User', 'Super Admin')
    def resolve_user(self, info, email):
        return UserModel.query.filter_by(email=email).first()

    @Auth.user_roles('Admin', 'Super Admin')
    def resolve_user_by_name(self, info, user_name):
        user_list = []
        user_name = ''.join(user_name.split()).lower()
        if not user_name:
            return_error.report_errors_bugsnag_and_graphQL(
                "Please provide the user name")
        active_users = User.get_query(info).filter_by(state="active")
        for user in active_users:
            exact_user_name = user.name.lower().replace(" ", "")
            if user_name in exact_user_name:
                user_list.append(user)
        if not user_list:
            return_error.report_errors_bugsnag_and_graphQL("User not found")

        return user_list
