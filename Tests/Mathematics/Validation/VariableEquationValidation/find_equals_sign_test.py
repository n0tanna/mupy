import pytest
from Mathematics.Validation.VariableEquationValidation import VariableEquationValidation
from Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError


def test_find_equals_sign_incorrect_equals_sign_usage_1():
    equation = ['=', '(', '2', '+', '2', ')']
    with pytest.raises(IncorrectEqualsSignUsageError):
        assert VariableEquationValidation.find_equals_sign(equation)


def test_find_equals_sign_incorrect_equals_sign_usage_2():
    equation = ['(', '2', '+', '2', ')', '=']
    with pytest.raises(IncorrectEqualsSignUsageError):
        assert VariableEquationValidation.find_equals_sign(equation)


def test_find_equals_sign1():
    equation = ['(', '2', '+', '2', ')', '=', 'a']
    assert VariableEquationValidation.find_equals_sign(equation) == 5


def test_find_equals_sign_no_sign1():
    equation = ['(', '2', '+', '2', ')', 'a']
    assert VariableEquationValidation.find_equals_sign(equation) == False
