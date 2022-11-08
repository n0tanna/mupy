from enum import Enum


class GroupingIdentifiers(Enum):
    LEFT_PARENTHESIS = '('
    RIGHT_PARENTHESIS = ')'
    LEFT_BRACKET = '['
    RIGHT_BRACKET = ']'
    LEFT_CURLY_BRACE = '{'
    RIGHT_CURLY_BRACE = '}'

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    @classmethod
    def has_left_value(cls, value):
        if value == '(':
            return value in cls._value2member_map_

        elif value == '[':
            return value in cls._value2member_map_

        elif value == '{':
            return value in cls._value2member_map_

    @classmethod
    def has_right_value(cls, value):
        if value == ')':
            return value in cls._value2member_map_

        elif value == ']':
            return value in cls._value2member_map_

        elif value == '}':
            return value in cls._value2member_map_
