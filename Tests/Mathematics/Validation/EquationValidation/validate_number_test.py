import pytest
from Exceptions.ValidationErrors.MathematicsValidation.IncorrectDecimalFormatError import IncorrectDecimalFormatError
from Mathematics.Validation.EquationValidation import EquationValidation


def test_validate_number1():
    number = ['1']
    validated_number = EquationValidation.validate_number(number)
    assert validated_number == 1.0


def test_validate_number2():
    number = ['1', '4']
    validated_number = EquationValidation.validate_number(number)
    assert validated_number == 14.0


def test_validate_number3():
    number = ['2', '.', '3']
    validated_number = EquationValidation.validate_number(number)
    assert validated_number == 2.3


def test_validate_number_decimal_error1():
    number = ['2', '.', '.', '5']
    with pytest.raises(IncorrectDecimalFormatError):
        assert EquationValidation.validate_number(number)


def test_validate_number_decimal_error2():
    number = ['.', '5']
    with pytest.raises(IncorrectDecimalFormatError):
        assert EquationValidation.validate_number(number)


def test_validate_number_decimal_error3():
    number = ['4', '.']
    with pytest.raises(IncorrectDecimalFormatError):
        assert EquationValidation.validate_number(number)

