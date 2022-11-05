from Mathematics.Eval.Parentheses import Parentheses
from Mathematics.Validation.EquationValidation import EquationValidation
from Mathematics.Calculations.Bedmas import Bedmas


class Evaluate:
    @staticmethod
    def evaluate(equation: str):
        equation = equation.replace(' ', '')
        equation = list(equation)
        validated_equation = EquationValidation.equation_validation(equation)
        get_key = validated_equation["equation"]
        has_parentheses = get_key[1]

        if not has_parentheses:
            calculated_answer = Bedmas.bedmas_calculation(get_key[0])

        else:
            calculated_answer = Parentheses.calculate_while_parentheses_exist(get_key[0])

            if calculated_answer.is_integer():
                calculated_answer = int(calculated_answer)

        return calculated_answer




