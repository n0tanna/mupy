from Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError
from Exceptions.ValidationErrors.VariableValidation.NoVariablesToSolveError import NoVariablesToSolveError
from Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError


class VariableEquationValidation:
    @staticmethod
    def find_equals_sign(equation: list):
        equation_length = len(equation)
        no_equals_sign = False

        for index in range(equation_length):
            if index == 0 and equation[index] == '=':
                raise IncorrectEqualsSignUsageError

            elif index == equation_length - 1 and equation[index] == '=':
                raise IncorrectEqualsSignUsageError

            elif equation[index] == '=':
                return index

            else:
                no_equals_sign = True

        return no_equals_sign

    @staticmethod
    def split_equation(equation: list, equal_sign_location: int):
        left_equation = []
        right_equation = []
        equation_length = len(equation)

        for index in range(equal_sign_location):
            left_equation.append(equation[index])

        for index in range(equal_sign_location + 1, equation_length):
            right_equation.append(equation[index])

        equations = [left_equation, right_equation]
        return equations

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

    @staticmethod
    def variable_equation_validation(equation: list):
        equation_length = len(equation)
        validated_equation = []