from Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError
from Exceptions.OperatorErrors.NoOperatorError import NoOperatorError
from Exceptions.OperatorErrors.OperatorWithNoValuesError import OperatorWithNoValuesError
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from Exceptions.ValidationErrors.MathematicsValidation.IncorrectDecimalFormatError import IncorrectDecimalFormatError
from Exceptions.ValidationErrors.VariableValidation.NoVariablesToSolveError import NoVariablesToSolveError
from Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError
from Mathematics.Calculations.PositiveNegativeConversion import PositiveNegativeConversion
from Mathematics.Validation.DecimalPlace import DecimalPlace


class VariableEquationValidation:
    @staticmethod
    def find_equals_sign(equation: list):
        equation_length = len(equation)
        no_equals_sign = True

        for index in range(equation_length):
            if index == 0 and equation[index] == '=':
                raise IncorrectEqualsSignUsageError

            elif index == equation_length - 1 and equation[index] == '=':
                raise IncorrectEqualsSignUsageError

            elif equation[index] == '=':
                return index

            else:
                no_equals_sign = False

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
        is_positive = False
        is_negative = False
        has_variable = False
        current_number = ''

        for index in range(equation_length):
            current_char = equation[index]
            if current_number:
                if current_char.isnumeric() or current_char == '.':
                    if current_number[len(current_number) - 1] == '.' and current_char == '.':
                        raise IncorrectDecimalFormatError

                    current_number += current_char

                elif current_char.isalpha():
                    current_number += current_char
                    has_variable = True

                elif current_char == '(':
                    DecimalPlace.decimal_place_location(current_number)

                    if is_positive:
                        number = PositiveNegativeConversion.convert_value('+', current_number)
                        is_positive = False

                    elif is_negative:
                        number = PositiveNegativeConversion.convert_value('-', current_number)
                        is_negative = False

                    elif has_variable:
                        number = current_number
                        has_variable = False

                    else:
                        number = float(current_number)

                    validated_equation.extend([number, '*', current_char])
                    current_number = ''

                elif current_char == ')':
                    DecimalPlace.decimal_place_location(current_number)

                    if is_positive:
                        number = PositiveNegativeConversion.convert_value('+', current_number)
                        validated_equation.extend(['+', number, current_char])
                        is_positive = False

                    elif is_negative:
                        number = PositiveNegativeConversion.convert_value('-', current_number)
                        validated_equation.extend(['+', number, current_char])
                        is_negative = False

                    elif has_variable:
                        number = current_number
                        validated_equation.extend([number, current_char])
                        has_variable = False

                    elif equation[index - 2] == ')':
                        raise NoOperatorError

                    else:
                        number = float(current_number)
                        validated_equation.extend([number, current_char])

                    current_number = ''

                elif index == equation_length - 1:
                    if current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/' or \
                            current_char == '^':
                        raise OperatorWithNoValuesError

                elif current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/' or \
                        current_char == '^':
                    DecimalPlace.decimal_place_location(current_number)

                    if is_positive:
                        number = PositiveNegativeConversion.convert_value('+', current_number)
                        is_positive = False

                    elif is_negative:
                        number = PositiveNegativeConversion.convert_value('-', current_number)
                        is_negative = False

                    elif has_variable:
                        number = current_number
                        has_variable = False

                    elif equation[index + 1] == ')':
                        raise OperatorWithNoValuesError

                    else:
                        number = float(current_number)

                    validated_equation.extend([number, current_char])
                    current_number = ''

                else:
                    raise IncorrectCharacterError

            else:
                if current_char.isnumeric() or current_char == '.':
                    current_number += current_char

                elif current_char.isalpha():
                    current_number += current_char
                    has_variable = True

                elif current_char == '(':
                    validated_equation.append('(')

                elif current_char == ')':
                    validated_equation.append(')')

                elif index == equation_length - 1:
                    if current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/' or current_char == '^':
                        raise OperatorWithNoValuesError

                    elif not current_char.isalnum() and not current_char == '(' and not current_char == ')':
                        raise IncorrectCharacterError

                elif equation_length > 0 and equation_length > index:
                    if equation[index - 1] == ')' and equation[index + 1] == '(':
                        if current_char == '/':
                            validated_equation.append('/')

                        elif current_char == '*':
                            validated_equation.append('*')

                        elif current_char == '^':
                            validated_equation.append('^')

                        elif current_char == '+':
                            validated_equation.append('+')

                        elif current_char == '-':
                            validated_equation.append('-')

                        elif not current_char.isnumeric() and not current_char == '.' and not current_char == '(' and not \
                                current_char == ')':
                            raise IncorrectCharacterError

                    elif (equation[index - 1] == '+' or equation[index - 1] == '-' or equation[index - 1] == '*' or
                          equation[index - 1] == '/' or equation[index - 1] == '^') and (not current_char == '+' or
                                                                                         current_char == '-'):
                        raise OperatorWithNoValuesError

                    elif current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/' or \
                            current_char == '^':
                        if current_char == '+':
                            is_positive = True

                        elif current_char == '-':
                            is_negative = True

                        elif current_char == '/':
                            validated_equation.append('/')

                        elif current_char == '*':
                            validated_equation.append('*')

                        elif current_char == '^':
                            validated_equation.append('^')

                    elif not current_char.isalnum() and not current_char == '.' and not current_char == '(' and not \
                            current_char == ')':
                        raise IncorrectCharacterError

                elif current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/' or \
                        current_char == '^':
                    if current_char == '+':
                        is_positive = True

                    elif current_char == '-':
                        is_negative = True

                    else:
                        raise OperatorWithNoValuesError

                else:
                    raise IncorrectCharacterError

        if current_number:
            if not validated_equation:
                if is_positive:
                    validated_equation.append(float(current_number))

                elif is_negative:
                    validated_equation.append(float(current_number) * -1)

                elif current_number.isalpha():
                    validated_equation.append(current_number)

                elif current_number == '.':
                    raise IncorrectDecimalFormatError

                else:
                    validated_equation.append(float(current_number))

            elif is_positive:
                number = PositiveNegativeConversion.convert_value('+', current_number)
                validated_equation.extend(['+', number])

            elif is_negative:
                number = PositiveNegativeConversion.convert_value('-', current_number)
                validated_equation.extend(['+', number])

            elif validated_equation[len(validated_equation) - 1] == ')':
                raise NoOperatorError

            elif current_number.isalnum():
                if current_number.isdigit():
                    validated_equation.append(float(current_number))

                else:
                    validated_equation.append(current_number)

            else:
                validated_equation.append(float(current_number))

        return validated_equation
