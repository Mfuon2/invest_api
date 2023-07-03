from datetime import datetime
from enum import Enum

from tortoise import Model
from tortoise.fields import UUIDField, TextField, FloatField, BooleanField, DatetimeField, ForeignKeyField, CASCADE, \
    CharField, CharEnumField, DateField, ReverseRelation, DecimalField, IntField

from app.models.enums import IdentityType, DocumentType


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
        "models.Investor", related_name="accounts", on_delete=CASCADE, null=True
    )
    fund = ForeignKeyField(
        "models.InvestorFund", related_name="funds", on_delete=CASCADE, null=True
    )

    class Meta:
        table = 'accounts'


class Investor(Model):
    id = UUIDField(pk=True, index=True)
    fullname = CharField(max_length=20, null=False)
    email = CharField(max_length=20, null=False)
    mobile = CharField(max_length=20, null=False)
    code = CharField(max_length=8, null=False)
    identity = CharField(max_length=8, null=False)
    identity_type = CharField(max_length=8, null=False)
    date_of_birth = DateField(null=False)
    created_at = DatetimeField(auto_now_add=True, default=datetime.utcnow())
    updated_at = DatetimeField(auto_now=True, default=datetime.utcnow())
    tax_number = CharField(null=False, max_length=11)
    accounts = ReverseRelation['InvestorAccount']
    documents = ReverseRelation['InvestorDocument']
    addresses = ReverseRelation['Address']

    class Meta:
        table = 'investors'


class InvestorDocument(Model):
    id = UUIDField(pk=True, index=True)
    document_type = CharField(max_length=100, null=False)
    document_url = CharField(max_length=200, null=False)
    created_at = DatetimeField(auto_now_add=True, default=datetime.utcnow())
    updated_at = DatetimeField(auto_now=True, default=datetime.utcnow())
    investor = ForeignKeyField(
        "models.Investor", related_name="documents", on_delete=CASCADE
    )

    class Meta:
        table = 'documents'


class InvestorFund(Model):
    id = UUIDField(pk=True, index=True)
    fund_name = CharField(max_length=20, null=False, index=True)
    early_withdrawal_penalty = FloatField(default=0.00)
    fund_share_class_code = CharField(max_length=4)
    guaranteed_interest_rate = FloatField(default=0.00)
    maximum_contribution = FloatField(default=0.00)
    maximum_withdrawal = FloatField(default=150000.00)
    minimum_contribution = FloatField(default=100.00)
    minimum_withdrawal = FloatField(default=50.00)
    withdrawal_limit = FloatField(default=0.00)
    withdrawal_limit_duration = IntField(default=1, description="In Hours")
    withdrawal_limit_duration_type = CharField(default="HRS", max_length=10)
    withdrawal_settlement_period = IntField(default=2, description="In Hours")
    withdrawal_settlement_period_type = CharField(default="DAYS", max_length=10)
    is_active = BooleanField(default=False)
    accounts = ReverseRelation['InvestorAccount']
    created_at = DatetimeField(auto_now_add=True, default=datetime.utcnow())
    updated_at = DatetimeField(auto_now=True, default=datetime.utcnow())

    class Meta:
        table = 'funds'


class Address(Model):
    id = UUIDField(pk=True, index=True)
    street = CharField(max_length=20, null=False, index=True)
    city = CharField(max_length=20, null=False, index=True)
    physical_address = CharField(max_length=100, null=False, index=True)
    postal_address = CharField(max_length=100, null=False, index=True)
    investor = ForeignKeyField(
        "models.Investor", related_name="addresses", on_delete=CASCADE
    )
    created_at = DatetimeField(auto_now_add=True, default=datetime.utcnow())
    updated_at = DatetimeField(auto_now=True, default=datetime.utcnow())

    class Meta:
        table = 'addresses'
