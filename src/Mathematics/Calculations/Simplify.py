from src.Mathematics.Enums.Operators import Operators


class Simplify:
    @staticmethod
    def edit_values_dictionary(variable: list, variables_dict: dict, coefficients: list):
        for index in range(len(variable)):
            current_element = variable[index]

            if (type(current_element) is str and
                    current_element is not Operators.EXPONENT.value and
                    current_element is not Operators.MULTIPLICATION.value):
                if current_element in variables_dict:
                    if index != len(variable) - 1:
                        if variable[index + 1] is Operators.EXPONENT:
                            variables_dict[current_element] += variable[index + 2]
                        else:
                            variables_dict[current_element] += 1

                    else:
                        variables_dict[current_element] += 1

                else:
                    variables_dict[current_element] = 1

            if type(current_element) is float:
                if index != 0:
                    if variable[index - 1] is Operators.EXPONENT.value:
                        continue

                    else:
                        coefficients.append(current_element)

                else:
                    coefficients.append(current_element)

        return [coefficients, variables_dict]

    @staticmethod
    def build_values_dictionary(variable: list):
        coefficients = []
        variables = dict()

        for index in range(len(variable)):
            current_value = variable[index]
            if (type(current_value) is str and
                    current_value is not Operators.EXPONENT.value and
                    current_value is not Operators.MULTIPLICATION.value):
                if current_value in variables:
                    if index != len(variable):
                        if variable[index + 1] is Operators.EXPONENT.value:
                            variables[current_value] += variable[index + 2]
                        else:
                            variables[current_value] += 1

                    else:
                        variables[current_value] += 1

                else:
                    if index != len(variable) - 1:
                        if variable[index + 1] is Operators.EXPONENT.value:
                            variables[current_value] = variable[index + 2]
                        else:
                            variables[current_value] = 1

                    else:
                        variables[current_value] = 1

            if type(current_value) is float:
                if index != 0:
                    if variable[index - 1] is Operators.EXPONENT.value:
                        continue

                    else:
                        coefficients.append(current_value)

                else:
                    coefficients.append(current_value)

        return [coefficients, variables]

    @staticmethod
    def simplify_multiplication(equation: list):
        new_variables = []
        for value in range(len(equation)):
            current_variable = equation[value]["variable"]
            current_operation = equation[value]["operator"]

            if ((Operators.has_value(current_operation) or current_operation == '') and
                    current_operation is not Operators.MULTIPLICATION.value):
                if value > 0:
                    if equation[value - 1]["operator"] is Operators.MULTIPLICATION.value:
                        continue

                new_variables.append([{'variable': current_variable}, {'operator': current_operation}])

            elif current_operation is Operators.MULTIPLICATION.value:
                final_coefficient = 1
                final_variable = []
                coefficients = []
                variables = dict()
                next_variable = equation[value + 1]["variable"]
                next_operation = equation[value + 1]["operator"]
                variable_operator = ''

                if new_variables:
                    variable_operator = new_variables[len(new_variables) - 1][1]['operator']

                if new_variables and variable_operator is Operators.MULTIPLICATION.value:
                    variable_holder = new_variables[len(new_variables) - 1][0]["variable"]
                    returned_values = Simplify.build_values_dictionary(variable_holder)
                    coefficients = returned_values[0]
                    variables = returned_values[1]

                else:
                    returned_values = Simplify.build_values_dictionary(current_variable)
                    coefficients = returned_values[0]
                    variables = returned_values[1]

                edited_values = Simplify.edit_values_dictionary(next_variable, variables, coefficients)
                coefficients = edited_values[0]
                variables = edited_values[1]

                if coefficients:
                    for element in coefficients:
                        final_coefficient *= element

                final_variable.append(final_coefficient)

                if variables:
                    for variable, exponent in variables.items():
                        if exponent > 1:
                            final_variable.extend(['*', variable, '^', exponent])
                        else:
                            final_variable.extend(['*', variable])

                if new_variables and current_operation is Operators.MULTIPLICATION.value:
                    if variable_operator is not Operators.MULTIPLICATION.value:
                        new_variables.append([{"variable": final_variable}, {"operator": next_operation}])

                    else:
                        del new_variables[len(new_variables) - 1]
                        new_variables.append([{"variable": final_variable}, {"operator": next_operation}])

                else:
                    new_variables.append([{"variable": final_variable}, {"operator": next_operation}])

        return new_variables
