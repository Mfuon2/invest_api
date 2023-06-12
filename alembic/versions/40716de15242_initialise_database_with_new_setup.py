"""initialise database with new setup

Revision ID: 40716de15242
Revises: 
Create Date: 2023-06-12 10:32:57.897298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40716de15242'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fund_name', sa.String(), nullable=True),
    sa.Column('early_withdrawal_penalty', sa.Float(), nullable=True),
    sa.Column('fund_share_class_code', sa.String(), nullable=True),
    sa.Column('guaranteed_interest_rate', sa.Float(), nullable=True),
    sa.Column('maximum_contribution', sa.Float(), nullable=True),
    sa.Column('maximum_withdrawal', sa.Float(), nullable=True),
    sa.Column('minimum_contribution', sa.Float(), nullable=True),
    sa.Column('minimum_withdrawal', sa.Float(), nullable=True),
    sa.Column('withdrawal_limit', sa.Float(), nullable=True),
    sa.Column('withdrawal_limit_duration', sa.Integer(), nullable=True),
    sa.Column('withdrawal_limit_duration_type', sa.String(), nullable=True),
    sa.Column('withdrawal_settlement_period', sa.Integer(), nullable=True),
    sa.Column('withdrawal_settlement_period_type', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_funds_fund_name'), 'funds', ['fund_name'], unique=False)
    op.create_index(op.f('ix_funds_id'), 'funds', ['id'], unique=False)
    op.create_table('investors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('mobile', sa.String(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('identity', sa.String(), nullable=True),
    sa.Column('identity_type', sa.String(), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('tax_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_investors_email'), 'investors', ['email'], unique=False)
    op.create_index(op.f('ix_investors_fullname'), 'investors', ['fullname'], unique=False)
    op.create_index(op.f('ix_investors_id'), 'investors', ['id'], unique=False)
    op.create_index(op.f('ix_investors_mobile'), 'investors', ['mobile'], unique=False)
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fund_name', sa.String(), nullable=True),
    sa.Column('units', sa.Float(), nullable=True),
    sa.Column('unit_price', sa.Float(), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('contributions', sa.Float(), nullable=True),
    sa.Column('cumulative_income', sa.Float(), nullable=True),
    sa.Column('market_value', sa.Float(), nullable=True),
    sa.Column('withdrawals', sa.Float(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('investor_id', sa.Integer(), nullable=True),
    sa.Column('investor_fund_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['investor_fund_id'], ['funds.id'], ),
    sa.ForeignKeyConstraint(['investor_id'], ['investors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accounts_fund_name'), 'accounts', ['fund_name'], unique=False)
    op.create_index(op.f('ix_accounts_id'), 'accounts', ['id'], unique=False)
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('physical_address', sa.String(), nullable=True),
    sa.Column('postal_address', sa.String(), nullable=True),
    sa.Column('investor_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['investor_id'], ['investors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('document_type', sa.String(), nullable=True),
    sa.Column('document_url', sa.String(), nullable=True),
    sa.Column('investor_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['investor_id'], ['investors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('documents')
    op.drop_table('addresses')
    op.drop_index(op.f('ix_accounts_id'), table_name='accounts')
    op.drop_index(op.f('ix_accounts_fund_name'), table_name='accounts')
    op.drop_table('accounts')
    op.drop_index(op.f('ix_investors_mobile'), table_name='investors')
    op.drop_index(op.f('ix_investors_id'), table_name='investors')
    op.drop_index(op.f('ix_investors_fullname'), table_name='investors')
    op.drop_index(op.f('ix_investors_email'), table_name='investors')
    op.drop_table('investors')
    op.drop_index(op.f('ix_funds_id'), table_name='funds')
    op.drop_index(op.f('ix_funds_fund_name'), table_name='funds')
    op.drop_table('funds')
    # ### end Alembic commands ###