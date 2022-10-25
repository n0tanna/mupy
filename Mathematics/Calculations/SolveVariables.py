from Mathematics.Validation.VariableEquationValidation import VariableEquationValidation

class SolveVariables:
    @staticmethod
    def solve_for_variables(equation: str, variables: str):
        equation = equation.replace(' ', '')
        equation = list(equation)

        if variables:
            variables = variables.replace(' ', '')
            variables = list(variables)
            find_variables = VariableEquationValidation.find_variable_values(equation, variables)

            if find_variables:
                find_equals_sign = VariableEquationValidation.find_equals_sign(equation)

                if not find_equals_sign:
                    split_equations = VariableEquationValidation.split_equation(equation, find_equals_sign)

                    left_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[0])
                    right_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[1])

                    equations = [left_equation_validation, right_equation_validation]

                else:
                    equation = VariableEquationValidation.variable_equation_validation(equation)

        else:
            find_equals_sign = VariableEquationValidation.find_equals_sign(equation)

            if not find_equals_sign:
                split_equations = VariableEquationValidation.split_equation(equation, find_equals_sign)

                left_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[0])
                right_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[1])

                equations = [left_equation_validation, right_equation_validation]

            else:
                equation = VariableEquationValidation.variable_equation_validation(equation)


