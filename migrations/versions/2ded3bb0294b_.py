"""empty message

Revision ID: 2ded3bb0294b
Revises: 4cda28e25775
Create Date: 2024-06-12 03:52:38.722057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ded3bb0294b'
down_revision = '4cda28e25775'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_username', sa.String(length=20), nullable=True),
    sa.Column('admin_pwd', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###
