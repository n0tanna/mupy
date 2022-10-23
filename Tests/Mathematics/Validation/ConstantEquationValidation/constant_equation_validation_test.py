import pytest

from Mathematics.Validation.ConstantEquationValidation import ConstantEquationValidation
from Exceptions.ValidationErrors.IncorrectDecimalFormatError import IncorrectDecimalFormatError
from Exceptions.OperatorErrors.OperatorWithNoValuesError import OperatorWithNoValuesError
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from Exceptions.OperatorErrors.NoOperatorError import NoOperatorError


# SINGLE DIGIT TESTS
def test_constant_equation_single_digit_positive_value1():
    equation = ['1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [1.0]


def test_constant_equation_single_digit_negative_value1():
    equation = ['-', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [-1.0]


def test_constant_equation_single_digit_positive_value2():
    equation = ['+', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [1.0]


# DOUBLE DIGIT TESTS
def test_constant_equation_double_digit_positive_value1():
    equation = ['1', '4']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [14.0]


def test_constant_equation_double_digit_negative_value1():
    equation = ['-', '3', '5']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [-35.0]


def test_constant_equation_double_digit_positive_value2():
    equation = ['+', '7', '9']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [79.0]


# DECIMAL TESTS
def test_constant_equation_decimal_positive_value1():
    equation = ['0', '.', '1', '4']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [0.14]


def test_constant_equation_decimal_positive_value2():
    equation = ['+', '0', '.', '7', '9']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [0.79]


def test_constant_equation_decimal_positive_value3():
    equation = ['0', '.', '7']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [0.7]


def test_constant_equation_decimal_negative_value1():
    equation = ['-', '0', '.', '3']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [-0.3]


def test_constant_equation_decimal_negative_value2():
    equation = ['-', '0', '.', '3', '5']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [-0.35]


# NO BRACKETS TESTS
def test_constant_equation_validation_addition1():
    equation = ['1', '+', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [1.0, '+', 1.0]


def test_constant_equation_validation_subtraction1():
    equation = ['1', '-', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [1.0, '-', 1.0]


def test_constant_equation_validation_multiplication1():
    equation = ['1', '*', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [1.0, '*', 1.0]


def test_constant_equation_validation_division1():
    equation = ['1', '/', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [1.0, '/', 1.0]


def test_constant_equation_validation_exponent1():
    equation = ['1', '^', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [1.0, '^', 1.0]


# PARENTHESIS TESTS
def test_constant_equation_validation_parenthesis_addition1():
    equation = ['(', '1', '+', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '+', 1.0, ')']


def test_constant_equation_validation_parenthesis_subtraction1():
    equation = ['(', '1', '-', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '-', 1.0, ')']


def test_constant_equation_validation_parenthesis_multiplication1():
    equation = ['(', '1', '*', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '*', 1.0, ')']


def test_constant_equation_validation_parenthesis_division1():
    equation = ['(', '1', '/', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '/', 1.0, ')']


def test_constant_equation_validation_parenthesis_exponent1():
    equation = ['(', '1', '^', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '^', 1.0, ')']


def test_constant_equation_validation_parenthesis_addition2():
    equation = ['(', '1', '+', '1', ')', '+', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '+', 1.0, ')', '+', 1.0]


def test_constant_equation_validation_parenthesis_subtraction2():
    equation = ['(', '1', '-', '1', ')', '-', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '-', 1.0, ')', '+', -1.0]


def test_constant_equation_validation_parenthesis_multiplication2():
    equation = ['(', '1', '*', '1', ')', '*', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '*', 1.0, ')', '*', 1.0]


def test_constant_equation_validation_parenthesis_division2():
    equation = ['(', '1', '/', '1', ')', '/', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '/', 1.0, ')', '/', 1.0]


def test_constant_equation_validation_parenthesis_exponent2():
    equation = ['(', '1', '^', '1', ')', '^', '1']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '^', 1.0, ')', '^', 1.0]


def test_constant_equation_validation_parenthesis_addition3():
    equation = ['(', '1', '+', '1', ')', '+', '(', '1', '+', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '+', 1.0, ')', '+', '(', 1.0, '+', 1.0, ')']


def test_constant_equation_validation_parenthesis_subtraction3():
    equation = ['(', '1', '-', '1', ')', '-', '(', '1', '-', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '-', 1.0, ')', '-', '(', 1.0, '-', 1.0, ')']


def test_constant_equation_validation_parenthesis_multiplication3():
    equation = ['(', '1', '*', '1', ')', '*', '(', '1', '*', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '*', 1.0, ')', '*', '(', 1.0, '*', 1.0, ')']


def test_constant_equation_validation_parenthesis_division3():
    equation = ['(', '1', '/', '1', ')', '/', '(', '1', '/', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '/', 1.0, ')', '/', '(', 1.0, '/', 1.0, ')']


def test_constant_equation_validation_parenthesis_exponent3():
    equation = ['(', '1', '^', '1', ')', '^', '(', '1', '^', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 1.0, '^', 1.0, ')', '^', '(', 1.0, '^', 1.0, ')']


def test_constant_equation_validation_parenthesis_addition4():
    equation = ['2', '+', '(', '1', '+', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [2.0, '+', '(', 1.0, '+', 1.0, ')']


def test_constant_equation_validation_parenthesis_subtraction4():
    equation = ['2', '-', '(', '1', '-', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [2.0, '-', '(', 1.0, '-', 1.0, ')']


def test_constant_equation_validation_parenthesis_multiplication4():
    equation = ['2', '*', '(', '1', '*', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [2.0, '*', '(', 1.0, '*', 1.0, ')']


def test_constant_equation_validation_parenthesis_division4():
    equation = ['2', '/', '(', '1', '/', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [2.0, '/', '(', 1.0, '/', 1.0, ')']


def test_constant_equation_validation_parenthesis_exponent4():
    equation = ['2', '^', '(', '1', '^', '1', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [2.0, '^', '(', 1.0, '^', 1.0, ')']


def test_constant_equation_validation_parenthesis_mixed1():
    equation = ['(', '2', '/', '(', '1', '-', '1', ')', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', 2.0, '/', '(', 1.0, '-', 1.0, ')', ')']


def test_constant_equation_validation_parenthesis_mixed2():
    equation = ['(', '(', '1', '-', '1', ')', '^', '(', '4', '*', '6', ')', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', '(', 1.0, '-', 1.0, ')', '^', '(', 4.0, '*', 6.0, ')', ')']


def test_constant_equation_validation_parenthesis_mixed3():
    equation = ['(', '(', '1', '-', '1', ')', '/', '4', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', '(', 1.0, '-', 1.0, ')', '/', 4.0, ')']


def test_constant_equation_validation_parenthesis_mixed4():
    equation = ['(', '(', '(', '1', '-', '1', ')', '/', '3', ')', '+', '4', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', '(', '(', 1.0, '-', 1.0, ')', '/', 3.0, ')', '+', 4.0, ')']


def test_constant_equation_validation_parenthesis_mixed5():
    equation = ['(', '(', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '+', '4', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', '(', '(', 1.2, '-', 1.0, ')', '/', 3.5, ')', '+', 4.0, ')']


def test_constant_equation_validation_parenthesis_mixed6():
    equation = ['(', '(', '2', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '+', '4', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', '(', 2.0, '*', '(', 1.2, '-', 1.0, ')', '/', 3.5, ')', '+', 4.0, ')']


def test_constant_equation_validation_parenthesis_mixed7():
    equation = ['2', '(', '(', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '+', '4', ')']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == [2.0, '*', '(', '(', '(', 1.2, '-', 1.0, ')', '/', 3.5, ')', '+', 4.0, ')']


def test_constant_equation_validation_parenthesis_mixed8():
    equation = ['(', '(', '5', '+', '5', '.', '3', ')', '+', '(', '1', '2', '-', '2', '.', '5', ')', '+', '(', '1', '2',
                '-', '2', '.', '5', ')', '+', '(', '1', '2', '-', '2', '.', '5', ')', '+', '(', '1', '2', '-', '2', '.',
                '5', ')', '+', '(', '1', '2', '-', '2', '.', '5', ')', ')', '^', '2']
    validated_equation = ConstantEquationValidation.constant_equation_validation(equation)
    assert validated_equation == ['(', '(', 5.0, '+', 5.3, ')', '+', '(', 12.0, '-', 2.5, ')', '+',
                                  '(', 12.0, '-', 2.5, ')', '+', '(', 12.0, '-', 2.5, ')', '+', '(', 12.0,
                                  '-', 2.5, ')', '+', '(', 12.0, '-', 2.5, ')', ')', '^', 2.0]


# INCORRECT CHARACTER ERROR
def test_constant_equation_validation_incorrect_character1():
    equation = ['(', '(', 'b', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '4', ')']
    with pytest.raises(IncorrectCharacterError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_incorrect_character2():
    equation = ['(', '(', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '=', ')']
    with pytest.raises(IncorrectCharacterError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_incorrect_character3():
    equation = ['w', '(', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')']
    with pytest.raises(IncorrectCharacterError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


# NO OPERATOR ERROR
def test_constant_equation_validation_no_operator1():
    equation = ['(', '(', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '4', ')']
    with pytest.raises(NoOperatorError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_no_operator2():
    equation = ['(', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '4']
    with pytest.raises(NoOperatorError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


# OPERATORS WITH NO VALUES
def test_constant_equation_validation_operator_no_value1():
    equation = ['(', '(', '1', '+', '*', '1', ')', '/', '3', '.', '5', ')']
    with pytest.raises(OperatorWithNoValuesError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_operator_no_value2():
    equation = ['(', '(', '1', '+', '1', ')', '/', '/', '3', '.', '5', ')']
    with pytest.raises(OperatorWithNoValuesError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_operator_no_value3():
    equation = ['-']
    with pytest.raises(OperatorWithNoValuesError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_operator_no_value4():
    equation = ['/']
    with pytest.raises(OperatorWithNoValuesError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


# DECIMAL ERROR TESTS
def test_constant_equation_validation_wrong_decimal_format1():
    equation = ['(', '(', '(', '1', '.', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '+', '4', ')']
    with pytest.raises(IncorrectDecimalFormatError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_wrong_decimal_format2():
    equation = ['(', '(', '(', '1', '.', '2', '-', '1', ')', '/', '3', '.', ')', '+', '4', ')']
    with pytest.raises(IncorrectDecimalFormatError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_wrong_decimal_format3():
    equation = ['(', '(', '(', '1', '.', '.', '2', '-', '1', ')', '/', '3', '.', '5', ')', '+', '4', ')']
    with pytest.raises(IncorrectDecimalFormatError):
        assert ConstantEquationValidation.constant_equation_validation(equation)


def test_constant_equation_validation_wrong_decimal_format4():
    equation = ['.']
    with pytest.raises(IncorrectDecimalFormatError):
        assert ConstantEquationValidation.constant_equation_validation(equation)