from Mathematics.Enums.EquationIdentifers import EquationIdentifiers

class VariableValidation:
    @staticmethod
    def check_for_variables(equation: list, variables: dict, equation_type: EquationIdentifiers):
        for value in equation:
            if type(value) is str:
                if value.isalpha():
                    pass


