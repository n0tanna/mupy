from Mathematics.Calculations.Reciprocal import Reciprocal
from Mathematics.Calculations.PositiveNegativeConversion import PositiveNegativeConversion
from Exceptions.MathematicErrors.DivisionByZeroError import DivisionByZeroError
from Exceptions.ValidationErrors.IncorrectExponentFormatError import IncorrectExponentFormatError


class Bedmas:
    @staticmethod
    def replace_values(equation: list, character: str, answer: float):
        equation.pop(equation.index(character) - 1)
        equation.pop(equation.index(character) + 1)
        equation[equation.index(character)] = float(answer)

        return equation

    @staticmethod
    def bedmas_calculation(equation: list):
        while True:
            equation_length = len(equation)

            if equation_length > 1:
                answer = 0
                find_exponent = equation.index('^') if '^' in equation else False

                if not find_exponent:
                    find_division = equation.index('/') if '/' in equation else False

                    if not find_division:
                        find_multiplication = equation.index('*') if '*' in equation else False

                        if not find_multiplication:
                            find_addition = equation.index('+') if '+' in equation else False
                            find_subtraction = equation.index('-') if '-' in equation else False

                            if find_addition and find_subtraction:
                                if find_addition < find_subtraction:
                                    left_term = equation[find_addition - 1]
                                    right_term = equation[find_addition + 1]
                                    answer = left_term + right_term

                                    equation = Bedmas.replace_values(equation, '+', answer)

                                else:
                                    left_term = equation[find_subtraction - 1]
                                    right_term = equation[find_subtraction + 1]
                                    answer = left_term - right_term

                                    equation = Bedmas.replace_values(equation, '-', answer)

                            elif not find_addition:
                                left_term = equation[find_subtraction - 1]
                                right_term = equation[find_subtraction + 1]
                                answer = left_term - right_term

                                equation = Bedmas.replace_values(equation, '-', answer)

                            elif not find_subtraction:
                                left_term = equation[find_addition - 1]
                                right_term = equation[find_addition + 1]
                                answer = left_term + right_term

                                equation = Bedmas.replace_values(equation, '+', answer)

                        else:
                            left_term = equation[find_multiplication - 1]
                            right_term = equation[find_multiplication + 1]
                            answer = left_term * right_term

                            equation = Bedmas.replace_values(equation, '*', answer)

                    else:
                        left_term = equation[find_division - 1]
                        right_term = equation[find_division + 1]

                        if right_term == 0:
                            raise DivisionByZeroError

                        else:
                            answer = left_term / right_term

                        equation = Bedmas.replace_values(equation, '/', answer)

                else:
                    left_term = equation[find_exponent - 1]
                    right_term = equation[find_exponent + 1]
                    reciprocal = False

                    if right_term < 0:
                        reciprocal = True
                        right_term = PositiveNegativeConversion.convert_value('-', right_term)

                    elif not float(right_term).is_integer():
                        raise IncorrectExponentFormatError

                    answer = left_term

                    for index in range(int(right_term - 1)):
                        answer *= left_term

                    if reciprocal:
                        answer = Reciprocal.get_reciprocal(answer)

                    if left_term < 0:
                        answer = PositiveNegativeConversion.convert_value('-', answer)

                    equation = Bedmas.replace_values(equation, '^', answer)

            else:
                break

        answer = equation[0]

        return answer

