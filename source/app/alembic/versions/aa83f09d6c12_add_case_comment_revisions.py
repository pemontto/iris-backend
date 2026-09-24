"""add revisions to case comments

Revision ID: aa83f09d6c12
Revises: c3f8a1d62e04
Create Date: 2026-09-24

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'aa83f09d6c12'
down_revision = 'c3f8a1d62e04'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'comments',
        sa.Column('comment_revisions', postgresql.JSONB(), nullable=False, server_default=sa.text("'[]'::jsonb")),
    )


def downgrade():
    op.drop_column('comments', 'comment_revisions')
