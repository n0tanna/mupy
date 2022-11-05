from Exceptions.ValidationErrors.VariableValidation.NoVariablesToSolveError import NoVariablesToSolveError


class FindVariables:
    @staticmethod
    def find_equations_variables(equation: list):
        equation_length = len(equation)
        variable_list = set()

        for index in range(equation_length):
            current_value = equation[index]
            if current_value.isalpha():
                variable_list.add(current_value)

        if variable_list:
            variable_list = sorted(variable_list)

        else:
            variable_list = []

        return variable_list
