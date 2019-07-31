from graphql import GraphQLError
from helpers.auth.user_details import get_user_from_db
from api.role.models import Role as RoleModel


def check_admin_restriction(new_role):
    '''
        Restricting users who is not a super admin
        from assigning the role 'super Admin.'
    '''
    admin_details = get_user_from_db()
    admin_role = RoleModel.query.filter_by(
        id=admin_details.roles[0].id).first()
    if admin_role.role != 'Super Admin' and new_role == 'Super Admin':
        raise GraphQLError('You are not authorized to assign this role')
