"""empty message

Revision ID: f812f3311c79
Revises: 8e2cd1f853bc
Create Date: 2019-01-29 18:45:23.899371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f812f3311c79'
down_revision = '8e2cd1f853bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.BigInteger(), primary_key=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('users', 'user_type',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'user_type',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('images')
    # ### end Alembic commands ###
