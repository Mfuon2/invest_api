from datetime import datetime
from enum import Enum

from tortoise import Model
from tortoise.fields import UUIDField, TextField, FloatField, BooleanField, DatetimeField, ForeignKeyField, CASCADE, \
    CharField, CharEnumField, DateField, ReverseRelation

from app.models.enums import IdentityType


class InvestorAccount(Model):
    id = UUIDField(pk=True, index=True)
    fund_name = TextField()
    units = FloatField(default=0.00)
    unit_price = FloatField(default=0.00)
    balance = FloatField(default=0.00)
    contributions = FloatField(default=0.00)
    cumulative_income = FloatField(default=0.00)
    market_value = FloatField(default=0.00)
    withdrawals = FloatField(default=0.00)
    is_active = BooleanField(default=False)
    created_at = DatetimeField(auto_now_add=True, default=datetime.utcnow())
    updated_at = DatetimeField(auto_now=True, default=datetime.utcnow())
    investor = ForeignKeyField(
        "models.Investor", related_name="accounts", on_delete=CASCADE
    )

    class Meta:
        table = 'investor_accounts'


class Investor(Model):
    id = UUIDField(pk=True, index=True)
    fullname = CharField(max_length=20, null=False)
    email = CharField(max_length=20, null=False)
    mobile = CharField(max_length=20, null=False)
    code = CharField(max_length=8, null=False)
    identity = CharField(max_length=8, null=False)
    identity_type = CharEnumField(enum_type=IdentityType)
    date_of_birth = DateField(null=False)
    created_at = DatetimeField(auto_now_add=True, default=datetime.utcnow())
    updated_at = DatetimeField(auto_now=True, default=datetime.utcnow())
    tax_number = CharField(null=False, max_length=11)
    accounts = ReverseRelation['InvestorAccount']

    # addresses = relationship(Address, cascade="all, delete-orphan", backref='investor_addresses')
    # documents = relationship(InvestorDocument, cascade="all, delete-orphan", backref='investor_documents')
    # accounts = relationship(InvestorAccount, cascade="all, delete-orphan", backref='investor_accounts'

    class Meta:
        table = 'investors'

