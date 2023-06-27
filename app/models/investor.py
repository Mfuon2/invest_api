from datetime import datetime
from enum import Enum

from tortoise import Model
from tortoise.fields import IntField, UUIDField, TextField, CharField, DatetimeField, DateField, CharEnumField, \
    ReverseRelation


class IdentityType(str, Enum):
    PASSPORT = 'PASSPORT'
    ID = 'NATIONAL ID'
    ALIEN= 'ALIEN'


class Investor(Model):
    id = UUIDField(pk=True, index=True)
    fullname = CharField(max_length=20, null=False)
    email = CharField(max_length=20, null=False)
    mobile = CharField(max_length=20,null=False)
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



