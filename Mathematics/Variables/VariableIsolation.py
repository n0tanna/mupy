class VariableIsolation:
    @staticmethod
    def isolate_variable(equation: dict, variable: str):
        if len(equation) > 1:
            left_equation = equation["left_equation"]
            left_has_parentheses = left_equation[1]

            right_equation = equation["right_equation"]
            right_has_parentheses = right_equation[1]

            if left_has_parentheses:
                pass








