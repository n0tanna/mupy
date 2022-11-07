from Mathematics.Eval.Classification import Classification
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers
from Exceptions.ValidationErrors.IncorrectCharacterError import IncorrectCharacterError
import pytest


def test_determine_variables1():
    equation = ['2', '>', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables2():
    equation = ['2', '+', '4', '^', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION)
    assert equation_type == EquationIdentifiers.EQUATION


def test_determine_variables3():
    equation = ['2', '-', '6', '.', '3', '=', '3', 'b']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION)
    assert equation_type == EquationIdentifiers.VARIABLES


def test_determine_variables4():
    equation = ['2', '-', '6', '.', '3', '=', '3', '+', '1', '0']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION)
    assert equation_type == EquationIdentifiers.EQUATION


def test_determine_variables5():
    equation = ['2', '<', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables6():
    equation = ['2', '=', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables7():
    equation = ['2', '=', '=', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables8():
    equation = ['2', '!', '=', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables9():
    equation = ['2', '>', '=', '3']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)
    assert equation_type == EquationIdentifiers.COMPARISON


def test_determine_variables10():
    equation = ['2', 'c', '-', '6', '.', '3', '=', '3', 'b']
    equation_type = Classification.determine_variables(equation, EquationIdentifiers.EQUATION)
    assert equation_type == EquationIdentifiers.VARIABLES


def test_determine_variables_incorrect_character1():
    equation = ['2', '>', '=', '3', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)


def test_determine_variables_incorrect_character2():
    equation = ['2', '=', '=', '3', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)


def test_determine_variables_incorrect_character3():
    equation = ['2', '=', '=', '=', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)


def test_determine_variables_incorrect_character4():
    equation = ['2', '>', 'a']
    with pytest.raises(IncorrectCharacterError):
        Classification.determine_variables(equation, EquationIdentifiers.COMPARISON)

