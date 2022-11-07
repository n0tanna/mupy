from Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError
from Exceptions.OperatorErrors.IncorrectAmountOfOperatorsError import IncorrectAmountOfOperatorsError
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from Mathematics.Enums.ComparisonOperator import ComparisonIdentifiers
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers


class Classification:
    @staticmethod
    def determine_variables(equation: list, equation_type: EquationIdentifiers):
        for char in equation:
            if char.isalpha() and equation_type == EquationIdentifiers.COMPARISON:
                raise IncorrectCharacterError

            elif char.isalpha() and equation_type == EquationIdentifiers.EQUATION:
                return EquationIdentifiers.VARIABLES

        return equation_type

    @staticmethod
    def determine_classification(equation: list):
        equality_sign_count = equation.count('=')
        equation_type = ''

        if 0 <= equality_sign_count or equality_sign_count == 1:
            if equality_sign_count == 1:
                equality_location = equation.index('=')
                if equality_location == 0:
                    raise IncorrectEqualsSignUsageError

                elif equality_location == len(equation) - 1:
                    raise IncorrectAmountOfOperatorsError

                elif ComparisonIdentifiers.has_value(equation[equality_location - 1]):
                    equation_type = EquationIdentifiers.COMPARISON

                else:
                    equation_type =  EquationIdentifiers.EQUATION

            else:
                greater_than_count = equation.count('>')
                less_than_count = equation.count('<')

                if ((not greater_than_count > 1 or not less_than_count > 1) or
                        (not greater_than_count == 0 or not less_than_count == 0)):
                    if greater_than_count == 1 and less_than_count == 1:
                        raise IncorrectAmountOfOperatorsError

                    elif greater_than_count > 1 or less_than_count > 1:
                        raise IncorrectAmountOfOperatorsError

                    else:
                        equation_type = EquationIdentifiers.COMPARISON

                else:
                    equation_type = EquationIdentifiers.EQUATION

        elif 2 <= equality_sign_count <= 3:
            first_equality_location = equation.index('=')
            equation.reverse()
            last_equality_location = equation.index('=')
            equation.reverse()

            if first_equality_location == 0 or last_equality_location == len(equation) - 1:
                raise IncorrectEqualsSignUsageError

            else:
                if equality_sign_count == 3:
                    for index in range(first_equality_location, last_equality_location):
                        if equation[index] != '=':
                            return IncorrectEqualsSignUsageError
                    equation_type = EquationIdentifiers.COMPARISON

                elif equality_sign_count == 2:
                    if first_equality_location + 1 == last_equality_location:
                        equation_type = EquationIdentifiers.COMPARISON

        else:
            raise IncorrectEqualsSignUsageError

        equation_type = Classification.determine_variables(equation, equation_type)

        return equation_type