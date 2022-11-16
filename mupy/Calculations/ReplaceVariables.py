from mupy.Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError
from mupy.Enums.EquationIdentifers import EquationIdentifiers
from mupy.Exceptions.ValidationErrors.VariableValidation.NoVariableValueError import NoVariableValueError


class ReplaceVariables:
    @staticmethod
    def replace_variables(equation: list, variables: dict, equation_type: EquationIdentifiers):
        variable_replaced = []
        for value in equation:
            if type(value) == str:
                if value.isalpha():
                    has_variable = False
                    for variable in variables:
                        if variable == value:
                            has_variable = True
                            variable_value = variables.get(variable)

                            if not variable_value:
                                if equation_type is EquationIdentifiers.COMPARISON_VARIABLES:
                                    raise NoVariableValueError

                                else:
                                    variable_replaced.append(variable)

                            else:
                                variable_replaced.append('(')

                                for char in variable_value:
                                    variable_replaced.append(char)

                                variable_replaced.append(')')

                    if has_variable is False:
                        raise VariableNotFoundError

                else:
                    variable_replaced.append(value)

            else:
                variable_replaced.append(value)

        return variable_replaced




