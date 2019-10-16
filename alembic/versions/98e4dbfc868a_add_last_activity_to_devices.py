"""Add_last_activity_to_devices

Revision ID: 98e4dbfc868a
Revises: ace641b9b89b
Create Date: 2019-10-15 09:22:19.847309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98e4dbfc868a'
down_revision = 'ace641b9b89b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('devices', sa.Column('last_activity', sa.String(), nullable=True))


def downgrade():
    op.drop_column('devices', 'last_activity')
