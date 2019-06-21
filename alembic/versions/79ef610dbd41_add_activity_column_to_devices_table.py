"""add activity column to devices table

Revision ID: 79ef610dbd41
Revises: a36af2be7b0c
Create Date: 2019-06-28 08:05:37.542613

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision = '79ef610dbd41'
down_revision = 'a36af2be7b0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    activitytype = postgresql.ENUM(
        'online', 'offline', name='activitytype')
    activitytype.create(op.get_bind())
    op.add_column('devices', sa.Column('activity', sa.Enum('online', 'offline', name='activitytype'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('devices', 'activity')
    # ### end Alembic commands ###
