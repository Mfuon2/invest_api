from datetime import datetime

from tortoise import models, fields, Model
from tortoise.fields import IntField, TextField, UUIDField, FloatField, BooleanField, ForeignKeyRelation, \
    ForeignKeyField

from app.models.investor import Investor


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
    created_at = fields.DatetimeField(auto_now_add=True, default=datetime.utcnow())
    updated_at = fields.DatetimeField(auto_now=True, default=datetime.utcnow())
    investor: ForeignKeyRelation[Investor] = ForeignKeyField(
        "models.Investor", related_name="investors", to_field="id"
    )

    class Meta:
        table = 'investor_accounts'



