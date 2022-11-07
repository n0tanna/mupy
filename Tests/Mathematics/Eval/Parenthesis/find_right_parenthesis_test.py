import pytest
from Exceptions.UnknownErrors.UnknownError import UnknownError
from Mathematics.Eval.Parentheses import Parentheses


def test_find_right_parenthesis1():
    equation = list('2+(3+2)')
    answer = Parentheses.find_right_parenthesis(equation, 2)
    assert answer == 6


def test_find_right_parenthesis2():
    equation = list('(2+((3+5)+2))')
    answer = Parentheses.find_right_parenthesis(equation, 4)
    assert answer == 8


def test_find_right_parenthesis3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5))^2')
    answer = Parentheses.find_right_parenthesis(equation, 45)
    assert answer == 52


def test_find_right_parenthesis_unknown_error1():
    equation = list('(2+3+2')
    with pytest.raises(UnknownError):
        assert Parentheses.find_right_parenthesis(equation, 0)


def test_find_right_parenthesis_unknown_error2():
    equation = list('((2+3+5+2')
    with pytest.raises(UnknownError):
        assert Parentheses.find_right_parenthesis(equation, 1)

