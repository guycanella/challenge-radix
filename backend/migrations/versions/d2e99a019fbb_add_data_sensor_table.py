"""add data_sensor table

Revision ID: d2e99a019fbb
Revises: 
Create Date: 2024-09-07 13:05:10.159258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2e99a019fbb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_sensor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('equipament_id', sa.String(length=100), nullable=False),
    sa.Column('value', sa.Numeric(), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('equipament_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_sensor')
    # ### end Alembic commands ###
