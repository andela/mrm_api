"""include cascading deletion on room tags

Revision ID: c058d462a21d
Revises: 98e4dbfc868a
Create Date: 2019-11-04 17:45:56.163962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c058d462a21d'
down_revision = '98e4dbfc868a'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('room_tags_tag_id_fkey',
                       'room_tags', type_='foreignkey')
    op.create_foreign_key(None, 'room_tags', 'tags', [
                          'tag_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('room_tags_room_id_fkey',
                       'room_tags', type_='foreignkey')
    op.create_foreign_key(None, 'room_tags', 'rooms', [
                          'room_id'], ['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('room_tags_room_id_fkey',
                       'room_tags', type_='foreignkey')
    op.create_foreign_key('room_tags_room_id_fkey', 'room_tags',
                          'rooms', ['room_id'], ['id'])
    op.drop_constraint('room_tags_tag_id_fkey', 'room_tags', type_='foreignkey')
    op.create_foreign_key('room_tags_tag_id_fkey', 'room_tags',
                          'tags', ['tag_id'], ['id'])
