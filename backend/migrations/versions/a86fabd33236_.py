"""empty message

Revision ID: a86fabd33236
Revises: a050561ccff9
Create Date: 2024-08-18 01:17:16.200980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a86fabd33236'
down_revision = 'a050561ccff9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_applications', schema=None) as batch_op:
        batch_op.alter_column('dob',
               existing_type=sa.DATE(),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student_applications', schema=None) as batch_op:
        batch_op.alter_column('dob',
               existing_type=sa.Text(),
               type_=sa.DATE(),
               existing_nullable=False)

    # ### end Alembic commands ###
