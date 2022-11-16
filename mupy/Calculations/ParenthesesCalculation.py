from Mathematics.Calculations.Bedmas import Bedmas
from Mathematics.Validation.ParenthesesValidation import ParenthesesValidation


class ParenthesesCalculation:
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
            are_there_brackets = ParenthesesValidation.parenthesis_amount_validation(equation)

            if not are_there_brackets and equation_length > 1:
                equation = Bedmas.bedmas_calculation(equation)
                break

            elif equation_length == 1:
                return equation[0]

            else:
                first_parenthesis = ParenthesesValidation.find_left_parenthesis(equation)
                last_parenthesis = ParenthesesValidation.find_right_parenthesis(equation, first_parenthesis)

                equation = ParenthesesCalculation.parentheses_calculation(equation, first_parenthesis, last_parenthesis)

        return equation
