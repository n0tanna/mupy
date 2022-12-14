import pytest
from src.Mathematics.Validation.ParenthesesValidation import ParenthesesValidation
from src.Exceptions.ValidationErrors.NoClosingParenthesisError import NoClosingParenthesisError
from src.Exceptions.ValidationErrors.NoOpeningParenthesisError import NoOpeningParenthesisError


def test_parenthesis_amount_validation_equation1():
    equation = list('(2+(2+3))')
    answer = ParenthesesValidation.parenthesis_amount_validation(equation)
    assert answer is True


def test_parenthesis_amount_validation_equation2():
    equation = list('(2+(2+3)+(6-2))^2')
    answer = ParenthesesValidation.parenthesis_amount_validation(equation)
    assert answer is True

def test_parenthesis_amount_validation_equation3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5)+(12-2.5))^2')
    answer = ParenthesesValidation.parenthesis_amount_validation(equation)
    assert answer is True


def test_parenthesis_amount_validation_equation4():
    equation = list('((5+5.3)+2)')
    answer = ParenthesesValidation.parenthesis_amount_validation(equation)
    assert answer is True


def test_parenthesis_amount_validation_equation5():
    equation = list('(2+2)')
    answer = ParenthesesValidation.parenthesis_amount_validation(equation)
    assert answer is True


def test_parenthesis_amount_validation_invalid_closing_parenthesis1():
    equation = list('(2+(2+3)')
    with pytest.raises(NoClosingParenthesisError):
        assert ParenthesesValidation.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_closing_parenthesis2():
    equation = list('(2+(2+3')
    with pytest.raises(NoClosingParenthesisError):
        assert ParenthesesValidation.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_closing_parenthesis3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+(12-2.5+(12-2.5)+(12-2.5))^2')
    with pytest.raises(NoClosingParenthesisError):
        assert ParenthesesValidation.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_opening_parenthesis1():
    equation = list('2+(2+3))')
    with pytest.raises(NoOpeningParenthesisError):
        assert ParenthesesValidation.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_opening_parenthesis2():
    equation = list('2+2+3))')
    with pytest.raises(NoOpeningParenthesisError):
        assert ParenthesesValidation.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_invalid_opening_parenthesis3():
    equation = list('((5+5.3)+(12-2.5)+(12-2.5)+12-2.5)+(12-2.5)+(12-2.5))^2')
    with pytest.raises(NoOpeningParenthesisError):
        assert ParenthesesValidation.parenthesis_amount_validation(equation)


def test_parenthesis_amount_validation_no_parentheses1():
    equation = list('1+1')
    answer = ParenthesesValidation.parenthesis_amount_validation(equation)
    assert answer is False



