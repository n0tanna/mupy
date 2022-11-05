import pytest
from Exceptions.UnknownErrors.UnknownError import UnknownError
from Mathematics.Eval.Parentheses import Parentheses


def test_find_left_parenthesis():
    equation = list('2+(3+2)')
    answer = Parentheses.find_left_parenthesis(equation)
    assert answer == 2.0


def test_find_left_parenthesis2():
    equation = list('(2+((3+5)+2))')
    answer = Parentheses.find_left_parenthesis(equation)
    assert answer == 4.0


def test_find_left_parenthesis3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5))^2')
    answer = Parentheses.find_left_parenthesis(equation)
    assert answer == 45.0


def test_find_left_parenthesis_unknown_error1():
    equation = list('2+3+2)')
    with pytest.raises(UnknownError):
        assert Parentheses.find_left_parenthesis(equation)


def test_find_left_parenthesis_unknown_error2():
    equation = list('2+3+5)+2))')
    with pytest.raises(UnknownError):
        assert Parentheses.find_left_parenthesis(equation)
