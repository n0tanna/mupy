import pytest

from src.Mathematics.Validation.EquationValidation import EquationValidation
from src.Exceptions.OperatorErrors.TooManyEqualSignsError import TooManyEqualSignsError
from src.Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError
from src.Exceptions.ValidationErrors.NoOpeningParenthesisError import NoOpeningParenthesisError
from src.Exceptions.ValidationErrors.NoClosingParenthesisError import NoClosingParenthesisError


def test_equation_validation_split_equation1():
    equation = ['(', '3', '+', '4', ')', '=', '4']
    validated_equation = EquationValidation.equation_validation(equation)
    assert validated_equation == {"left_equation": [['(', 3.0, '+', 4.0, ')'], True], "right_equation": [[4.0], False]}


def test_equation_validation_split_equation2():
    equation = ['4', '=', '(', '3', '+', '4', ')']
    validated_equation = EquationValidation.equation_validation(equation)
    assert validated_equation == {"left_equation": [[4.0], False], "right_equation": [['(', 3.0, '+', 4.0, ')'], True]}


def test_equation_validation_split_equation3():
    equation = ['(', '3', '+', '4', ')', '=', '(', '(', '4', '-', '5', ')', '-', '3', ')']
    validated_equation = EquationValidation.equation_validation(equation)
    assert validated_equation == {"left_equation": [['(', 3.0, '+', 4.0, ')'], True], "right_equation": [['(', '(', 4.0, '-', 5.0, ')', '-', 3.0, ')'], True]}


def test_equation_validation_split_equation4():
    equation = ['(', '3', '+', '4', ')', '=', '(', '(', '4', '-', '5', ')', '-', '3', ')']
    validated_equation = EquationValidation.equation_validation(equation)
    assert validated_equation == {"left_equation": [['(', 3.0, '+', 4.0, ')'], True], "right_equation": [['(', '(', 4.0, '-', 5.0, ')', '-', 3.0, ')'], True]}


def test_equation_validation_split_equation_too_many_equal_signs1():
    equation = ['(', '3', '+', '4', ')', '=', '(', '(', '4', '=', '5', ')', '-', '3', ')']
    with pytest.raises(TooManyEqualSignsError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_split_equation_incorrect_equal_sign_usage1():
    equation = ['=', '3', '+', '4', ')', '(', '(', '4', '+', '5', ')', '-', '3', ')']
    with pytest.raises(IncorrectEqualsSignUsageError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_split_equation_incorrect_equal_sign_usage2():
    equation = ['(', '3', '+', '4', ')', '(', '(', '4', '+', '5', ')', '-', '3', ')', '=']
    with pytest.raises(IncorrectEqualsSignUsageError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_split_equation_no_opening_parenthesis1():
    equation = ['3', '+', '4', ')', '=', '(', '4', '+', '5', ')', '-', '3']
    with pytest.raises(NoOpeningParenthesisError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_split_equation_no_opening_parenthesis2():
    equation = ['(', '3', '+', '4', ')', '=', '4', '+', '5', ')', '-', '3', ')']
    with pytest.raises(NoOpeningParenthesisError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_split_equation_no_closing_parenthesis1():
    equation = ['(', '3', '+', '4', ')', '=', '(', '(', '4', '+', '5', ')', '-', '3']
    with pytest.raises(NoClosingParenthesisError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_split_equation_no_closing_parenthesis2():
    equation = ['(', '3', '+', '4', '=', '(', '(', '4', '+', '5', ')', '-', '3', ')']
    with pytest.raises(NoClosingParenthesisError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_single_equation1():
    equation = ['(', '3', '+', '4', ')']
    validated_equation = EquationValidation.equation_validation(equation)
    assert validated_equation == {"equation": [['(', 3.0, '+', 4.0, ')'], True]}


def test_equation_validation_single_equation2():
    equation = ['3', '+', '4']
    validated_equation = EquationValidation.equation_validation(equation)
    assert validated_equation == {"equation": [[3.0, '+', 4.0], False]}


def test_equation_validation_single_equation_no_opening_parenthesis1():
    equation = ['3', '+', '4', ')']
    with pytest.raises(NoOpeningParenthesisError):
        EquationValidation.equation_validation(equation)


def test_equation_validation_single_equation_no_closing_parenthesis1():
    equation = ['(', '3', '+', '4']
    with pytest.raises(NoClosingParenthesisError):
        EquationValidation.equation_validation(equation)

