import pytest
from Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError
from Exceptions.OperatorErrors.IncorrectAmountOfOperatorsError import IncorrectAmountOfOperatorsError
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
from Mathematics.Eval.Classification import Classification
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers


def test_determine_variables1():
    equation = ['2', '>', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables2():
    equation = ['2', '<', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables3():
    equation = ['2', '>', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables4():
    equation = ['2', '=', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables5():
    equation = ['2', '=', '=', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables6():
    equation = ['2', '!', '=', '3']
    equation_type = Classification.determine_classification(equation)
    assert equation_type == EquationIdentifiers.COMPARISON


