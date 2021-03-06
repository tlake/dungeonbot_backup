"""empty message

Revision ID: c1a39bca68bc
Revises: None
Create Date: 2016-09-16 16:28:41.863139

"""

# revision identifiers, used by Alembic.
revision = 'c1a39bca68bc'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('karma_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('string_id', sa.String(length=256), nullable=True),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.Column('karma', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quest_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('description', sa.String(length=2048), nullable=True),
    sa.Column('quest_giver', sa.String(length=256), nullable=True),
    sa.Column('location_given', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('completed_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quest_model')
    op.drop_table('karma_model')
    ### end Alembic commands ###
