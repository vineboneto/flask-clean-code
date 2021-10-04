"""audit

Revision ID: 5c88bf991330
Revises: ea62e9b74d34
Create Date: 2021-10-03 20:43:18.480888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c88bf991330'
down_revision = 'ea62e9b74d34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Account', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Account', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Account', 'updated_at')
    op.drop_column('Account', 'created_at')
    # ### end Alembic commands ###
