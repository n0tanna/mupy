from mupy.Exceptions.ValidationErrors.NoClosingParenthesisError import NoClosingParenthesisError
from mupy.Exceptions.ValidationErrors.NoOpeningParenthesisError import NoOpeningParenthesisError
from mupy.Exceptions.UnknownErrors.UnknownError import UnknownError
from mupy.Calculations.Bedmas import Bedmas


class Parentheses:
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

    @staticmethod
    def parentheses_calculation(equation: list, first_parentheses: int, last_parentheses: int):
        no_parentheses_equation = []

        for index in range(first_parentheses + 1, last_parentheses):
            no_parentheses_equation.append(equation[index])

        for index in range(first_parentheses, last_parentheses):
            del equation[first_parentheses]

        calculated_result = Bedmas.bedmas_calculation(no_parentheses_equation)
        equation[first_parentheses] = calculated_result

        return equation

    @staticmethod
    def calculate_while_parentheses_exist(equation: list):
        while True:
            equation_length = len(equation)
            are_there_brackets = Parentheses.parenthesis_amount_validation(equation)

            if not are_there_brackets and equation_length > 1:
                equation = Bedmas.bedmas_calculation(equation)
                break

            elif equation_length == 1:
                return equation[0]

            else:
                first_parenthesis = Parentheses.find_left_parenthesis(equation)
                last_parenthesis = Parentheses.find_right_parenthesis(equation, first_parenthesis)

                equation = Parentheses.parentheses_calculation(equation, first_parenthesis, last_parenthesis)

        return equation
