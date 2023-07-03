from enum import Enum


class IdentityType(str, Enum):
    PASSPORT = 'PASSPORT'
    ID = 'NATIONAL ID'
    ALIEN = 'ALIEN'


class DocumentType(str, Enum):
    TAX_CERTIFICATE = 'TAX NUMBER CERTIFICATE'
    ID = 'NATIONAL ID'
    OTHER = 'OTHER'
