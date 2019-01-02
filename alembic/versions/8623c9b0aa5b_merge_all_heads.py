"""merge all heads

Revision ID: 8623c9b0aa5b
Revises: b45e82fc1a6b, 420bfd812496, bf07b4a2605c
Create Date: 2019-01-02 13:13:58.030083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8623c9b0aa5b'
down_revision = ('b45e82fc1a6b', '420bfd812496', 'bf07b4a2605c')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
