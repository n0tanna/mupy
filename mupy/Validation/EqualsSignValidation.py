from mupy.Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError
from mupy.Exceptions.OperatorErrors.TooManyEqualSignsError import TooManyEqualSignsError


class EqualsSignValidation:
    @staticmethod
    def amount_of_equal_signs(equation: list):
        equals_sign_amount = equation.count('=')

        if equals_sign_amount > 1:
            raise TooManyEqualSignsError

        elif equals_sign_amount == 0:
            return False

        else:
            return True

    @staticmethod
    def find_equals_sign(equation: list):
        equation_length = len(equation)

        for index in range(equation_length):
            if index == 0 and equation[index] == '=':
                raise IncorrectEqualsSignUsageError

            elif index == equation_length - 1 and equation[index] == '=':
                raise IncorrectEqualsSignUsageError

            elif equation[index] == '=':
                return index

    @staticmethod
    def split_equation(equation: list, equal_sign_location: int):
        left_equation = []
        right_equation = []
        equation_length = len(equation)

        for index in range(equal_sign_location):
            left_equation.append(equation[index])

        for index in range(equal_sign_location + 1, equation_length):
            right_equation.append(equation[index])

        equations = [left_equation, right_equation]
        return equations
