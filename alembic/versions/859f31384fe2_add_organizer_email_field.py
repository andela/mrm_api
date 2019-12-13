"""add organizer email field

Revision ID: 859f31384fe2
Revises: c058d462a21d
Create Date: 2019-11-18 09:26:07.682060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '859f31384fe2'
down_revision = 'c058d462a21d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('events', sa.Column(
        'organizer_email', sa.String(), nullable=True))


def downgrade():
    op.drop_column('events', 'organizer_email')
