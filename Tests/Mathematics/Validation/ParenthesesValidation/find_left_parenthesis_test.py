import pytest
from Exceptions.UnknownErrors.UnknownError import UnknownError
from Mathematics.Validation.ParenthesesValidation import ParenthesesValidation


def test_find_left_parenthesis():
    equation = list('2+(3+2)')
    answer = ParenthesesValidation.find_left_parenthesis(equation)
    assert answer == 2.0


def test_find_left_parenthesis2():
    equation = list('(2+((3+5)+2))')
    answer = ParenthesesValidation.find_left_parenthesis(equation)
    assert answer == 4.0


def test_find_left_parenthesis3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5))^2')
    answer = ParenthesesValidation.find_left_parenthesis(equation)
    assert answer == 45.0


def test_find_left_parenthesis_unknown_error1():
    equation = list('2+3+2)')
    with pytest.raises(UnknownError):
        assert ParenthesesValidation.find_left_parenthesis(equation)


def test_find_left_parenthesis_unknown_error2():
    equation = list('2+3+5)+2))')
    with pytest.raises(UnknownError):
        assert ParenthesesValidation.find_left_parenthesis(equation)
