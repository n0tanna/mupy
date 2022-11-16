from Exceptions.ValidationErrors.NoClosingParenthesisError import NoClosingParenthesisError
from Exceptions.ValidationErrors.NoOpeningParenthesisError import NoOpeningParenthesisError
from Exceptions.UnknownErrors.UnknownError import UnknownError


class ParenthesesValidation:
    @staticmethod
    def parenthesis_amount_validation(equation: list):
        left_parenthesis = equation.count('(')
        right_parenthesis = equation.count(')')

        if left_parenthesis == right_parenthesis and not left_parenthesis == 0 and not right_parenthesis == 0:
            return True

        elif left_parenthesis > right_parenthesis:
            raise NoClosingParenthesisError

        elif left_parenthesis < right_parenthesis:
            raise NoOpeningParenthesisError

        elif left_parenthesis == 0 and right_parenthesis == 0:
            return False

    @staticmethod
    def find_left_parenthesis(equation: list):
        equation.reverse()
        equation_length = len(equation)
        left_parenthesis = 0

        for index in range(equation_length):
            if equation[index] == '(':
                left_parenthesis = len(equation) - index - 1
                break

            else:
                left_parenthesis = -1

        if left_parenthesis == -1:
            raise UnknownError

        equation.reverse()

        return left_parenthesis

    @staticmethod
    def find_right_parenthesis(equation: list, left_parenthesis: int):
        right_parenthesis = 0
        equation_length = len(equation)

        for index in range(left_parenthesis, equation_length):
            if equation[index] == ')':
                right_parenthesis = index
                break

            else:
                right_parenthesis = -1

        if right_parenthesis == -1:
            raise UnknownError

        return right_parenthesis
