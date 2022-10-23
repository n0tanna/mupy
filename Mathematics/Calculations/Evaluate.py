from Mathematics.Validation.Parentheses import Parentheses
from Mathematics.Validation.ConstantEquationValidation import ConstantEquationValidation
from Mathematics.Calculations.Bedmas import Bedmas


class Evaluate:
    @staticmethod
    def evaluate(equation: str):
        equation = equation.replace(' ', '')
        equation = list(equation)
        validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
        are_there_parentheses = Parentheses.parenthesis_amount_validation(equation)

        if not are_there_parentheses:
            calculated_answer = Bedmas.bedmas_calculation(validated_equation)

        else:
            calculated_answer = Parentheses.calculate_while_parentheses_exist(validated_equation)

            if calculated_answer.is_integer():
                calculated_answer = int(calculated_answer)

        return calculated_answer




