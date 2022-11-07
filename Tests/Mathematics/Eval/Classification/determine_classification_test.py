import pytest
from Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError
from Exceptions.OperatorErrors.IncorrectAmountOfOperatorsError import IncorrectAmountOfOperatorsError
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from Exceptions.ValidationErrors.VariableValidation.VariableNotFoundError import VariableNotFoundError
from Mathematics.Eval.Classification import Classification
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers


def test_determine_classification1():
    equation = ['2', '>', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_classification2():
    equation = ['2', '<', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_classification3():
    equation = ['2', '>', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_classification4():
    equation = ['2', '=', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_classification5():
    equation = ['2', '=', '=', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_classification6():
    equation = ['2', '!', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_classification7():
    equation = ['2', '!', '=', 'a']
    equation_type = Classification.determine_classification(equation, ['a'])
    assert equation_type == EquationIdentifiers.COMPARISON_VARIABLES


def test_determine_classification_incorrect_equals_sign_usage1():
    equation = ['2', '3', '!', '=', '3', '6', '=']
    with pytest.raises(IncorrectEqualsSignUsageError):
        Classification.determine_classification(equation)


def test_determine_classification_incorrect_equals_sign_usage2():
    equation = ['=', '2', '3', '!', '=', '3', '6']
    with pytest.raises(IncorrectEqualsSignUsageError):
        Classification.determine_classification(equation)


def test_determine_classification_incorrect_equals_sign_usage3():
    equation = ['=', '2', '3', '=', '3', '6']
    with pytest.raises(IncorrectEqualsSignUsageError):
        Classification.determine_classification(equation)


def test_determine_classification_incorrect_equals_sign_usage4():
    equation = ['2', '3', '=', '=', '=', '=', '3', '6']
    with pytest.raises(IncorrectEqualsSignUsageError):
        Classification.determine_classification(equation)


def test_determine_classification_incorrect_amount_of_operators1():
    equation = ['2', '3', '>', '>', '3', '6']
    with pytest.raises(IncorrectAmountOfOperatorsError):
        Classification.determine_classification(equation)


def test_determine_classification_incorrect_amount_of_operators2():
    equation = ['2', '3', '<', '<', '3', '6']
    with pytest.raises(IncorrectAmountOfOperatorsError):
        Classification.determine_classification(equation)


def test_determine_classification_incorrect_character_error1():
    equation = ['2', 'b', '<', '3', '6']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_classification(equation)


def test_determine_classification_variable_not_found_error1():
    equation = ['2', '2', '+', '3', '=', '3', '.', '2']
    with pytest.raises(VariableNotFoundError):
        Classification.determine_classification(equation, ['a'])


def test_determine_classification_variable_not_found_error2():
    equation = ['2', '2', '+', '3', '>', '3', '.', '2']
    with pytest.raises(VariableNotFoundError):
        Classification.determine_classification(equation, ['a'])


