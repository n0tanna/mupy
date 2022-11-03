from Mathematics.ToBeRemoved.VariableEquationValidation import VariableEquationValidation
from Mathematics.Validation.FindVariables import FindVariables


class SolveVariables:
    @staticmethod
    def solve_for_variables(equation: str, variables: str):
        equation = equation.replace(' ', '')
        equation = list(equation)

        if variables:
            variables = variables.replace(' ', '')
            variables = sorted(set(variables))
            find_variables = VariableEquationValidation.find_variable_values(equation, variables)

            if find_variables:
                find_equals_sign = VariableEquationValidation.find_equals_sign(equation)

                if not find_equals_sign:
                    split_equations = VariableEquationValidation.split_equation(equation, find_equals_sign)

                    left_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[0])
                    right_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[1])

                else:
                    equation = VariableEquationValidation.variable_equation_validation(equation)

        else:
            get_variables = FindVariables.find_equations_variables(equation)
            find_equals_sign = VariableEquationValidation.find_equals_sign(equation)

            if find_equals_sign:
                split_equations = VariableEquationValidation.split_equation(equation, find_equals_sign)

                left_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[0])
                right_equation_validation = VariableEquationValidation.variable_equation_validation(split_equations[1])

            else:
                equation = VariableEquationValidation.variable_equation_validation(equation)

