import pytest
from Mathematics.ToBeRemoved.DecimalPlace import DecimalPlace
from Exceptions.ValidationErrors.MathematicsValidation.IncorrectDecimalFormatError import IncorrectDecimalFormatError


def test_decimal_place_location_incorrect_decimal_format1():
    with pytest.raises(IncorrectDecimalFormatError):
        assert DecimalPlace.decimal_place_location('.2')


def test_decimal_place_location_incorrect_decimal_format2():
    with pytest.raises(IncorrectDecimalFormatError):
        assert DecimalPlace.decimal_place_location('2.')

