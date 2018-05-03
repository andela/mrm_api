"""create table users

Revision ID: 5ba451d1fa9d
Revises: 
Create Date: 2018-04-12 23:08:29.551474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ba451d1fa9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('users')
