from Mathematics.Validation.ParenthesesValidation import ParenthesesValidation
from Mathematics.Enums.Operators import Operators
from Mathematics.Calculations.Expand import Expand


class VariableParentheses:
    @staticmethod
    def solve_variable_parentheses(equation: list, variable: str):
        left_parentheses = ParenthesesValidation.find_left_parenthesis(equation)
        right_parentheses = ParenthesesValidation.find_right_parenthesis(equation, left_parentheses)

        if right_parentheses is not len(equation) - 1:
            if equation[right_parentheses + 1] is Operators.EXPONENT.value:
                parentheses_equation = []
                exponent = equation[right_parentheses + 2]
                for index in range(left_parentheses + 1, right_parentheses):
                    parentheses_equation.append(equation[index])

                simplified_equation = Expand.expansion(parentheses_equation, exponent)















