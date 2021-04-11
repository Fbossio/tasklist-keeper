"""Add boolean field to Todo model

Revision ID: 715579e0607a
Revises: 7eab1017ea9d
Create Date: 2021-04-10 02:57:20.334153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '715579e0607a'
down_revision = '7eab1017ea9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
