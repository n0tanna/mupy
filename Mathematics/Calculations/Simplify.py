from Mathematics.Enums.Operators import Operators


class Simplify:
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
                    for index in range(len(variable_holder)):
                        current_value = variable_holder[index]
                        if (type(current_value) is str and
                                current_value is not Operators.EXPONENT.value and
                                current_value is not Operators.MULTIPLICATION.value):
                            if current_value in variables:
                                if index != len(variable_holder):
                                    if variable_holder[index + 1] is Operators.EXPONENT.value:
                                        variables[current_value] += variable_holder[index + 2]
                                    else:
                                        variables[current_value] += 1

                                else:
                                    variables[current_value] += 1

                            else:
                                if index != len(variable_holder) - 1:
                                    if variable_holder[index + 1] is Operators.EXPONENT.value:
                                        variables[current_value] = variable_holder[index + 2]
                                    else:
                                        variables[current_value] = 1

                                else:
                                    variables[current_value] = 1

                        if type(current_value) is float:
                            if index != 0:
                                if variable_holder[index - 1] is Operators.EXPONENT.value:
                                    continue

                                else:
                                    coefficients.append(current_value)

                            else:
                                coefficients.append(current_value)
                else:
                    for index in range(len(current_variable)):
                        current_value = current_variable[index]
                        if (type(current_value) is str and
                                current_value is not Operators.EXPONENT.value and
                                current_value is not Operators.MULTIPLICATION.value):
                            if current_value in variables:
                                if index != len(current_variable) - 1:
                                    if current_variable[index + 1] is Operators.EXPONENT.value:
                                        variables[current_value] += current_variable[index + 2]
                                    else:
                                        variables[current_value] += 1

                                else:
                                    variables[current_value] += 1

                            else:
                                if index != len(current_variable) - 1:
                                    if current_variable[index + 1] is Operators.EXPONENT.value:
                                        variables[current_value] = current_variable[index + 2]
                                    else:
                                        variables[current_value] = 1

                                else:
                                    variables[current_value] = 1

                        if type(current_value) is float:
                            if index != 0:
                                if current_variable[index - 1] is Operators.EXPONENT.value:
                                    continue

                                else:
                                    coefficients.append(current_value)

                            else:
                                coefficients.append(current_value)

                for element in range(len(next_variable)):
                    current_element = next_variable[element]

                    if (type(current_element) is str and
                            current_element is not Operators.EXPONENT.value and
                            current_element is not Operators.MULTIPLICATION.value):
                        if current_element in variables:
                            if element != len(next_variable) - 1:
                                if next_variable[value + 1] is Operators.EXPONENT:
                                    variables[current_element] += equation[value + 2]
                                else:
                                    variables[current_element] += 1

                            else:
                                variables[current_element] += 1

                        else:
                            variables[current_element] = 1

                    if type(current_element) is float:
                        if element != 0:
                            if next_variable[element - 1] is Operators.EXPONENT.value:
                                continue

                            else:
                                coefficients.append(current_element)

                        else:
                            coefficients.append(current_element)

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
