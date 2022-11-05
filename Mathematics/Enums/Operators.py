from enum import Enum


class Operators(Enum):
    ADDITION = '+'
    SUBTRACTION = '-'
    DIVISION = '/'
    MULTIPLICATION = '*'
    EXPONENT = '^'
    RADICAL = '√'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
