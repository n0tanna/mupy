from Exceptions.ValidationErrors.VariableValidation.IncorrectVariableFormat import IncorrectVariableFormat
from Mathematics.Validation.Parentheses import Parentheses


class IsolateVariable:
    @staticmethod
    def isolate_selected_variable(variable: str, left_equation: list, right_equation: list):
        for variable_value in range(len(variable)):
            if not right_equation or right_equation[0] == 0:
                left_equation_has_ps = Parentheses.parenthesis_amount_validation(left_equation)
                if left_equation_has_ps:
                    left_ps = Parentheses.find_left_parenthesis(left_equation)
                    right_ps = Parentheses.find_right_parenthesis(left_equation)












