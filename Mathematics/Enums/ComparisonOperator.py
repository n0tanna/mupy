from enum import Enum


class GroupingIdentifiers(Enum):
    EQUAL = '=='
    IDENTICAL = '==='
    NOT_EQUAL = '!='
    NOT_IDENTICAL = '!=='
    LESS_THAN = '<'
    GREATER_THAN = '>'
    LESS_THAN_OR_EQUAL = '<='
    GREATER_THAN_OR_EQUAL = '>='
