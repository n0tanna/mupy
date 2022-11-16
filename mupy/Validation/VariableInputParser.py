from mupy.Exceptions.ValidationErrors.VariableValidation.IncorrectVariableFormat import IncorrectVariableFormat
from mupy.Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError


class VariableInputParser:
    @staticmethod
    def variable_input_parser(variables: str):
        variables_and_values = dict()
        equal_sign_found = False
        current_variable = ''
        variable_value = ''

        for value in variables:
            if value.isalpha() and not current_variable:
                current_variable = value

            elif value.isalpha() and current_variable:
                raise IncorrectVariableFormat

            elif value == '=' and not current_variable:
                raise IncorrectVariableFormat

            elif value == '=' and equal_sign_found:
                raise IncorrectEqualsSignUsageError

            elif value == '=' and current_variable:
                equal_sign_found = True

            elif equal_sign_found and not value == ',':
                variable_value += value

            elif value == ',':
                equal_sign_found = False

                if variable_value:
                    variables_and_values[current_variable] = variable_value

                else:
                    variables_and_values[current_variable] = ''

                current_variable = ''
                variable_value = ''

        if current_variable and not variable_value:
            variables_and_values[current_variable] = ''

        else:
            variables_and_values[current_variable] = variable_value

        return variables_and_values




