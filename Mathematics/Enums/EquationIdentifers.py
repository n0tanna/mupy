from enum import Enum


class EquationIdentifiers(Enum):
    EQUATION = "EQUATION"
    VARIABLES = "VARIABLES"
    COMPARISON = "COMPARISON"
    COMPARISON_VARIABLES = "COMPARISON_VARIABLES"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
