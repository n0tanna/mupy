from Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers
from Exceptions.ValidationErrors.VariableValidation.NoVariableValueError import NoVariableValueError
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError


class VariableReplacement:
    @staticmethod
    def replace_variables(equation: list, variables: dict, equation_type: EquationIdentifiers):
        variable_replaced = []
        variables_not_in_dict = set()

        for value in equation:
            if type(value) is str:
                if value.isalpha():
                    has_variable = False
                    for variable in variables:
                        variables_not_in_dict.add(value)
                        if variable == value:
                            has_variable = True
                            variable_value = variables.get(variable)

                            if not variable_value:
                                if equation_type is EquationIdentifiers.COMPARISON_VARIABLES:
                                    raise NoVariableValueError

                                else:
                                    if variable_replaced[len(variable_replaced) - 1] == ')':
                                        variable_replaced.extend(['*', value])

                                    else:
                                        variable_replaced.append(variable)

                            else:
                                variable_replaced.append('(')

                                for char in variable_value:
                                    variable_replaced.append(char)

                                variable_replaced.append(')')

                            break

                    if has_variable is False and equation_type is EquationIdentifiers.COMPARISON_VARIABLES:
                        raise VariableNotFoundError

                    elif has_variable is False:
                        if variable_replaced[len(variable_replaced) - 1] == ')':
                            variable_replaced.extend(['*', value])

                        else:
                            variable_replaced.extend([value])

                else:
                    variable_replaced.append(value)

            else:
                variable_replaced.append(value)

        if len(variables_not_in_dict) > len(variables):
            if equation_type is EquationIdentifiers.COMPARISON_VARIABLES:
                raise VariableNotFoundError

            else:
                for variable in variables_not_in_dict:
                    is_variable_in_dict = True
                    for value in variables:
                        if variable != value:
                            is_variable_in_dict = False

                        else:
                            is_variable_in_dict = True
                            break

                    if not is_variable_in_dict:
                        variables[variable] = ''

                return [variable_replaced, variables]

        elif len(variables_not_in_dict) < len(variables):
            raise VariableNotFoundError

        return variable_replaced
