import pytest
from Mathematics.Validation.EqualsSignValidation import EqualsSignValidation
from Exceptions.OperatorErrors.TooManyEqualSignsError import TooManyEqualSignsError


def test_amount_of_equal_signs_no_sign1():
    equation = ['(', '2', '+', '2', ')', 'a']
    assert EqualsSignValidation.amount_of_equal_signs(equation) == False


def test_amount_of_equal_signs_with_sign_1():
    equation = ['(', '2', '+', '2', ')', '=', 'a']
    assert EqualsSignValidation.amount_of_equal_signs(equation) == True


def test_amount_of_equal_signs_incorrect_equals_sign_usage_1():
    equation = ['(', '2', '=', '2', ')', '=']
    with pytest.raises(TooManyEqualSignsError):
        assert EqualsSignValidation.amount_of_equal_signs(equation)
