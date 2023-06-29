from enum import Enum


class IdentityType(str, Enum):
    PASSPORT = 'PASSPORT'
    ID = 'NATIONAL ID'
    ALIEN = 'ALIEN'
