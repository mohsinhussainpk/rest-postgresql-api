"""empty message

Revision ID: d1b4cd9a2a9e
Revises: db542b18a79e
Create Date: 2018-08-17 03:37:38.443636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1b4cd9a2a9e'
down_revision = 'db542b18a79e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('titles', sa.Column('title_id', sa.Integer(), nullable=False))
    op.drop_column('titles', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('titles', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('titles', 'title_id')
    # ### end Alembic commands ###