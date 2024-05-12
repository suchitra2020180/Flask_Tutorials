"""Added city column

Revision ID: abafa2c8b4bf
Revises: 
Create Date: 2024-04-16 14:04:41.378207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abafa2c8b4bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppies', schema=None) as batch_op:
        batch_op.drop_column('city')

    # ### end Alembic commands ###
