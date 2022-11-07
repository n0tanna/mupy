from enum import Enum


class ComparisonIdentifiers(Enum):
    EQUAL = '=='
    IDENTICAL = '==='
    NOT_EQUAL = '!='
    NOT_IDENTICAL = '!=='
    LESS_THAN = '<'
    GREATER_THAN = '>'
    LESS_THAN_OR_EQUAL = '<='
    GREATER_THAN_OR_EQUAL = '>='
    NOT = '!'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
