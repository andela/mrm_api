"""refactor code structure

Revision ID: ee5c60d6b79c
Revises: 67e294b4271c
Create Date: 2019-02-28 15:05:32.292747

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ee5c60d6b79c'
down_revision = '67e294b4271c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('rooms_floor_id_fkey', 'rooms', type_='foreignkey')
    op.drop_constraint('rooms_wing_id_fkey', 'rooms', type_='foreignkey')
    op.drop_column('rooms', 'wing_id')
    op.drop_column('rooms', 'floor_id')
    op.drop_index('ix_unique_wing_content', table_name='wings')
    op.drop_table('wings')
    op.drop_index('ix_unique_floor_content', table_name='floors')
    op.drop_table('floors')
    op.drop_index('ix_unique_block_content', table_name='blocks')
    op.drop_table('blocks')
    op.drop_index('ix_unique_office_content', table_name='offices')
    op.drop_table('offices')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offices',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('offices_id_seq'::regclass)"), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('location_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('state', postgresql.ENUM('active', 'archived', 'deleted', name='statetype'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name='offices_location_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='offices_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_unique_office_content', 'offices', ['name'], unique=True)
    op.create_table('blocks',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('blocks_id_seq'::regclass)"), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('office_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('state', postgresql.ENUM('active', 'archived', 'deleted', name='statetype'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['office_id'], ['offices.id'], name='blocks_office_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='blocks_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_unique_block_content', 'blocks', ['name'], unique=True)
    op.create_table('floors',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('block_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('state', postgresql.ENUM('active', 'archived', 'deleted', name='statetype'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['blocks.id'], name='floors_block_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='floors_pkey')
    )
    op.create_index('ix_unique_floor_content', 'floors', ['name'], unique=True)
    op.create_table('wings',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('floor_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('state', postgresql.ENUM('active', 'archived', 'deleted', name='statetype'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['floor_id'], ['floors.id'], name='wings_floor_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='wings_pkey')
    )
    op.create_index('ix_unique_wing_content', 'wings', ['name'], unique=True)
    op.add_column('rooms', sa.Column('floor_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('rooms', sa.Column('wing_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('rooms_wing_id_fkey', 'rooms', 'wings', ['wing_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('rooms_floor_id_fkey', 'rooms', 'floors', ['floor_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
