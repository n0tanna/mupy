from Mathematics.Eval.Parentheses import Parentheses
from Mathematics.Validation.EquationValidation import EquationValidation
from Mathematics.Calculations.Bedmas import Bedmas
from Mathematics.Eval.Classification import Classification
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers
from Mathematics.Validation.ComparisonValidation import ComparisonValidation
from Mathematics.Eval.Comparison import Comparison


class Evaluate:
    @staticmethod
    def call_calculation_method(equation: list):
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

    @staticmethod
    def evaluate(equation: str, variables=None):
        if variables is None:
            variables = []

        else:
            pass

        equation = equation.replace(' ', '')
        equation = list(equation)
        equation_type = Classification.determine_classification(equation, variables)

        if equation_type is EquationIdentifiers.VARIABLES:
            pass

        elif equation_type is EquationIdentifiers.EQUATION:
            calculated_answer = Evaluate.call_calculation_method(equation)
            return calculated_answer

        elif equation_type is EquationIdentifiers.COMPARISON:
            split_equation = ComparisonValidation.split_comparison(equation)
            left_equation = split_equation["left_equation"]
            right_equation = split_equation["right_equation"]
            comparison_type = split_equation["comparison_type"]

            left_calculated_answer = Evaluate.call_calculation_method(left_equation)
            right_calculated_answer = Evaluate.call_calculation_method(right_equation)

            response = Comparison.compare_values(left_calculated_answer, right_calculated_answer, comparison_type)

            return response

        elif equation_type is EquationIdentifiers.COMPARISON_VARIABLES:
            split_equation = ComparisonValidation.split_comparison(equation)
            left_equation = split_equation["left_equation"]
            right_equation = split_equation["right_equation"]
            comparison_type = split_equation["comparison_type"]


