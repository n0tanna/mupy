class VariableIsolation:
    @staticmethod
    def isolate_variable(equation: dict, variable: str):
        if len(equation) > 1:
            left_equation = equation["left_equation"]
            right_equation = equation["right_equation"]

            for value in left_equation:



