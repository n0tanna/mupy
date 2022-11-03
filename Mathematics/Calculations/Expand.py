from Mathematics.Validation.Parentheses import Parentheses


class Expand:
    @staticmethod
    def multiplication_into_parenthesis(original_expression: list, first_parenthesis: int, last_parenthesis: int, equation_length: int):
        multiplication_value = original_expression[0]

        for index in range(first_parenthesis, last_parenthesis):
            pass


    @staticmethod
    def expand_equation(original_expression: list):
        equation_length = len(original_expression)
        first_parenthesis = Parentheses.find_left_parenthesis(original_expression)
        last_parenthesis = Parentheses.find_right_parenthesis(original_expression, first_parenthesis)

        if not first_parenthesis == 0 and not last_parenthesis == equation_length:
            pass
        elif not first_parenthesis == 0:
            pass
        elif not last_parenthesis == equation_length:
            pass
        else:
            pass
