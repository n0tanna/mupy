from Exceptions.ValidationErrors.MathematicsValidation.IncorrectDecimalFormatError import IncorrectDecimalFormatError


class DecimalPlace:
    @staticmethod
    def decimal_place_location(number: str):
        if number[0] == '.':
            raise IncorrectDecimalFormatError

        elif number[len(number) - 1] == '.':
            raise IncorrectDecimalFormatError
