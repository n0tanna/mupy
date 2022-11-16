from src.Mathematics.Calculations.ParenthesesCalculation import ParenthesesCalculation
from src.Mathematics.Validation.EquationValidation import EquationValidation
from src.Mathematics.Calculations.Bedmas import Bedmas
from src.Mathematics.Eval.Classification import Classification
from src.Mathematics.Enums.EquationIdentifers import EquationIdentifiers
from src.Mathematics.Validation.ComparisonValidation import ComparisonValidation
from src.Mathematics.Eval.Comparison import Comparison
from src.Mathematics.Validation.VariableInputParser import VariableInputParser
from src.Mathematics.Variables.VariableReplacement import VariableReplacement
from src.Mathematics.Variables.VariableExistence import VariableExistence


class Evaluate:
    @staticmethod
    def call_calculation_method(equation: list):
        validated_equation = EquationValidation.equation_validation(equation)
        get_key = validated_equation["equation"]
        has_parentheses = get_key[1]

        if not has_parentheses:
            calculated_answer = Bedmas.bedmas_calculation(get_key[0])

        else:
            calculated_answer = ParenthesesCalculation.calculate_while_parentheses_exist(get_key[0])

            if calculated_answer.is_integer():
                calculated_answer = int(calculated_answer)

        return calculated_answer

    @staticmethod
    def evaluate(equation: str, variables=None):
        if variables is None:
            variables = []

        else:
            variables = variables.replace(' ', '')
            variables = VariableInputParser.variable_input_parser(variables)

        equation = equation.replace(' ', '')
        equation = list(equation)
        equation_type = Classification.determine_classification(equation, variables)

        if equation_type is EquationIdentifiers.VARIABLES:
            variables_exist = VariableExistence.find_if_variables_exist(equation)
            while variables_exist:
                equation = VariableReplacement.replace_variables(equation, variables, equation_type)
                variables_exist = VariableExistence.find_if_variables_exist(equation)
                validated_equation = EquationValidation.equation_validation(equation)

            calculated_answer = Evaluate.call_calculation_method(equation)

            return calculated_answer

        elif equation_type is EquationIdentifiers.EQUATION:
            calculated_answer = Evaluate.call_calculation_method(equation)
            return calculated_answer

        elif equation_type is EquationIdentifiers.COMPARISON:
            split_equation = ComparisonValidation.split_comparison(equation)
            comparison_type = split_equation["comparison_type"]
            left_calculated_answer = Evaluate.call_calculation_method(split_equation["left_equation"])
            right_calculated_answer = Evaluate.call_calculation_method(split_equation["right_equation"])

            response = Comparison.compare_values(left_calculated_answer, right_calculated_answer, comparison_type)

            return response

        elif equation_type is EquationIdentifiers.COMPARISON_VARIABLES:
            replace_variables = VariableReplacement.replace_variables(equation, variables, equation_type)
            split_equation = ComparisonValidation.split_comparison(replace_variables)
            left_calculated_answer = Evaluate.call_calculation_method(split_equation["left_equation"])
            right_calculated_answer = Evaluate.call_calculation_method(split_equation["right_equation"])
            comparison_type = split_equation["comparison_type"]

            response = Comparison.compare_values(left_calculated_answer, right_calculated_answer, comparison_type)

            return response



