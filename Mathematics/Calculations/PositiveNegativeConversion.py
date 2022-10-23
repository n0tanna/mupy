from Exceptions.ValidationErrors.IncorrectConversionTypeError import IncorrectConversionTypeError


class PositiveNegativeConversion:
    @staticmethod
    def convert_value(conversion_type: str, value: str):
        number = float(value)
        if conversion_type == '+':
            number *= 1

        elif conversion_type == '-':
            number *= -1

        else:
            raise IncorrectConversionTypeError

        return number

