from Mathematics.Validation.DecimalPlace import DecimalPlace

from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from Exceptions.OperatorErrors.OperatorWithNoValuesError import OperatorWithNoValuesError
from Mathematics.Calculations.PositiveNegativeConversion import PositiveNegativeConversion
from Exceptions.OperatorErrors.NoOperatorError import NoOperatorError
from Exceptions.ValidationErrors.MathematicsValidation.IncorrectDecimalFormatError import IncorrectDecimalFormatError


class ConstantEquationValidation:
    @staticmethod
    def constant_equation_validation(equation: list):
        equation_length = len(equation)
        validated_equation = []
        is_positive = False
        is_negative = False
        current_number = ''

        for index in range(equation_length):
            current_char = equation[index]
            if current_number:
                if current_char.isnumeric() or current_char == '.':
                    if current_number[len(current_number) - 1] == '.' and current_char == '.':
                        raise IncorrectDecimalFormatError

                    current_number += current_char

                elif current_char == '(':
                    DecimalPlace.decimal_place_location(current_number)

                    if is_positive:
                        number = PositiveNegativeConversion.convert_value('+', current_number)
                        is_positive = False

                    elif is_negative:
                        number = PositiveNegativeConversion.convert_value('-', current_number)
                        is_negative = False

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

                    elif equation[index - 2] == ')':
                        raise NoOperatorError

                    else:
                        number = float(current_number)
                        validated_equation.extend([number, current_char])

                    current_number = ''

                elif current_char == '+' or current_char == '-' or current_char == '*' or current_char == '/' or current_char == '^':
                    number = 0
                    DecimalPlace.decimal_place_location(current_number)

                    if is_positive:
                        number = PositiveNegativeConversion.convert_value('+', current_number)
                        is_positive = False

                    elif is_negative:
                        number = PositiveNegativeConversion.convert_value('-', current_number)
                        is_negative = False

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

                elif current_char == '(':
                    validated_equation.append('(')

                elif current_char == ')':
                    validated_equation.append(')')

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
                                                                                         not current_char == '-'):
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

                    elif not current_char.isnumeric() and not current_char == '.' and not current_char == '(' and not \
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

            elif equation[len(equation) - 2] == ')':
                raise NoOperatorError

            else:
                validated_equation.append(float(current_number))

        return validated_equation






