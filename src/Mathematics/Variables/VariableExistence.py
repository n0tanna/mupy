class VariableExistence:
    @staticmethod
    def find_if_variables_exist(equation: list):
        for value in equation:
            if type(value) is str:
                if value.isalpha():
                    return True

        return False
