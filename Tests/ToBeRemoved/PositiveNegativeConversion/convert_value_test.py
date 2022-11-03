import pytest
from Exceptions.ValidationErrors.MathematicsValidation.IncorrectConversionTypeError import IncorrectConversionTypeError
from Mathematics.ToBeRemoved.PositiveNegativeConversion import PositiveNegativeConversion


def test_convert_value_positive1():
    answer = PositiveNegativeConversion.convert_value('+', '3')
    assert answer == 3.0


def test_convert_value_negative2():
    answer = PositiveNegativeConversion.convert_value('-', '3')
    assert answer == -3.0


def test_convert_value_incorrect_conversion_type1():
    with pytest.raises(IncorrectConversionTypeError):
        assert PositiveNegativeConversion.convert_value('*', '3')