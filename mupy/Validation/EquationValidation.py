from mupy.Eval.Parentheses import Parentheses
from mupy.Validation.EqualsSignValidation import EqualsSignValidation
from mupy.Enums.Operators import Operators
from mupy.Enums.GroupingIdentifers import GroupingIdentifiers
from mupy.Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from mupy.Exceptions.ValidationErrors.MathematicsValidation.IncorrectDecimalFormatError import IncorrectDecimalFormatError
from mupy.Exceptions.OperatorErrors.OperatorWithNoValuesError import OperatorWithNoValuesError
from mupy.Exceptions.OperatorErrors.NoOperatorError import NoOperatorError
from mupy.Exceptions.OperatorErrors.IncorrectAmountOfOperatorsError import IncorrectAmountOfOperatorsError
from mupy.Exceptions.ValidationErrors.VariableValidation.IncorrectVariableFormat import IncorrectVariableFormat


class EquationValidation:
    @staticmethod
    def switch_sign(equation: list):
        switched_equation = []

        for index in range(len(equation)):
            current_char = equation[index]
            if index == 0 and current_char is Operators.SUBTRACTION.value:
                value = equation[index + 1]

                if GroupingIdentifiers.has_left_value(value):
                    switched_equation.extend([-1.0, '*'])

                else:
                    switched_equation.append(value * -1)

            elif current_char is Operators.SUBTRACTION.value:
                right_value = equation[index + 1]
                left_value = equation[index - 1]

                if GroupingIdentifiers.has_left_value(left_value) and type(right_value) is float:
                    switched_equation.append(right_value * -1.0)

                elif GroupingIdentifiers.has_left_value(right_value) and GroupingIdentifiers.has_left_value(left_value):
                    switched_equation.extend([-1.0, '*'])

                else:
                    switched_equation.append(current_char)

            else:
                if switched_equation:
                    if type(switched_equation[len(switched_equation) - 1]) == float and type(current_char) == float:
                        pass

                    else:
                        switched_equation.append(current_char)

                else:
                    switched_equation.append(current_char)

        return switched_equation

    @staticmethod
    def validate_number(number: list):
        number_length = len(number)
        decimal_amount = number.count('.')

        if decimal_amount > 1:
            raise IncorrectDecimalFormatError

        else:
            if decimal_amount == 0:
                number_joined = float(''.join(number))

            else:
                decimal_location = number.index('.')
                if decimal_location == number_length - 1 or decimal_location == 0:
                    raise IncorrectDecimalFormatError

                else:
                    number_joined = float(''.join(number))

        return number_joined

    @staticmethod
    def format_equation(equation: list):
        equation_length = len(equation)
        validated_equation = []
        current_number = []

        if equation_length == 1:
            if Operators.has_value(equation[0]) or GroupingIdentifiers.has_value(equation[0]):
                raise OperatorWithNoValuesError
            elif equation[0].isnumeric():
                return [float(equation[0])]

        for index in range(equation_length):
            current_char = equation[index]
            if current_char.isnumeric() or current_char == '.':
                current_number.append(current_char)

                if index is equation_length - 1:
                    number = EquationValidation.validate_number(current_number)

                    if index > 0 and len(validated_equation) >= 1:
                        if GroupingIdentifiers.has_value(validated_equation[len(validated_equation) - 1]):
                            raise NoOperatorError

                        elif validated_equation:
                            if type(validated_equation[len(validated_equation) - 1]) == str:
                                if validated_equation[len(validated_equation) - 1].isalpha():
                                    raise IncorrectVariableFormat

                    validated_equation.append(number)
                    current_number = []

            else:
                if (Operators.has_value(current_char) or GroupingIdentifiers.has_value(current_char) or
                        current_char.isalpha()):

                    if current_number:
                        number = EquationValidation.validate_number(current_number)
                        current_number = []

                        if GroupingIdentifiers.has_left_value(current_char):
                            validated_equation.extend([number, '*', '('])

                        elif current_char.isalpha():
                            validated_equation.extend([number, '*', current_char])

                        else:
                            if GroupingIdentifiers.has_right_value(current_char):
                                if GroupingIdentifiers.has_right_value(validated_equation[len(validated_equation) - 1]):
                                    raise NoOperatorError

                                elif validated_equation:
                                    if type(validated_equation[len(validated_equation) - 1]) == str:
                                        if validated_equation[len(validated_equation) - 1].isalpha():
                                            raise IncorrectVariableFormat

                                validated_equation.extend([number, ')'])

                            else:
                                if index == equation_length - 1 and Operators.has_value(current_char):
                                    raise OperatorWithNoValuesError

                                validated_equation.extend([number, current_char])

                    elif GroupingIdentifiers.has_right_value(current_char):
                        if Operators.has_value(validated_equation[len(validated_equation) - 1]):
                            raise OperatorWithNoValuesError

                        elif (type(validated_equation[len(validated_equation) - 1]) == str and
                              GroupingIdentifiers.has_right_value(validated_equation[len(validated_equation) - 2])):
                            if validated_equation[len(validated_equation) - 1].isalpha():
                                raise IncorrectVariableFormat

                        validated_equation.append(')')

                    elif GroupingIdentifiers.has_left_value(current_char):
                        if validated_equation:
                            if type(validated_equation[len(validated_equation) - 1]) == str:
                                if validated_equation[len(validated_equation) - 1].isalpha():
                                    validated_equation.append('*')

                                elif GroupingIdentifiers.has_right_value(
                                        validated_equation[len(validated_equation) - 1]):
                                    raise NoOperatorError

                        validated_equation.append('(')

                    elif current_char.isalpha():
                        validated_equation.append(current_char)

                    else:
                        if len(validated_equation) >= 1:
                            if (Operators.has_value(validated_equation[len(validated_equation) - 1]) and
                                    Operators.SUBTRACTION.value is not validated_equation[len(validated_equation) - 1]):
                                raise IncorrectAmountOfOperatorsError

                            elif GroupingIdentifiers.has_left_value(validated_equation[len(validated_equation) - 1]):
                                if Operators.ADDITION.value is current_char or Operators.SUBTRACTION.value is current_char:
                                    if Operators.SUBTRACTION.value is current_char:
                                        validated_equation.append(current_char)

                                else:
                                    raise IncorrectCharacterError

                            elif GroupingIdentifiers.has_right_value(validated_equation[len(validated_equation) - 1]):
                                validated_equation.append(current_char)

                            else:
                                if Operators.has_value(validated_equation[len(validated_equation) - 1]):
                                    raise IncorrectAmountOfOperatorsError

                                else:
                                    validated_equation.append(current_char)

                        else:
                            if Operators.ADDITION.value is current_char or Operators.SUBTRACTION.value is current_char:
                                if Operators.SUBTRACTION.value is current_char:
                                    validated_equation.append(current_char)

                            else:
                                raise IncorrectAmountOfOperatorsError

                else:
                    raise IncorrectCharacterError

        if len(validated_equation) > 1:
            validated_equation = EquationValidation.switch_sign(validated_equation)

        if Operators.has_value(validated_equation[len(validated_equation) - 1]):
            raise IncorrectAmountOfOperatorsError

        return validated_equation

    @staticmethod
    def equation_validation(equation: list):
        equals_sign_exists = EqualsSignValidation.amount_of_equal_signs(equation)

        if equals_sign_exists:
            equals_sign_location = EqualsSignValidation.find_equals_sign(equation)
            split_equations = EqualsSignValidation.split_equation(equation, equals_sign_location)

            validated_left = EquationValidation.format_equation(split_equations[0])
            validated_right = EquationValidation.format_equation(split_equations[1])

            are_there_parentheses_left = Parentheses.parenthesis_amount_validation(validated_left)
            are_there_parentheses_right = Parentheses.parenthesis_amount_validation(validated_right)

            return {"left_equation": [validated_left, are_there_parentheses_left], "right_equation": [validated_right, are_there_parentheses_right]}

        else:
            validated = EquationValidation.format_equation(equation)
            are_there_parentheses = Parentheses.parenthesis_amount_validation(validated)

            return {"equation": [validated, are_there_parentheses]}

