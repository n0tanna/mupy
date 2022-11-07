from enum import Enum


class EquationIdentifiers(Enum):
    EQUATION = "EQUATION"
    VARIABLES = "VARIABLES"
    COMPARISON = "COMPARISON"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
