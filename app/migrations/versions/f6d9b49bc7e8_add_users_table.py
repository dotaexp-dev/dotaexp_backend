"""add_users_table

Revision ID: f6d9b49bc7e8
Revises: c3f2aaca0b88
Create Date: 2024-07-03 07:44:28.422320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6d9b49bc7e8'
down_revision: Union[str, None] = 'c3f2aaca0b88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('steam_id', sa.String(length=17), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('avatar_url', sa.String(length=200), nullable=False),
    sa.Column('avatar_medium_url', sa.String(length=200), nullable=False),
    sa.Column('avatar_full_url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__users'))
    )
    op.create_index(op.f('ix__users__steam_id'), 'users', ['steam_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix__users__steam_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
