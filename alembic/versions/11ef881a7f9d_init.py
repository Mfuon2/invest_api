"""init

Revision ID: 11ef881a7f9d
Revises: 
Create Date: 2023-05-22 12:57:13.166557

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '11ef881a7f9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('investors',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('fullname', sa.String(), nullable=True),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('mobile', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_investors_email'), 'investors', ['email'], unique=True)
    op.create_index(op.f('ix_investors_fullname'), 'investors', ['fullname'], unique=True)
    op.create_index(op.f('ix_investors_id'), 'investors', ['id'], unique=False)
    op.create_index(op.f('ix_investors_mobile'), 'investors', ['mobile'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_investors_mobile'), table_name='investors')
    op.drop_index(op.f('ix_investors_id'), table_name='investors')
    op.drop_index(op.f('ix_investors_fullname'), table_name='investors')
    op.drop_index(op.f('ix_investors_email'), table_name='investors')
    op.drop_table('investors')
    # ### end Alembic commands ###
