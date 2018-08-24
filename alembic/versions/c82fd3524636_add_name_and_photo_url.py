"""add name and photo url

Revision ID: c82fd3524636
Revises: 127ff4285598
Create Date: 2018-08-23 15:08:03.401316


"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c82fd3524636'
down_revision = '127ff4285598'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(), nullable=False))
    op.add_column('users', sa.Column('picture', sa.String()))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'picture')
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
