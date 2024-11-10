"""empty message

Revision ID: 2f9838abb588
Revises: 2493a15d7b0b
Create Date: 2024-11-10 21:10:32.842040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f9838abb588'
down_revision = '2493a15d7b0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.drop_table('people')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('pid', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('job', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    op.drop_table('users')
    # ### end Alembic commands ###