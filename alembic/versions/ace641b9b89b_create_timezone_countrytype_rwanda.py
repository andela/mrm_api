"""create-timezone-countrytype-Rwanda

Revision ID: ace641b9b89b
Revises: 964435a2570d
Create Date: 2019-09-05 13:02:37.703150

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ace641b9b89b'
down_revision = '964435a2570d'
branch_labels = None
depends_on = None


def upgrade():
    timezone_type = postgresql.ENUM('EAST_AFRICA_TIME', 'WEST_AFRICA_TIME','CENTRAL_AFRICA_TIME', name='timezone_type')
    country_type = postgresql.ENUM('Uganda', 'Kenya', 'Nigeria','Rwanda', name='country_type')

    op.alter_column('locations', 'country', existing_type=sa.Enum('Uganda', 'Kenya', 'Nigeria', name='country_type'), type_=sa.VARCHAR())
    country_type.drop(op.get_bind())
    country_type.create(op.get_bind())
    op.alter_column('locations', 'country', existing_type=sa.VARCHAR(), type_=country_type, postgresql_using='country::country_type')

    op.alter_column('locations', 'time_zone', existing_type=sa.Enum('EAST_AFRICA_TIME', 'WEST_AFRICA_TIME', name='timezone_type'),type_=sa.VARCHAR())
    timezone_type.drop(op.get_bind())
    timezone_type.create(op.get_bind())
    op.alter_column('locations', 'time_zone', existing_type=sa.Enum('EAST_AFRICA_TIME', 'WEST_AFRICA_TIME',
                    name='timezone_type'), type_=timezone_type , postgresql_using='time_zone::timezone_type')


def downgrade():
    timezone_type = postgresql.ENUM('EAST_AFRICA_TIME', 'WEST_AFRICA_TIME', name='timezone_type')
    country_type = postgresql.ENUM('Uganda', 'Kenya', 'Nigeria', name='country_type')

    op.alter_column('locations', 'country', existing_type=sa.Enum('Uganda', 'Kenya', 'Nigeria','Rwanda', name='country_type'), type_=sa.VARCHAR())
    country_type.drop(op.get_bind())
    country_type.create(op.get_bind())
    op.alter_column('locations', 'country', existing_type=sa.VARCHAR(), type_=country_type, postgresql_using='country::country_type')

    op.alter_column('locations', 'time_zone', existing_type=sa.Enum('EAST_AFRICA_TIME', 'WEST_AFRICA_TIME', 'CENTRAL_AFRICA_TIME', name='timezone_type'),type_=sa.VARCHAR())
    timezone_type.drop(op.get_bind())
    timezone_type.create(op.get_bind())
    op.alter_column('locations', 'time_zone', existing_type=sa.Enum('EAST_AFRICA_TIME', 'WEST_AFRICA_TIME',
                    name='timezone_type'), type_=timezone_type , postgresql_using='time_zone::timezone_type')