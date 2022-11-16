import pytest
from src.Mathematics.Validation.EqualsSignValidation import EqualsSignValidation
from src.Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError


def test_find_equals_sign_incorrect_equals_sign_usage_1():
    equation = ['=', '(', '2', '+', '2', ')']
    with pytest.raises(IncorrectEqualsSignUsageError):
        assert EqualsSignValidation.find_equals_sign(equation)


def test_find_equals_sign_incorrect_equals_sign_usage_2():
    equation = ['(', '2', '+', '2', ')', '=']
    with pytest.raises(IncorrectEqualsSignUsageError):
        assert EqualsSignValidation.find_equals_sign(equation)


def test_find_equals_sign1():
    equation = ['(', '2', '+', '2', ')', '=', 'a']
    assert EqualsSignValidation.find_equals_sign(equation) == 5


