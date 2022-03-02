"""empty message

Revision ID: 4da3fa44ca9e
Revises: 2481ef49ace9
Create Date: 2022-03-01 20:30:38.230726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4da3fa44ca9e'
down_revision = '2481ef49ace9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('user', sa.String(), nullable=False))
    op.add_column('event_type', sa.Column('user', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event_type', 'user')
    op.drop_column('event', 'user')
    # ### end Alembic commands ###
