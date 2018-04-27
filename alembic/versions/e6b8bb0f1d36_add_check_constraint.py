"""Add check constraint

Revision ID: e6b8bb0f1d36
Revises: 
Create Date: 2018-04-20 15:25:32.814657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6b8bb0f1d36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('abbreviation', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('floors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['blocks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('room_type', sa.String(), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('floor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['floor_id'], ['floors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipments')
    op.drop_table('rooms')
    op.drop_table('floors')
    op.drop_table('blocks')
    op.drop_table('locations')
    # ### end Alembic commands ###
