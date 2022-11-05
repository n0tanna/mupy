from Exceptions.ValidationErrors.VariableValidation.NoVariablesToSolveError import NoVariablesToSolveError
from Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError


class VariablesToSolveFor:

    @staticmethod
    def find_variable_values(equation: list, variable_values_to_solve_for: list):
        equation_length = len(equation)
        variable_values_length = len(variable_values_to_solve_for)
        variables_found = []

        if variable_values_to_solve_for:
            for index in range(equation_length):
                current_char = equation[index]

                for value in range(variable_values_length):
                    if current_char == variable_values_to_solve_for[value]:
                        duplicate_variable = False

                        if variables_found:
                            for variable in range(len(variables_found)):
                                if current_char == variables_found[variable]:
                                    duplicate_variable = True

                            if duplicate_variable:
                                variables_found.append(current_char)

                        else:
                            variables_found.append(current_char)
            if len(variables_found) == variable_values_length:
                return True

            else:
                raise VariableNotFoundError

        else:
            raise NoVariablesToSolveError
