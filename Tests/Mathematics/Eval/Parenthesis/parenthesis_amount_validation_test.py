import pytest
from mupy.Eval.Parentheses import Parentheses
from mupy.Exceptions.ValidationErrors.NoClosingParenthesisError import NoClosingParenthesisError
from mupy.Exceptions.ValidationErrors.NoOpeningParenthesisError import NoOpeningParenthesisError


def test_parenthesis_amount_validation_equation1():
    equation = list('(2+(2+3))')
    answer = Parentheses.parenthesis_amount_validation(equation)
    assert answer == True


def test_parenthesis_amount_validation_equation2():
    equation = list('(2+(2+3)+(6-2))^2')
    answer = Parentheses.parenthesis_amount_validation(equation)
    assert answer == True


def test_parenthesis_amount_validation_equation3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5))^2')
    answer = Parentheses.parenthesis_amount_validation(equation)
    assert answer == True


def test_parenthesis_amount_validation_equation4():
    equation = list('((5+5.3)+2)')
    answer = Parentheses.parenthesis_amount_validation(equation)
    assert answer == True


def test_parenthesis_amount_validation_equation5():
    equation = list('(2+2)')
    answer = Parentheses.parenthesis_amount_validation(equation)
    assert answer == True


def test_parenthesis_amount_validation_invalid_closing_parenthesis1():
    equation = list('(2+(2+3)')
    with pytest.raises(NoClosingParenthesisError):
        assert Parentheses.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_closing_parenthesis2():
    equation = list('(2+(2+3')
    with pytest.raises(NoClosingParenthesisError):
        assert Parentheses.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_closing_parenthesis3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+(12-2.5+(12-2.5)+(12-2.5))^2')
    with pytest.raises(NoClosingParenthesisError):
        assert Parentheses.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_opening_parenthesis1():
    equation = list('2+(2+3))')
    with pytest.raises(NoOpeningParenthesisError):
        assert Parentheses.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_opening_parenthesis2():
    equation = list('2+2+3))')
    with pytest.raises(NoOpeningParenthesisError):
        assert Parentheses.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_opening_parenthesis3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+12-2.5)+(12-2.5)+(12-2.5))^2')
    with pytest.raises(NoOpeningParenthesisError):
        assert Parentheses.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_no_parentheses1():
    equation = list('1+1')
    answer = Parentheses.parenthesis_amount_validation(equation)
    assert answer == False


