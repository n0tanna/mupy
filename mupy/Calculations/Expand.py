from Mathematics.Enums.Operators import Operators
from Mathematics.Calculations.Simplify import Simplify


class Expand:
    @staticmethod
    def group_variables(equation: list, index: int):
        term_value = []
        next_operator = ''

        for element in range(index, len(equation)):
            if (Operators.has_value(equation[element]) and
                    equation[element] is not Operators.MULTIPLICATION.value and
                    equation[element] is not Operators.EXPONENT.value):
                next_operator = equation[element]
                break

            else:
                if equation[element] is Operators.MULTIPLICATION.value:
                    if element != 0 and element != len(equation) - 1:
                        if type(equation[element - 1]) is float and type(equation[element + 1]) is float:
                            next_operator = equation[element]
                            break

                        elif type(equation[element - 1]) is str and type(equation[element + 1]) is float:
                            if equation[element - 1] is not Operators.EXPONENT.value:
                                next_operator = equation[element]
                                break

                term_value.append(equation[element])

        return {"variable": term_value, "operator": next_operator}

    @staticmethod
    def expansion(equation: list, exponent: int):
        variables = []
        index = 0

        while index < len(equation):
            variable = Expand.group_variables(equation, index)
            variables.append(variable)
            index += len(variable["variable"]) + 1

        variables = Simplify.simplify_multiplication(variables)
        variable_dict = Simplify.build_values_dictionary(variables)
        simplified_variables = variables
        simplified_variables_dict = variable_dict

        for exponent in range(exponent):
            if exponent > 1:
                pass


















