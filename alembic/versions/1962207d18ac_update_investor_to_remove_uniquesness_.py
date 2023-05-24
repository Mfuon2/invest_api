"""update investor to remove uniquesness for email

Revision ID: 1962207d18ac
Revises: 11ef881a7f9d
Create Date: 2023-05-23 09:32:35.876567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1962207d18ac'
down_revision = '11ef881a7f9d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_investors_email', table_name='investors')
    op.create_index(op.f('ix_investors_email'), 'investors', ['email'], unique=False)
    op.drop_index('ix_investors_fullname', table_name='investors')
    op.create_index(op.f('ix_investors_fullname'), 'investors', ['fullname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_investors_fullname'), table_name='investors')
    op.create_index('ix_investors_fullname', 'investors', ['fullname'], unique=False)
    op.drop_index(op.f('ix_investors_email'), table_name='investors')
    op.create_index('ix_investors_email', 'investors', ['email'], unique=False)
    # ### end Alembic commands ###